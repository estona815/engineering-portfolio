# 권준 · Kwon Jun

### AI 도구로 시제품을 만들고, 동작과 검수 근거로 설명합니다.

메카트로닉스 전공 · QA·테스트 · AI 업무자동화 · 장치·데이터 운영

[GitHub](https://github.com/estona815) · [QA·자동화 이력서](docs/RESUME_QA_KO.md) · [로봇·데이터 운영 이력서](docs/RESUME_ROBOT_OPS_KO.md) · [수상·선정 근거](docs/ACHIEVEMENTS.md)

한국폴리텍대학 서울정수캠퍼스 메카트로닉스과 전문학사 과정, **2027년 2월 졸업예정**입니다. 개인·학교 프로젝트에서 AI 도구와 협업해 구현하고, 입력·상태·오류·검토 기록을 연결하는 작업을 해왔습니다. 서울 근무와 졸업 전 조기취업이 가능하며 입사일은 협의합니다.

## 채용 검토: 이 순서로 보세요

| 지원 분야 | 먼저 볼 자료 | 확인할 내용 |
|---|---|---|
| QA·소프트웨어 테스트 | [Company Workbench](case-studies/company-workbench.md) → [GlyphCheck](case-studies/glyphcheck.md) | 결함·수정 비교, 경계값, 중복 보류, 편집 후 재검토 |
| 로봇·장치 운영 / 데이터 검수 | [NUTRONICS](case-studies/nutronics.md) → [StockBridge](case-studies/company-workbench.md) | 정상·걸림·재시도, 로그, 제작 증빙, 원본 행 대조 |
| AI Product / 업무자동화 | [Company Workbench](case-studies/company-workbench.md) → [ContextPatch](case-studies/contextpatch-ai-datahub-2026.md) | 요구사항·실행 조건·검증·승인·보고서의 연결 |

**[직무별 상세 읽기](docs/ROLE_GUIDE.md)**에서 백엔드·ML·데이터·모바일 검토 경로도 확인할 수 있습니다.

## 대표 프로젝트

### Company Workbench — 재현할 수 있는 업무 표본

React·TypeScript·Vite 기반 여섯 개의 개인 시제품입니다. **FaultLab**은 의도된 결함과 수정 함수를 동일 입력으로 비교하고, **StockBridge**는 CSV 재고 대조 결과를 원본 행까지 추적합니다. 특정 기업의 의뢰나 실무 경력으로 표시하지 않습니다.

[사례와 검증 범위](case-studies/company-workbench.md) · [소스](https://github.com/estona815/contextpatch-ai-datahub-2026/tree/portfolio/company-workbench-20260929/employer-workbench)

### NUTRONICS — 장치의 동작과 예외를 보여주는 발표 웹

스마트 영양제 디스펜서 졸업 팀 프로젝트입니다. 웹·시뮬레이터·검증 자료·발표 준비를 담당했으며, 정상 배출·걸림·재시도 흐름과 이벤트 로그를 보여줍니다. 시뮬레이션과 실물 장치 시험의 결과를 구분합니다.

[사례](case-studies/nutronics.md) · [소스](https://github.com/estona815/smart-pill-sim-website) · [시뮬레이터](https://estona815.github.io/smart-pill-sim-website/website/simulator.html)

### GlyphCheck · 줄대조 — 원본과 수정 결과를 함께 검토

한·영 OCR 검수 시제품입니다. 원본 영역·인식문·수정문을 연결하고, 내용 변경 후 재검토하도록 하는 상태 관리와 결과 내보내기를 다룹니다.

[사례](case-studies/glyphcheck.md) · [소스](https://github.com/estona815/glyphcheck)

## 수상과 별도 선정

| 구분 | 확인된 결과 |
|---|---|
| 수상 · 2026.10 | 수성 건축·조경 시각작품 국제 공모전 **일반 부문 장려상** |
| 수상 · 2026.10 | Lucasverse Fanfiction Contest **1위**, 「Authorized Driver」 · [공식 발표](https://www.lucasflint.com/2026-lucasverse-fanfiction-contest-winner-authorized-driver-by-kwon-jun/) |
| 수상 · 2026.08 | 코레일유통 대국민 아이디어 공모전 **수상** · 확인한 통지에 세부 등급 미기재 |
| 선정 · 2026.09 | Build Beyond Hackathon · FitShadow **Top 20 Finalists** · [공개 결과](https://devpost.com/software/fitshadow-tolerance-ghost-lab) |

[수상·선정 근거 및 표기 기준](docs/ACHIEVEMENTS.md). 창작·아이디어 수상을 개발 해커톤 우승으로 바꾸어 설명하지 않으며, 전원 참가 항목이나 접수 완료는 수상으로 세지 않습니다.

## 확장 프로젝트와 코드 표본

| 관심 분야 | 프로젝트 | 검토할 지점 |
|---|---|---|
| 제품·백엔드 | [TuberBot Market](case-studies/tuberbot-market.md) | 계약·복식부기 원장·outbox·멱등성·권한 |
| Agent workflow | [ContextPatch AI](case-studies/contextpatch-ai-datahub-2026.md) | 제한된 패치·검증·승인·recorded replay |
| Edge AI | [SOUNDMARK EDGE](case-studies/soundmark-edge.md) | Python/Kotlin 계약·INT8·few-shot·UNKNOWN 거절 |
| ML 평가 | [AbstainLab](case-studies/abstainlab.md) | 그룹 분리·validation-only 선택·holdout 실패 공개 |
| 데이터 분석 | [Seoul Bicycle Audit](case-studies/ttareungi-monthly-audit-2026-koreashe95427.md) | 모집단 통제·원본 hash·누락과 0 구분 |
| 모바일 | [Focus Battery](case-studies/focus-battery.md) · [Study Merge](case-studies/study-merge.md) | 로컬 상태·도메인 분리·샘플 콘텐츠 경계 |

[CreatorOps의 승인 정책](samples/creatorops/publish-policy.ts), [비용 계산 도메인](samples/paper-risk/cost_model.py), [INSTATOON의 프로젝트 식별자](samples/instatoon/project-id.ts)는 로컬 프로젝트에서 발췌한 코드입니다. 전체 소스 snapshot은 비공개로 보관하며 샘플은 완성된 배포 패키지가 아닙니다.

## 증거를 읽는 기준

요구사항을 상태·데이터·권한·실패 조건으로 나누고, 작은 실행 경로와 검토 근거를 연결합니다. AI 도구 활용, 본인 담당, 저장소 구현, 실제 운영 성과를 각각 구분합니다. 저장소 관리 권한은 모든 코드의 단독 저작 증거가 아닙니다.

- [AI 사용·개인 기여·증거 기준](docs/EVIDENCE.md) · [기존 검증 기록](docs/VALIDATION.md)
- [기존 전체 공개 이력](docs/PROJECTS.md) · [개발 타임라인](docs/TIMELINE.md) · [로컬 프로젝트 기록](docs/LOCAL_PROJECTS.md)
- [코드 샘플](samples/README.md) · [기존 공개 증거 CSV](evidence/public-claims.csv) · [English archive](README.en.md)

**갱신 구분:** 2026-10-31에는 수상 통지·공식 발표·채용 문서·대표 사례를 대조해 정리했습니다. 기존 전체 목록, 소스 패키지 manifest, CSV와 과거 검증 자료는 2026-10-16 등의 당시 기록이며 현재 전수 재검증 결과가 아닙니다. 상용 사용자·매출·실결제·실물 성능은 새 증거 없이 추가하지 않았습니다. 개인 연락처·메일 원문·계약·인증정보는 공개하지 않습니다.
