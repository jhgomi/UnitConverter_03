"""GREEN PASS Approval Test — Golden Master · Boundary · CLI Exit Criteria (TEST_PLAN §9)."""

from __future__ import annotations

from validate_lines import validate_lines

# PRD §8.1 L2 Test ID — GREEN PASS 승인 대상
APPROVAL_L2_TEST_IDS = (
    "T-FMT-01",
    "T-NEG-01",
    "T-SAME-01",
    "T-FMT-ERR",
    "T-NUM-ERR",
    "T-UNIT-ERR",
    "T-CONV-FT",
)

# Boundary T-VAL-* — GREEN PASS 승인 대상
APPROVAL_L1_TEST_IDS = (
    "T-VAL-PASS-01",
    "T-VAL-FAIL-01",
    "T-VAL-INC-01",
    "T-VAL-INC-02",
)

# Golden Master — GREEN PASS 승인 대상
APPROVAL_GM_IDS = (
    "GM-SC2-METER",
    "GM-SC2-FEET",
    "GM-SC1-BYTES",
)


def test_approval_golden_grid_passes_validate_lines(golden_sc2_grid):
    """AT-GM-01: GM-SC2-METER grid → validate_lines pass (L4 ↔ L1 승인)."""
    # Arrange
    grid = golden_sc2_grid

    # Act
    result = validate_lines(grid)

    # Assert
    assert result["status"] == "pass"
    assert result["failed_lines"] == []


def test_approval_cli_stdout_validates_as_golden_grid(run_cli, golden_sc2_grid, golden_sc2_text):
    """AT-GM-02: CLI meter:2.5 stdout == golden · grid → validate_lines pass."""
    # Arrange
    user_input = "meter:2.5"

    # Act
    stdout, stderr, _exit_code = run_cli(user_input)
    lines = stdout.rstrip("\n").split("\n")
    result = validate_lines(lines)

    # Assert
    assert stderr == ""
    assert stdout == golden_sc2_text
    assert lines == golden_sc2_grid
    assert result["status"] == "pass"
    assert result["failed_lines"] == []


def test_approval_mom_test_wrong_precision_rejected():
    """AT-SC2-01: Mom Test F1(8.2021) grid → validate_lines fail (SC-2 승인)."""
    # Arrange
    grid = [
        "2.5 meter = 2.5 meter",
        "2.5 meter = 8.2021 feet",
        "2.5 meter = 2.7 yard",
    ]

    # Act
    result = validate_lines(grid)

    # Assert
    assert result["status"] == "fail"
    assert "2.5 meter = 8.2021 feet" in result["failed_lines"]


def test_approval_green_pass_exit_criteria_registered():
    """AT-EXIT-01: GREEN PASS Exit Criteria Test ID · Golden ID 등록 확인."""
    # Arrange / Act / Assert
    assert len(APPROVAL_L2_TEST_IDS) == 7
    assert len(APPROVAL_L1_TEST_IDS) == 4
    assert len(APPROVAL_GM_IDS) == 3
    assert "GM-SC2-METER" in APPROVAL_GM_IDS
    assert "T-VAL-PASS-01" in APPROVAL_L1_TEST_IDS
