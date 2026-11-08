"""
Unit Tests: Dashboard and Photoview Artifact Integrity
EconAgent Platform v2.1.0
"""

import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

class TestDashboardIntegrity(unittest.TestCase):

    def test_dashboard_html_exists_and_substantial(self):
        dash_path = REPO_ROOT / "platform_ui" / "EconAgent_Dashboard.html"
        self.assertTrue(dash_path.exists(), "EconAgent_Dashboard.html must exist")
        size = dash_path.stat().st_size
        self.assertGreater(size, 1_000_000, f"Dashboard size ({size} bytes) should exceed 1 MB")

    def test_bmap_html_exists(self):
        bmap_path = REPO_ROOT / "platform_ui" / "Bloomberg_BMAP_Terminal.html"
        self.assertTrue(bmap_path.exists(), "Bloomberg_BMAP_Terminal.html must exist")
        size = bmap_path.stat().st_size
        self.assertGreater(size, 500_000, f"BMAP size ({size} bytes) should exceed 500 KB")

    def test_photoview_screenshots_exist(self):
        scr_dir = REPO_ROOT / "docs" / "screenshots"
        self.assertTrue(scr_dir.exists(), "docs/screenshots directory must exist")
        
        expected_shots = [
            "terminal_hero_overview.png",
            "terminal_f10_macro_simulator.png",
            "terminal_f5_soic_scorecard.png",
            "terminal_f3_weinstein_technicals.png",
            "terminal_f8_financing_flows.png",
            "terminal_institutional_titans.png",
            "terminal_damodaran_94_industries.png",
            "terminal_sectoral_rotation.png",
            "terminal_semiconductor_cockpit.png",
            "terminal_global_company_lookup.png",
            "terminal_topnotch_agent_pods.png",
            "terminal_bmap_maritime_radar.jpg",
            "terminal_bmap_chokepoints.jpg"
        ]
        
        for shot_name in expected_shots:
            p = scr_dir / shot_name
            self.assertTrue(p.exists(), f"Screenshot {shot_name} must exist")
            self.assertGreater(p.stat().st_size, 10_000, f"Screenshot {shot_name} must not be empty")


if __name__ == "__main__":
    unittest.main()
