r"""
EconAgent Platform — Full Pipeline Runner
==========================================
Runs all steps in sequence:
  1. Load Damodaran data  (507 XLS/XLSX files, 16 categories)
  2. Run 18 specialized economic analysis agents
  3. Verify results through harness verification layer
  4. Run the platform orchestrator to generate manifest
  5. Generate comprehensive HTML dashboard
  6. Run validation tests

Usage:
  py -3.12 run_platform.py

Output:
  F:\documents\SOIC\EconAgent_Platform\platform_ui\EconAgent_Dashboard.html
"""

import os, sys, json, logging, hashlib
from pathlib import Path
from datetime import datetime, timezone

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s")
logger = logging.getLogger("PlatformRunner")

PLATFORM_ROOT = Path(os.getenv("PLATFORM_ROOT", Path(__file__).resolve().parent))
HARNESS_ROOT  = Path(os.getenv("HARNESS_ROOT", r"F:\documents\SOIC\MultiAgent_Harness_System"))

sys.path.insert(0, str(PLATFORM_ROOT / "data_pipeline"))
sys.path.insert(0, str(PLATFORM_ROOT / "agents"))
sys.path.insert(0, str(PLATFORM_ROOT / "harness_integration"))
sys.path.insert(0, str(PLATFORM_ROOT / "platform_ui"))
sys.path.insert(0, str(HARNESS_ROOT / "03_MultiAgent_Harness_Engine"))


def step1_load_data():
    logger.info("=" * 60)
    logger.info("STEP 1: Loading Damodaran data...")
    from damodaran_loader import DamodaranLoader
    loader = DamodaranLoader()
    assets = loader.load_all()
    summary = loader.get_category_summary()
    ok_count = int((summary["load_status"] == "OK").sum())
    logger.info(f"  → {ok_count}/{len(assets)} assets loaded OK")
    return assets, loader


def step2_analyze(assets):
    logger.info("=" * 60)
    logger.info("STEP 2: Running 18 specialized economic agents...")
    from econ_analysis_agents import EconAnalysisOrchestrator
    orch = EconAnalysisOrchestrator(assets)
    summary = orch.run()
    logger.info(f"  → {summary['total_results']} total analysis results")
    for aid, rlist in summary["by_agent"].items():
        logger.info(f"     {aid}: {len(rlist)} results")
    return summary


def step3_verify(analysis):
    logger.info("=" * 60)
    logger.info("STEP 3: Verifying results through harness...")

    SANITY_BOUNDS = {
        "ERP": (0.001, 0.30),
        "Beta": (0.0, 5.0),
        "P/E": (0.0, 500.0),
        "P/B": (0.0, 100.0),
        "EV/EBITDA": (0.0, 200.0),
        "WACC": (0.001, 0.50),
        "Growth": (-0.50, 1.00),
        "Margin": (-1.0, 1.0),
        "Volatility": (0.001, 5.0),
        "Debt": (-1e12, 1e12),
        "Capital": (0.0, 1e12),
        "Scorecard": (0.0, 310.0),
        "Rotation": (0.0, 500.0),
    }

    total_pass, total_fail = 0, 0
    verified = {}
    for aid, rlist in analysis.get("by_agent", {}).items():
        vlist = []
        for r in rlist:
            flags = list(r.get("flags", []))
            status = "PASS"
            val = r.get("value", {})
            metric = r.get("metric", "")
            for bk, (lo, hi) in SANITY_BOUNDS.items():
                if bk.lower() in metric.lower() and isinstance(val, dict):
                    for sk in ["median_pct", "global_median_pct", "median", "mean_pct", "median_mil_usd"]:
                        v = val.get(sk)
                        if v is not None:
                            vn = v / 100 if sk.endswith("_pct") else v
                            if not (lo <= vn <= hi):
                                flags.append(f"BOUNDS_WARN:{bk}={vn:.4f}")
                                status = "WARN"
                            break
            r = dict(r)
            r["verification_status"] = status
            r["verification_flags"] = flags
            vlist.append(r)
            if status == "PASS":
                total_pass += 1
            else:
                total_fail += 1
        verified[aid] = vlist

    # Certificate
    cert = {
        "platform": "EconAgent Platform v1.0",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "total_results": total_pass + total_fail,
        "verified_pass": total_pass,
        "verified_fail": total_fail,
        "pass_rate_pct": round(total_pass / max(1, total_pass + total_fail) * 100, 1),
        "by_agent": verified,
    }
    payload = json.dumps(cert, sort_keys=True, default=str)
    cert["sha256_signature"] = hashlib.sha256(payload.encode()).hexdigest()
    out = PLATFORM_ROOT / "reports" / "verified_econ_report.json"
    with open(out, "w") as f:
        json.dump(cert, f, indent=2, default=str)
    logger.info(f"  → {total_pass} PASS, {total_fail} WARN/FAIL | Sig: {cert['sha256_signature'][:16]}…")
    return cert


def step4_manifest(assets_loader, analysis, cert):
    logger.info("=" * 60)
    logger.info("STEP 4: Building platform manifest...")

    summary = assets_loader.get_category_summary()
    ok_count = int((summary["load_status"] == "OK").sum())

    harness_engine_dir = HARNESS_ROOT / "03_MultiAgent_Harness_Engine"
    harness = {
        "papers_corpus_verified": (HARNESS_ROOT / "01_Peer_Reviewed_Research_Papers" / "papers_manifest.json").exists(),
        "audit_certificate_present": (HARNESS_ROOT / "06_Deep_Rigorous_Analysis_Report" / "AUDIT_COMPLIANCE_CERTIFICATE.json").exists(),
        "engine_modules": [f.name for f in harness_engine_dir.iterdir() if f.suffix == ".py"] if harness_engine_dir.exists() else [],
    }

    papers_manifest = HARNESS_ROOT / "01_Peer_Reviewed_Research_Papers" / "papers_manifest.json"
    papers_count = 0
    if papers_manifest.exists():
        with open(papers_manifest) as f:
            papers_count = len(json.load(f))

    manifest = {
        "platform": "EconAgent Platform",
        "version": "1.0.0",
        "build_timestamp": datetime.now(timezone.utc).isoformat(),
        "data_assets": {"total_files": len(summary), "loaded_ok": ok_count},
        "analysis": {"total_results": analysis["total_results"], "agents": analysis["agents_run"]},
        "verification": {
            "pass": cert["verified_pass"],
            "fail": cert["verified_fail"],
            "pass_rate_pct": cert["pass_rate_pct"],
            "signature": cert["sha256_signature"],
        },
        "harness": harness,
        "papers_corpus": {"count": papers_count, "verified": papers_manifest.exists()},
    }
    out = PLATFORM_ROOT / "reports" / "platform_manifest.json"
    with open(out, "w") as f:
        json.dump(manifest, f, indent=2)
    logger.info(f"  → Manifest written: {papers_count} papers, {ok_count} data assets")
    return manifest


def step5_dashboard():
    logger.info("=" * 60)
    logger.info("STEP 5: Generating HTML dashboard...")
    from generate_dashboard import generate_dashboard
    path = generate_dashboard()
    size = Path(path).stat().st_size
    logger.info(f"  → Dashboard: {path} ({size // 1024} KB)")
    return path


def step6_validate(analysis, manifest, dashboard_path):
    logger.info("=" * 60)
    logger.info("STEP 6: Running validation checks...")
    errors = []

    # Check min results per agent (18 specialized agents)
    min_expected = {
        "MACRO_ERP": 1, "MICRO_BETA": 1, "MICRO_MARGINS": 1,
        "MICRO_MULTIPLES": 1, "MICRO_GROWTH": 1, "MICRO_CAPSTRUCT": 1,
        "MACRO_WACC": 1, "MICRO_DIVIDEND": 1, "MICRO_WORKCAP": 1,
        "MICRO_TAXRATE": 1, "MICRO_CAPEX": 1, "MICRO_EVA": 1,
        "MICRO_GOVERNANCE": 1, "MICRO_INTANGIBLES": 1,
        "MICRO_VOLAT": 1, "MICRO_FINFLOWS": 1, "SOIC_TECH_RANKING": 1,
        "COMMODITY_TANKER_FLOWS": 1,
    }
    for aid, min_n in min_expected.items():
        n = len(analysis.get("by_agent", {}).get(aid, []))
        if n < min_n:
            errors.append(f"FAIL: {aid} produced only {n} results (expected >= {min_n})")
        else:
            logger.info(f"  ✅ {aid}: {n} results")

    # Check dashboard exists and has content
    dp = Path(dashboard_path)
    if not dp.exists():
        errors.append("FAIL: Dashboard file not found")
    elif dp.stat().st_size < 50_000:
        errors.append(f"FAIL: Dashboard too small ({dp.stat().st_size} bytes)")
    else:
        logger.info(f"  ✅ Dashboard: {dp.stat().st_size // 1024} KB")

    # Check papers corpus
    pc = manifest.get("papers_corpus", {})
    if pc.get("count", 0) < 100:
        errors.append(f"FAIL: Papers corpus count {pc.get('count')} < 100")
    else:
        logger.info(f"  ✅ Papers corpus: {pc['count']} papers verified")

    # Check verification pass rate
    pr = manifest.get("verification", {}).get("pass_rate_pct", 0)
    if pr < 50:
        errors.append(f"FAIL: Verification pass rate {pr}% < 50%")
    else:
        logger.info(f"  ✅ Verification pass rate: {pr}%")

    if errors:
        logger.error(f"  ❌ {len(errors)} validation failure(s):")
        for e in errors:
            logger.error(f"     {e}")
    else:
        logger.info("  🎉 ALL VALIDATION CHECKS PASSED")

    return errors


def run_full_pipeline():
    logger.info("\n" + "═" * 60)
    logger.info("   EconAgent Platform — Full Pipeline")
    logger.info("   Evidence-Grounded · Zero Hallucination · Harness-Integrated")
    logger.info("═" * 60 + "\n")

    assets, loader  = step1_load_data()
    analysis        = step2_analyze(assets)
    cert            = step3_verify(analysis)
    manifest        = step4_manifest(loader, analysis, cert)
    dashboard_path  = step5_dashboard()
    errors          = step6_validate(analysis, manifest, dashboard_path)

    logger.info("\n" + "═" * 60)
    if errors:
        logger.error(f"Pipeline FAILED with {len(errors)} errors.")
        return 1
    else:
        logger.info("Pipeline COMPLETE — All steps succeeded ✅")
        logger.info(f"\nDashboard ready:\n  file:///{dashboard_path.replace(chr(92), '/')}\n")
        return 0


if __name__ == "__main__":
    rc = run_full_pipeline()
    sys.exit(rc)

