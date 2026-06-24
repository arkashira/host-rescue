import pytest
from migration_report import generate_migration_report, save_migration_report
from tempfile import TemporaryDirectory
import json

def test_generate_migration_report():
    migration_id = "test-migration"
    status = "success"
    details = "migration completed successfully"
    report = generate_migration_report(migration_id, status, details)
    assert report.migration_id == migration_id
    assert report.status == status
    assert report.details == details

def test_save_migration_report():
    with TemporaryDirectory() as tmpdir:
        migration_id = "test-migration"
        status = "success"
        details = "migration completed successfully"
        report = generate_migration_report(migration_id, status, details)
        filename = f"{tmpdir}/migration_report.json"
        save_migration_report(report, filename)
        with open(filename, "r") as f:
            data = json.load(f)
            assert data["migration_id"] == migration_id
            assert data["status"] == status
            assert data["details"] == details

def test_generate_migration_report_edge_case():
    migration_id = ""
    status = "success"
    details = "migration completed successfully"
    report = generate_migration_report(migration_id, status, details)
    assert report.migration_id == migration_id
    assert report.status == status
    assert report.details == details
