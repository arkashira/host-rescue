import json
from dataclasses import dataclass
from datetime import datetime

@dataclass
class MigrationReport:
    migration_id: str
    start_time: str
    end_time: str
    status: str
    details: str

def generate_migration_report(migration_id: str, status: str, details: str) -> MigrationReport:
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return MigrationReport(migration_id, start_time, end_time, status, details)

def save_migration_report(report: MigrationReport, filename: str) -> None:
    data = {
        "migration_id": report.migration_id,
        "start_time": report.start_time,
        "end_time": report.end_time,
        "status": report.status,
        "details": report.details
    }
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
