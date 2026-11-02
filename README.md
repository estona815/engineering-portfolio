# 권준 · Kwon Jun

### QA·테스트 / AI 업무자동화 신입

**오류가 생기는 조건을 재현하고, 원본과 결과를 연결하는 도구를 만듭니다.**

메카트로닉스를 전공하며 웹 시제품과 장치 시뮬레이터를 제작했습니다. 입력 조건·상태·예외를 정리하고, AI 도구와 협업한 구현을 재현 절차와 검토 기록으로 설명합니다.

한국폴리텍대학 서울정수캠퍼스 메카트로닉스과 · **2027년 2월 졸업예정**  
서울 근무·졸업 전 조기취업 가능 · 입사일 협의

**[이력서](docs/RESUME_QA_KO.md)** · [프로젝트 안내](docs/PROJECT_INDEX.md) · [수상·선정 근거](docs/ACHIEVEMENTS.md) · [English](README.en.md)

## 먼저 볼 세 가지

| 보여드릴 역량 | 프로젝트에서 확인할 동작 | 바로 보기 |
|---|---|---|
| 결함 재현과 수정 확인 | 같은 입력으로 결함 함수와 수정 함수를 비교하고, 현재 관측한 실패를 보고서로 기록 | [Company Workbench](case-studies/company-workbench.md) |
| 원본 대조와 수정 내용 보존 | OCR 원문·수정문·검토 상태를 연결하고, 새 OCR 요청 실패 시 이전 교정 유지 | [GlyphCheck](case-studies/glyphcheck.md) |
| 장치의 상태와 예외 설명 | 정상 배출·걸림·재시도를 전환하며 상태와 이벤트 로그 확인 | [NUTRONICS](case-studies/nutronics.md) |

## 01 Company Workbench
### 결함 재현과 CSV 재고 검수를 위한 웹 도구

**개인 시제품 · React / TypeScript / Vite**

테스트 결과나 재고 차이만 보면 어떤 입력과 규칙에서 나온 결과인지 놓치기 쉽습니다. FaultLab은 결함과 수정 함수를 같은 조건에서 비교하고, StockBridge는 차이가 생긴 원본 CSV 행까지 연결합니다.

**핵심 판단:** 충돌하는 중복 행을 자동 합산하면 오류 원인이 가려질 수 있어 검토 대상으로 보류합니다. 입력이 바뀌면 이전 결과와 검토 상태도 다시 확인하도록 구성했습니다.

**담당:** 문제 선정, AI 도구와 협업한 시제품 제작·검토, 재현 절차와 검증 자료 정리.

**최근 확인:** 2026-11-03 기존 엔진·저장 경계 회귀 테스트 **112/112 통과**. [실행 근거](docs/VALIDATION.md)

[사례와 재현 절차](case-studies/company-workbench.md) · [소스와 테스트](https://github.com/estona815/contextpatch-ai-datahub-2026/tree/portfolio/company-workbench-20260929/employer-workbench)

## 02 GlyphCheck · 줄대조
### 원본 이미지와 수정 내용을 연결하는 OCR 검수 도구

**개인 시제품 · Python / JavaScript / Tesseract.js**

한·영 인쇄문 OCR 결과를 원본 영역과 함께 확인하고 수정합니다. 원문·수정문·원본 hash·검토 상태를 JSON에 남겨 결과의 출처를 추적할 수 있습니다.

**핵심 판단:** 문장을 편집하면 이전 검토 완료 상태를 해제합니다. 새 OCR 요청이 실패했을 때는 사용자가 이미 수정한 내용을 유지합니다.

**제작 방식:** 개인 프로젝트이며 설계·구현·테스트·문서에 Codex를 활용했습니다. 기존 OCR 엔진을 통합한 검수 흐름이 중심입니다.

**최근 확인:** 2026-11-03 기존 프런트 논리 회귀 **13/13 통과**. [실행 범위](docs/VALIDATION.md)

[사례와 검토 절차](case-studies/glyphcheck.md) · [소스](https://github.com/estona815/glyphcheck)

## 03 NUTRONICS
### 스마트 영양제 디스펜서의 동작·예외 시뮬레이터

**졸업 팀 프로젝트 · HTML / CSS / JavaScript**

팀이 제작한 장치의 동작을 발표 중 직접 비교할 수 있도록 웹과 시뮬레이터를 구성했습니다. 배출 대기열·현재 상태·이벤트 로그와 제작 자료를 연결합니다.

**핵심 판단:** 정상 동작과 함께 걸림·재시도 흐름을 보여주어 장치가 어떤 상태인지 설명합니다.

**담당:** 웹·시뮬레이터·검증 자료·발표 준비. 기구·회로·제어는 팀 역할에 따라 분담했습니다. 공개 시연은 발표용 시뮬레이션입니다.

[시뮬레이터 열기](https://estona815.github.io/smart-pill-sim-website/website/simulator.html) · [사례](case-studies/nutronics.md) · [소스](https://github.com/estona815/smart-pill-sim-website)

## 외부 평가와 수상

| 분야 | 확인된 결과 |
|---|---|
| 개발 해커톤 | **Build Beyond Hackathon · FitShadow · Top 20 Finalists** |
| 플랫폼 심사 | **앱인토스 「싸괄」 20260703-3 버전 승인** |
| 아이디어 | **코레일유통 2026 대국민 아이디어 공모전 수상** |
| 시각작품 | **2026 수성 건축·조경 시각작품 국제 공모전 일반 부문 장려상** |
| 창작소설 | **2026 Lucasverse Fanfiction Contest 1위 · Authorized Driver** |

[공식 발표·통지 근거와 전체 이력](docs/ACHIEVEMENTS.md)

## 확인 자료

프로젝트별 담당, AI 활용, 실행 환경과 검증 범위는 각 사례에 기재했습니다.

[검증 기록](docs/VALIDATION.md) · [AI 활용과 기여 기준](docs/EVIDENCE.md) · [장치·데이터 운영 이력서](docs/RESUME_ROBOT_OPS_KO.md)

<details>
<summary>다른 프로젝트와 보관 자료</summary>

- [직무별로 더 보기](docs/ROLE_GUIDE.md)
- [프로젝트 안내와 공개 저장소 목록](docs/PROJECT_INDEX.md)
- [ContextPatch AI](case-studies/contextpatch-ai-datahub-2026.md) · [TuberBot Market](case-studies/tuberbot-market.md) · [SOUNDMARK EDGE](case-studies/soundmark-edge.md)
- [코드 표본](samples/README.md) · [기존 프로젝트 기록](docs/PROJECTS.md) · [개발 타임라인](docs/TIMELINE.md)

</details>

문서 갱신: 2026-11-03

