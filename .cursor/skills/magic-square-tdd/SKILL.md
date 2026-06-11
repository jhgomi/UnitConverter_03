---
name: magic-square-tdd
description: >-
  UnitConverter_03 ARRR TDD 루프(Command 체인·Phase 선언·SSOT)를 안내한다.
  /red-test-plan, /red-skeleton, /green-minimal, /golden-master,
  /refactor-smell, /refactor-safe 사용 시 또는 ARRR·Test Loop·pytest TDD
  실습 시 적용한다.
---

# magic-square-tdd — UnitConverter_03 ARRR Test Loop

## ARRR ↔ Command 매핑

| ARRR | Phase | Command | 변경 허용 | 산출 |
|------|-------|---------|-----------|------|
| **A** (Ask) | RED ③ | `/red-test-plan` | 없음 (채팅만) | C2C · 테스트 플랜 |
| **R** (Red) | RED ④ | `/red-skeleton` | `tests/` | 실패 pytest |
| **G** (Green) | GREEN ⑤ | `/green-minimal` | `src/` | 1 TC green |
| **G+** | GREEN ⑤+ | `/golden-master` | `tests/` fixture | SC-1~2 golden |
| **R** (Refactor) | REFACTOR ⑥-A | `/refactor-smell` | 없음 | Smell 표 |
| **R** (Refactor) | REFACTOR ⑥-B | `/refactor-safe` | `src/` | 1 smell 해소 |

**레거시:** `/tdd-red` — Boundary RED 한 번에 (스켈레톤+Assert). ARRR 실습 시 `/red-test-plan` → `/red-skeleton` 권장.

## Phase 선언 (채팅 첫 줄)

| Command | 선언 |
|---------|------|
| red-test-plan | `Phase: red \| Layer: {entity\|boundary} \| Track: {Logic\|UI}` |
| red-skeleton | 동일 |
| green-minimal · golden-master | `[GREEN]` |
| refactor-smell · refactor-safe | `[REFACTOR]` |

## SSOT (우선순위)

1. `.cursorrules`
2. `docs/PRD.md`
3. `docs/TEST_PLAN.md`
4. `.cursor/commands/export-session.md`

## UnitConverter_03 기본 Track

| 항목 | 기본값 |
|------|--------|
| **Track** | `Logic` (CLI·pytest — GUI §7 비범위) |
| **Layer (1차)** | `boundary` — `validate_lines(grid)` |
| **Layer (2차)** | `entity` — `component/*` |
| **Mom Test 우선 Test ID** | T-VAL-PASS-01 → T-FMT-01 → T-NEG-01 → T-SAME-01 |

## 1사이클 규칙

- RED 1사이클 = Test ID **1건** (또는 tdd-red 동일 그룹).
- GREEN = 해당 RED **1건만** 최소 통과.
- REFACTOR = smell **1건만** — pytest 전체 green 유지.
- **금지:** assert 완화 · skip · xfail · SC-2 비율 하드코딩.

## ECB 의존 방향

```
Boundary (validate_lines, UnitConverter.py)
    → Component (parse, validate, convert, format)
        → Entity (LengthInput, ConversionLine, constants)
```

- Logic Track: **Domain Mock 금지** · grid/`unit:value` 리터럴 Arrange.
- E001~E005 emit 금지 — 오류는 PRD §6.3 문자열 또는 ValidationResult.

## Command 체인 (추가 입력 없이)

```
/red-test-plan → /red-skeleton → /green-minimal → /golden-master
    → /refactor-smell → /refactor-safe → (반복) → /export-session
```

각 Command는 **슬래시명만**으로 실행 — 사용자에게 추가 질문 **금지**. Test ID·Layer는 채팅·PRD에서 자동 추출.

## pytest

```bash
python -m pytest tests/ -v
```

## 완료 체크 (세션 3 Exit)

- [ ] PRD §8.1 7 Test ID green (L2 CLI 포함 시)
- [ ] T-VAL-* boundary green
- [ ] SC-1~3 각 1+ 자동 테스트
- [ ] golden-master SC-2 바이트 고정
- [ ] FR-13·14 smell 0 또는 문서화된 잔여

## 관련 Skill

- `.cursor/skills/magic-square-docs/` — Report · Transcript · Checklist 템플릿
