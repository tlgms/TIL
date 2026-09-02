<!-- notion-page-id: 3cf2cdd741ac80e0af23c467d81ad62f -->

# PER(Probabilistic Early Recomputation)

캐시 스탬피드 현상을 해결하기 위한 방법 중 하나이다.

- 캐시 유효 기간이 만료되기 전 일정 확률로 캐시를 재연산

- 만료 직전에 일부 요청만 갱신을 걸고, 나머지는 기존 캐시를 사용

```java
currentTime - ( timeToCompute * beta * log(rand()) ) > expiry
```

- **`currentTime`** : 현재 남아있는 캐시 만료 시간

- **`timeToCompute`** : 캐시된 값을 다시 계산하는 데 걸리는 시간

- **`beta`** : 기본적으로 1.0보다 큰 값으로 설정 가능

- **`rand()`** : 0 ~ 1 사이의 랜덤 값을 반환하는 함수

- **`expiry`** : 키를 재설정할 때 새로 적용할 만료 시간

`timeToCompute * beta * log(rand())` 는 무작위 값을 생성, 이 값을 현재 시간에서 빼서 expire와 비교

- 값 < expire → 캐시 갱신 필요(true)

- 값 > expire → 갱신 필요 없음(false)

캐시가 완전히 만료되기 전이라도 일정 확률로 일부 요청이 캐시를 미리 재계산하게 되고, 나머지 요청들은 여전히 기존 캐시를 활용한다.

한 번에 TTL이 만료되어 재연산 요청이 몰리는 경우는 엄청난 대형 서비스 아니면 생길 일이 없기 떄문에 존재만 알아두자…
