import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from component.convert import convert
from component.format import format_lines
from component.parse import parse
from component.validate import validate_input


def main() -> None:
    input_str = input().strip()

    length_input, parse_error = parse(input_str)
    if parse_error is not None:
        print(parse_error)
        return

    validation_error = validate_input(length_input)
    if validation_error is not None:
        print(validation_error)
        return

    conversion_lines = convert(length_input)
    for line in format_lines(conversion_lines, length_input):
        print(line)


if __name__ == "__main__":
    main()
