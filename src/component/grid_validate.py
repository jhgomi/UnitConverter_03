from component.convert import convert
from component.format import format_lines
from component.parse import parse
from entity.grid_validation import GridValidationOutcome

REQUIRED_GRID_LINES = 3


def parse_grid_line(line: str) -> tuple[str, str] | None:
    if " = " not in line:
        return None

    left, _right = line.split(" = ", 1)
    parts = left.rsplit(" ", 1)
    if len(parts) != 2:
        return None

    return parts[0], parts[1]


def evaluate_grid(grid: list[str]) -> GridValidationOutcome:
    if not grid:
        return GridValidationOutcome(status="incomplete", failed_lines=[])

    if len(grid) < REQUIRED_GRID_LINES:
        return GridValidationOutcome(status="incomplete", failed_lines=[])

    parsed = parse_grid_line(grid[0])
    if parsed is None:
        return GridValidationOutcome(status="fail", failed_lines=[grid[0]])

    value_str, unit = parsed
    input_str = f"{unit}:{value_str}"
    length_input, parse_error = parse(input_str)
    if parse_error is not None or length_input is None:
        return GridValidationOutcome(status="fail", failed_lines=list(grid))

    expected = format_lines(convert(length_input), length_input)
    failed_lines = [
        line for line, expected_line in zip(grid, expected) if line != expected_line
    ]

    if failed_lines:
        return GridValidationOutcome(status="fail", failed_lines=failed_lines)

    return GridValidationOutcome(status="pass", failed_lines=[])
