<!-- notion-page-id: 3ba2cdd741ac80439fd6d740650552fe -->

# 리터럴 타입 (Literal Types)

특정 타입 전체가 아니라 정확히 지정한 값만 허용하도록 범위를 좁힌다.

```typescript
type Direction = "left" | "right" | "up" | "down";

let move: Direction;
move = "left";  // OK
// move = "우빵"; // 에러 발생
```
