"""PRD §4 성공 기준 (SC-1~3) — AAA 스켈레톤.

| SC | 기준 | Test ID |
|----|------|---------|
| SC-1 | 동일 입력 → 바이트 동일 | T-SAME-01 |
| SC-2 | README 비율·정밀도 (`8.2 feet`, `2.7 yard`) | T-FMT-01 · T-VAL-PASS-01 |
| SC-3 | 음수·형식·미지원 단위 → 변환 없이 오류 | T-NEG-01 · T-FMT/NUM/UNIT-ERR |
"""

from __future__ import annotations

import pytest

from validate_lines import validate_lines

CONVERSION_LINE = " = "


def _combined_output(stdout: str, stderr: str) -> str:
    return stdout + stderr


def _assert_no_conversion_output(stdout: str) -> None:
    """변환 줄 `{value} {unit} = {converted} {target}` 패턴 없음."""
    for line in stdout.splitlines():
        if CONVERSION_LINE in line:
            parts = line.split(CONVERSION_LINE, 1)
            if len(parts) == 2 and parts[1].strip():
                raise AssertionError(f"unexpected conversion line: {line!r}")


# --- SC-1 | FR-12 | 동일 입력 → 바이트 단위 동일 ---


def test_sc1_deterministic_output(run_cli):
    """SC-1: meter:2.5 2회 연속 → stdout·stderr 바이트 동일."""
    # Arrange
    user_input = "meter:2.5"

    # Act
    stdout_first, stderr_first, _ = run_cli(user_input)
    stdout_second, stderr_second, _ = run_cli(user_input)

    # Assert
    assert stdout_first == stdout_second
    assert stderr_first == stderr_second


# --- SC-2 | FR-3,10 | README 비율·문서화된 정밀도 ---


def test_sc2_cli_readme_precision(run_cli, golden_sc2_text):
    """SC-2: meter:2.5 → §6.2 3줄 · 8.2 feet · 2.7 yard."""
    # Arrange
    user_input = "meter:2.5"

    # Act
    stdout, stderr, _exit_code = run_cli(user_input)

    # Assert
    assert "8.2 feet" in stdout
    assert "2.7 yard" in stdout
    assert stdout == golden_sc2_text
    assert stderr == ""


def test_sc2_grid_validate_lines_passes(golden_sc2_grid):
    """SC-2: §6.2 정답 grid → validate_lines pass."""
    # Arrange
    grid = golden_sc2_grid

    # Act
    result = validate_lines(grid)

    # Assert
    assert result["status"] == "pass"
    assert result["failed_lines"] == []


# --- SC-3 | FR-6~9 | 변환 없이 오류 메시지 ---


@pytest.mark.parametrize(
    "user_input,expected_error",
    [
        ("meter:-2.5", "Negative value not allowed: -2.5"),
        ("meter", "Invalid format. Use unit:value (ex: meter:2.5)"),
        ("meter:abc", "Invalid number: abc"),
        ("inch:1", "Unknown unit: inch"),
    ],
    ids=["negative", "format", "number", "unit"],
)
def test_sc3_error_without_conversion(run_cli, user_input, expected_error):
    """SC-3: 오류 입력 → 변환 줄 없음 · §6.3 오류 메시지."""
    # Arrange / Act
    stdout, stderr, _exit_code = run_cli(user_input)
    output = _combined_output(stdout, stderr)

    # Assert
    assert expected_error in output
    _assert_no_conversion_output(stdout)
