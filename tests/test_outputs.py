import json
from pathlib import Path


def _load_report():
    report_path = Path("/app/report.json")
    assert report_path.exists(), "report.json missing at /app/report.json"
    with open(report_path) as f:
        return json.load(f)


def test_total_requests():
    """Success criterion 1: `total_requests` is the total number of HTTP requests in the log."""
    data = _load_report()
    assert data.get("total_requests") == 6


def test_unique_ips():
    """Success criterion 2: `unique_ips` is the count of unique client IP addresses."""
    data = _load_report()
    assert data.get("unique_ips") == 3


def test_top_path():
    """Success criterion 3: `top_path` is the exact path of the most frequently requested page."""
    data = _load_report()
    assert data.get("top_path") == "/index.html"
