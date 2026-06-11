from dataclasses import dataclass


@dataclass
class LengthInput:
    unit: str
    value: float
    value_str: str
