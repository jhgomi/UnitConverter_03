# green-minimal

ARRR **G 단계 (Green = GREEN ⑤)** 전용. 현재 **RED 1사이클** 테스트를 통과시키는 **최소 구현**만 `src/`(및 필요 시 `UnitConverter.py`)에 추가한다.

## Phase 선언

- 응답 **첫 줄**에 반드시: `[GREEN]`
- 이어서 (선택): `Layer: {entity|boundary} | Track: Logic | Test ID: T-…`

## 동작 조건

- **추가 입력 없이** `/green-minimal` 만으로 실행한다.
- **선행:** `/red-skeleton`으로 추가된 **실패 테스트**가 채팅·워크스페이스에 존재.
- Test ID·대상 함수는 채팅·`tests/` 최신 실패 테스트에서 **자동 추출**.
- 한 사이클 = **RED 1건**을 green으로 만드는 **최소 diff**만.

## SSOT

| 우선순위 | 문서 |
|----------|------|
| 1 | 실패 pytest traceback · 해당 테스트 Assert |
| 2 | `.cursorrules` · `docs/PRD.md` FR·§6 |
| 3 | ECB — Boundary → Component → Entity |

## 최소 구현 원칙

| 원칙 | 내용 |
|------|------|
| **범위** | 실패 Assert를 통과하는 **가장 작은** 코드만 |
| **테스트** | `tests/` **수정 금지** (Assert 완화 금지) |
| **비율** | `entity/constants.py` SSOT만 · SC-2 **하드코딩 금지** |
| **ECB** | Boundary(`validate_lines`)는 Component 위임 · Entity는 순수 데이터 |
| **OCP** | if/elif 난무 OK(1차 GREEN) — 레지스트리는 REFACTOR |

## Layer별 GREEN 대상

| Layer | 수정 허용 경로 |
|-------|----------------|
| **boundary** | `src/validate_lines.py` + 호출 Component |
| **entity** | `src/component/{parse,validate,convert,format}.py` |
| **CLI (L2)** | `UnitConverter.py` — T-FMT-01 등 §8.1 CLI TC일 때만 |

## 실행

```bash
python -m pytest tests/test_validate_lines.py::test_… -v
# 또는
python -m pytest tests/ -v
```

**GREEN 완료 조건:** 해당 Test ID 테스트 **PASSED** · 기존 green 테스트 **유지**.

## 완료 보고 (채팅)

```
[GREEN]
## green-minimal 완료
- Test ID: T-VAL-…
- 변경: src/… (+N lines)
- pytest: PASSED (해당 TC)
- 다음: /golden-master (또는 다음 RED)
```

## 금지

- `tests/` 수정 (assert 완화·삭제)
- **REFACTOR** (구조 정리·이름 변경·추출)
- SC-2 맞추기 위한 **임의 상수**
- `skip` · `xfail`
- git commit (사용자 요청 시만)

## 완료 (채팅 마지막 한 줄)

```
/golden-master 으로 넘길 준비됐다
```
