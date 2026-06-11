from dataclasses import dataclass


@dataclass
class LengthInput:
    unit: str
    value: float
