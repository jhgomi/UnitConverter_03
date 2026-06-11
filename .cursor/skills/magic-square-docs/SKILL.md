---
name: magic-square-docs
description: >-
  UnitConverter_03 세션 Report·Transcript·Checklist를 magic-square 템플릿으로
  작성·Export한다. /export-session, Report/Prompting 저장, ARRR 세션 마감,
  STEP 보고서 작성 시 적용한다.
---

# magic-square-docs — UnitConverter_03 세션 문서

## 용도

- `/export-session` 실행 시 Report · Transcript 본문 생성
- ARRR 실습 **세션 마감** 체크리스트
- `Report/{NN}.REPORT.md` · `Prompting/{NN}.Export-Transcript.md` 형식 통일

## SSOT

| 우선순위 | 문서 |
|----------|------|
| 1 | `.cursor/commands/export-session.md` |
| 2 | `.cursorrules` · `docs/PRD.md` |
| 3 | `Report/*.REPORT.md` (기존 톤) |

## NN 규칙

```
NN = max(Report 폴더 NN, Prompting 폴더 NN) + 1
```

- **덮어쓰기 금지**
- 없으면 `01`

## 템플릿 (3종)

| 템플릿 | 경로 | 용도 |
|--------|------|------|
| **Report** | [templates/report-template.md](templates/report-template.md) | `Report/{NN}.REPORT.md` |
| **Transcript** | [templates/transcript-template.md](templates/transcript-template.md) | `Prompting/{NN}.Export-Transcript.md` |
| **Checklist** | [templates/checklist-template.md](templates/checklist-template.md) | 세션 self-check · Report 부록 |

`{N}`, `{NN}`, `{제목}`, `{Phase}` 등은 **채팅·기존 Report에서 자동 치환**.

## Export 절차 (`/export-session`)

1. 채팅에서 STEP · Phase · Command · Test ID · 변경 파일 추출
2. NN 계산
3. `report-template.md` → `Report/{NN}.REPORT.md` 작성
4. `transcript-template.md` → `Prompting/{NN}.Export-Transcript.md` 작성
5. (선택) checklist를 Report §부록 또는 채팅에 출력
6. 완료 보고 — **pytest는 실행한 경우만** 기재

## Report 필수 포함

- 메타 표 (프로젝트 · 경로 · 작성일 · 단계 · Phase · Transcript 링크)
- ARRR Command 표 (해당 세션)
- 생성·변경 파일 목록
- pytest (실행 시)

## Transcript 필수 포함

- Export 메타 · Report 역링크
- User / Cursor 교차 기록
- Command **완료 한 줄** (`/red-skeleton 으로 넘길 준비됐다` 등)

## Checklist 사용 시점

| 시점 | 항목 |
|------|------|
| RED 전 | SSOT · `/red-test-plan` |
| GREEN 후 | 금지 위반 · TC pass |
| REFACTOR 후 | smell · 전체 pytest |
| 세션 마감 | Exit Criteria · `/export-session` |

## 금지

- git commit (사용자 요청 시만)
- 채팅에 없는 pytest·실행 결과 **허위 기재**
- 기존 NN **덮어쓰기**
- Mom Test·SC-1~3와 충돌하는 문서화

## 관련

- `.cursor/skills/magic-square-tdd/SKILL.md` — ARRR Command 체인
- `.cursor/commands/export-session.md` — Export Command
