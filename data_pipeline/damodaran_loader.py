"""
Damodaran Data Loader — EconAgent Platform
==========================================
Reads all Damodaran macro/micro economic Excel files from the
existing Damodaran_Data directory WITHOUT modifying originals.
Produces structured in-memory DataFrames for every category.

Architecture: Evidence-grounded, zero-hallucination.
Every data point is traceable to its source file.
"""

import os
import json
import hashlib
import logging
from pathlib import Path
from typing import Dict, Optional, List, Tuple
from dataclasses import dataclass, field

import pandas as pd
import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("DamodaranLoader")

# ── Source root (READ-ONLY — never modified) ──────────────────────────────────
DAMODARAN_ROOT = Path(os.getenv("DAMODARAN_ROOT", r"F:\documents\SOIC\Damodaran_Data"))
PLATFORM_ROOT  = Path(os.getenv("PLATFORM_ROOT", Path(__file__).resolve().parent.parent))

@dataclass
class DataAsset:
    """Single loaded data asset with provenance metadata."""
    name: str
    category: str
    region: str
    source_path: str
    sha256: str
    df: pd.DataFrame
    row_count: int
    col_count: int
    load_status: str = "OK"
    error_msg: str = ""

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "category": self.category,
            "region": self.region,
            "source_path": self.source_path,
            "sha256": self.sha256,
            "row_count": self.row_count,
            "col_count": self.col_count,
            "load_status": self.load_status,
            "error_msg": self.error_msg,
        }


CATEGORY_MAP = {
    "01_Corporate_Governance":          "Corporate Governance",
    "02_Risk_and_Discount_Rates":       "Risk & Discount Rates",
    "03_Cost_of_Capital":               "Cost of Capital",
    "04_Company_and_Market_Metrics":    "Company & Market Metrics",
    "05_Return_on_Capital_and_EVA":     "Return on Capital & EVA",
    "06_Capital_Structure_and_Debt":    "Capital Structure & Debt",
    "07_Dividend_and_Payout_Policy":    "Dividend & Payout Policy",
    "08_Cash_Flows_and_CapEx":          "Cash Flows & CapEx",
    "09_Balance_Sheet_and_Intangibles": "Balance Sheet & Intangibles",
    "10_Margins_and_Profitability":     "Margins & Profitability",
    "11_Financing_and_Capital_Flows":   "Financing & Capital Flows",
    "12_Working_Capital":               "Working Capital",
    "13_Growth_Rates":                  "Growth Rates",
    "14_Valuation_Multiples":           "Valuation Multiples",
    "15_Tax_Rates":                     "Tax Rates",
    "16_Option_Pricing_and_Volatility": "Option Pricing & Volatility",
}

REGION_KEYWORDS = {
    "Global": "Global", "India": "India", "China": "China",
    "Europe": "Europe", "Japan": "Japan", "emerg": "Emerging Markets",
    "Rest": "Rest of World", "EB": "Emerging (Book-based)",
}


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()[:16]


def _infer_region(stem: str) -> str:
    for kw, label in REGION_KEYWORDS.items():
        if kw in stem:
            return label
    return "US / Developed Markets"


def _safe_read_excel(path: Path) -> Tuple[Optional[pd.DataFrame], str]:
    """
    Read Damodaran Excel files. .xls files use xlrd and prefer the
    'Industry Averages' sheet (data sheet). Falls back to openpyxl for .xlsx.
    Returns (df, error_msg).
    """
    suffix = path.suffix.lower()

    # ── XLS path: use xlrd directly to pick the right sheet ──────────────────
    if suffix == ".xls":
        try:
            import xlrd
            wb = xlrd.open_workbook(str(path))
            sheet_names = wb.sheet_names()
            # Prefer Industry Averages or the largest data sheet
            target = None
            for preferred in ["Industry Averages", "Data", "Sheet1", "Sheet 1"]:
                for sn in sheet_names:
                    if preferred.lower() in sn.lower():
                        target = sn
                        break
                if target:
                    break
            if not target:
                target = max(sheet_names, key=lambda s: wb.sheet_by_name(s).nrows)

            # Damodaran XLS: find the actual data header row by scanning xlrd directly
            # Key insight: row 0 of col-0 is "Industry Name" (exact), not URL metadata
            ws = wb.sheet_by_name(target)
            header_row = 9  # Damodaran default: 9 header/metadata rows before data
            # Tight scan: look for a row whose col-0 is exactly "Industry Name" or "Country"
            EXACT_HDRS = ["industry name", "country", "industry", "region"]
            for r in range(min(20, ws.nrows)):
                c0 = str(ws.cell_value(r, 0)).strip().lower()
                # Must be short (< 25 chars) and match a header keyword exactly
                if c0 in EXACT_HDRS or (len(c0) < 25 and any(c0 == kw for kw in EXACT_HDRS)):
                    header_row = r
                    break

            df = pd.read_excel(path, engine="xlrd",
                               sheet_name=target, header=header_row)
            df.dropna(how="all", inplace=True)
            df.dropna(axis=1, how="all", inplace=True)
            df.reset_index(drop=True, inplace=True)
            return df, ""
        except Exception as e:
            return None, str(e)

    # ── XLSX path ─────────────────────────────────────────────────────────────
    try:
        import openpyxl
        wb = openpyxl.load_workbook(str(path), data_only=True, read_only=True)
        sheet_names = wb.sheetnames
        wb.close()

        # Prefer the data sheet
        target = None
        for preferred in ["Industry Averages", "ERPs by country", "Country Lookup",
                          "Data", "Sheet1"]:
            for sn in sheet_names:
                if preferred.lower() in sn.lower():
                    target = sn
                    break
            if target:
                break

        # First pass: load with header=0 to scan for the real header row
        df_scan = pd.read_excel(path, engine="openpyxl",
                                sheet_name=target or 0, header=0, nrows=25)

        # Damodaran XLSX: col-0 of the real header row is exactly "Industry Name" or "Country..."
        EXACT_HDRS = ["industry name", "country", "industry", "region"]
        header_row = 0
        for r in range(len(df_scan)):
            c0 = str(df_scan.iloc[r, 0]).strip().lower()
            # Tight match: short label, exact keyword
            if c0 in EXACT_HDRS or (len(c0) < 25 and any(c0.startswith(kw) for kw in EXACT_HDRS)):
                header_row = r + 1  # +1 because df_scan header=0 consumed row 0
                break
                break

        # Second pass: load with correct header
        df = pd.read_excel(path, engine="openpyxl",
                           sheet_name=target or 0, header=header_row)
        df.dropna(how="all", inplace=True)
        df.dropna(axis=1, how="all", inplace=True)
        df.reset_index(drop=True, inplace=True)
        return df, ""
    except Exception as e:
        return None, str(e)


class DamodaranLoader:
    """
    Loads Damodaran data from all 16 macro/micro economic categories.
    Read-only: source files are never modified.
    """

    def __init__(self):
        self.assets: Dict[str, DataAsset] = {}
        self.load_log: List[dict] = []

    def load_all(self) -> Dict[str, DataAsset]:
        """Main entry point: load every Excel file found in Damodaran_Data."""
        logger.info(f"Loading Damodaran data from: {DAMODARAN_ROOT}")

        # Category subdirs
        cat_root = DAMODARAN_ROOT / "01_Current_Data_by_Category"
        for folder in sorted(cat_root.iterdir()):
            if not folder.is_dir():
                continue
            cat_label = CATEGORY_MAP.get(folder.name, folder.name)
            self._load_folder(folder, cat_label)

        # Regional data
        region_root = DAMODARAN_ROOT / "02_Current_Data_by_Region"
        if region_root.exists():
            for folder in sorted(region_root.iterdir()):
                if folder.is_dir():
                    self._load_folder(folder, f"Regional/{folder.name}")

        # Industry taxonomy
        tax_folder = DAMODARAN_ROOT / "03_Industry_Taxonomy_Company_Lookup"
        if tax_folder.exists():
            self._load_folder(tax_folder, "Industry Taxonomy")

        # Tools/models
        tools_folder = DAMODARAN_ROOT / "04_Data_Tools_and_Models"
        if tools_folder.exists():
            self._load_folder(tools_folder, "Data Tools & Models")

        logger.info(f"Total assets loaded: {len(self.assets)}")
        self._write_load_report()
        return self.assets

    def _load_folder(self, folder: Path, category: str):
        for f in sorted(folder.iterdir()):
            if f.suffix.lower() not in (".xls", ".xlsx"):
                continue
            self._load_file(f, category)

    def _load_file(self, path: Path, category: str):
        stem = path.stem
        region = _infer_region(stem)
        sha = _sha256(path)
        key = f"{category}/{stem}"

        df, err = _safe_read_excel(path)

        if df is not None and not df.empty:
            asset = DataAsset(
                name=stem,
                category=category,
                region=region,
                source_path=str(path),
                sha256=sha,
                df=df,
                row_count=len(df),
                col_count=len(df.columns),
                load_status="OK",
            )
            self.assets[key] = asset
            self.load_log.append({"key": key, "status": "OK", "rows": len(df), "cols": len(df.columns)})
            logger.debug(f"  OK  {stem} [{len(df)}r x {len(df.columns)}c]")
        else:
            asset = DataAsset(
                name=stem, category=category, region=region,
                source_path=str(path), sha256=sha,
                df=pd.DataFrame(), row_count=0, col_count=0,
                load_status="ERROR", error_msg=err,
            )
            self.assets[key] = asset
            self.load_log.append({"key": key, "status": "ERROR", "error": err})
            logger.warning(f"  ERR {stem}: {err[:80]}")

    def _write_load_report(self):
        ok  = sum(1 for l in self.load_log if l["status"] == "OK")
        err = sum(1 for l in self.load_log if l["status"] == "ERROR")
        report = {
            "total_files": len(self.load_log),
            "loaded_ok": ok,
            "load_errors": err,
            "log": self.load_log,
        }
        out = PLATFORM_ROOT / "reports" / "data_load_report.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        with open(out, "w") as f:
            json.dump(report, f, indent=2)
        logger.info(f"Load report: {ok} OK, {err} errors → {out}")

    def get_category_summary(self) -> pd.DataFrame:
        """Return a summary DataFrame of all loaded assets."""
        rows = [a.to_dict() for a in self.assets.values()]
        return pd.DataFrame(rows)

    def get_asset(self, key: str) -> Optional[DataAsset]:
        return self.assets.get(key)

    def search(self, keyword: str) -> List[DataAsset]:
        kw = keyword.lower()
        return [a for a in self.assets.values()
                if kw in a.name.lower() or kw in a.category.lower()]


if __name__ == "__main__":
    loader = DamodaranLoader()
    assets = loader.load_all()
    summary = loader.get_category_summary()
    print(summary[["category", "region", "name", "row_count", "load_status"]].to_string())
    print(f"\nTotal: {len(assets)} files loaded")
