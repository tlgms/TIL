<!-- notion-page-id: 3a02cdd741ac808cbb4ddf47ae8651dd -->

# Stream

[https://futurecreator.github.io/2018/08/26/java-8-streams/](https://futurecreator.github.io/2018/08/26/java-8-streams/)

- Filtering
  필터는 스트림 내의 요소들을 하나씩 평가해서 걸러내는 작업이다.
```java
Stream<T> filter(Fredicate<? super T> predicate);
------------------------------------------------------------------
Stream<String> stream = 
    names.stream()
    	.filter(name -> name.contains("a"));
```
  스트림의 각 요소에 대해서 평가식을 실행, 'a'가 들어간 스트림 리턴

- Mapping
  맵은 스트림 내의 요소들을 하나씩 특정값으로 반환해줍니다.
```java
<R>Stream<R> map(Function<? super T, ? extends R> mapper);
------------------------------------------------------------------
Stream<String> stream = 
    names.stream()
    	.map(String::toUppercase);
```
  스트림 내의 String의 toUppercase메소드 실행해서 대문자로 변환한 값이 담긴 스트림 리턴

- for each
  stream에서 제공하는 forEach문은 java의 forEach문을 람다식으로 간단하게 할 수 있도록 도와줍니다.
```java
Stream<String> stream = 
    names.stream()
    	.forEach(System.out::println);
```
  간단하고 편리하지만, 무분별하게 사용하게 된다면 효율적이지 않을 수 있다.
```java
// forEach문 사용시
IntStream.range(1, 100).forEach(i -> {
    if (i > 50) {
      return;
      //각 수행에 대해 다음 수행을 막을 뿐, 100번 모두 조건을 확인한 후에야 종료한다.
    }
    System.out.println(i);
});

// 중간 연산에 filter 사용하고 마지막 연산에서 forEach문 사용
IntStream.range(1, 100)
        .filter(i -> i <= 50)
        .forEach(System.out::println);
```
  위의 코드에서 볼 수 있듯이 중간 연산자 filter, map, sort를 사용하여 충분히 구현할 수 있다.

### Stream.toList와 Stream.collect(toList())의 차이

> Stream.toList 메소드는 JDK16에서 생긴 메소드이다. ([참조](https://bugs.openjdk.org/browse/JDK-8180352))
  java17부터는 `Stream.toLis` 을 권장한다고 한다.

둘의 차이점은 반환되는 값의 타입이 다르다는 것이다. `Stream.collect(toList())` 에서는 List를 반환하고, 
`Stream.toList` 는 Collectors.UnmodifiableList또는 Collectors.UnmodifiableRandomAccessList
를 반환한다. `Stream.toList` 은 수정이 불가능한 List를 반환한다.

수정되지 않는 List를 반환하는 `collect(Collectors.toUnmodifiableList())` 가 있지만, `collect(Collectors.toUnmodifiableList())` 은 Null을 허용하지 않기 때문에 NPE가 일어날 가능성이 크다.

>  `Stream.toList` 와 `Stream.collect(toList())` 에서는 Null을 허용한다.
