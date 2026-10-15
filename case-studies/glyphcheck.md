# GlyphCheck · 줄대조

OCR 결과를 원본 영역과 함께 검토

## 문제와 제품

한·영 인쇄 텍스트 이미지에서 실제 OCR 결과와 근사 원본 영역을 연결하고 수정·검토 상태를 export합니다.

## 저장소에서 확인할 설계

- Tesseract.js 7 기반 한·영 로컬 CPU OCR
- 편집 시 검토 완료 상태 해제, 원문·수정문·source hash 보존
- loopback 서비스와 제한된 이미지 입력·실행 시간

## 증거와 검증

README의 real OCR integration 절차와 검토 export 계약을 확인했습니다. 이번에는 모델 다운로드·OCR 실행을 하지 않았습니다.

[소스 저장소](https://github.com/estona815/glyphcheck) · [검토한 README 고정 SHA](https://github.com/estona815/glyphcheck/blob/64ff6626e877c8cc327d7dc52387e0c8dec72923/README.md)

## 범위와 개인 기여

pretrained 모델 활용이며 자체 모델 학습·독자적 정확도·의료/법률 판정 능력을 주장하지 않습니다.

개인별 기여는 [증거 기준](../docs/EVIDENCE.md)을 따릅니다. 저장소 구현 설명을 후보자의 모든 코드 직접 작성 증거로 해석하지 않습니다. AI 활용 내역은 각 원본 저장소의 disclosure를 우선합니다.

[전체 프로젝트](../docs/PROJECTS.md) · [포트폴리오](../README.md)
