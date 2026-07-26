<!-- notion-page-id: 3a92cdd741ac8086b8a2d4723a950cb3 -->

# 문자열 상수 풀 (String Constant Pool)

일반적으로 자바를 배울 때 자주 접하는 상수 풀은 문자열 상수 풀(String Constant Pool)인 경우가 많다.

- **위치:** **힙(Heap) 영역**에 존재합니다.

- **목적:** 자바에서 문자열(`String`)은 사용 빈도가 매우 높기 때문에, 메모리를 절약하기 위해 동일한 문자열 리터럴은 단 하나만 생성하고 공유(재사용)하도록 설계된 공간입니다.

```java
String s1 = "Java"; // 문자열 상수 풀에 "Java" 생성 및 참조
String s2 = "Java"; // 이미 풀에 있는 "Java"를 재사용 (s1 == s2는 true)
String s3 = new String("Java"); // 힙 영역에 새로운 객체 생성 (s1 == s3는 false)
```
