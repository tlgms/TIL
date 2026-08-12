<!-- notion-page-id: 3ba2cdd741ac80cf9ecefb7bd4b6aa82 -->

# Export

한 파일에서 여러 개의 값이나 타입을 내보낼 때 가장 많이 사용하는 방식이다.
내보낸 이름 그대로 가져와야(import) 한다.

## 1. Named Export (이름을 지정해서 내보내기)

한 파일에서 여러 개의 값이나 타입을 내보낼 때 가장 많이 사용하는 방식이다.
내보낸 이름 그대로 가져와야(`import`) 한다

### 선언과 동시에 내보내기

```typescript
// 변수 및 함수
export const API_URL = "https://api.example.com";
export function add(a: number, b: number): number {
  return a + b;
}

// TypeScript 전용: 타입 및 인터페이스
export type UserRole = "admin" | "user" | "guest";
export interface User {
  id: number;
  name: string;
  role: UserRole;
}
```

### 선언 후 묶어서 내보내기

```typescript
const MAX_SIZE = 100;
function logMessage(msg: string): void {
  console.log(msg);
}

// 파일 하단에서 한 번에 export
export { MAX_SIZE, logMessage };
```

## 2. Default Export (기본값으로 내보내기)

파일당 단 하나의 대표 값(또는 클래스, 함수)만 내보낼 때 사용한다. 
가져오는 쪽에서 이름을 자유롭게 지을 수 잇따!

```typescript
// 단일 함수 default export
export default function mainConfig() {
  return { env: "production" };
}

// 또는 클래스/객체
class Calculator {
  // ...
}
export default Calculator;
```

> **참고**: `type`이나 `interface`도 `export default`가 가능하지만, 가독성과 타입 추론을 위해 주로 **Named Export** 방식을 권장합니다.

## 3. Type-only Export (타입 전용 내보내기)

TypeScript 3.8 이상에서는 번들링 시 실제 JavaScript 코드에 포함되지 않는 **순수 타입 전용 export**를 명시할 수 있다. (컴파일 후 제거되어 번들 크기가 최적화됩니다.)

```typescript
// 1. 개별 타입 export
export type { User, UserRole };

// 2. 일반 값과 타입을 함께 내보낼 때 구분 (TS 4.5+)
export { createUser, type UserConfig };
```

## 4. Re-export (다시 내보내기)

다른 모듈에서 가져온 요소를 현재 파일에서 바로 다시 외부로 내보낼 때 사용한다. 주로 `index.ts` 파일에서 여러 모듈을 하나로 묶어 제공할 때 자주 쓰인다.

```typescript
// ./components/Button.ts 와 ./components/Input.ts 의 모든 항목 내보내기
export * from "./components/Button";
export * from "./components/Input";

// 특정 항목만 선택해서 내보내기
export { default as Header } from "./components/Header";
export type { ButtonProps } from "./components/Button";
```

## 💡 Gemini가 정리해준 한눈에 보는 Import / Export 짝꿍


| **내보내기 방식** | **Export 코드** | **Import 코드** |
|---|---|---|
| **Named Export** | `export const name = "Kim";` | `import { name } from "./file";` |
| **Default Export** | `export default function myFunc() {}` | `import customName from "./file";` |
| **Type-only Export** | `export type { MyType };` | `import type { MyType } from "./file";` |
