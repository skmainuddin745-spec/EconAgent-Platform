"""
Unit Tests: Econometric Sanity Bounds and Metric Distributions
EconAgent Platform v2.1.0
"""

import unittest
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

class TestSanityBounds(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        report_path = REPO_ROOT / "reports" / "verified_econ_report.json"
        with open(report_path, "r", encoding="utf-8") as f:
            cls.report = json.load(f)
        cls.by_agent = cls.report.get("by_agent", {})

    def test_all_18_agents_present(self):
        expected_agents = [
            "MACRO_ERP", "MICRO_BETA", "MICRO_MARGINS", "MICRO_MULTIPLES",
            "MICRO_GROWTH", "MICRO_CAPSTRUCT", "MACRO_WACC", "MICRO_DIVIDEND",
            "MICRO_WORKCAP", "MICRO_TAXRATE", "MICRO_CAPEX", "MICRO_EVA",
            "MICRO_GOVERNANCE", "MICRO_INTANGIBLES", "MICRO_VOLAT",
            "MICRO_FINFLOWS", "SOIC_TECH_RANKING", "COMMODITY_TANKER_FLOWS"
        ]
        for aid in expected_agents:
            self.assertIn(aid, self.by_agent, f"Agent {aid} must be present in report")
            self.assertGreater(len(self.by_agent[aid]), 0, f"Agent {aid} must produce at least one metric")

    def test_implied_erp_bounds(self):
        erp_results = self.by_agent.get("MACRO_ERP", [])
        primary_erp = next((r for r in erp_results if "Implied ERP by Country" in r.get("metric", "")), None)
        self.assertIsNotNone(primary_erp, "Primary country ERP metric must exist")
        
        val = primary_erp.get("value", {})
        us_erp = val.get("us_erp_pct")
        global_median = val.get("global_median_pct")
        
        self.assertIsNotNone(us_erp)
        self.assertAlmostEqual(us_erp, 4.40, places=1, msg="US Implied ERP must be ~4.40%")
        self.assertGreater(global_median, us_erp, "Global median ERP must reflect sovereign risk premium over US")

    def test_wacc_bounds(self):
        wacc_results = self.by_agent.get("MACRO_WACC", [])
        for r in wacc_results:
            val = r.get("value", {})
            for k in ["median_pct", "mean_pct"]:
                if k in val:
                    w_pct = val[k]
                    self.assertGreaterEqual(w_pct, 1.0, f"WACC {w_pct}% too low")
                    self.assertLessEqual(w_pct, 30.0, f"WACC {w_pct}% unreasonably high")

    def test_beta_bounds(self):
        beta_results = self.by_agent.get("MICRO_BETA", [])
        for r in beta_results:
            val = r.get("value", {})
            for bk in ["unlevered_beta_median", "levered_beta_median", "median"]:
                if bk in val:
                    b = val[bk]
                    self.assertGreater(b, 0.1, f"Beta {b} below realistic bound")
                    self.assertLess(b, 4.0, f"Beta {b} above realistic bound")


if __name__ == "__main__":
    unittest.main()
