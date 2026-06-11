"""PRD §4 SC-2 · T-VAL-* — Boundary (L1) AAA 스켈레톤."""

from validate_lines import validate_lines


def test_sc2_valid_grid_passes():
    """T-VAL-PASS-01: SC-2 정답 grid 3줄 → pass, failed_lines=[]."""
    # Arrange
    grid = [
        "2.5 meter = 2.5 meter",
        "2.5 meter = 8.2 feet",
        "2.5 meter = 2.7 yard",
    ]

    # Act
    result = validate_lines(grid)

    # Assert
    assert result["status"] == "pass"
    assert result["failed_lines"] == []


def test_wrong_precision_fails():
    """T-VAL-FAIL-01: Mom Test F1 — feet 줄 8.2021 → fail, 해당 줄 in failed_lines."""
    # Arrange
    grid = [
        "2.5 meter = 2.5 meter",
        "2.5 meter = 8.2021 feet",
        "2.5 meter = 2.7 yard",
    ]

    # Act
    result = validate_lines(grid)

    # Assert
    assert result["status"] == "fail"
    assert "2.5 meter = 8.2021 feet" in result["failed_lines"]


def test_empty_grid_is_incomplete():
    """T-VAL-INC-01: grid == [] → incomplete, failed_lines=[]."""
    # Arrange
    grid: list[str] = []

    # Act
    result = validate_lines(grid)

    # Assert
    assert result["status"] == "incomplete"
    assert result["failed_lines"] == []


def test_short_grid_is_incomplete():
    """T-VAL-INC-02: 3단위 미만(2줄) → incomplete."""
    # Arrange
    grid = [
        "2.5 meter = 2.5 meter",
        "2.5 meter = 8.2 feet",
    ]

    # Act
    result = validate_lines(grid)

    # Assert
    assert result["status"] == "incomplete"
    assert result["failed_lines"] == []
