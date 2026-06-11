from component.grid_validate import evaluate_grid
from entity.validation_result import ValidationResult


def validate_lines(grid: list[str]) -> ValidationResult:
    outcome = evaluate_grid(grid)
    return {
        "status": outcome.status,
        "failed_lines": outcome.failed_lines,
    }
