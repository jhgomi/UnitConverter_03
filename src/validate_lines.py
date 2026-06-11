from component.convert import convert
from component.format import format_lines
from component.parse import parse
from entity.validation_result import ValidationResult


def _parse_grid_line(line: str) -> tuple[str, str] | None:
    if " = " not in line:
        return None

    left, _right = line.split(" = ", 1)
    parts = left.rsplit(" ", 1)
    if len(parts) != 2:
        return None

    return parts[0], parts[1]


def validate_lines(grid: list[str]) -> ValidationResult:
    if not grid:
        return {"status": "incomplete", "failed_lines": []}

    if len(grid) < 3:
        return {"status": "incomplete", "failed_lines": []}

    parsed = _parse_grid_line(grid[0])
    if parsed is None:
        return {"status": "fail", "failed_lines": [grid[0]]}

    value_str, unit = parsed
    input_str = f"{unit}:{value_str}"
    length_input, parse_error = parse(input_str)
    if parse_error is not None or length_input is None:
        return {"status": "fail", "failed_lines": list(grid)}

    expected = format_lines(convert(length_input), length_input)
    failed_lines = [line for line, expected_line in zip(grid, expected) if line != expected_line]

    if failed_lines:
        return {"status": "fail", "failed_lines": failed_lines}

    return {"status": "pass", "failed_lines": []}
