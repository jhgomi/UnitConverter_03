from entity.conversion_line import ConversionLine
from entity.length_input import LengthInput


def _format_converted_value(
    converted_value: float, target_unit: str, source: LengthInput
) -> str:
    if target_unit == source.unit:
        return source.value_str
    return f"{round(converted_value, 1):.1f}"


def format_lines(
    conversion_lines: list[ConversionLine], source: LengthInput
) -> list[str]:
    return [
        f"{source.value_str} {source.unit} = "
        f"{_format_converted_value(line.converted_value, line.target_unit, source)} "
        f"{line.target_unit}"
        for line in conversion_lines
    ]
