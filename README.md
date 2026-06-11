# Unit Converter (Python) — UnitConverter_03

![unit-converter](./unit-converter.jpg)

길이 값(`단위:값`)을 한 번 입력하면, **아래 변환 규칙·출력 형식·검증 기대**에 맞는 결과를 일관되게 돌려받는 CLI 프로그램.

> 상세 요구·테스트: [docs/PRD.md](docs/PRD.md) · [docs/TEST_PLAN.md](docs/TEST_PLAN.md)

---

## Overview

- 사용자가 입력한 길이(`단위:값`)를 meter 기준으로 변환해 **지원 단위 전체**를 출력한다.
- 새 단위 추가 시 기존 코드 변경을 최소화하도록 설계한다 (**OCP**).
- 파싱 / 검증 / 변환 / 출력 책임을 분리한다 (**SRP**).
- 변환·검증 동작은 **pytest**로 검증한다.

---

## 실행

### 가상환경 (선택)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

deactivate   # 비활성화
```

### CLI

```bash
python UnitConverter.py
```

프롬프트에 `단위:값` 형식으로 입력한다.

### 테스트

```bash
python -m pytest tests/ -v
```

---

## 기본 요구사항

### 1. 입력·출력

**입력 예:**

```
meter:2.5
```

**출력 예** (입력 단위 meter 포함 **3단위 전부**, feet/yard는 소수 **1자리**):

```
2.5 meter = 2.5 meter
2.5 meter = 8.2 feet
2.5 meter = 2.7 yard
```

- 출력 형식: `{value} {unit} = {converted} {target_unit}` (줄 단위)
- **meter**: 입력에 표시된 값 그대로 유지
- **feet / yard**: 소수 첫째 자리까지 (예: `8.2`, `2.7`)

### 2. 지원 단위

| 단위 | 식별자 |
|------|--------|
| meter | `meter` |
| feet | `feet` |
| yard | `yard` |

- 소문자 식별자만 사용한다.
- **기준 단위는 meter** — 모든 변환의 중간값.

### 3. 변환 비율 (SSOT)

| 변환 | 비율 |
|------|------|
| meter → feet | `1 m = 3.28084 ft` |
| meter → yard | `1 m = 1.09361 yd` |

- feet ↔ yard 변환은 **meter를 거쳐** 계산한다.
- feet / yard → meter: `value / ratio`

### 4. 입력 검증

잘못된 입력은 **변환하지 않고** 오류 메시지 1줄을 출력한 뒤 종료한다.

| 조건 | 입력 예 | 오류 메시지 |
|------|---------|-------------|
| `:` 없음 | `meter` | `Invalid format. Use unit:value (ex: meter:2.5)` |
| 숫자 아님 | `meter:abc` | `Invalid number: abc` |
| 미지원 단위 | `inch:1` | `Unknown unit: inch` |
| 음수 | `meter:-2.5` | `Negative value not allowed: -2.5` |

### 5. 설계·품질

- **OCP**: 새 단위 추가 시 기존 변환 로직 최소 수정 (전략·레지스트리 패턴 권장)
- **SRP**: 파싱 / 검증 / 변환 / 출력 분리
- **결정성**: 동일 입력 → 동일 출력 문자열 (매 실행마다 결과가 달라지면 안 됨)
- 변환 비율·정밀도 정책은 한 곳(`constants.py` 등)에서 관리

### 6. 테스트

- Mom Test에서 확인한 기대를 pytest로 고정한다.
- TDD: **RED → GREEN → REFACTOR** (한 사이클에 한 행동)
- RED: `tests/`만 수정 · GREEN: `src/` 또는 `UnitConverter.py`

| Test ID | Given | Then (요약) |
|---------|-------|-------------|
| T-FMT-01 | `meter:2.5` | `8.2 feet`, `2.7 yard` 포함 · §출력 예 3줄 |
| T-NEG-01 | `meter:-2.5` | 변환 없음 · 오류 |
| T-SAME-01 | `meter:2.5` 2회 | 출력 문자열 완전 동일 |
| T-FMT-ERR | `meter` | `Invalid format` |
| T-NUM-ERR | `meter:abc` | `Invalid number: abc` |
| T-UNIT-ERR | `inch:1` | `Unknown unit: inch` |
| T-CONV-FT | `feet:8.2` | meter·yard 변환 줄 출력 |

자세한 플랜: [docs/TEST_PLAN.md](docs/TEST_PLAN.md)

---

## 프로젝트 구조

```
UnitConverter_03/
├── UnitConverter.py          # CLI 진입점
├── src/
│   ├── entity/               # LengthInput, constants, …
│   ├── component/            # parse, validate, convert, format
│   └── validate_lines.py     # Boundary — grid 검증 API
├── tests/
├── docs/
│   ├── PRD.md
│   └── TEST_PLAN.md
└── README.md                 # 본 문서 (과제·비율·출력 SSOT)
```

---

## 추가 요구사항 (세션 4 — 현재 범위 밖)

아래는 **추가 과제**이며, 세션 3 기본 구현 범위에 포함하지 않는다.

- **설정 외부화** — 변환 비율을 JSON/YAML 등 외부 설정에서 로드
- **동적 단위 등록** — 예: `1 cubit = 0.4572 meter` 런타임 등록
- **출력 포맷 선택** — JSON / CSV / 표 형태 출력

---

## 생성형 AI 활용 Activities (6시간)

1. **문제 코드 및 기본 요구사항 분석** (0.5시간)  
   기본 코드 구조·로직 이해 · [docs/PRD.md](docs/PRD.md) · Mom Test

2. **기본 요구사항 및 품질 요구사항 구현** (2시간)  
   OCP 인터페이스 · SRP 클래스 분리 · 입력값 검증

3. **TC 구현** (0.5시간)  
   단위 변환·입력 검증 pytest · RED → GREEN → REFACTOR

4. **추가 요구사항 구현** (2시간)  
   세션 4 항목 3개 및 TC

5. **회고 및 발표** (1시간)  
   실습 목표·달성도 · AI 활용 · TC·리팩터링 회고

---

## 참고 문서

| 문서 | 내용 |
|------|------|
| [docs/PRD.md](docs/PRD.md) | FR · SC · API · 테스트 요구 |
| [docs/TEST_PLAN.md](docs/TEST_PLAN.md) | pytest 플랜 · ARRR |
| [Report/01.REPORT.md](Report/01.REPORT.md) | Mom Test |
| [Report/03.REPORT.md](Report/03.REPORT.md) | 세션 3 워크북 |
