# VoltScope TraceLab

센서 신호보다 먼저 기록의 무결성을 확인

## 문제와 제품

누락 패킷·시계 재시작·값의 이상을 구분하고, 원본 행과 hash를 따라 재검증하는 브라우저 도구입니다.

## 저장소에서 확인할 설계

- sequence·device/received time 검증과 trace segmentation
- median/MAD 기반 deviation 관측과 원본 CSV 행 연결
- 브라우저 로컬 분석, source SHA-256 및 report 재검증

## 증거와 검증

README와 체크인 synthetic fixture의 재현 절차를 검토했습니다. 실제 설비의 원인 진단·안전 판단으로 검증한 결과는 없습니다.

[소스 저장소](https://github.com/estona815/voltscope-tracelab) · [검토한 README 고정 SHA](https://github.com/estona815/voltscope-tracelab/blob/db990d311557185720cfea075d62094e9279387f/README.md)

## 범위와 개인 기여

hash 일치는 원본 측정의 진실성·저자 신원·전자서명을 증명하지 않습니다.

개인별 기여는 [증거 기준](../docs/EVIDENCE.md)을 따릅니다. 저장소 구현 설명을 후보자의 모든 코드 직접 작성 증거로 해석하지 않습니다. AI 활용 내역은 각 원본 저장소의 disclosure를 우선합니다.

[전체 프로젝트](../docs/PROJECTS.md) · [포트폴리오](../README.md)
