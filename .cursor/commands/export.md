# export

Report 폴더와 Prompting 폴더에 보고서와 프롬프트(대화 기록)를 저장해줘.

## 동작 조건

- **추가 입력 없이** `/export` 만으로 실행한다.
- STEP 번호·Phase·주제는 **채팅 맥락**과 `Report/*.REPORT.md`에서 **자동 추출**한다.
- 기존 파일 **덮어쓰기 금지** — `NN = max(Report NN, Prompting NN) + 1` (없으면 `01`).

## 저장 규칙

| 폴더 | 파일 패턴 | 내용 |
|------|-----------|------|
| `Report/` | `{NN}.REPORT.md` | 세션 보고서 (Mom Test · 워크북 · 구현 · Export) |
| `Prompting/` | `{NN}.Export-Transcript.md` 또는 `{NN}.REPORT.md` | User/Cursor 대화 기록 |

## Report 필수 섹션

1. 메타 표 (프로젝트 · 경로 · 작성일 · 단계 · Transcript 링크)
2. 개요 · Mom Test 입력(해당 시)
3. 본문 (워크북 / 구현 / Command 등 세션별)
4. 생성·변경 파일 목록

## Transcript 필수 형식

```markdown
# UnitConverter_03 STEP {N} — {제목} (대화 기록)

_Exported on {M/D/YYYY} from Cursor — UnitConverter_03 workspace_
_Source: {agent-transcript uuid 또는 n/a}_

**Report:** [Report/{NN}.REPORT.md](../Report/{NN}.REPORT.md)

---

**User** / **Cursor** 교차 기록
```

## 완료 보고 (채팅)

```
## Export 완료
- Report: Report/{NN}.REPORT.md
- Transcript: Prompting/{NN}.…
- 변경 파일: …
```

## 금지

- git commit (사용자 요청 시만)
- 채팅에 없는 pytest·실행 결과 허위 기재
- 기존 NN 덮어쓰기
