from dataclasses import dataclass


@dataclass
class ConversionLine:
    source_value: float
    source_unit: str
    converted_value: float
    target_unit: str
