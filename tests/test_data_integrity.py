"""
Unit Tests: Data Integrity and Cryptographic Provenance
EconAgent Platform v2.1.0
"""

import unittest
import json
import hashlib
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

class TestDataIntegrity(unittest.TestCase):

    def test_verified_econ_report_exists_and_valid(self):
        report_path = REPO_ROOT / "reports" / "verified_econ_report.json"
        self.assertTrue(report_path.exists(), "verified_econ_report.json must exist")
        with open(report_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        self.assertIn("total_results", data)
        self.assertEqual(data["total_results"], 251, "Must contain exactly 251 derived metrics")
        self.assertGreaterEqual(data["pass_rate_pct"], 98.0, "Pass rate must be >= 98.0%")
        self.assertIn("sha256_signature", data)
        self.assertEqual(len(data["sha256_signature"]), 64, "SHA-256 signature must be 64 hex characters")

    def test_platform_manifest(self):
        manifest_path = REPO_ROOT / "reports" / "platform_manifest.json"
        self.assertTrue(manifest_path.exists(), "platform_manifest.json must exist")
        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest = json.load(f)
        
        self.assertEqual(manifest.get("platform"), "EconAgent Platform")
        agents = manifest.get("analysis", {}).get("agents", [])
        self.assertEqual(len(agents), 18, "Must track all 18 specialized agents")
        self.assertIn("ERPAnalysisAgent", agents)
        self.assertIn("OilTankerCommodityAgent", agents)

    def test_data_load_report(self):
        load_report_path = REPO_ROOT / "reports" / "data_load_report.json"
        self.assertTrue(load_report_path.exists(), "data_load_report.json must exist")
        with open(load_report_path, "r", encoding="utf-8") as f:
            load_data = json.load(f)
        
        loaded_ok = load_data.get("loaded_ok", 0)
        self.assertGreaterEqual(loaded_ok, 500, f"Must have loaded >= 500 workbooks (got {loaded_ok})")


if __name__ == "__main__":
    unittest.main()
