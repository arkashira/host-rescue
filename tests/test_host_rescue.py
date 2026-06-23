import pytest
from host_rescue import perform_migration, main
import sys

def test_perform_migration_supported_platform():
    result = perform_migration("aws")
    assert result.success
    assert result.message == "Migration to aws successful"

def test_perform_migration_unsupported_platform():
    result = perform_migration("unknown")
    assert not result.success
    assert result.message == "Unsupported platform: unknown"

def test_main_success(capsys, monkeypatch):
    monkeypatch.setattr("sys.argv", ["host-rescue", "aws"])
    exit_code = main()
    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out == "Migration to aws successful\n"

def test_main_failure(capsys, monkeypatch):
    monkeypatch.setattr("sys.argv", ["host-rescue", "unknown"])
    exit_code = main()
    captured = capsys.readouterr()
    assert exit_code == 1
    assert captured.out == "Error: Unsupported platform: unknown\n"
