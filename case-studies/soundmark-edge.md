# SOUNDMARK EDGE

휴대전화 안에서 학습하는 소리 인식 실험

## 문제와 제품

개인 공간의 소리를 소수 예시로 등록하고 로컬 embedding과 UNKNOWN 거절로 구분하는 Android PoC입니다.

## 저장소에서 확인할 설계

- Python/Kotlin log-mel 계약 및 LiteRT FP32/INT8 encoder
- few-shot prototype, threshold·margin·temporal agreement
- Compose 화면과 Arm64 test APK, benchmark export

## 증거와 검증

공개 README의 synthetic holdout 56개 기록: INT8 파일 10,776 B, FP32 34,384 B, 3-shot macro F1 0.9353. 저장소 보고이며 이번 독립 모델 실행은 없습니다.

[소스 저장소](https://github.com/estona815/soundmark-edge) · [검토한 README 고정 SHA](https://github.com/estona815/soundmark-edge/blob/e06ac9ca1dc7ce8c8131813ecb450f6f4a35e084/README.md)

## 범위와 개인 기여

실물 Android 기기 지연·발열·마이크·진동·배터리 결과는 미검증입니다. 합성 데이터 수치를 현장 정확도로 해석하지 않습니다.

개인별 기여는 [증거 기준](../docs/EVIDENCE.md)을 따릅니다. 저장소 구현 설명을 후보자의 모든 코드 직접 작성 증거로 해석하지 않습니다. AI 활용 내역은 각 원본 저장소의 disclosure를 우선합니다.

[전체 프로젝트](../docs/PROJECTS.md) · [포트폴리오](../README.md)
