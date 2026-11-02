# GlyphCheck · 줄대조
## 원본 이미지와 수정 내용을 연결하는 OCR 검수 도구

[포트폴리오](../README.md) · [소스와 실행 안내](https://github.com/estona815/glyphcheck)

| 항목 | 내용 |
|---|---|
| 형태 | 한·영 인쇄문 이미지를 검수하는 로컬 시제품 |
| 제작 방식 | 권준 개인 프로젝트. 설계·구현·테스트·문서에 Codex 활용 |
| 기술 | Python · JavaScript · Tesseract.js 7 · 사전학습 한·영 OCR 모델 |
| 공개 결과물 | 원본 대조 화면, 수정·검토 상태, TXT·JSON 내보내기 |
| 현재 범위 | 단일 PNG/JPEG 이미지의 OCR과 사람의 교정 작업 |

## 해결하려던 문제

OCR 결과를 별도 편집기에 옮기면 어떤 원본에서 나온 문장인지, 무엇을 수정했는지 확인하기 어려워집니다. GlyphCheck는 원본 영역·인식문·수정문을 같은 검토 흐름에 두고 결과의 출처를 남깁니다.

## 중요한 설계 선택

### 1 문장이 바뀌면 검토 완료 상태를 해제

검토가 끝난 내용이 다시 수정되면 앞선 확인을 그대로 사용할 수 없습니다. 편집 시 `reviewed=false`로 돌아가 다시 검토할 대상을 구분합니다. OCR 엔진의 신뢰도는 원래 인식 결과의 값으로 유지합니다.

### 2 새 OCR이 실패해도 이전 교정을 보존

새 결과가 유효한지 확인한 뒤 기존 상태를 교체합니다. 이미지 읽기, HTTP 응답, 모델 실행, JSON 파싱, 시간 초과에서 실패했을 때 사용자가 이미 수정한 내용을 유지하는 흐름입니다.

### 3 내보낸 결과에도 출처와 검토 상태를 유지

JSON에 원문·수정문·원본 hash·검토 여부를 함께 남깁니다. 미검토 행도 내보낼 수 있으며 화면 안내와 JSON 상태로 구분합니다. 원본 이미지 영역과 OCR 신뢰도는 사람이 검토할 때 참고하는 정보입니다.

[화면과 상태 처리](https://github.com/estona815/glyphcheck/blob/64ff6626e877c8cc327d7dc52387e0c8dec72923/web/app.js) · [프런트 회귀 테스트](https://github.com/estona815/glyphcheck/blob/64ff6626e877c8cc327d7dc52387e0c8dec72923/tests/frontend_regression.cjs)

## 직접 확인할 흐름

| 순서 | 확인할 행동 | 기대하는 관측 |
|---|---|---|
| 1 | PNG/JPEG를 열고 OCR 실행 | 인식문과 근사 원본 영역을 함께 확인 |
| 2 | 한 줄을 검토 완료한 뒤 다시 편집 | 해당 줄의 검토 완료 상태가 해제됨 |
| 3 | 기존 교정이 있는 상태에서 새 요청 실패 상황 확인 | 이전 교정 내용이 유지됨 |
| 4 | TXT와 JSON 내보내기 | JSON에서 원문·수정문·검토 상태·hash를 확인 |

## 재현 방법

Python 3.9+와 Node.js 22+가 필요합니다. 최초 준비 단계에서 고정된 무료 OCR 모델을 내려받고 SHA-256을 확인합니다.

```bash
npm install
python3 fetch_models.py
python3 server.py
```

`http://127.0.0.1:8765`에서 실행합니다. 준비 후 OCR은 로컬 CPU에서 수행합니다.

[HTTP 통합 테스트](https://github.com/estona815/glyphcheck/blob/64ff6626e877c8cc327d7dc52387e0c8dec72923/tests/test_http.py) · [모델 출처와 라이선스](https://github.com/estona815/glyphcheck/blob/64ff6626e877c8cc327d7dc52387e0c8dec72923/THIRD_PARTY_NOTICES.md)

## 검증과 적용 범위

이번에 확인한 소스는 `64ff6626e877c8cc327d7dc52387e0c8dec72923`입니다. **2026-11-03 기존 프런트 논리 회귀 13/13 통과**를 확인했습니다. Node VM·최소 DOM·모의 응답으로 상태와 오류 처리를 검사한 결과입니다. 실제 OCR·HTTP·실브라우저 시험과 구분하며 [검증 기록](../docs/VALIDATION.md)에 명령과 로그를 기재합니다.

사전학습 OCR을 통합한 검수 도구입니다. 손글씨·복잡한 다단 문서·흐린 인쇄물의 정확도와 읽기 순서는 별도 평가가 필요하며, 원본을 보면서 교정하는 절차를 전제로 합니다.

[QA 이력서](../docs/RESUME_QA_KO.md) · [AI 활용과 기여 기준](../docs/EVIDENCE.md)

