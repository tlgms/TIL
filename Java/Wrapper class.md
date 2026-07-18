<!-- notion-page-id: 3a02cdd741ac80ce910ce22d0f815d3a -->

# Wrapper class

**래퍼 클래스(Wrapper class)**
| 기본타입 | 래퍼클래스 |
|---|---|
| long | Long |
| int | Integer |
| float | Float |
| char | Character |
| double | Double |

기본타입의 데이터를 객체로 변환해 주는 클래스로 java.lang 패키지에 포함되어 제공된다.

**래퍼클래스와 기본타입의 차이점**

### 박싱(Boxing)과 언박싱(UnBoxing)

박싱 : 기본타입 =>래퍼클래스                언박싱 : 래퍼클래스  =>기본타입

```java
Integer num = new Integer(17); // 박싱
int n = num.intValue();        // 언박싱

Character ch = 'X'; //오토박싱
// Character ch = new Character('X'); 
char c = ch; //오토언박싱
// char c = ch.charValue();
```

둘의 가장 큰 다른점은 객체냐 아니냐 인것 같다. int를 객체로 사용해야 할 때 Integer로 사용함!!
