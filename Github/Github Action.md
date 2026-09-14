<!-- notion-page-id: 3da2cdd741ac80f5bdaff96ea7268101 -->

# Github Action

Github Action이란 Github 저장소를 기반으로 소프트웨어 개발 **Workflow**를 자동화 할 수 있는 도구이다.

Github 내부에서 프로젝트를 빌드, 테스트, 릴리즈 또는 배포를 지원하는 기능으로서, Github에서 제공하는 CI/CD 도구라고 생각하면 될 것이다.

추가적인 CI/CD 툴을 사용하지 않고 깃허브 하나로 버전관리부터 테스트 배포까지 가능한 점이 Github Action의 장점이라고 생각한다.

Github Action에는 4가지 개념이 존재한다.

`workflow`, `Job`, `event`, `stop`이렇게 4가지가 존재한다.

이들의 관계와 흐름을 이해해야만 각종 조건과 그에 따른 액션을 스스로 정의할 수 있다.

### workflow

`workflow`는 프로젝트를 빌드, 테스트, 패키지, 릴리스 또는 배포하기 위한 전체적인 프로세스이다.

workflow는 여러개의 `Job`으로 구성되어 `event`기반으로 동작한다.
이 Job 설정을 통해 workflow를 커스텀 할 수 있다.

GitHub에게 나만의 동작을 정의한 workflow file를 만들어 전달하면 GitHub Actions이 그것을 보고 그대로 실행 시켜준다.

### Job

Job은 하나의 인스턴스(리눅스, 맥, 윈도우 등등)에서 여러 Step을 그룹시켜 실행하는 역할을 한다.

### step

Step은 순차적으로 명령어를 수행한다.

크게 Uses와 Run으로 작업 단위가 나뉘는데, Uses는 이미 다른 사람들이 정의한 명령어를 가져와 실행하는 것이고, Run은 `npm install`나 `mkdir example`과 같이 가상환경 내에서 실행할 수 있는 스크립트를 말한다.

### event

워크플로우를 실행시키는 조건을 설정한다.

예를 들어 Github에 Push나 Pull Request 같은 이벤트가 발생 했을때 실행하도록 설정하는 것이 있다.
