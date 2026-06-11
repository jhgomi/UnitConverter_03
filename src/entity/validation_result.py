from typing import Literal, TypedDict

ValidationStatus = Literal["pass", "fail", "incomplete"]


class ValidationResult(TypedDict):
    status: ValidationStatus
    failed_lines: list[str]
