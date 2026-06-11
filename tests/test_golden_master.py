"""Golden Master — SC-1·SC-2 회귀 고정 (PRD §6.2 · §4 SC-1~2)."""

from __future__ import annotations

from pathlib import Path

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def _combined_output(stdout: str, stderr: str) -> str:
    return stdout + stderr


# --- GM-SC2-METER | PRD §6.2 · SC-2 | meter:2.5 ---


def test_gm_sc2_meter_cli_matches_fixture(run_cli, golden_sc2_text):
    """GM-SC2-METER: meter:2.5 CLI stdout == golden_sc2_meter.txt (바이트 고정)."""
    # Arrange
    user_input = "meter:2.5"

    # Act
    stdout, stderr, _exit_code = run_cli(user_input)

    # Assert
    assert stdout == golden_sc2_text
    assert stderr == ""


def test_gm_sc2_meter_grid_matches_fixture(golden_sc2_grid, golden_sc2_text):
    """GM-SC2-METER: golden grid 3줄 == fixture 텍스트 split."""
    # Arrange / Act
    lines_from_text = golden_sc2_text.rstrip("\n").split("\n")

    # Assert
    assert golden_sc2_grid == lines_from_text
    assert golden_sc2_grid == [
        "2.5 meter = 2.5 meter",
        "2.5 meter = 8.2 feet",
        "2.5 meter = 2.7 yard",
    ]


# --- GM-SC2-FEET | FR-4·5 · T-CONV-FT | feet:8.2 ---


def test_gm_sc2_feet_cli_matches_fixture(run_cli, golden_sc2_feet_text):
    """GM-SC2-FEET: feet:8.2 → 3단위 · SSOT 비율 · FR-10 1자리."""
    # Arrange
    user_input = "feet:8.2"

    # Act
    stdout, stderr, _exit_code = run_cli(user_input)

    # Assert
    assert stdout == golden_sc2_feet_text
    assert stderr == ""


# --- GM-SC1-BYTES | SC-1 · T-SAME-01 | meter:2.5 2회 ---


def test_gm_sc1_bytes_deterministic_and_golden(run_cli, golden_sc2_text):
    """GM-SC1-BYTES: 동일 입력 2회 stdout 바이트 동일 + §6.2 golden 일치."""
    # Arrange
    user_input = "meter:2.5"

    # Act
    stdout_first, stderr_first, _ = run_cli(user_input)
    stdout_second, stderr_second, _ = run_cli(user_input)

    # Assert
    assert stdout_first == stdout_second
    assert stderr_first == stderr_second
    assert stdout_first == golden_sc2_text
    assert _combined_output(stdout_first, stderr_first) == golden_sc2_text
