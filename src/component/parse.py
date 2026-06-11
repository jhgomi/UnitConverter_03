from entity.length_input import LengthInput


def parse(input_str: str) -> tuple[LengthInput | None, str | None]:
    if ":" not in input_str:
        return None, "Invalid format. Use unit:value (ex: meter:2.5)"

    unit, value_str = input_str.split(":", 1)

    try:
        value = float(value_str)
    except ValueError:
        return None, f"Invalid number: {value_str}"

    return LengthInput(unit=unit, value=value, value_str=value_str), None
