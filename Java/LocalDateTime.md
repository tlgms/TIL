<!-- notion-page-id: 3a02cdd741ac8013b287ed312036ec11 -->

# LocalDateTime

## java.util.Date 

이 클래스는 Util패키지 안에 있는 클래스이며, 날짜 및 시각 정보를 관리하는 클래스이다.

- 생성자
  - Date()에 들어가는 매개변수 값에 따라 다른 내용을 담는다
    - Date(int year, int month, int date, int hrs, int min, int sec) // 년, 월, 일, 시, 분, 초
      매개변수에 들어간 형식대로 담는다.

- 주요 메소드

**문제점**

- 불변 객체가 아니다

- set메소드를 제공하기 때문에 불변객체가 아니기에 여러곳에서 공유되었을때 원치 않은 결과 값을 얻게 되는 문제점이 발생한다.

- 오류에 둔감한 timezone id 지정
```java
TimeZone timeZone = TimeZone.getTimeZone("Seoul/Asia");
testZone.getID(); // GMT
```
  - TimeZone ID에 Seoul/Asia는 존재하지 않지만 오류는 발생하지 않는다.

- java.util.Date의 하위 클래스 문제
  - 하위 클래스 timestamp는 equals() 대칭성을 어겼다. Date 타입과 TimeStamp 타입을 섞어 쓰면 a.equals(b)가 true라도 b.equals(a)는 false인 경우가 생길 수 있다.

> 이러한 문제점을 개선하고자 java.time 패키지가 나오게 되었다. java8이상의 프로젝트에서는 가급적 time패키지 사용을 권장한다. 한국에서 사용한다면 LocalDateTime 으로 처리해도 되지만, 글로벌 서비스라면 timezone이 추가된 ZonedDateTime 사용을 고려해야한다.
  `java.util.Date(1.0) -> java.util.Calendar(1.1) -> java.time.* (1.8)`

# [java.time.*](https://www.joda.org/joda-time/)

1. **LocalDate 클래스**
```java
LocalDate nowDate = LocalDate.now(); // 현재 날짜를 저장
LocalDate Date = LocalDate.of(2022, 1, 30); // 인자 값의 날짜를 저장
```
  메소드
  현재 달의 첫번째, 마지막 날짜 구하기
```java
LocalDate.now().with(TemporalAdjusters.firstDayOfMonth());
LocalDate.now().with(TemporalAdjusters.lastDayOfMonth());
```

1. **LocalTime 클래스**
```java
LocalTime nowTime = LocalTime.now(); // 현재 시간을 저장
LocalTime Time = LocalTime.of(22, 1, 30); // 인자 값의 시간을 저장
LocalDate curDate = LocalDate.now();
LocalTime curTime = LocalTime.now();
LocalDateTime targetDateTime = LocalDateTime.of(curDate, curTime);
```
  메소드

1. **LocalDateTime 클래스**
```java
LocalDateTime curDateTime = LocalDateTime.now(); // 현재 날짜와 시간을 저장

LocalDate curDate = LocalDate.now();
LocalTime curTime = LocalTime.now();
LocalDateTime targetDateTime = LocalDateTime.of(curDate, curTime); // 시간 + 날짜
```
  날짜와 시간을 모두 표현 하고 싶으면 LocalDateTime 사용하면 된다.

---

날짜와 시간 비교
  LocalDate와 LocalTime 클래스에 객체를 비교할 수 있는 compareTo() 메소드가 오버라이딩되어 있다.
  - isEqual() : equals()메소드와 달리 오직 날짜만 비교(LocalDate 클래스에서만 제공)
  - isBefore() : 두 날짜의 날짜와 시간을 비교하여 현재보다 앞선 시간인지 비교
  - isAfter() : 두 날짜의 날짜와 시간을 비교하여 현재보다 늦은 시간인지 비교
