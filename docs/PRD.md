# UnitConverter_03 — Product Requirements Document (PRD)

| 항목 | 내용 |
|------|------|
| **프로젝트** | UnitConverter_03 |
| **버전** | 0.1 (세션 3 — 변환·검증·Test Loop) |
| **작성일** | 2026-06-11 |
| **SSOT** | 본 문서 · [Report/01.UnitConverter_ProblemDefinition_Report.md](../Report/01.UnitConverter_ProblemDefinition_Report.md) · `Report/03` |
| **현재 범위** | 길이 단위 변환 CLI · 입력 검증 · OCP/SRP · pytest Test Loop |

---

## 1. 개요

### 1.1 한 줄 요약

**길이 값(`단위:값`)을 한 번 입력했을 때, README에 적힌 변환 규칙과 검증 기대에 맞는 결과만 일관되게 돌려받을 수 있게 한다** — README와 출력 불일치·음수 무차단으로 재실행·수동 검증에 시간을 쓰는 일을 줄이기 위함.

### 1.2 배경

Python 실습 Unit Converter에서 학습자는 `UnitConverter.py` CLI로 meter / feet / yard 변환을 확인한다. Mom Test 인터뷰(2026-06-11)에서 **README 예시(`8.2 feet`)와 실제 출력(`8.2021 feet`) 불일치**로 같은 입력을 **3회** 재실행했고, README가 요구하는 **음수 검증**이 구현되지 않아 `meter:-2.5`를 **직접 넣어** 확인했다.

### 1.3 증거 3줄 (Mom Test)

1. `meter:2.5` **3회** 재실행 — `8.2021 feet` vs README `8.2 feet`
2. `feet:8.2` 후 README·출력 차이 **메모장 기록**
3. `meter:-2.5` **에러 없이** 변환 (README 음수 검증과 불일치)

---

## 2. 페르소나·문제

### 2.1 페르소나 (Role)

Python 실습 중 **UnitConverter 학습자**. README를 읽고 `UnitConverter.py`를 터미널에서 실행·검증하는 단계.

### 2.2 진짜 문제

README에 적힌 기대(반올림 예시, 음수 차단)와 실제 프로그램 출력·동작이 일치하지 않아, 변환 결과를 믿고 쓰기 전에 같은 입력을 반복 실행하고 직접 잘못된 값을 넣어 검증하는 데 시간을 썼다.

### 2.3 표면 문제 (비목표)

- 「**단위 변환 프로그램**을 만든다」
- 「**JSON/CSV/표** 출력을 넣는다」 (추가 요구 — 세션 4)
- 「**cubit** 등 단위를 런타임 등록한다」 (세션 4)

→ 솔루션명이 섞인 정의. **세션 3 PRD 목표가 아님.**

---

## 3. R-G-I-O

| | 내용 |
|---|------|
| **Role** | §2.1 페르소나 |
| **Goal** | **재실행·수동 대조 없이** README 기준 변환·검증 결과를 신뢰 |
| **Input** | `단위:값` 문자열 (예: `meter:2.5`, `feet:8.2`) |
| **Output** | 지원 단위(meter, feet, yard) 각각 `{value} {unit} = {converted} {target_unit}` 형식. 오류 시 메시지 1줄 후 종료 |

---

## 4. 성공 기준

| # | 기준 | Mom Test 연결 |
|---|------|---------------|
| **SC-1** | 동일 입력을 여러 번 실행해도 출력이 **바이트 단위 동일** | 3회 재실행 확인 행동 제거 |
| **SC-2** | 변환 결과가 README 비율·**문서화된 정밀도**와 일치 (`meter:2.5` → `8.2 feet`, `2.7 yard`) | `8.2021` vs `8.2` 메모 문제 |
| **SC-3** | 음수·형식 오류·미지원 단위 → **변환 없이** 오류 메시지 | `meter:-2.5` 무차단 해소 |

---

## 5. 기능 요구사항 (FR)

### 5.1 변환 (Domain)

| ID | 요구 | 상세 |
|----|------|------|
| **FR-1** | 지원 단위 | `meter`, `feet`, `yard` (소문자 식별자) |
| **FR-2** | 기준 단위 | **meter** — 모든 변환의 중간값 |
| **FR-3** | 변환 비율 | `METER_TO_FEET = 3.28084`, `METER_TO_YARD = 1.09361` (README SSOT) |
| **FR-4** | 역변환 | feet·yard → meter: `value / ratio` |
| **FR-5** | 출력 범위 | 입력 단위 포함 **3단위 전부** 출력 |

### 5.2 입력 검증

| ID | 요구 | 상세 |
|----|------|------|
| **FR-6** | 형식 | `:` 포함 `unit:value`. 없으면 `Invalid format. Use unit:value (ex: meter:2.5)` |
| **FR-7** | 숫자 | `value`는 `float` 파싱 가능. 실패 시 `Invalid number: {value}` |
| **FR-8** | 음수 | `value < 0` → 변환 금지, 오류 메시지 (README 품질 요구) |
| **FR-9** | 미지원 단위 | `Unknown unit: {unit}` |

### 5.3 출력·포맷

| ID | 요구 | 상세 |
|----|------|------|
| **FR-10** | 정밀도 정책 | **meter**: 입력 표시값 유지 · **feet/yard**: 소수 **1자리** (README 예시 `8.2`, `2.7`) |
| **FR-11** | 출력 형식 | `{value} {unit} = {converted} {target_unit}` (줄 단위) |
| **FR-12** | 결정성 | 동일 입력 → 동일 출력 문자열 (SC-1) |

### 5.4 설계 (품질)

| ID | 요구 | 상세 |
|----|------|------|
| **FR-13** | OCP | 새 단위 추가 시 기존 변환 로직 **최소 수정** (전략·레지스트리 패턴) |
| **FR-14** | SRP | **파싱 / 검증 / 변환 / 출력** 책임 분리 |
| **FR-15** | 상수 SSOT | 변환 비율·정밀도 정책을 한 곳에서 관리 (예: `constants.py` 또는 설정 모듈) |

### 5.5 실패 조건 (Mom Test → FR)

| ID | 조건 | 대응 |
|----|------|------|
| **F1** | README 예시와 출력 소수 자릿수 불일치 | FR-10 + SC-2 테스트 |
| **F2** | 음수 입력이 변환됨 | FR-8 + SC-3 테스트 |
| **F3** | 동일 입력마다 출력이 달라짐 | FR-12 + SC-1 테스트 |
| **F4** | 단위 추가 시 `main()` 전체 if/elif 수정 | FR-13 위반 |

---

## 6. API·CLI 계약

### 6.1 CLI 진입점

```python
# UnitConverter.py
def main() -> None:
    """프롬프트 → parse → validate → convert → format → print"""
```

### 6.2 입력·출력 예 (README)

**입력:** `meter:2.5`

**출력 (FR-10 적용):**

```
2.5 meter = 2.5 meter
2.5 meter = 8.2 feet
2.5 meter = 2.7 yard
```

### 6.3 오류 메시지 (기존 관례 유지)

| 조건 | 메시지 |
|------|--------|
| `:` 없음 | `Invalid format. Use unit:value (ex: meter:2.5)` |
| 숫자 아님 | `Invalid number: {value_str}` |
| 미지원 단위 | `Unknown unit: {unit}` |
| 음수 | `Negative value not allowed: {value}` (문구는 구현 시 고정) |

### 6.4 권장 내부 모듈 (초안)

| 모듈 | 책임 | FR |
|------|------|-----|
| `parser` | `unit:value` 분리 | FR-6 |
| `validator` | 형식·숫자·음수·단위 | FR-6~9 |
| `converter` | meter 기준 변환 | FR-1~5 |
| `formatter` | 정밀도·출력 문자열 | FR-10~12 |

---

## 7. 비범위 (Out of Scope — 세션 3)

| 항목 | 사유 |
|------|------|
| **GUI** | Mom Test 증거는 CLI만 |
| **JSON / CSV / 표** 출력 | README 추가 요구 — 세션 4 |
| **cubit** 등 **동적 단위 등록** | 세션 4 |
| **YAML/JSON 설정 외부화** | 세션 4 |
| **반올림만 임시 적용** (테스트 없이) | SC-2는 정책 + Test Loop |
| 8계층 **Memory, Hook, MCP, Automation** | 세션 3 범위 밖 |

---

## 8. 테스트 요구사항

### 8.1 Mom Test → RED 우선 케이스

| Test ID | FR | Given | Then |
|---------|-----|-------|------|
| **T-SAME-01** | FR-12, SC-1 | `meter:2.5` 2회 연속 | 출력 문자열 **완전 동일** |
| **T-FMT-01** | FR-3,10, SC-2 | `meter:2.5` | `8.2 feet`, `2.7 yard` 포함 |
| **T-NEG-01** | FR-8, SC-3 | `meter:-2.5` | 변환 출력 **없음**, 오류 |
| **T-FMT-ERR** | FR-6 | `meter` (콜론 없음) | `Invalid format` |
| **T-NUM-ERR** | FR-7 | `meter:abc` | `Invalid number: abc` |
| **T-UNIT-ERR** | FR-9 | `inch:1` | `Unknown unit: inch` |
| **T-CONV-FT** | FR-4,5 | `feet:8.2` | meter·yard 변환 줄 출력 |

### 8.2 TDD 규칙

- 순서: **RED → GREEN → REFACTOR**. 한 사이클에 한 행동.
- RED: `tests/`만. GREEN: `src/` 또는 리팩터 대상 모듈만.
- 금지: assert 완화, skip, xfail, SC-2를 맞추기 위한 **하드코딩 상수** (비율 SSOT 유지).

### 8.3 pytest

```bash
python -m pytest tests/ -v
```

---

## 9. 개발 워크플로

### 9.1 세션 3 Command 절차

1. `UnitConverter.py` 구조 분석 → FR-14 책임 분리
2. meter/feet/yard 변환 (FR-1~5)
3. 입력 검증 (FR-6~9)
4. 출력 포맷터 (FR-10~12)
5. pytest → SC-1~3 → Test Loop

### 9.2 Test Loop

```
[Red]   Mom Test 증거 → T-SAME-01, T-FMT-01, T-NEG-01 등
[Green] 최소 구현 (OCP/SRP 점진 적용)
[Refactor] if/elif 제거 · 레지스트리 (TC green 유지)
[Repeat] pytest 전체
```

### 9.3 8계층 (세션 3)

| 계층 | 내용 |
|------|------|
| **Rule** | FR·SC·Mom Test 진짜 문제 |
| **Command** | §9.1 절차 · `.cursor/commands/` |
| **Skill** | `unit-converter-test-loop` (선택) |
| **Test Loop** | §8 · §9.2 |

---

## 10. 기술 스택·구조

```
UnitConverter_03/
├── docs/
│   └── PRD.md                          # 본 문서
├── UnitConverter.py                    # CLI 진입점
├── src/                                # (예정) parser, validator, converter, formatter
├── tests/                              # (예정) test_*.py
├── Report/
│   ├── 01.UnitConverter_ProblemDefinition_Report.md
│   └── 03.REPORT.md
├── Prompting/
├── .cursor/commands/
│   └── export.md
└── README.md
```

| 항목 | 값 |
|------|-----|
| **언어** | Python 3 |
| **테스트** | pytest |
| **실행** | `python UnitConverter.py` |

---

## 11. 로드맵

| 단계 | 내용 | 상태 |
|------|------|------|
| STEP 1 | Mom Test · Problem Definition Report | ✅ |
| STEP 3 | 워크북 · PRD 초안 | ✅ |
| STEP 3 impl | OCP/SRP · 검증 · 포맷 · pytest | ⏳ |
| 세션 4 | 설정 외부화 · 동적 단위 · JSON/CSV/표 | ⏳ 범위 밖 |

---

## 12. 참고 문서

| 문서 | 내용 |
|------|------|
| [Report/01.UnitConverter_ProblemDefinition_Report.md](../Report/01.UnitConverter_ProblemDefinition_Report.md) | Mom Test · 문제 정의 |
| [Report/03.REPORT.md](../Report/03.REPORT.md) | 세션 3 워크북 |
| [README.md](../README.md) | 과제·비율·Activities |
| [Prompting/01.REPORT.md](../Prompting/01.REPORT.md) | Mom Test transcript |

---

## 13. 변경 이력

| 버전 | 날짜 | 변경 |
|------|------|------|
| 0.1 | 2026-06-11 | 초안 — Mom Test·워크북·README 통합. FR-1~15, F1~F4, Test ID 7건, SC-1~3 |
