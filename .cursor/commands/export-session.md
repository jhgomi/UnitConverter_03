# export-session

Report 폴더와 Prompting 폴더에 **세션 보고서**와 **대화 기록(Transcript)** 을 저장한다.

## 동작 조건

- **추가 입력 없이** `/export-session` 만으로 실행한다.
- STEP 번호·Phase·주제·Test ID는 **채팅 맥락**과 `Report/*.REPORT.md`에서 **자동 추출**한다.
- 기존 파일 **덮어쓰기 금지** — `NN = max(Report NN, Prompting NN) + 1` (없으면 `01`).
- 본문·Transcript 형식은 `.cursor/skills/magic-square-docs/` 템플릿을 따른다.

## 저장 규칙

| 폴더 | 파일 패턴 | 내용 |
|------|-----------|------|
| `Report/` | `{NN}.REPORT.md` | 세션 보고서 (Mom Test · 워크북 · ARRR · Export) |
| `Prompting/` | `{NN}.Export-Transcript.md` | User/Cursor 대화 기록 |

## Report 필수 섹션

1. 메타 표 (프로젝트 · 경로 · 작성일 · 단계 · Phase · Transcript 링크)
2. 개요 · Mom Test 입력(해당 시)
3. 본문 (워크북 / ARRR Command / 구현 등 세션별)
4. 생성·변경 파일 목록
5. pytest 결과(실행한 경우만 — **허위 기재 금지**)

## Transcript 필수 형식

`.cursor/skills/magic-square-docs/templates/transcript-template.md` 참조.

## 완료 보고 (채팅)

```
## export-session 완료
- Report: Report/{NN}.REPORT.md
- Transcript: Prompting/{NN}.Export-Transcript.md
- 변경 파일: …
```

## 금지

- git commit (사용자 요청 시만)
- 채팅에 없는 pytest·실행 결과 허위 기재
- 기존 NN 덮어쓰기
