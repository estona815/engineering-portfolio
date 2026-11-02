# NUTRONICS
## 스마트 영양제 디스펜서의 동작과 예외를 보여주는 시뮬레이터

[포트폴리오](../README.md) · [발표 웹](https://estona815.github.io/smart-pill-sim-website/) · [시뮬레이터](https://estona815.github.io/smart-pill-sim-website/website/simulator.html) · [소스](https://github.com/estona815/smart-pill-sim-website)

| 항목 | 내용 |
|---|---|
| 형태 | 4인 졸업 팀 프로젝트의 발표 웹·시뮬레이터 |
| 본인 담당 | 웹·시뮬레이터·검증 자료·발표 준비 |
| 팀 분담 | 기구 설계, 회로·전원, 제어·DB, 웹·문서·발표 |
| 기술 | HTML · CSS · JavaScript · GitHub Pages |
| 공개 결과물 | 동작 시뮬레이션, 상태·이벤트 로그, 제작 자료 |

## 해결하려던 문제

장치가 정상적으로 동작하는 장면만으로는 걸림이 생겼을 때의 상태와 복구 과정을 설명하기 어렵습니다. 발표 중 같은 조건에서 시나리오를 바꾸어 보고, 상태 변화와 로그를 함께 읽을 수 있는 화면을 구성했습니다.

## 중요한 설계 선택

### 1 정상 동작과 예외 흐름을 함께 시연

배출 대기열과 현재 상태를 표시하고 `다음 배출`, `PASS`, `Jam Test`, `RETRY`를 통해 동작을 설명합니다. 걸림과 재시도를 별도 흐름으로 보여줍니다.

### 2 상태 변화와 이벤트 로그를 연결

화면의 움직임과 함께 로그를 남겨 어떤 일이 먼저 일어났는지 확인할 수 있도록 했습니다. 발표자가 결과뿐 아니라 과정과 예외 조건을 설명하는 데 활용합니다.

### 3 제작 자료와 소프트웨어 역할을 연결

구조 설명, 제작 사진·회로도·UI 자료를 발표 웹에서 확인할 수 있도록 정리했습니다. 본인 담당은 웹·시뮬레이터·자료·발표이며, 하드웨어는 팀의 역할 분담에 따라 진행했습니다. 웹 구현과 문서 작업에는 AI 도구를 활용했습니다.

[시뮬레이터 코드](https://github.com/estona815/smart-pill-sim-website/blob/5befdc7448d5f1d19613ba12d8c160ffb4ebd424/website/simulator.js) · [팀 역할과 실행 안내](https://github.com/estona815/smart-pill-sim-website/blob/5befdc7448d5f1d19613ba12d8c160ffb4ebd424/README.md)

## 직접 확인할 흐름

| 시나리오 | 확인할 내용 |
|---|---|
| 정상 배출 | 대기열과 배출 상태가 어떻게 바뀌는지 확인 |
| 걸림 | Jam Test 후 상태와 오류 로그를 함께 확인 |
| 재시도 | RETRY 후 상태가 어떻게 전환되는지 확인 |
| 발표 설명 | 제작 자료와 시뮬레이터의 담당 범위를 연결해 설명 |

## 재현 방법

정적 웹이므로 저장소에서 로컬 서버를 실행하면 됩니다.

```bash
python3 -m http.server 4173
```

`http://localhost:4173/website/simulator.html`을 엽니다.

## 검증과 적용 범위

공개 결과물은 발표용 시뮬레이터입니다. 실제 센서·모터 구동, 배출 성공률, 연속 운전 신뢰성은 실물 시험으로 확인할 항목입니다. 소스 검토 대상은 `5befdc7448d5f1d19613ba12d8c160ffb4ebd424`이며, 이번 확인 범위는 [검증 기록](../docs/VALIDATION.md)에 기재합니다.

[장치·데이터 운영 이력서](../docs/RESUME_ROBOT_OPS_KO.md) · [AI 활용과 기여 기준](../docs/EVIDENCE.md)

