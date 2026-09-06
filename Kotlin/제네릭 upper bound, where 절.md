<!-- notion-page-id: 3d32cdd741ac8011bd92d103fbf12dbd -->

# 제네릭 upper bound, where 절

## 상한(upper bound)

제네릭 타입 파라미터 `T`는 아무 제약이 없으면 무엇이든 될 수 있는 타입이기 때문에 컴파일러가 아는 게 거의 없디.

```kotlin
fun <T> sum(a: T, b: T): T = a + b // 컴파일 에러: String일 수도 있음
```

상한을 걸면 컴파일러가 적어도 이 타입이다라고 알게 되어 그 타입의 멤버를 쓸 수 있다

```kotlin
fun <T : Number> average(values: List<T>): Double =
    values.sumOf { it.toDouble() } / values.size
```

여기서 `T : Number`는 상속이 아니라 제약이다. `T` 자리에 들어올 수 있는 타입을 `Number`와 그 하위 타입으로 좁히는 것이다.

---

## null 막기

명시하지 않으면 `Any?`이다. 즉 nullable 타입도 통과하기 때문에 null을 막고 싶으면 `Any`를 상한으로 걸어야 한다.

```kotlin
fun <T : Any> requireItem(item: T): T = item

requireItem(null)  // 컴파일 에러
```

---

## `where` 절

문법적 제약입니다. 두 개 이상 걸려면 `where` 절로 빼야 한다.

```kotlin
fun <T> appendBang(item: T)
    where T : CharSequence,
          T : Appendable {
    if (item.isNotEmpty()) item.append("!")
}
```

## `where` 여러 타입

제약 대상이 `T` 하나가 아니라면 이렇게 사용 가능하다.

```kotlin
fun <K, V> mergeSorted(map: Map<K, V>): List<V>
    where K : Comparable<K>,
          V : Any =
    map.entries.sortedBy { it.key }.map { it.value }
```
