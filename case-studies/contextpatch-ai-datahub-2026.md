# ContextPatch AI

변경 제안에 영향 분석과 승인 근거를 연결

## 문제와 제품

데이터 변경을 영향 그래프·제한된 패치·검증·사람 승인으로 나누고 기록된 replay로 설명합니다.

## 저장소에서 확인할 설계

- Python 기반 정책·실행 경계와 Next.js replay UI
- 경로·명령 allowlist, patch ID와 일치하는 승인
- 변경 전후 diff와 평가·provenance 추적

## 증거와 검증

기존 고정 SHA의 체크인 보고서: synthetic routing/security 25/25, dbt sandbox 16 passed. 저장소 보고이며 이번 독립 재실행이나 운영 성능 수치가 아닙니다.

[소스 저장소](https://github.com/estona815/contextpatch-ai-datahub-2026) · [검토한 README 고정 SHA](https://github.com/estona815/contextpatch-ai-datahub-2026/blob/838678d85fadce583f6b8256d9d6c0903f00ed36/README.md)

## 범위와 개인 기여

hosted replay는 recorded static demo입니다. live DataHub/MCP/LLM/production write-back과 개인 구현 귀속은 입증되지 않았습니다.

개인별 기여는 [증거 기준](../docs/EVIDENCE.md)을 따릅니다. 저장소 구현 설명을 후보자의 모든 코드 직접 작성 증거로 해석하지 않습니다. AI 활용 내역은 각 원본 저장소의 disclosure를 우선합니다.

[전체 프로젝트](../docs/PROJECTS.md) · [포트폴리오](../README.md)
