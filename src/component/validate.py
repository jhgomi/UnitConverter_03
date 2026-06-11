from entity.constants import SUPPORTED_UNITS
from entity.length_input import LengthInput


def validate_input(length_input: LengthInput) -> str | None:
    if length_input.value < 0:
        return f"Negative value not allowed: {length_input.value_str}"

    if length_input.unit not in SUPPORTED_UNITS:
        return f"Unknown unit: {length_input.unit}"

    return None
