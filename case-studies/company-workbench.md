# Company Workbench
## 결함을 재현하고 재고 차이를 원본까지 추적하는 웹 도구

[포트폴리오](../README.md) · [소스와 실행 안내](https://github.com/estona815/contextpatch-ai-datahub-2026/tree/portfolio/company-workbench-20260929/employer-workbench)

| 항목 | 내용 |
|---|---|
| 형태 | 공개 직무·제품 맥락을 참고한 개인 시제품 6개 |
| 먼저 볼 모듈 | FaultLab · StockBridge |
| 담당 | 문제 선정, AI 도구와 협업한 제작·검토, 재현 절차와 검증 자료 |
| 기술 | React · TypeScript · Vite · Node 테스트 |
| 현재 범위 | 합성 입력을 사용하는 브라우저 작업 표본 |

## 해결하려던 문제

결함 보고서에 실패 결과만 있으면 같은 문제를 다시 확인하기 어렵습니다. 재고 대조에서도 합계만 보면 빈 수량·충돌 중복·통화 차이가 결과에 섞일 수 있습니다. 이 표본은 **입력 → 적용 규칙 → 관측 결과 → 원본 근거**를 연결합니다.

## 중요한 설계 선택

### 1 결함 함수와 수정 함수를 같은 입력으로 비교

FaultLab은 수량, 할인, 중복 주문, 만료 시각, 검색 응답 순서, 반복 취소의 여섯 시나리오를 제공합니다. 수정 함수와 별도의 업무 규칙으로 기대값을 계산하여 비교합니다.

유효한 입력에서 결함이 재현되지 않으면 그 결과를 그대로 보여줍니다. 잘못된 실험 입력은 별도로 처리하고, 현재 실행에서 관측한 실패를 Markdown·JSON 보고서에 남깁니다.

[엔진](https://github.com/estona815/contextpatch-ai-datahub-2026/blob/0669f4c8a0e066d1d3ee9dd19f193a640fa86473/employer-workbench/src/modules/wisewires/engine.ts) · [기존 테스트](https://github.com/estona815/contextpatch-ai-datahub-2026/blob/0669f4c8a0e066d1d3ee9dd19f193a640fa86473/employer-workbench/tests/wisewires.test.mjs)

### 2 불명확한 데이터는 합산 전에 보류

StockBridge는 SKU와 지역을 기준으로 CSV 재고를 대조합니다. 빈 수량은 입력 오류로 처리하고, 충돌하는 중복은 검토 대상으로 보류합니다. 금액은 통화별로 계산하며 결과에서 원본 행과 원래 값을 확인할 수 있습니다.

자동 처리 범위를 줄이는 선택이지만, 잘못된 합계를 정상 결과로 받아들이는 일을 막고 검수할 위치를 분명히 합니다.

[엔진](https://github.com/estona815/contextpatch-ai-datahub-2026/blob/0669f4c8a0e066d1d3ee9dd19f193a640fa86473/employer-workbench/src/modules/vibers/engine.ts) · [기존 테스트](https://github.com/estona815/contextpatch-ai-datahub-2026/blob/0669f4c8a0e066d1d3ee9dd19f193a640fa86473/employer-workbench/tests/vibers.test.mjs)

### 3 입력이 바뀌면 이전 검토를 다시 확인

CSV나 열 연결이 바뀌면 앞선 결과에 대한 검토·내보내기를 현재 입력에 그대로 적용할 수 없습니다. 이 상태를 무효화해 사용자가 다시 계산하고 검토하도록 합니다.

## 직접 확인할 흐름

| 순서 | 확인할 행동 | 기대하는 관측 |
|---|---|---|
| FaultLab | 할인 초과 또는 만료 경계 등 입력을 바꾸어 결함·수정 함수를 비교 | 입력·기대값·실제값과 재현 여부가 함께 표시됨 |
| StockBridge | 빈 수량과 충돌 중복을 포함한 CSV를 대조 | 정상 계산과 보류·오류 행을 구분함 |
| 결과 추적 | 결과의 원본 행과 내보낸 근거를 대조 | 같은 입력을 설명하는 자료인지 확인할 수 있음 |
| 변경 처리 | 검토 후 CSV 또는 열 연결을 바꿈 | 이전 검토·내보내기 상태가 무효화됨 |

## 재현 방법

저장소의 `portfolio/company-workbench-20260929` 브랜치에서 실행합니다.

```bash
cd employer-workbench
npm ci
npm test
npm run typecheck
npm run build
```

[기존 공개 데모](https://kwon-work-49mnyp.v2.appdeploy.ai/) · [릴리스 검증 기록](https://github.com/estona815/contextpatch-ai-datahub-2026/blob/0669f4c8a0e066d1d3ee9dd19f193a640fa86473/employer-workbench/docs/RELEASE_REPORT.md)

## 검증과 적용 범위

**2026-11-03 기존 엔진·저장 경계 회귀 테스트를 재실행해 112/112 통과를 확인했습니다.** 원본 README의 TypeScript 검사·Vite 빌드는 과거 기록입니다. 과거 기록과 이번 확인 범위는 [검증 기록](../docs/VALIDATION.md)에서 구분합니다. 시연용 결함 함수의 FAIL은 의도된 동작이며 회귀 테스트 실패와 별개입니다.

현재는 개인 작업 표본입니다. 실제 재고·광고·고객 DB와의 연동, 서버 인증·권한·동시성은 추가 구현과 현장 검증이 필요한 범위입니다.

<details>
<summary>나머지 네 가지 표본</summary>

| 표본 | 확인할 동작 |
|---|---|
| AdSpec | 광고 설정 규칙·버전 비교, 변경 후 재검토 |
| FlowMap | 단계·권한·승인 조건, 중복 실행과 재시도 |
| BriefLedger | 요구사항과 정상·오류·권한 시나리오 연결 |
| AvatarOps | 사용자 범위·승인 순서·중복 적용 비교 |

</details>

[QA 이력서](../docs/RESUME_QA_KO.md) · [AI 활용과 기여 기준](../docs/EVIDENCE.md)

