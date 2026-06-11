"""pytest fixtures — README · PRD §6.2 golden · CLI runner."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]

# README §1 출력 예 · PRD §6.2 · SC-2
GOLDEN_METER_25 = (
    "2.5 meter = 2.5 meter\n"
    "2.5 meter = 8.2 feet\n"
    "2.5 meter = 2.7 yard\n"
)


@pytest.fixture
def run_cli():
    """UnitConverter.py를 subprocess로 1회 실행. (stdout, stderr, returncode) 반환."""

    def _run(user_input: str) -> tuple[str, str, int]:
        result = subprocess.run(
            [sys.executable, str(ROOT / "UnitConverter.py")],
            input=f"{user_input}\n",
            capture_output=True,
            text=True,
            cwd=str(ROOT),
        )
        return result.stdout, result.stderr, result.returncode

    return _run


@pytest.fixture
def golden_meter_25() -> str:
    return GOLDEN_METER_25
