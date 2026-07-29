<!-- notion-page-id: 3a02cdd741ac807581f4ee828e11cb02 -->

# Optional

null은 NullPointerException를 만들어내기 때문에 null을 대신하기 위해 만들어진 래퍼 클래스이다.
Optional은 null이나 null이 아닌 값을 담을 수 있는 클래스이다.

메소드


| 메소드 | 설명 |
|---|---|
| isPresent() | 저장된 값이 존재하면 true, 값이 존재하지 않으면 false |
| get() | 저장된 값을 반환 |
| orElse(T other) | 저장된 값이 존재하면 값 반환, 존재하지 않으면 인수로 전달된 값 반환 |
| orElseThrow(Supplier< ? extends X>  exceptionSupplier) | 저장된 값이 존재하면 값 반환, 존재하지 않으면 인수로 전달된 예외 발생 |

JPA의 사용 예제

```java
Delivery delivery = deliveryRepository.findById(id)
        .orElseThrow(() -> DeliveryNotFoundException.EXCEPTION);

```

```java
if (userRepository.findByEmail(email).isPresent()) {
    throw EmailExistsException.EXCEPTION;
}

```
