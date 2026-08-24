<!-- notion-page-id: 3c62cdd741ac8028b9bdcf0636895e13 -->

# 봉인된 인터페이스(Sealed Interface)

인터페이스를 구현(상속)할 수 있는 클래스나 레코드를 제한합니다.

---

`sealed` 키워드와 `permits` 키워드로 허용할 클래스를 명시합니다.


```java
// 허용할 구현체를 permits로 지정
public sealed interface Result permits Success, Failure {}

public final class Success implements Result {
    private final String data;
    public Success(String data) { this.data = data; }
}

public final class Failure implements Result {
    private final Throwable error;
    public Failure(Throwable error) { this.error = error; }
}

// switch 패턴 매칭 시 default가 필요 없음
String message = switch (result) {
    case Success s -> "성공: " + s.getData();
    case Failure f -> "실패: " + f.getError().getMessage();
};
```
