<!-- notion-page-id: 3d52cdd741ac80eca701c1fe6210f2ba -->

# declare

이미 어딘가(외부 라이브러리, HTML 스크립트 태그, 런타임 환경 등)에 존재하는 변수나 모듈의 타입 정보만 컴파일러에게 알려주는 키워드이다.

실제 자바스크립트 실행 코드를 생성하지 않으며, 이 대상은 런타임에 반드시 존재하니 타입 검사 시 오류를 내지 말라고 컴파일러에게 전달하는 역할을 한다.

```typescript
// 컴파일러에게 Kakao라는 전역 객체가 존재한다고 알림
declare const Kakao: any;

Kakao.init('API_KEY'); // 컴파일 에러 없이 작성 가능
```
