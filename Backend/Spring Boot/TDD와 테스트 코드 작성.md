<!-- notion-page-id: 39f2cdd7-41ac-80b7-8082-d94cf0e8f787 -->
# TDD와 테스트 코드 작성

> 미리 알아야할 지식들을 아래에 정리 해두었다. (아직 정리 안함)
> [assertion과 **Mock객체**](https://app.notion.com/p/39f2cdd741ac80069289ec668f1c9e0b)

> 🐤 테스트코드 많이 들어보긴 했지만, 나는 시간이 없다는 핑계를 대며 작성하지 않았다…! 사실 코드를 짤때 테스트 코드는 뒷전으로 두고 공부를 하지 않았다💦 이제는 더이상 미룰 수 없다! 테스트 코드를 작성해보고자 한다.

TDD 어디서 많이 들어봤다 했더니…! 스프링부트 책에서 정리한 적이 있는 부분이었다! 여기서는 TDD와 단위테스트는 다른것이라고 말하고 있었다! 맞는 말이다. TDD는 개발 방식중 하나이니까!

# 들어는 봤지만 제대로 모르는 지식! TDD

TDD는 Test-Driven-Development의 약자로 **테스트 주도 개발**을 뜻한다.

원래는 코드를 개발 한 후 테스트 코드를 작성했다면, TDD는 **테스크 코드를 먼저 작성한 후** 코드 개발을 진행한다.

애자일 방법론 중 하나인 eXtream Programming(XP)의 Test-First 개념에 기반을 둔 방식이라고 한다.

TDD는 불확실성이 높은 프로젝트 시 피드백과 협력을 통해 좋은 결과를 낼 수 있다. 하지만 개발속도가 느려진다. 기존보다 2배의 코드를 짜야하고, 계속적으로 코드를 고쳐나가기 때문에 일반적인 개발 방식보다는 길어질 수 있다.

정리하면 정리할수록 TDD의 장점을 잘 **이해하지 못했었다..** 그 이유는 테스트코드를 제대로 사용하지 않았기 때문이라고 생각된다. 일단 나는 개발 코드에 맞춰서 **테스트 코드를 고쳤다.** 근데 사실 고치는 건 테스트 코드가 아니라… 개발 코드여야 했다. 테스트 코드를 처음 작성해보는 나에게는 당연히 테스트 코드가 잘못되었다는 인식이 있었기 때문에 발생한 일이었다.

테스트 코드가 정확히 작성되어있다면 테스트 코드를 작성 후에 개발코드를 작성하고 개발 코드를 수정할 수 있을 것이다.

## TDD의 장점과 단점

이렇게 모아보면 장점이 더 많은 것 같지만… 다 안쓰는데에는 이유가 있는 법이라고 배웠슴다…

<details>
<summary><strong>장점</strong></summary>

- **빠르게 피드백**을 받을 수 있다.
  - 개발을 모두 마친후 테스트 코드를 작성하기 때문에 모두 완성하기 전까지는 피드백을 받기 힘들다. 또한 **정확한 피드백**을 받을 수 있다.
- 불안정성을 개선해준다.
  - 미리 내 코드를 진단 할 수 있기 때문에 코드에 대한 불안정성을 개선해준다.
- 재설계 시간을 단축해준다.
  - 테스트 코드를 작성하면서 미리 예외와 시나리오를 구상하기 때문에 원래는 코드를 짜면서 생각해야하는 것들을 **테스트 코드를 짜면서 미리 생각**할 수 있게 된다.
- 추가 구현이 용이하다.
  - 테스트 코드를 통하여 **추가 구현을 했을 때 미치는 영향**을 미리 확인 할 수 있다.

</details>

<details>
<summary><strong>단점</strong></summary>

- 생산성이 저하된다.
  - 처음부터 2개의 코드를 짜고 중간중간 코드를 고치기까지 해야하기 때문에 **개발 시간이 늘어난다.**
- 개발 방식을 바꾸기 어렵다.
  - 기존에 하던 개발 방식을 바꾸기란… 참 어려운 것이여…

</details>

# 테스트 코드 머가 중요하길래~!

나는 코드를 다 작성 한 후 **포스트맨을 통해 수동으로** 테스트를 해주었다. 사실 하나의 에러가 나올때마다 정말 귀찮은 작업이었다. 데이터베이스를 설정해야했으며, 어떤 프로젝트에서는 api가 대략 30개 정도가 있었는데 그걸 **모두 테스트하고 코드 고칠때마다 테스트**를 돌리니까 미치기 직전이었다.

그래서 우리에게는 **테스트 코드**가 있는 것이다….! 우리가 수동으로 테스트를 하지 않아도 내가 작성한 코드가 내 뜻대로 작동하고 있는 지 확인 할 수 있기 때문이다. 그리고 한번 작성해놓으면, **코드를 고치더라도 작성 해놓은 테스트 코드를 돌려주면** 되기 때문에 더욱 편하게 작업할 수 있다.

테스트 코드의 종류를 검색해보니까 많이 나오지만 여기서는 단위 테스트와 통합 테스트에 대해 알아볼까 한다.

## 단위 테스트

**가장 작은 단위로 테스트를 진행**한다고 생각하면된다. 편하게 생각하면 메서드 단위로 테스트를 한다고 보면 편하다. 작은 단위로 테스트를 하기 때문에 모든 **프로젝트가 완성되지 않아도** 테스트를 할 수 있으며, 미리 오류를 잡아낼 수 있다. 또한 코드에 대한 이해가 더 쉬워진다. 하지만, 프로그램의 **모든 오류를 잡아낼 수 없다**는 한계를 가지고 있다.

<details>
<summary>단위 테스트 지원 도구</summary>

1. JUnit : Java 프로그래밍 언어에 사용되는 테스트 도구. 데이터를 테스트 한 다음 코드에 삽입
2. NUnit : 모든 .net 언어에 널리 사용되는 단위 테스트 프레임 워크. 병렬로 실행할 수 있는 데이터 중심 테스트 지원
3. JMockit : 오픈 소스 단위 테스트 도구. 기록 및 검증 구문으로 API를 Mocking 할 수 있음
4. EMMA : 코드 분석 오픈 소스 툴 킷. JAVA 기반 이므로 외부 라이브러리 종속성이 없으며 소스 코드에 액세스 할 수 있음
5. PHPUnit: PHP 프로그래머를 위한 단위 테스트 도구

</details>

## 통합 테스트

서로 다른 모듈 혹은 클래스간의 상호작용의 유효성을 검사하는 테스트이다. 단위 테스트로 모든 모듈이 잘 작동한다고 하더라도 서로 상호작용시에 생기는 문제점은 발견 할 수 없다. 그렇기 때문에 단위테스트보다 넓은 통합 테스트가 필요하다.

## 테스트 하기 좋은 코드와 어려운 코드

[https://jojoldu.tistory.com/674](https://jojoldu.tistory.com/674)

→ 정리하기 귀찮아서 남겨 놓음.. (나중에 정리하겠지….)

# JAVA에서 JUnit을 통해 테스트 코드를 작성해보자

> 🐤 테스트 코드에 대해 정확하게 아는 것이 아닌 상태로 작성했기 때문에 미흡한 점이 있을 수 있음

JUnit는 전 세계적으로 많이 사용되는 java 단위 테스트 **프레임워크**라고 한다.

→ 자바 뿐만 아니라 다른 언어에서도 단위 테스트 프레임워크가 존재하며, 이름을 **xUnit**로 지칭해서 부른다

```java
testImplementation 'org.springframework.boot:spring-boot-starter-test'
```

👆 여기서 테스트에 관련한 의존성들을 다 불러와 준다!

## 테스트 코드 작성 전 준비 과정

### JUnit의 메소드와 어노테이션을 알아보자

→ [http://junit.sourceforge.net/javadoc/org/junit/Assert.html](http://junit.sourceforge.net/javadoc/org/junit/Assert.html)

| 메소드 | 설명 |
| --- | --- |
| assertEquals(A, B) | 객체 A와 B가 같은 값을 가지는지 확인한다. |
| assertEquals(A, B, C) | 객체 A와 B가 같은 값을 가지는 지 확인한다. C는 오차 범위이다. |
| assertArrayEquals(A, B) | 배열 A와 B가 일치하는 지 확인한다. |
| assertSame(A, B) | 객체 A와 B가 같은 객체인지 확인한다. |
| assertTrue(A) | 조건 A가 참인지 확인한다. |
| assertNull(A) | 객체 A가 Null인지 확인한다. |
| assertNotNull(A) | 객체 A가 Null이 아닌지 확인한다. |

`@Test` 메서드 위에 선언을 해주면 테스트 메소드 라는 것을 명시해준다.
`@Test(timeout=밀리초)` 테스트 코드의 수행 시간을 지정해준다. 시간이 넘어가면 테스트는 실패
`@Test(expected=예외)` 지정해둔 예외가 발생해야 테스트가 성공한다

`@Ignore` 해당 어노테이션이 선언된 테스트 메소드는 실행하지 않도록 지정한다.

`@BeforeEach` @Test 메서드가 실행되기 전에 실행되는 메소드를 지정한다.

- @Test 메서드에서 공동으로 하는 작업에 붙여주면 용이하다

`@AfterEach` @Test 메서드가 실행이 끝난 후에 실행되는 메소드를 지정한다.

`@BeforeAll` 현재 클래스의 모든 테스트가 실행되기 전에 실행되는 메소드를 지정한다.
`@AfterAll` 현제 클래스의 모든 테스트가 실행된 후에 실행될 메소드를 지정한다.

@BeforeEach 와 @BeforeAll의 차이

`@BeforeEach`은 @Test 어노테이션이 있는 메소드 하나가 시작되기 전마다 실행되는 메소드를 지정하는 반면, `@BeforeAll` 은 `@BeforeAll` 어노테이션이 있는 클래스의 모든 테스트가 실행되기 전에 실행될 메소드를 지정한다. 예를 들어 하나의 테스트 클래스를 실행한다고 했을때, `@BeforeEach`가 붙어있는 메소드는 하나의 메소드가 실행될 때마다 실행되지만 `@BeforeAll`가 붙어있는 메소드는 딱 한번 실행된다.

`@ExtendWith` 사용자 저의 확장자명을 지정하는 데 사용된다라는 식으로 적혀있는데, 확장 기능을 구현할 수 있도록 해주는 어노테이션이라고 생각하면 된다.
확장기능은 `org.junit.jupiter.api.extension.Extension` 인터페이스를 상속한 인터페이스로 되어 있으면 JUnit5에서 제공하는 기능 상당수가 여기에 있다고 한다.

`@DisplayName` 테스트 클래스 또는 테스트 메소드의 사용자 정의 이름을 표시 (어떤 테스트인지 개발자가 명시)

`@Nested` 공통적인 기능이 있는 메소드를 중첩클래스로 묶을 때 `@Nested`어노테이션을 붙여서 `@Nested` 클래스를 둘러싸고 있는 클래스의 인스턴스와 설정및 상태를 공부할 수 있는 중첩된 비정적 테스트 클래스가 만들어진다고 한다. (같은 기능들끼리 메소드를 묶고 싶을 때 사용해라)

→ [https://junit.org/junit5/docs/current/user-guide/#writing-tests-nested](https://junit.org/junit5/docs/current/user-guide/#writing-tests-nested)

`@Disable` 테스트 클래스나 메소드를 비활성화 시킨다.

`@TestMethodOrder(OrderAnnotation.class)` 테스트 코드의 순서를 지정해준다.
`@Order(순서)` 어노테이션을 메서드 위에 붙여주면 지정해둔 순서대로 테스트코드가 실행된다.

`@RepeatedTest(반복 횟수)` 반복 테스트 시 반복할 횟수를 적어주면 그만큼 반복되어 돌아간다

### AssertJ와 AssertJ의 메서드를 알아보자

[assertion](https://app.notion.com/p/39f2cdd741ac80069289ec668f1c9e0b)을 제공하는 java 라이브러리이다.
AssertJ를 사용하면 코드가 직관적이다 → 테스트코드의 **가독성을 높여준다.**

```java
import static org.assertj.core.api.Assertions.*;
```

테스트 코드의 시작은 **asssertThat()**으로 시작해서 메서드를 추가해서 사용한다.

```java
asssertThat(테스트 타겟).메서드1().메서드2().메서드3();
```

내가 공부한 글에서 JUnit의 assertEquals(expected, actual)와 AssertJ의 assertThat(actual).isEqaulTo(expected)을 비교한 글인데 확실히 **AssertJ가 더 직관적이었다.**

| 메소드 | 설명 |
| --- | --- |
| isEqualTo(Object o) | equals()로 실제값이 기대값과 같은지 확인 |
| isNotEqualTo(Object o) | equals()로 실제값이 기대값과 다른지 확인 |
| isNotNull() | 실제값이 null이 아닌지 확인 |
| isNull() | 실제값이 null인지 확인 |
| isInstanceOf(Class\<?\> type) | 실제값이 기대값 타입의 인스턴스인지 검증 |
| isNotInstanceOf(Class\<?\> type) | 실제값이 기대값 타입의 인스턴스가 아닌지 검증 |
| isSameAs(Object o) | ==로 실제값이 기대값과 주소값이 같은지 검증 |
| isNotSameAs(Object o) | ==로 실제값이 기대값과 주소값이 다른지 검증 |

더 많은 메서드 → [https://pjh3749.tistory.com/241](https://pjh3749.tistory.com/241)

## 테스트 코드 작성하기

> 테스트 코드를 작성하기 위한 준비 과정이 너무 길었다…
> 이제 아래의 테스트 코드를 보면서 테스트 코드에 대해서 이해 해보자.

```java
@ExtendWith(MockitoExtension.class) // ----------- 1
class UserServiceTest {

	@Mock // --------------------------------------- 2
	UserRepository userRepository;

	@InjectMocks // -------------------------------- 3
	UserService userService;

	@Nested
	@DisplayName("유저 정보 저장")
	class save {
		@Test
		void 유저_엔티티를_통해_체형정보_저장() {
			//given -> 어떤 상황이 주어졌을 때
			long userId = anyLong();
			User user = User.builder()
				.name("김플로")
				.email("hello123@naver.com")
				.phoneNumber("010-1234-5678")
				.build();
			UserRequest request = new UserRequest("김플로", BasicShape.MUSCLE, BodyShape.AVERAGE, BodyShape.AVERAGE, 160, 50, 240, Gender.WOMAN);

			ArgumentCaptor<User> userCaptor = ArgumentCaptor.forClass(User.class); // ------- 4

			when(userRepository.findById(userId)).thenReturn(Optional.of(user)); // --------- 5

			//when -> 검증할 것을 실행했을 때
			userService.saveUser(userId, request);

			//then -> 검증한 결과가 나와야함
			verify(userRepository).save(userCaptor.capture()); 
			assertThat(userCaptor.getValue().getShape()).isNotNull();
		}

		@Test
		void 이미_유저_정보를_등록한_경우_예외_반환() {
			//given
			long userId = anyLong();
			User user = User.builder()
				.name("김플로")
				.email("hello123@naver.com")
				.phoneNumber("010-1234-5678")
				.build();
			Shape shape = Shape.builder()
				.bodyShape(BasicShape.SOFT)
				.upperBody(BodyShape.AVERAGE)
				.lowerBody(BodyShape.AVERAGE)
				.height(160)
				.weight(50)
				.footSize(240)
				.gender(Gender.WOMAN)
				.build();
			user.saveNicknameAndShape("김플로",shape);
			when(userRepository.findById(userId)).thenReturn(Optional.of(user));

			//when
			AbstractThrowableAssert<?, ? extends Throwable> e = assertThatThrownBy(() -> userService.saveUser(userId, new UserRequest()));

			//then
			e.isInstanceOf(ConflictException.class);
		}
	}
```

### 테스트 코드 기본 틀

> 🐤 테스트 코드 메소드의 이름은 **한글**로 작성되며, 작성시 띄어쓰기는 **_**로 구별하고 있다. 메소드의 이름은 영어로 쓰는 것이 규칙이지만, 테스트 코드에서 만큼은 가독성이 높은 한글을 사용하는 것이 좋다.

```java
@Test
void 테스트_코드_이름() {

}
```

### 어노테이션 설명

**@ExtendWith(MockitoExtension.class)**

@ExtendWith 어노테이션은 사용하는 확장자명을 적는데 이용하는 어노테이션이다. 지금 테스트코드에서는 MockitoExtension.class를 불러왔다. Mockito의 [Mock](https://app.notion.com/p/39f2cdd741ac80069289ec668f1c9e0b)**를 사용하기 위해**서 불러온 것이다.

- JUnit4에서는 RunWith(MockitoJUnitRunner.class)를, JUnit5에서는 ExtendWith를 쓰도록 되어있다

**@Mock**

Mock 객체를 생성해준다.

**@InjectMocks**

생성한 Mock 객체를 주입하여 사용할 수 있도록 만든 객체라고 한다….

> @InjectMocks 어노테이션을 찾아봤는데 자료도 별로 없고 설명도 이해할 수 있도록 적히지 않았다

그래서 설명을 좀 해보면 @InjectMocks 어노테이션이 붙은 객체 안에서 @Mock를 사용해야하는 객체를 실제 코드에 적지 않아도 테스트 코드에서 @Mock를 선언하면 @InjectMocks 어노테이션이 붙은 객체 안에서 **@Mock이 붙은 것처럼 작동**하게 되도록 한다고 생각하면 된다.

```java
class TestService {
	private final TestRepository testRepository;

	public void 메소드() {
	}
}
```

여기서 TestRepository는 @Mock을 붙여야하지만 TestService에 @InjectMocks을 붙이면 TestRepository는 @Mock 어노테이션이 붙은 것처럼 사용할 수 있다.

### 코드 설명

```java
ArgumentCaptor<User> userCaptor = ArgumentCaptor.forClass(User.class);
```

위의 코드는 User타입의 **ArgumentCaptor 객체를 만들어주는** 코드인데, **ArgumentCaptor**가 뭘까??

```java
verify(userRepository).save(userCaptor.capture()); 
```

ArgumentCaptor을 알기 위해서는 위의 코드도 같이 보면 편하다. verify를 사용할때 보통은 아큐먼트(인자) 값을 지정하지만, **ArgumentCaptor을 사용하면 capture를 통해 아큐먼트값을 넘길 수 있다.**

위에서는 userRepository를 save했을 때의 값이 userCaptor로 들어가도록 되어 있다.

```java
assertThat(userCaptor.getValue().getShape()).isNotNull();
```

그래서 verify 코드 아래의 코드에서 userCaptor값을 통해 null인지 검사하고 있는 것이다.

그렇다면 verify가 뭘까? verify는 영어를 해석하면 확인하다이다. 영어뜻 그래로 **mock 객체의 메소드가 특정 조건으로 잘 실행되었는지 검증**할 수 있다.

| 메소드 | 설명 |
| --- | --- |
| atLeastOnece() | 적어도 한번 수행되었는지 검증 |
| atLeast(int n) | 적어도 n번 수행되었는지 검증 |
| times(int n) | 무조건 n번 수행되었는지 검증 |
| atMost(int n) | 최대한 n번 수행했는지 검증 |
| never() | 수행되지 않았는 지 검증 (수행되었으면 오류로 간주) |

검증할 수 있는 메소드는 아래와 같이 있고, 메소드의 예제는 아래 있으니 참고!

```java
verify(T mock, 메소드()).method()
```

verify안에 있는 메소드는 mock를 검증하기 위한 제공되는 메소드이지만 verify().메소드()에서의 메소드는 검증할 mock 객체의 메소드이다. 내가 검증할 mock 객체의 메소드가 실행되어

```java
when(userRepository.findById(userId)).thenReturn(Optional.of(user));
```

위의 코드를 설명하기 위해서는 when()메서드를 알아야 한다. when()메서드는 테스트 기능중 일부가 완성되지 않았을 때나 다른 시스템과 통신이 필요한 경우 **미리 리턴값을 선언하여 사용**할 수 있도록 해준다.

대부분 **데이터베이스와 통신을 해야하는 repository**에 사용한다.

| **.thenReturn()** | **.doReturn()** |
| --- | --- |
| 메소드를 실제로 실행하고, 리턴값을 지정한다. | 메소드를 실제로 실행하지 않고, 리턴값을 지정한다. |
| 메소드의 작업이 오래 걸릴경우 끝날때까지 대기해야한다. | 메소드가 실행되지 않아 .thenReturn()보다 빠르다 |
| 실제 메소드를 호출하기 때문에 해당 메소드의 문제가 있을 경우 발견할 수 있다. | 실제 메소드를 호출하지 않기 때문에 해당 메소드의 문제점을 파악 할 수 없다. |
