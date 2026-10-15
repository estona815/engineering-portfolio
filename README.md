# 권준 · Kwon Jun

### AI 도구로 제품을 만들고, 코드와 검증 근거로 설명합니다.

Python · TypeScript · React / Next.js · React Native · 데이터 검증 · 로컬 AI

[GitHub](https://github.com/estona815) · [English](README.en.md) · [전체 프로젝트 목록](docs/PROJECTS.md) · [수상과 증빙](docs/ACHIEVEMENTS.md) · [코드 샘플](samples/README.md)

## 먼저 볼 프로젝트

| 관심 분야 | 프로젝트 | 검토할 지점 |
|---|---|---|
| 제품·백엔드 | [TuberBot Market](case-studies/tuberbot-market.md) | 계약, 복식부기 원장, outbox, 멱등성, 권한 |
| Agent workflow | [ContextPatch AI](case-studies/contextpatch-ai-datahub-2026.md) | 제한된 패치, 검증, 승인, recorded replay |
| Edge AI | [SOUNDMARK EDGE](case-studies/soundmark-edge.md) | Python/Kotlin 계약, INT8, few-shot, UNKNOWN 거절 |
| ML 평가 | [AbstainLab](case-studies/abstainlab.md) | 그룹 분리, validation-only 선택, holdout 실패 공개 |
| 데이터 분석 | [Seoul Bicycle Audit](case-studies/ttareungi-monthly-audit-2026-koreashe95427.md) | 모집단 통제, 원본 hash, 누락과 0 구분 |
| 모바일 | [Focus Battery](case-studies/focus-battery.md) · [Study Merge](case-studies/study-merge.md) | 로컬 상태, 도메인 분리, 샘플 콘텐츠 경계 |

## 일하는 방식

요구사항을 상태·데이터·권한·실패 조건으로 나누고, 작은 실행 경로를 만든 뒤 테스트·보고서·diff로 확인하는 방식을 지향합니다. Codex 등 AI 도구를 설계·구현·문서화에 활용하며, 프로젝트별 AI 고지와 개인 기여 증거를 구분합니다.

[CreatorOps의 승인 정책](samples/creatorops/publish-policy.ts), [비용 계산 도메인](samples/paper-risk/cost_model.py), [INSTATOON의 프로젝트 식별자](samples/instatoon/project-id.ts)는 로컬 프로젝트에서 발췌한 코드입니다. 전체 소스 snapshot은 비공개로 보관하며 샘플은 완성된 배포 패키지가 아닙니다.

## 확인된 성과

- **2026 Lucasverse Fanfiction Contest 1위** — 「Authorized Driver」. [주최자 공식 발표](https://www.lucasflint.com/2026-lucasverse-fanfiction-contest-winner-authorized-driver-by-kwon-jun/), 2026-10-01.
- **2026 수성 건축·조경 시각작품 국제 공모전 일반 부문 장려상** — 2026-10-08 주최 측 개별 통지와 [공식 수상 공고](https://www.sscf.or.kr/~newsscf/pages/sub.htm?mode=view&mv_data=aWR4PTg2ODMmc3RhcnRQYWdlPTAmbGlzdE5vPTUxMSZ0YWJsZT1jc19iYnNfZGF0YSZuYXZfY29kZT1uZXcxNjI4NTk0NDI5JmNvZGU9YmlkJnNlYXJjaF9pdGVtPSZzZWFyY2hfb3JkZXI9Jm9yZGVyX2xpc3Q9Jmxpc3Rfc2NhbGU9JnZpZXdfbGV2ZWw9JnZpZXdfY2F0ZT0mdmlld19jYXRlMj0%3D%7C%7C) 대조. 공개 명단은 이름·이메일이 마스킹되어 있어 개인 식별은 비공개 개별 통지에 근거합니다.

개발 프로젝트와 창작 수상은 각각의 근거로 표시합니다. 위 수상을 개발 해커톤 수상으로 바꾸어 설명하지 않습니다.

## 검증 자료와 개발 이력

- [프로젝트별 사례 11개](docs/PROJECTS.md): 문제, 저장소 구현, 검증 범위, 한계와 고정 commit 링크
- [공개 저장소 59개 목록](docs/PROJECTS.md): fork·빈 저장소를 별도 표시한 계정 이력
- [로컬 프로젝트](docs/LOCAL_PROJECTS.md): 중복 worktree를 제외한 추가 소스 정리
- [증거 기준·AI 사용·개인 기여](docs/EVIDENCE.md)
- [기계 판독 가능한 공개 증거](evidence/public-claims.csv) · [재현 가능한 샘플 검증](docs/VALIDATION.md)

저장소 관리 권한과 전체 개인 저작은 다릅니다. 기존 감사에서 TuberBot의 계정 연결 커밋 일부를 확인했고, 다른 프로젝트의 개인별 구현 범위는 별도 증거가 없는 한 저장소 수준으로 제시합니다. 체크인 보고서, 과거 로컬 테스트, 이번 실행 검증도 각각 표시합니다.

수집 기준: 2026-10-16 KST. 상용 사용자·매출·실결제·현장 성능은 증거가 있는 경우에만 기재합니다. 개인정보와 공개 권한이 불명확한 원문 자료는 비공개로 보존합니다.
