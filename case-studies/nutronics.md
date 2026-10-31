# NUTRONICS · 스마트 영양제 디스펜서

**검토 직무:** 로봇 운영·테스트, 소프트웨어 QA, 기술 문서화

졸업 팀 프로젝트의 제작 과정과 배출 흐름을 설명하는 웹사이트·시뮬레이터입니다. 실제 장치 제작과 발표용 소프트웨어를 구분해 보여줍니다.

[소스 저장소](https://github.com/estona815/smart-pill-sim-website) · [발표 웹사이트](https://estona815.github.io/smart-pill-sim-website/) · [시뮬레이터](https://estona815.github.io/smart-pill-sim-website/website/simulator.html)

## 문제와 동작 흐름

영양제 배출 과정을 단순 성공 화면이 아니라 정상 배출, 걸림, 재시도, 상태 변화로 설명합니다. 발표 중 시나리오를 전환하면서 이벤트 로그와 시각화를 함께 확인할 수 있도록 구성했습니다.

저장소 README에 안내된 시연 동작은 `다음 배출`, `PASS`, `Jam Test`, `RETRY`입니다. 배출 장치의 구조 설명, 제작 사진·회로도·UI 등 증빙 자료와 발표 흐름을 연결합니다.

## 본인 담당과 팀 작업의 경계

본인 제공 이력의 담당 범위는 웹·시뮬레이터·검증 자료·발표 준비입니다. 기구, 회로·전원, 제어·DB와 웹·문서 작업은 팀의 역할 분담이며, 전체 하드웨어를 혼자 제작했다고 표현하지 않습니다. 웹 구현과 문서 정리에는 AI 도구를 활용했습니다.

## 검토할 기술 요소

- 정적 HTML/CSS/JavaScript 기반 발표 웹과 시뮬레이터.
- 정상·오류·재시도 상태와 이벤트 로그를 통한 동작 설명.
- GitHub Pages의 루트 및 하위 경로를 함께 고려한 상대경로 구성.
- 입력·시나리오·관측 상태를 연결하는 검수 및 발표 자료.

## 재현 시작점

아래는 저장소에 안내된 실행 절차이며, 이번 문서 정리에서 실행한 테스트 명령이 아닙니다.

```bash
git clone https://github.com/estona815/smart-pill-sim-website.git
cd smart-pill-sim-website
python3 -m http.server 4173
```

브라우저에서 `http://localhost:4173/website/simulator.html`을 열고 각 시나리오의 상태와 로그를 비교합니다.

## 검증 범위

2026-10-31 원본 README를 확인했습니다. 확인한 파일의 Git blob SHA는 `8637ddcc51992699837e000e61ab25157e14f813`입니다. 이는 파일 식별자이며 저장소 전체의 commit SHA나 테스트 결과가 아닙니다.

이번 갱신에서는 실물 장치·센서·모터를 구동하거나 배출 성공률을 재측정하지 않았습니다. 시뮬레이터 시연을 실제 배출 성능, 안전성, 신뢰성 보장으로 전용하지 않습니다. 상세 개인 기여와 장치 시험 결과는 추가 원본 증빙으로 구분해 설명합니다.

[포트폴리오](../README.md) · [로봇·데이터 운영 이력서](../docs/RESUME_ROBOT_OPS_KO.md) · [증거 기준](../docs/EVIDENCE.md)
