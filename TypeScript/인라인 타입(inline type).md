<!-- notion-page-id: 3d02cdd741ac80fc8772c38f4c56814a -->

# 인라인 타입(inline type) 

인라인 타입(inline type) 또는 익명 객체 타입(anonymous object type)은 속성의 타입을 그 자리에서 지정한 것이다.

반대로 `interface`나 `type` 별칭으로 이름을 붙여 쓰는 건 **named type** 또는 **type alias**라고 합니다.

```typescript
interface ApiResponse {

  // object type literal (인라인)
  error?: { message: string };
}
```

`error?: string`과 별 차이 없어 보이지만 값이 message 키를 가진 객체이다.
