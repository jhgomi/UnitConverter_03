# red-test-plan

ARRR **A 단계 (Ask = RED ③)** 전용. **C2C 설계표·테스트 플랜만** 채팅에 출력한다.  
코드·테스트 **파일은 생성하지 않는다** — 다음 단계 `/red-skeleton` 에서 스켈레톤을 만든다.

## Phase 선언

- 응답 **첫 줄**에 반드시 아래 형식 (값은 채팅·PRD에서 자동 결정):

```
Phase: red | Layer: {entity|boundary} | Track: {Logic|UI}
```

| 필드 | UnitConverter_03 기본값 | 판단 근거 |
|------|-------------------------|-----------|
| **Layer** | `boundary` | `validate_lines(grid)` · PRD §8.1 + `tdd-red` T-VAL-* |
| **Layer** | `entity` | Component(parse/validate/convert/format) 단위 RED |
| **Track** | `Logic` | 세션 3 — CLI·pytest (GUI 없음, PRD §7) |
| **Track** | `UI` | (세션 4+ GUI 시에만) |

**Track A (boundary):** Layer를 `boundary`로 두면 본 Command 출력 템플릿을 **그대로 재사용**한다.  
**Track B (Logic / entity·component):** Layer를 `entity`로 두고 블록 2·3의 대상 함수·파일 경로만 Component 모듈로 치환한다.

## 동작 조건

- **추가 입력 없이** `/red-test-plan` 만으로 실행한다.
- 세션 주제·Test ID·FR·SC는 **채팅 맥락** · `docs/PRD.md` · `docs/TEST_PLAN.md` · `.cursorrules`에서 **자동 추출**한다.
- 이미 채팅에서 RED 대상 Test ID가 정해져 있으면 **그 1건**(또는 동일 행동 1그룹)만 플랜한다.
- 없으면 Mom Test 우선순위(§8.1): **T-FMT-01 → T-NEG-01 → T-SAME-01** … 또는 `tdd-red` **T-VAL-PASS-01** 중 **아직 플랜되지 않은 첫 ID**를 선택한다.

## SSOT

| 우선순위 | 문서 |
|----------|------|
| 1 | `.cursorrules` — Domain · API · ECB · SC-1~3 |
| 2 | `docs/PRD.md` — FR · §6 입출력 · §8.1 Test ID |
| 3 | `docs/TEST_PLAN.md` — 계층 · 우선순위 · Exit Criteria |
| 4 | `.cursor/commands/tdd-red.md` — Boundary RED · T-VAL-* · AAA |
| 5 | `.cursor/commands/export-session.md` — 세션 Export |

---

## C2C 규칙 (Rule 1~3)

블록 1 표는 아래 3규칙을 **행 단위**로 채운다.

| Rule | 의미 | 채우는 열 |
|------|------|-----------|
| **Rule 1** | SSOT 계약 인용 | **PRD FR** (및 SC·F 해당 시) |
| **Rule 2** | RED 1사이클 = 행동 1개 | **To-Do** (동사 1개, 구현·파일 생성 없음) |
| **Rule 3** | 검증 가능한 시나리오 | **Test ID · Given · When · Then** |

---

## 출력 형식 (필수 4블록)

아래 4블록을 **표 형식**으로 순서대로 출력한다. 코드 블록·파일 diff **금지**.

### 블록 1 — C2C (Rule 1~3)

| Rule | PRD FR (인용) | To-Do (1개) | Test ID | Given | When | Then |
|------|---------------|-------------|---------|-------|------|------|
| 1~3 | 예: FR-10, SC-2 | 예: T-VAL-PASS-01 RED 시나리오 확정 | T-VAL-PASS-01 | grid 3줄 (§6.2) | `validate_lines(grid)` 호출 | `status=="pass"`, `failed_lines==[]` |

- FR 열에는 **ID + 한 줄 요약** (PRD §5 표에서 인용).
- Then은 PRD §6.2·§6.3·§8.1과 **바이트 수준**으로 맞출 것을 명시.

---

### 블록 2 — Track B 표

Logic Track(entity) 또는 Boundary Track(boundary) 공통 컬럼:

| Test ID | 대상 함수 | Given → Then | Invariant | Expected RED Failure |
|---------|-----------|--------------|-----------|----------------------|
| T-VAL-PASS-01 | `validate_lines` | 정답 grid → pass | SC-2: `8.2 feet`, `2.7 yard` · 비율 SSOT | `NotImplementedError` / stub `...` / AssertionError on status |
| T-FMT-01 | `main` 또는 파이프라인 | `meter:2.5` → 3줄 출력 | SC-2 · FR-11 형식 | feet 줄 정밀도 불일치 등 |

- **Layer=boundary** → 대상: `validate_lines` (`src/validate_lines.py`).
- **Layer=entity** → 대상: `parse_*` / `validate_*` / `convert_*` / `format_*` (`src/component/*.py`).
- **Invariant:** SC-1~3 · `.cursorrules` 불변식 · FR-12 결정성 등 **깨지면 안 되는 조건**.
- **Expected RED Failure:** `/red-skeleton` 후 pytest 시 **기대되는 실패 유형·메시지**(아직 구현 없음 가정).

---

### 블록 3 — 테스트 플랜

| 항목 | 내용 |
|------|------|
| **파일 경로** | 예: `tests/test_validate_lines.py` (boundary) / `tests/test_parse.py` (entity) |
| **함수명** | 예: `test_sc2_valid_grid_passes` — Test ID와 1:1 매핑 |
| **conftest 픽스처** | 필요 시만: `valid_meter_grid`, `sc2_three_lines` 등 **이름·역할만** 기술 (파일 생성 금지) |
| **pytest 명령** | `python -m pytest tests/test_validate_lines.py::test_… -v` |
| **RED 묶음 범위** | 이번 1사이클에 포함 Test ID (1건 또는 tdd-red 동일 그룹) · **제외** ID 명시 |

UnitConverter_03 boundary 기본값:

| 항목 | 기본값 |
|------|--------|
| 파일 | `tests/test_validate_lines.py` |
| conftest | `tests/conftest.py` — `valid_sc2_grid` (§6.2 3줄 리터럴) |
| 명령 | `python -m pytest tests/test_validate_lines.py -v` |
| RED 묶음 | T-VAL-PASS-01 단독 (또는 채팅에서 지정한 1 ID) |

---

### 블록 4 — ECB · Mock 점검

| 점검 항목 | Logic Track | Boundary Track | UI Track |
|-----------|-------------|----------------|----------|
| **의존 방향** | Test → SUT(Component/Boundary) → Entity | Test → `validate_lines` → Component | — |
| **Domain Mock** | **금지** — Entity·Component 순수 로직 직접 호출 | Boundary는 Component **실물** 또는 stub 최소 | UI driver만 허용 |
| **E001~E005 emit** | 테스트·SUT에서 **에러 코드 emit 금지** (예외/반환값으로 표현) | 동일 | 동일 |
| **I/O** | Entity/Component 테스트에 stdin/stdout **금지** | grid는 Arrange 리터럴 | 세션 3 비범위 |
| **SSOT 상수** | `constants.py` 비율만 · SC-2 하드코딩 **금지** | 동일 | — |

체크리스트 (모두 ☐ → 출력 시 ☑/☐ 로 표시):

| # | 질문 | Pass 조건 |
|---|------|-----------|
| 1 | SUT가 ECB Boundary/Component에 맞는가? | Layer 선언과 대상 함수 일치 |
| 2 | Domain Mock 없이 Given을 리터럴로 고정했는가? | grid / `unit:value` 문자열 |
| 3 | E001~E005 emit 경로가 없는가? | 오류는 PRD §6.3 **문자열** 또는 ValidationResult |
| 4 | Then이 SC·FR과 충돌하지 않는가? | SSOT 인용 가능 |
| 5 | RED만 범위인가? | GREEN/REFACTOR·src 변경 없음 |

---

## UnitConverter_03 — Boundary 예시 (참고)

`/red-test-plan` 단독 실행 시 Layer=`boundary`이면 블록 1 첫 행을 아래처럼 채운다.

| Rule | PRD FR | To-Do | Test ID | Given | When | Then |
|------|--------|-------|---------|-------|------|------|
| 1~3 | FR-10, FR-11, SC-2 | T-VAL-PASS-01 시나리오·플랜 확정 | T-VAL-PASS-01 | §6.2 grid 3줄 | `validate_lines(grid)` | pass, `failed_lines=[]` |

---

## 금지

- `src/` · `UnitConverter.py` **수정**
- `tests/` · `src/` **파일 생성·삭제**
- **GREEN** · **REFACTOR** 단계 작업
- `skip` · `xfail` · assert 완화 제안
- SC-2 맞추기 위한 **비율 하드코딩** 제안
- git commit (사용자 요청 시만)
- pytest **실행 결과 허위 기재** (본 Command는 설계만)

## 완료 (채팅 마지막 한 줄)

```
/red-skeleton 으로 넘길 준비됐다
```

## 완료 보고 (채팅 헤더)

```
Phase: red | Layer: boundary | Track: Logic
## red-test-plan 완료
- Test ID: T-VAL-…
- Layer / Track: …
- 블록: C2C · Track B · 테스트 플랜 · ECB·Mock
- 다음: /red-skeleton
```
