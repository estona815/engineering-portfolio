# 추가 로컬 프로젝트

기존 공개 저장소 이외의 로컬 개발 자료입니다. 원본을 변경하지 않고 소스 snapshot을 비공개 보관했으며, 일부 읽기 쉬운 샘플만 공개했습니다. 전체 실행·배포 완료를 의미하지 않습니다.

## INSTATOON STUDIO

TypeScript 모노레포에서 아이디어→스토리보드→이미지→합성→QC→카루셀 패키지를 ports/adapters로 분리한 로컬 도구입니다. 게시 작업은 수동이며 Instagram 로그인·자동 게시는 포함하지 않습니다.

보관된 소스 파일: 81개. 민감 이름·실행 환경·데이터·인증 모듈이 제외된 curated snapshot입니다.

## CreatorOps Studio

typed API, 도메인, 정책 엔진, 워크플로 상태와 media worker를 분리한 로컬 제작 도구입니다. 공개 샘플은 실제 네트워크 업로드 없이 QC·권리·정확한 콘텐츠 hash 승인·feature flag를 검증하는 정책 함수입니다.

보관된 소스 파일: 88개. 민감 이름·실행 환경·데이터·인증 모듈이 제외된 curated snapshot입니다.

## Paper Risk Engine

Python 기반 paper/dry-run 연구 엔진의 비용·리스크 도메인입니다. 공개 샘플은 Decimal 수수료·spread·slippage 계산이며, 금융 API·계좌·주문·수익률 주장을 포함하지 않습니다.

보관된 소스 파일: 364개. 민감 이름·실행 환경·데이터·인증 모듈이 제외된 curated snapshot입니다.

## LogicArchiveManager

Logic 프로젝트 보관 전 비파괴 감사와 삭제 gate를 분리한 로컬 관리 도구입니다. 구현 문서의 범위는 감사이며 원본 삭제·원격 복원 성공을 성과로 주장하지 않습니다.

보관된 소스 파일: 11개. 민감 이름·실행 환경·데이터·인증 모듈이 제외된 curated snapshot입니다.

## 미디어·운영 도구

인터넷 메모리 뮤직비디오 구성 도구, short-form video agent, 오디오 처리 유틸리티, 저장 용량·작업 조정 하네스의 선택 소스도 비공개로 보관했습니다. 원본 미디어·동의서·개인정보·중앙 상태 DB는 업로드하지 않았습니다.

SOL AUDIO의 33개 작업 폴더는 동일 Git common directory로 연결된 worktree이며 하나의 프로젝트로 취급합니다. 기존 비공개 제품 소스를 공개로 전환하지 않았습니다.

[개발 타임라인](TIMELINE.md) · [코드 샘플](../samples/README.md)

## 추가 보관 범위

REAPER Lua/ReaScript, mix/master 하네스, 오디오 복구 유틸리티, Logic MCP 서버, SOL AUDIO의 대표 작업 트리와 별도 로컬 프로토타입, 로컬 영상 엔진의 선택 소스도 비공개로 보관했습니다. 최종 선택 소스는 16개 위치·2,120개 파일이며 제품 수가 아닙니다. SOL AUDIO 복사본은 하나의 제품군으로 묶습니다. 모델·미디어·인증·Git 원문 이력은 복사하지 않았으며, 원본 저장소와 미커밋 변경은 보존했습니다.
