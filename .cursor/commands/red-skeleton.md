# red-skeleton

ARRR **R 단계 (Red = RED ④)** 전용. `/red-test-plan`에서 확정한 **Test ID 1건**의 pytest **스켈레톤**을 `tests/`에만 추가한다.

## Phase 선언

- 응답 **첫 줄**에 반드시:

```
Phase: red | Layer: {entity|boundary} | Track: {Logic|UI}
```

- 채팅에 `/red-test-plan` 결과가 있으면 **동일 Layer·Track·Test ID**를 사용한다.
- 없으면 Layer=`boundary`, Track=`Logic`, Test ID=`T-VAL-PASS-01` (Mom Test · SC-2 우선).

## 동작 조건

- **추가 입력 없이** `/red-skeleton` 만으로 실행한다.
- **선행:** `/red-test-plan` 완료(채팅에 C2C·테스트 플랜) 또는 PRD §8.1 Test ID가 채팅에 존재.
- 한 사이클 = **테스트 함수 1개**(또는 tdd-red 동일 그룹 1묶음)만 추가.

## SSOT

| 우선순위 | 문서 |
|----------|------|
| 1 | 채팅 — `/red-test-plan` 블록 2·3 |
| 2 | `.cursorrules` · `docs/PRD.md` §8.1 |
| 3 | `.cursor/commands/tdd-red.md` · `docs/TEST_PLAN.md` |

## 대상 (UnitConverter_03)

| Layer | 테스트 파일 | SUT import |
|-------|-------------|------------|
| **boundary** | `tests/test_validate_lines.py` | `from validate_lines import validate_lines` |
| **entity** | `tests/test_{module}.py` | `from component.{module} import …` |

## AAA 스켈레톤 규칙

1. **Arrange** — Given 리터럴(grid / `unit:value`). conftest 픽스처는 플랜에 있을 때만 추가.
2. **Act** — SUT **1회** 호출.
3. **Assert** — Then을 PRD §6·§8.1과 **엄격** 비교. 주석 `# Arrange` / `# Act` / `# Assert` 필수.

boundary 예 (`T-VAL-PASS-01`):

```python
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
```

## 실행

```bash
python -m pytest tests/test_validate_lines.py::test_… -v
```

**RED 완료 조건:** 새 테스트 **FAILED** (stub `...` · 미구현 · AssertionError). PASSED면 테스트 약함 — RED 재검토.

## 완료 보고 (채팅)

```
Phase: red | Layer: boundary | Track: Logic
## red-skeleton 완료
- Test ID: T-VAL-…
- 파일: tests/test_validate_lines.py (+N lines, 함수명)
- pytest: FAILED — … (expected)
- 다음: /green-minimal
```

## 금지

- `src/` · `UnitConverter.py` **수정**
- **GREEN** · **REFACTOR**
- assert 완화·`skip`·`xfail`
- 플랜과 무관한 Test ID 동시 추가
- git commit (사용자 요청 시만)

## 완료 (채팅 마지막 한 줄)

```
/green-minimal 으로 넘길 준비됐다
```
