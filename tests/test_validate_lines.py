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
