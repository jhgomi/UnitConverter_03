# tdd-red

`validate_lines(grid)` TDD **RED** 단계 전용. 실패하는 테스트를 `tests/`에만 추가한다.

## Phase 선언

- 응답 **첫 줄**에 반드시: `[RED]`
- 한 사이클 = **테스트 1건**(또는 동일 행동 1그룹)만 추가. GREEN·REFACTOR는 이 Command 범위 밖.

## 대상

| 항목 | 값 |
|------|-----|
| **Boundary API** | `validate_lines(grid) -> ValidationResult` |
| **grid** | conversion line `list[str]` — `{value} {unit} = {converted} {target}` |
| **반환** | `{ "status": "pass"\|"fail"\|"incomplete", "failed_lines": [...] }` |
| **테스트 파일** | `tests/test_validate_lines.py` |
| **SSOT** | `.cursorrules` · `docs/PRD.md` §8.1 (Mom Test TC) |

## AAA 절차

각 테스트는 **Arrange → Act → Assert** 순서로 작성한다.

1. **Arrange** — `grid`(입력 줄 리스트)와 기대 `status`·`failed_lines`를 Given으로 고정.
2. **Act** — `result = validate_lines(grid)` 한 번 호출.
3. **Assert** — `result["status"]`, `result["failed_lines"]`를 PRD/README 기대와 **엄격히** 비교.

주석으로 AAA 구간을 표시한다.

```python
def test_empty_grid_is_incomplete():
    # Arrange
    grid = []

    # Act
    result = validate_lines(grid)

    # Assert
    assert result["status"] == "incomplete"
    assert result["failed_lines"] == []
```

## RED 우선 케이스 (Mom Test → validate_lines)

| Test ID | Given (grid) | Then |
|---------|--------------|------|
| **T-VAL-PASS-01** | SC-2 정답 3줄 (`meter:2.5` 변환) | `status == "pass"`, `failed_lines == []` |
| **T-VAL-FAIL-01** | feet 줄이 `8.2021`(README 불일치) | `status == "fail"`, `failed_lines`에 해당 줄 |
| **T-VAL-INC-01** | `grid == []` | `status == "incomplete"` |
| **T-VAL-INC-02** | 필수 줄 1~2개만 (3단위 미만) | `status == "incomplete"` |

SC-2 정답 grid 예 (Arrange용):

```python
grid = [
    "2.5 meter = 2.5 meter",
    "2.5 meter = 8.2 feet",
    "2.5 meter = 2.7 yard",
]
```

## pytest 예시

```python
from validate_lines import validate_lines


def test_sc2_valid_grid_passes():
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
```

## 실행

```bash
python -m pytest tests/test_validate_lines.py -v
```

RED 완료 조건: **새 테스트가 FAILED** (구현 미완 또는 `...` stub). PASSED면 테스트가 약하거나 이미 GREEN — RED 재검토.

## 완료 보고 (채팅)

```
[RED]
## RED 완료
- Test ID: T-VAL-…
- Given: …
- Then: …
- 변경: tests/test_validate_lines.py (+N lines)
- pytest: FAILED — … (expected)
```

## 금지

- `src/` 및 `UnitConverter.py` **수정** (GREEN에서만)
- assert 완화·삭제·`skip`·`xfail`
- 테스트 통과를 위해 기대값을 실제(잘못된) 출력에 맞추기
- 한 RED 사이클에 여러 무관 Test ID 동시 추가
- git commit (사용자 요청 시만)
