"""pytest fixtures — README · PRD §6.2 golden · CLI runner."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = Path(__file__).resolve().parent / "fixtures"

GOLDEN_SC2_METER_PATH = FIXTURES / "golden_sc2_meter.txt"
GOLDEN_SC2_FEET_PATH = FIXTURES / "golden_sc2_feet.txt"


def _load_fixture_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _load_fixture_grid(path: Path) -> list[str]:
    text = _load_fixture_text(path)
    return text.rstrip("\n").split("\n")


# README §1 · PRD §6.2 · SC-2 (fixture SSOT)
GOLDEN_METER_25 = _load_fixture_text(GOLDEN_SC2_METER_PATH)


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
    """T-FMT-01 호환 alias — golden_sc2_text와 동일."""
    return GOLDEN_METER_25


@pytest.fixture
def golden_sc2_text() -> str:
    """GM-SC2-METER: PRD §6.2 3줄 (줄바꿈 \\n 고정)."""
    return GOLDEN_METER_25


@pytest.fixture
def golden_sc2_grid() -> list[str]:
    """GM-SC2-METER: §6.2 grid 리스트."""
    return _load_fixture_grid(GOLDEN_SC2_METER_PATH)


@pytest.fixture
def golden_sc2_feet_text() -> str:
    """GM-SC2-FEET: feet:8.2 3줄 (SSOT 비율 · FR-10 1자리)."""
    return _load_fixture_text(GOLDEN_SC2_FEET_PATH)
