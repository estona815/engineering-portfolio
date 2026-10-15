# TuberBot Market

계약과 원장의 일관성을 지키는 마켓플레이스

## 문제와 제품

크리에이터와 광고주 간 제안·계약·검수·원장·지급 준비 상태가 서로 모순되지 않도록 거래 흐름을 모델링한 제품 프리뷰입니다.

## 저장소에서 확인할 설계

- Next.js·TypeScript·PostgreSQL 기반 모듈형 모놀리스
- 계약 스냅샷, 정수 금액·수수료, 복식부기 원장
- transactional outbox, 멱등성, 재시도·dead-letter, 주문 당사자 권한

## 증거와 검증

2026-08-05 기존 로컬 감사 기록: dirty working tree에서 58개 테스트 파일·306개 테스트, typecheck·lint·build 통과. 이번에는 재실행하지 않았으며 공개 main/배포본의 테스트 결과로 전용하지 않습니다.

[소스 저장소](https://github.com/estona815/tuberbot-market) · [검토한 README 고정 SHA](https://github.com/estona815/tuberbot-market/blob/9eb834e11ce310e6e133a5811d0dae9666b04c08/README.md)

## 범위와 개인 기여

공개 사이트는 샘플 데이터 프리뷰입니다. 실결제·지급·고객·매출은 입증되지 않았습니다. 기존 감사는 계정 연결 커밋 2개의 부분 기여만 확인했습니다.

개인별 기여는 [증거 기준](../docs/EVIDENCE.md)을 따릅니다. 저장소 구현 설명을 후보자의 모든 코드 직접 작성 증거로 해석하지 않습니다. AI 활용 내역은 각 원본 저장소의 disclosure를 우선합니다.

[전체 프로젝트](../docs/PROJECTS.md) · [포트폴리오](../README.md)
