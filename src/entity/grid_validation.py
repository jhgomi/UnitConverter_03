from dataclasses import dataclass

from entity.validation_result import ValidationStatus


@dataclass(frozen=True)
class GridValidationOutcome:
    status: ValidationStatus
    failed_lines: list[str]
