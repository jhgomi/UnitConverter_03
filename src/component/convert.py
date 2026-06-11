from entity.constants import METER_TO_FEET, METER_TO_YARD, SUPPORTED_UNITS
from entity.conversion_line import ConversionLine
from entity.length_input import LengthInput


def _to_meters(length_input: LengthInput) -> float:
    if length_input.unit == "meter":
        return length_input.value
    if length_input.unit == "feet":
        return length_input.value / METER_TO_FEET
    if length_input.unit == "yard":
        return length_input.value / METER_TO_YARD
    raise ValueError(f"Unknown unit: {length_input.unit}")


def _from_meters(meters: float, target_unit: str) -> float:
    if target_unit == "meter":
        return meters
    if target_unit == "feet":
        return meters * METER_TO_FEET
    if target_unit == "yard":
        return meters * METER_TO_YARD
    raise ValueError(f"Unknown unit: {target_unit}")


def convert(length_input: LengthInput) -> list[ConversionLine]:
    meters = _to_meters(length_input)
    return [
        ConversionLine(
            source_value=length_input.value,
            source_unit=length_input.unit,
            converted_value=_from_meters(meters, target_unit),
            target_unit=target_unit,
        )
        for target_unit in SUPPORTED_UNITS
    ]
