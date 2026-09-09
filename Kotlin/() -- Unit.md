<!-- notion-page-id: 3d62cdd741ac801884b4e5ce9c7242fa -->

# () -> Unit

`() -> Unit`이 제네릭 타입 인자로 들어간 것이다.

Kotlin에서 함수는 값의 타입을 `(파라미터타입) -> 반환타입` 형태로 씁니다.

```kotlin
val a: () -> Unit                    // 인자 없음, 반환 없음
val b: (Int) -> String               // Int 받아서 String 반환
val c: (Int, Int) -> Int             // Int 둘 받아서 Int 반환
```
