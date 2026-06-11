"""PRD §8.1 Test ID — CLI (L2) · SC-1~3 AAA 스켈레톤."""

from __future__ import annotations

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


# --- T-FMT-01 | FR-3,10 SC-2 | meter:2.5 ---


def test_t_fmt_01_meter_output_sc2(run_cli, golden_meter_25):
    """T-FMT-01: meter:2.5 → README §출력 예 3줄 · 8.2 feet · 2.7 yard."""
    # Arrange
    user_input = "meter:2.5"

    # Act
    stdout, stderr, _exit_code = run_cli(user_input)
    output = _combined_output(stdout, stderr)

    # Assert
    assert "8.2 feet" in output
    assert "2.7 yard" in output
    assert stdout == golden_meter_25


# --- T-NEG-01 | FR-8 SC-3 | meter:-2.5 ---


def test_t_neg_01_negative_meter_rejected(run_cli):
    """T-NEG-01: meter:-2.5 → 변환 없음 · Negative value not allowed."""
    # Arrange
    user_input = "meter:-2.5"

    # Act
    stdout, stderr, _exit_code = run_cli(user_input)
    output = _combined_output(stdout, stderr)

    # Assert
    assert "Negative value not allowed: -2.5" in output
    _assert_no_conversion_output(stdout)


# --- T-SAME-01 | FR-12 SC-1 | meter:2.5 2회 ---


def test_t_same_01_deterministic_output(run_cli):
    """T-SAME-01: 동일 입력 2회 → stdout 바이트 동일."""
    # Arrange
    user_input = "meter:2.5"

    # Act
    stdout_first, stderr_first, _ = run_cli(user_input)
    stdout_second, stderr_second, _ = run_cli(user_input)

    # Assert
    assert stdout_first == stdout_second
    assert stderr_first == stderr_second


# --- T-FMT-ERR | FR-6 | meter (콜론 없음) ---


def test_t_fmt_err_missing_colon(run_cli):
    """T-FMT-ERR: meter → Invalid format."""
    # Arrange
    user_input = "meter"

    # Act
    stdout, stderr, _exit_code = run_cli(user_input)
    output = _combined_output(stdout, stderr)

    # Assert
    assert "Invalid format. Use unit:value (ex: meter:2.5)" in output
    _assert_no_conversion_output(stdout)


# --- T-NUM-ERR | FR-7 | meter:abc ---


def test_t_num_err_invalid_number(run_cli):
    """T-NUM-ERR: meter:abc → Invalid number: abc."""
    # Arrange
    user_input = "meter:abc"

    # Act
    stdout, stderr, _exit_code = run_cli(user_input)
    output = _combined_output(stdout, stderr)

    # Assert
    assert "Invalid number: abc" in output
    _assert_no_conversion_output(stdout)


# --- T-UNIT-ERR | FR-9 | inch:1 ---


def test_t_unit_err_unknown_unit(run_cli):
    """T-UNIT-ERR: inch:1 → Unknown unit: inch."""
    # Arrange
    user_input = "inch:1"

    # Act
    stdout, stderr, _exit_code = run_cli(user_input)
    output = _combined_output(stdout, stderr)

    # Assert
    assert "Unknown unit: inch" in output
    _assert_no_conversion_output(stdout)


# --- T-CONV-FT | FR-4,5 | feet:8.2 ---


def test_t_conv_ft_feet_input_three_units(run_cli):
    """T-CONV-FT: feet:8.2 → meter·yard 변환 줄 · 3단위 전부."""
    # Arrange
    user_input = "feet:8.2"

    # Act
    stdout, stderr, _exit_code = run_cli(user_input)
    output = _combined_output(stdout, stderr)
    lines = [ln for ln in stdout.splitlines() if ln.strip()]

    # Assert
    assert len(lines) == 3
    assert any("feet" in ln and "8.2" in ln for ln in lines)
    assert any(" meter" in ln or ln.endswith(" meter") for ln in lines)
    assert any(" yard" in ln or ln.endswith(" yard") for ln in lines)
    assert CONVERSION_LINE in output
