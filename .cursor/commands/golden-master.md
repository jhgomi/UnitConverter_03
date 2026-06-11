# golden-master

ARRR **G 단계 보강 (Golden Master = GREEN ⑤+)** 전용. SC-1·SC-2 **기대 출력**을 golden fixture로 고정하고, 회귀 테스트를 `tests/`에 **추가 또는 보강**한다.

## Phase 선언

- 응답 **첫 줄**에 반드시: `[GREEN]`
- 이어서: `Golden Master | Layer: {entity|boundary} | Track: Logic`

## 동작 조건

- **추가 입력 없이** `/golden-master` 만으로 실행한다.
- **선행:** `/green-minimal`로 **최소 1건 GREEN** (채팅 또는 pytest green).
- Mom Test·PRD §6.2·SC-1~2에서 golden 문자열을 **자동 추출**.

## SSOT

| 우선순위 | 문서 |
|----------|------|
| 1 | `docs/PRD.md` §6.2 · §4 SC-1~2 |
| 2 | `.cursorrules` grid · 불변식 |
| 3 | 채팅 — 최근 GREEN Test ID |

## Golden 대상 (UnitConverter_03)

| Golden ID | SSOT | 용도 |
|-----------|------|------|
| **GM-SC2-METER** | §6.2 3줄 | SC-2 · `meter:2.5` grid / CLI 출력 |
| **GM-SC2-FEET** | FR-4·5 · `feet:8.2` | 역변환 3단위 (T-CONV-FT) |
| **GM-SC1-BYTES** | SC-1 | 동일 입력 2회 출력 **바이트 동일** assert |

## fixture 배치

| 경로 | 내용 |
|------|------|
| `tests/fixtures/golden_sc2_meter.txt` | §6.2 3줄 (줄바꿈 `\n` 고정) |
| `tests/conftest.py` | `golden_sc2_grid`, `golden_sc2_text` 픽스처 |
| `tests/test_golden_master.py` (또는 기존 파일에 추가) | golden 대비 assert |

boundary grid golden 예:

```python
GOLDEN_SC2_GRID = [
    "2.5 meter = 2.5 meter",
    "2.5 meter = 8.2 feet",
    "2.5 meter = 2.7 yard",
]
```

SC-1 테스트 패턴:

```python
def test_sc1_deterministic_output(run_cli):
    out1 = run_cli("meter:2.5")
    out2 = run_cli("meter:2.5")
    assert out1 == out2
    assert out1 == GOLDEN_SC2_TEXT  # optional byte lock
```

## 출력 (채팅 3블록)

| 블록 | 내용 |
|------|------|
| **1. Golden 표** | Golden ID · SSOT 인용 · 바이트 문자열(또는 grid) |
| **2. 파일 계획** | fixture 경로 · conftest · 테스트 함수명 |
| **3. 불변식 점검** | SC-1 바이트 · SC-2 `8.2`/`2.7` · 비율 SSOT |

## 실행

```bash
python -m pytest tests/test_golden_master.py -v
python -m pytest tests/ -v
```

## 완료 보고 (채팅)

```
[GREEN]
## golden-master 완료
- Golden ID: GM-SC2-METER …
- fixture: tests/fixtures/…
- pytest: PASSED
- 다음: /refactor-smell 또는 다음 RED
```

## 금지

- golden을 **실제(잘못된) 출력**에 맞추기 (Mom Test `8.2021` 등)
- SC-2 **하드코딩 상수**
- `src/` **리팩터** (동작 변경 없는 fixture 경로 추가만 tests/ 허용)
- `skip` · `xfail`
- git commit (사용자 요청 시만)

## 완료 (채팅 마지막 한 줄)

```
/refactor-smell 으로 넘길 준비됐다
```
