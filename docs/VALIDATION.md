# 검증 기록

## 2026-11-03 대표작 재실행

포트폴리오 정리 과정에서 ChatGPT가 공개 저장소의 고정 커밋을 가져와 기존 테스트를 실행했습니다. 소스와 테스트를 수정하지 않았으며, 사용한 28개 파일의 Git blob SHA가 원본과 일치하는지 확인했습니다. 환경은 Node.js 24.22.1입니다.

| 대상 | 결과 | 이번에 확인한 범위 |
|---|---|---|
| Company Workbench | **112/112 통과**, 실패·건너뜀 0 | 기존 순수 엔진·입력·저장 경계 회귀 테스트 |
| GlyphCheck | **13/13 통과** | Node VM·최소 DOM·모의 응답 기반 프런트 논리 회귀 |
| NUTRONICS | 소스와 README 확인 | 정상·걸림·재시도·로그의 구현 경로 |

[실행 요약](../evidence/validation-20261103/summary.json) · [원본 파일과 SHA](../evidence/validation-20261103/source-manifest.json)

### Company Workbench

소스 커밋: `0669f4c8a0e066d1d3ee9dd19f193a640fa86473`

`npm test` 성공 후 같은 원본 테스트를 아래 명령으로 실행하여 개별 112개 결과를 확인했습니다. 첫 명령의 환경 reporter는 테스트 파일 7개로 요약했습니다.

```bash
cd employer-workbench
npm test
node --test --test-isolation=none --test-reporter=tap tests/*.test.mjs
```

[112개 테스트 로그](../evidence/validation-20261103/workbench-node-tests-detailed.tap)

TypeScript 검사와 Vite 빌드는 이번에 실행하지 않았습니다. 원본 README의 기존 빌드 기록과 이번 테스트 결과를 구분합니다.

### GlyphCheck

소스 커밋: `64ff6626e877c8cc327d7dc52387e0c8dec72923`

```bash
node tests/frontend_regression.cjs --expected-sha b4a825d2460372833abfc7714a5ec9c78163f4eb663da17807ef631db17069d4
```

[13개 논리 회귀 로그](../evidence/validation-20261103/glyphcheck-frontend-regression.log)

실제 OCR 모델 실행, HTTP 통합, 실브라우저 E2E는 이번 범위에 포함하지 않았습니다. 13개 결과는 수정 내용 보존·검토 상태·timeout 등의 논리 회귀이며 OCR 정확도 수치가 아닙니다.

### 문서와 공개 범위

대표 사례의 내부 링크, 코드 샘플 SHA, 기존 카탈로그 규칙과 선택된 개인정보 패턴을 저장소 검증 스크립트로 확인합니다. 최신 공개 목록은 [2026-11-03 메타데이터](../evidence/public-repositories-20261103.json), 아래 과거 수집 목록은 당시 기록입니다.

## 과거 검증 기록

실행일: 2026-10-16 KST. Node.js 24.19.0 및 Python 표준 라이브러리 사용. 유료 API·모델 다운로드·실제 게시·금융 주문 없이 실행했습니다.

## 코드 샘플

```sh
node --test scripts/policy.test.mjs
python3 -B -m unittest discover -s scripts -p 'test_*.py' -v
python3 -B scripts/validate_portfolio.py
```

- CreatorOps 정책 발췌: **10 tests PASS**. 콘텐츠 변경 후 승인 무효화, QC, provenance, feature flag, 공개/예약 추가 승인, fixture 차단, 프로젝트 불일치, disclosure, untrusted directive 처리.
- 비용 계산 도메인 발췌: **4 tests PASS**. Decimal 정밀 비용·bps, 매도 규제 비용 분리, stress의 원본 불변성, 0 notional 정의.
- 포트폴리오 검사: 상대 파일 링크, 저장소 목록 중복·fork 분류, 샘플 SHA-256, 일부 민감정보 패턴. 재실행 명령은 위와 같습니다.

발췌 검사 통과는 CreatorOps 전체 서비스나 금융 엔진 전체, 실제 게시·실거래의 검증을 뜻하지 않습니다. INSTATOON 식별자 샘플은 원본 패키지 import를 유지한 코드 열람용이며 단독 실행 패키지가 아닙니다. 패턴 검사는 모든 형태의 민감정보 부재를 보증하지 않습니다.

## 실행되지 않은 검사

INSTATOON 원본 workspace에서 Vitest 실행을 시도했으나 설치된 `vitest/vitest.mjs`를 찾지 못해 `MODULE_NOT_FOUND`로 종료했습니다. 테스트 통과로 기록하지 않았습니다. 원본 의존성을 재설치하거나 원본 lockfile을 변경하지 않았습니다. 로컬 재현은 원본 workspace의 pnpm 11.19.0과 Node 22+ 환경에서 `pnpm install --frozen-lockfile`, `pnpm test`, `pnpm typecheck` 순서입니다.

기존 프로젝트 65개 전체를 빌드·테스트하지 않았고, 기기 모델·인증·외부 서비스가 필요한 검증은 수행하지 않았습니다. 이전 날짜의 체크인 결과와 로컬 감사 기록은 각 사례에서 날짜·범위를 함께 표시합니다.

## 출처와 보존

공개 계정 inventory는 GitHub API에서 수집했고 생성일·HEAD·주요 언어·fork·빈 저장소 상태를 기록했습니다. 소스 발췌와 비공개 snapshot의 SHA-256을 원본 파일과 대조했습니다. 원본 프로젝트·Git 이력·미커밋 변경·미디어를 이동·삭제하지 않았습니다.

수상은 공개 주최자 발표와 두 건의 개별 수상 통지를 확인했습니다. 수성 공고의 이름은 마스킹되어 있어 공개 PDF만으로 신원을 확인했다고 주장하지 않습니다. 계약서나 수상작 원문은 재배포하지 않았습니다.