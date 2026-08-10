<!-- notion-page-id: 3b82cdd741ac80919af1e5c8843174f7 -->

# Nest.js란?

- TypeScript 기반의 Node.js 서버 프레임워크로, 모듈형 아키텍처와 의존성 주입(DI) 패턴을 사용하여 대규모 프로젝트와 협업에 최적화된 설계를 제공합니다 

- **핵심 구성 요소**:
  - **Controller**: 클라이언트의 요청(HTTP Request)을 받고 응답(Response)을 처리하는 입구 역할을 합니다.
  - **Service**: 실제 비즈니스 로직, 데이터 연산, DB 통신 등을 담당하는 핵심 처리부입니다.
  - **Module**: 관련된 Controller와 Service를 하나의 기능 단위로 묶어 관리하는 조직화 도구입니다 

- **의존성 주입(Dependency Injection)**: 서비스를 모듈의 프로바이더(Provider)에 등록하여 재사용성을 높이고, 생성자(Constructor)를 통해 주입받아 사용하는 방식을 사용합니다.

> Spring Boot와 거의 유사한 패턴을 갖고 있다.

# 설치법

[**Nest CLI**](https://nestjs.burt.pe.kr/cli/overview)를 사용해 프로젝트를 생성하거나 [**스타터 프로젝트를 복제**](https://nestjs.burt.pe.kr/#alternatives)할 수 있습니다. 두 방법 모두 동일한 결과를 제공합니다.

```bash

$ npm i -g @nestjs/cli
$ nest new project-name
```

- 더 엄격한 기능 세트를 가진 TypeScript 프로젝트를 생성하려면 `nest new` 명령어에 `--strict` 플래그를 추가하면 된다.

### **Git**을 사용하여 TypeScript 스타터 프로젝트를 설치하는 방법도 있다.

```bash
$ git clone https://github.com/nestjs/typescript-starter.git project
$ cd project
$ npm install
$ npm run start
```
