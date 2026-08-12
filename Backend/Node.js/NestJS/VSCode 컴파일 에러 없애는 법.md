<!-- notion-page-id: 3ba2cdd741ac8040ad2ae150aab34bfc -->

# VSCode 컴파일 에러 없애는 법

`describe`, `it`, `expect`는 Jest가 런타임에 주입하는 전역이라 타입 선언이 없으면 VSCode는 평생 코드에 문제가 있다는 걸로 착각해버려 코드에 미친 빨간딱지들을 붙여버린다.

# `@types/jest` 누락

## 01.

이를 해결하기 해결하는 방법으로는 `@types/jest`의존성을 추가하는 방법이 있다!

```bash
npm i -D @types/jest
```

## 02.

`@types/jest`의존성을 추가하고나서 `tsconfig.json`의 `types`에 jest를 추가하면 코드에 빨간줄은 말끔히 사라질 것이다!

```json
{
  "compilerOptions": {
    "types": ["node", "jest"]
  }
}
```

이렇게 해도 안되는 경우가 가끔 있는데, 그럴 떈 일일히 `@types/jest`를 import하면 된다

# Property baseUrl is not allowed

이 문제를 해결하는 방법은 두 가지가 있습니다.

## 경고를 끄기

```javascript
"ignoreDeprecations": "6.0",
```

위 설정을 추가하면 경고를 끌 수 있다. 하지만 이는 유예를 주는 것 뿐이기에 추천하지는 않는다.

## tsconfig 파일 위치 기준 상대 경로로 만들어주기

```javascript
{
  "compilerOptions": {
    "paths": {
      "@app/*": ["./src/*"],
      "@test/*": ["./test/*"]
    }
    // baseUrl 삭제, ignoreDeprecations 삭제
  }
}
```

- `baseUrl`은 `paths` 없이도 `import { X } from 'src/foo/bar'`처럼 **루트 기준 비상대 경로 import**를 가능하게 해줌
