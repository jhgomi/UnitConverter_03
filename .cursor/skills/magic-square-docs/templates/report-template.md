# UnitConverter_03 STEP {N} — {세션 제목}

| 항목 | 내용 |
|------|------|
| **프로젝트** | UnitConverter_03 |
| **경로** | `c:\김정화\DEV\UnitConverter_03` |
| **작성일** | {YYYY-MM-DD} |
| **단계** | STEP {N} — {Mom Test / 워크북 / ARRR / Export / …} |
| **Phase** | {red / green / refactor / …} |
| **Command** | {/red-test-plan · /export-session · …} |
| **참고** | [Report/…](…) · `docs/PRD.md` |
| **Transcript** | [Prompting/{NN}.Export-Transcript.md](../Prompting/{NN}.Export-Transcript.md) |

---

## 1. 개요

{세션 한 줄 요약 — Mom Test 문제 또는 ARRR 사이클 목표}

| 항목 | 상태 |
|------|------|
| {산출물 1} | ✅ / ⏳ / ❌ |
| {산출물 2} | … |

---

## 2. Mom Test 입력 (해당 시)

| 항목 | 내용 |
|------|------|
| **페르소나** | UnitConverter 학습자 |
| **진짜 문제** | README 기대 ↔ 실제 불일치 → 재실행·수동 검증 |
| **증거 3줄** | ① `meter:2.5` 3회 ② 메모 ③ `meter:-2.5` |

---

## 3. 본문

### 3.1 {주제}

{워크북 · ARRR Command · 구현 · 리뷰 등 세션별 본문}

### 3.2 ARRR / Test Loop (해당 시)

| ARRR | Command | Test ID | 결과 |
|------|---------|---------|------|
| A | /red-test-plan | T-VAL-… | 플랜 완료 |
| R | /red-skeleton | … | pytest FAILED |
| G | /green-minimal | … | pytest PASSED |
| R | /refactor-safe | S-… | green 유지 |

---

## 4. 생성·변경 파일

| 경로 | 설명 |
|------|------|
| `.cursor/commands/…` | … |
| `tests/…` | … |
| `src/…` | … |

---

## 5. pytest (실행한 경우만)

| 명령 | 결과 |
|------|------|
| `python -m pytest tests/ -v` | {passed/failed — 허위 기재 금지} |

---

## 6. 다음 단계

{다음 Command · Test ID · FR}
