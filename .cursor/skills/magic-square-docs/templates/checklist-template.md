# UnitConverter_03 — ARRR 세션 체크리스트

| 항목 | 값 |
|------|-----|
| **세션** | STEP {N} — {제목} |
| **날짜** | {YYYY-MM-DD} |
| **Test ID (현재 사이클)** | {T-VAL-…} |

---

## SSOT 확인

| # | 항목 | ☐/☑ |
|---|------|-----|
| 1 | `docs/PRD.md` FR·SC·§8.1 Test ID 확인 | ☐ |
| 2 | `.cursorrules` SC-1~3 · grid · API | ☐ |
| 3 | Mom Test 증거(F1~F3)와 Test ID 연결 | ☐ |

---

## ARRR Command 체인

| # | Command | 완료 | 산출 |
|---|---------|------|------|
| 1 | `/red-test-plan` | ☐ | C2C · Track B · 플랜 · ECB 점검 |
| 2 | `/red-skeleton` | ☐ | tests/ · pytest **FAILED** |
| 3 | `/green-minimal` | ☐ | src/ · 해당 TC **PASSED** |
| 4 | `/golden-master` | ☐ | GM-SC2 · SC-1 바이트 |
| 5 | `/refactor-smell` | ☐ | Smell 표 · To-Do 1~3 |
| 6 | `/refactor-safe` | ☐ | smell 1건 · pytest 전체 green |
| 7 | `/export-session` | ☐ | Report · Transcript |

---

## TDD 금지 (PRD §8.2)

| # | 금지 | 위반 ☐ |
|---|------|--------|
| 1 | assert 완화 | ☐ |
| 2 | skip / xfail | ☐ |
| 3 | SC-2 비율 하드코딩 | ☐ |
| 4 | RED에서 src/ 수정 | ☐ |
| 5 | GREEN에서 tests/ 수정 | ☐ |

---

## Exit Criteria (세션 3)

| # | 기준 | ☐/☑ |
|---|------|-----|
| 1 | §8.1 7 Test ID green | ☐ |
| 2 | T-VAL-* boundary green | ☐ |
| 3 | SC-1~3 각 1+ 테스트 | ☐ |
| 4 | golden SC-2 바이트 고정 | ☐ |
| 5 | `python -m pytest tests/ -v` 전체 pass | ☐ |

---

## 메모

{다음 Test ID · 잔여 smell · 블로커}
