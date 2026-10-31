# 직무에 맞춰 읽기

2026-10-31 채용 문서 갱신. 아래 순서는 지원 직무에 맞춘 검토 경로이며, 특정 기업의 채용 진행·합격·재직을 의미하지 않습니다.

## QA·소프트웨어 테스트 / AI 업무자동화

**[공개 이력서](RESUME_QA_KO.md)** → [Company Workbench](../case-studies/company-workbench.md)의 FaultLab·StockBridge → [GlyphCheck](../case-studies/glyphcheck.md) → [NUTRONICS](../case-studies/nutronics.md).

입력·기대 규칙·관측값·재현 조건을 연결해서 확인합니다. 정상 동작뿐 아니라 경계값, 충돌 중복, 내용 변경 후 재검토, 실패·재시도에 주목하세요. 의도된 결함 시연과 회귀 테스트 실패를 구분합니다.

## 로봇 운영·테스트 / AI 데이터 검수

**[공개 이력서](RESUME_ROBOT_OPS_KO.md)** → [NUTRONICS](../case-studies/nutronics.md) → [GlyphCheck](../case-studies/glyphcheck.md) → [StockBridge](../case-studies/company-workbench.md).

장치의 동작 순서, 정상·오류·복구 상태, 로그, 원문 대조, 수정 기록을 중심으로 봅니다. 메카트로닉스와 팀 프로젝트 경험을 활용하는 신입 지원이며, 실제 산업용 로봇·VR 원격조종의 유급 실무 경력을 주장하지 않습니다. 발표용 시뮬레이션은 실물 장치 성능 시험과 별개입니다.

## AI Product / Backend Engineer

[Company Workbench](../case-studies/company-workbench.md) → [TuberBot](../case-studies/tuberbot-market.md) → [ContextPatch](../case-studies/contextpatch-ai-datahub-2026.md) → [CreatorOps 정책 샘플](../samples/creatorops/publish-policy.ts).

상태 전이, 거래 원장, outbox, 멱등성, 권한, 실패 시 동작을 중심으로 검토합니다. 외부 결제·운영 연동이 없는 부분과 개인 기여 범위를 따로 확인합니다.

## ML / Edge AI Engineer

[SOUNDMARK EDGE](../case-studies/soundmark-edge.md) → [AbstainLab](../case-studies/abstainlab.md) → [GlyphCheck](../case-studies/glyphcheck.md).

전처리 계약, 양자화 크기, UNKNOWN 거절, 그룹 분리, holdout 실패, pretrained 모델 활용의 범위를 확인합니다. 실물 기기 검증과 합성 데이터 결과를 구분합니다.

## Data / Analytics Engineer

[Seoul Bicycle Audit](../case-studies/ttareungi-monthly-audit-2026-koreashe95427.md) → [ContextPatch](../case-studies/contextpatch-ai-datahub-2026.md) → [VoltScope](../case-studies/voltscope-tracelab.md).

원본 hash, 동일 모집단, 누락 처리, 패치 검증, 측정 기록 무결성을 중심으로 검토합니다. 관측 관계와 인과 효과는 구분합니다.

## Frontend / Mobile Engineer

[Focus Battery](../case-studies/focus-battery.md) → [Study Merge](../case-studies/study-merge.md) → [GlyphCheck](../case-studies/glyphcheck.md).

로컬 상태, 도메인과 UI 분리, 검토 상태 전이, export, 콘텐츠 검증과 실기기 QA의 잔여 범위를 확인합니다.

## 면접에서 제시할 근거

본인 담당 → 구현된 동작 → 입력·기대값·관측 결과 → 아직 검증하지 않은 부분 순으로 설명합니다. 과거 실행 기록에는 날짜와 대상 소스가 따라야 합니다. 저장소 소유를 전체 코드의 단독 저작으로 확대하거나, 체크인 보고서를 이번 실행 결과로 바꾸지 않습니다.

창작·아이디어 수상과 개발 프로젝트는 각각의 증거로 표시합니다. [수상 및 선정 이력](ACHIEVEMENTS.md) · [AI 사용·개인 기여 기준](EVIDENCE.md) · [포트폴리오](../README.md)
