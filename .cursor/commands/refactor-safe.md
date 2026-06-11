# refactor-safe

ARRR **R 단계 (Refactor = REFACTOR ⑥-B)** 전용. `/refactor-smell` To-Do **1건**만 **동작-preserving** 리팩터. pytest **전체 green** 유지.

## Phase 선언

- 응답 **첫 줄**에 반드시: `[REFACTOR]`
- 이어서: `Safe Refactor | Smell ID: S-… | Layer: …`

## 동작 조건

- **추가 입력 없이** `/refactor-safe` 만으로 실행한다.
- **선행:** `/refactor-smell` 블록 3 To-Do (채팅) 또는 smell 표.
- To-Do **1건**만 수행 — 여러 smell 동시 수정 금지.
- Smell ID가 없으면 우선순위 **S-IFELIF** → **S-GOD-FUNC** 순.

## SSOT

| 우선순위 | 문서 |
|----------|------|
| 1 | 채팅 — `/refactor-smell` To-Do |
| 2 | `docs/PRD.md` FR-13 · FR-14 |
| 3 | `.cursorrules` ECB |

## 안전 리팩터 규칙

| 규칙 | 내용 |
|------|------|
| **테스트 고정** | `tests/` **수정 금지** (green 유지) |
| **행동 동일** | 공개 API·출력 바이트·ValidationResult 불변 |
| **ECB** | Component 추출 · Boundary는 위임만 · Entity I/O 없음 |
| **OCP** | 단위 레지스트리·전략 패턴으로 if/elif 축소 |
| **범위** | smell 1건에 필요한 **최소 diff** |

## Layer별 허용 변경

| Layer | 경로 |
|-------|------|
| Component | `src/component/*.py` |
| Entity | `src/entity/*.py` (순수 데이터·상수) |
| Boundary | `src/validate_lines.py`, `UnitConverter.py` (위임만) |

## Smell → 패턴 매핑

| Smell ID | 안전 패턴 |
|----------|-----------|
| **S-IFELIF** | `UNIT_REGISTRY: dict[str, Converter]` 추출 |
| **S-GOD-FUNC** | parse / validate / convert / format 함수 분리 |
| **S-MAGIC-NUM** | `entity/constants.py`로 이동 |
| **S-FMT-SCATTER** | `component/format.py` 단일 정책 |
| **S-BOUND-LEAK** | Boundary → Component 호출만 |
| **S-DUP-ERR** | validator 내 상수 dict |

## 실행

```bash
python -m pytest tests/ -v
```

**완료 조건:** 전체 **PASSED** · smell 1건 해소 · SC-1~3·golden **불변**.

## 완료 보고 (채팅)

```
[REFACTOR]
## refactor-safe 완료
- Smell ID: S-…
- 변경: src/… (+N / -M lines)
- pytest: 전체 PASSED
- 잔여 smell: … (다음 /refactor-smell)
```

## 금지

- **RED** · **GREEN** (새 기능·새 assert)
- tests/ assert 완화 · `skip` · `xfail`
- SC-2 **하드코딩**
- smell 1건 초과 **대규모 재작성**
- git commit (사용자 요청 시만)

## 완료 (채팅 마지막 한 줄)

```
/refactor-smell 으로 재스캔하거나 /export-session 으로 세션을 마친다
```
