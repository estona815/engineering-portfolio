# AbstainLab

모델이 판단을 보류해야 하는 경우를 드러내기

## 문제와 제품

그룹 단위로 분리한 train/validation/test에서 판단 보류 임계값을 validation으로만 정하는 분류 실험 도구입니다.

## 저장소에서 확인할 설계

- scikit-learn StandardScaler + LogisticRegression
- group-disjoint 분리와 validation-only threshold 선택
- holdout별 결정·오류·human review 및 모델 계수 export

## 증거와 검증

README의 합성 기본 fixture: 144개 holdout 중 108개 수락, 수락 오류 8개(7.4074%), coverage 75%. validation 5% 목표가 holdout에서 미달한 점을 그대로 제시합니다.

[소스 저장소](https://github.com/estona815/abstainlab) · [검토한 README 고정 SHA](https://github.com/estona815/abstainlab/blob/bf009cace9b396fc57cbfb9b54f851adcc7f34b7/README.md)

## 범위와 개인 기여

운영 정확도·순비용 절감·형식적 위험 통제 보장이 아닙니다. 이번 실행에서는 모델을 재학습하지 않았습니다.

개인별 기여는 [증거 기준](../docs/EVIDENCE.md)을 따릅니다. 저장소 구현 설명을 후보자의 모든 코드 직접 작성 증거로 해석하지 않습니다. AI 활용 내역은 각 원본 저장소의 disclosure를 우선합니다.

[전체 프로젝트](../docs/PROJECTS.md) · [포트폴리오](../README.md)
