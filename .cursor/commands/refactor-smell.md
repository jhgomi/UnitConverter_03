# refactor-smell

ARRR **R 단계 (Refactor = REFACTOR ⑥-A)** 전용. **코드 냄새 목록만** 출력한다. **파일 수정 금지.**

## Phase 선언

- 응답 **첫 줄**에 반드시: `[REFACTOR]`
- 이어서: `Smell Scan | Layer: {entity|boundary|all} | Track: Logic`

## 동작 조건

- **추가 입력 없이** `/refactor-smell` 만으로 실행한다.
- **선행:** GREEN 이상 (채팅에 `/green-minimal` 또는 pytest green 언급).
- 대상 코드: `src/` · `UnitConverter.py` — 채팅·워크스페이스에서 **자동 스캔**.

## SSOT

| 우선순위 | 문서 |
|----------|------|
| 1 | `docs/PRD.md` FR-13 · FR-14 · F4 |
| 2 | `.cursorrules` ECB · SRP · OCP |
| 3 | pytest green 유지 전제 |

## Smell 카탈로그 (UnitConverter_03)

| Smell ID | 징후 | PRD / Rule | 심각도 |
|----------|------|------------|--------|
| **S-IFELIF** | `main()` 또는 converter에 단위별 if/elif | F4 · FR-13 | 높음 |
| **S-GOD-FUNC** | parse+validate+convert+format 한 함수 | FR-14 | 높음 |
| **S-MAGIC-NUM** | 3.28084 등이 constants 밖 | FR-15 | 중간 |
| **S-FMT-SCATTER** | 정밀도 로직 분산 | FR-10 | 중간 |
| **S-BOUND-LEAK** | Boundary가 변환 비율 직접 계산 | ECB | 중간 |
| **S-DUP-ERR** | 오류 문자열 중복 | FR-6~9 · §6.3 | 낮음 |
| **S-STUB** | `...` · TODO 잔존 | GREEN 잔재 | 낮음 |

## 출력 (필수 3블록, 표 형식)

### 블록 1 — Smell 표

| Smell ID | 위치 (파일:함수/영역) | 근거 (FR/Rule) | 리팩터 힌트 | 우선순위 |
|----------|----------------------|----------------|-------------|----------|

### 블록 2 — ECB 위반

| 위반 | 현재 | 목표 (ECB) |
|------|------|------------|

### 블록 3 — `/refactor-safe` To-Do (1~3개)

| 순서 | To-Do (동사 1개) | 대상 Smell ID | 예상 변경 파일 |
|------|------------------|---------------|----------------|

- To-Do는 **한 번에 1 smell** — `/refactor-safe` 1사이클 = 1 To-Do.

## 완료 보고 (채팅)

```
[REFACTOR]
## refactor-smell 완료
- 스캔: src/ … · UnitConverter.py
- Smell: N건 (S-…)
- 다음 To-Do: …
- 다음: /refactor-safe
```

## 금지

- `src/` · `tests/` · `UnitConverter.py` **수정**
- **GREEN** · **RED** (테스트·구현 추가)
- smell 없는데 **임의 리팩터** 제안
- git commit (사용자 요청 시만)

## 완료 (채팅 마지막 한 줄)

```
/refactor-safe 으로 넘길 준비됐다
```
