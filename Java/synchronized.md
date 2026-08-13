<!-- notion-page-id: 3bb2cdd741ac80518b38d692986e1894 -->

# synchronized

자바에서 지원하느 Synchronized 키워드는 여러개의 스레드가 한개의 자원을 사용하고자 할 때, 현재 데이터를 사용하고 있는 해당 스레드를 제외하고 나머지 스레드들은 데이터에 접근 할 수 없도록 막는 개념이다.

`synchronized`는 크게 메서드 단위와 블록 단위 두 가지 방식으로 사용할 수 있다.

```java
// 1. 메서드에서 사용하는 경우
public synchronized void method(){ // 코드 }

 

// 2. 객체 변수에 사용하는 경우(block문)
private Object obj = new Object();

public void exampleMethod(){
		synchronized(obj){ //코드 }
}
```

- 메서드에 선언하기
  - 메서드 전체를 임계 영역으로 지정한다.
    - 인스턴스 메서드: 해당 객체(`this`)의 락을 사용한다.
    - 정적(static) 메서드: 해당 클래스의 `Class` 객체 락을 사용한다.

- 메서드 전체가 아닌, 필요한 특정 코드 영역만 선택하여 동기화한다. 성능 효율성이 좋아 실무에서 더 선호된다.
