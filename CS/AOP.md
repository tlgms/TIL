<!-- notion-page-id: 3a22cdd741ac80069067cc7e1f204e30 -->

# AOP

Aspect Oriented Programming의 약자로 관점지향 프로그램이라고 불린다. 찾아보면 "흩어진 Aspect들을 모아서 모듈화 하는 기법이다."라고 나오는데 쉽게 설명하면 같은 기능들을 묶어 놓는 다고 생각하면 된다.

OOP는 비지니스 로직의 모듈화라고 생각하면, AOP는 부가 기능들의 모듈화이다. -> 모듈화는 결국 공통된 기능을 모듈화 함으로써 재사용성이 좋다.

```java
부가 기능이라고 해서 일반적인 로직에서 중복되는 코드인가 생각했는데 아니었다...!
예를 들어서 로그처리, 보안처리, DB트랜잭션 처리 등이 있다고 한다. 
그니까 비지니스 로직 처리 전이나 후에 처리하는 부가적인 기능들을 모듈화 한 것이라고 생각하면 된다.
```

OOP에서는 모듈화를 하기 위해 상속을 사용했다. 하지만 부가기능들을 상속으로 처리하기에 깔끔하지 않다. 이러한 문제를 해결하기 위해 AOP가 등장했다.

**AOP 용어**

- 타겟(Target) : 부가기능을 부여할 대상, Aspect를 적용하는 곳

- 어드바이스(Advice) : 실질적으로 부가기능을 담는 구현체로, 타겟 오브젝트에 종속되지 않는다.

- 조인포인트(JoinPoint) : Spring에서는 메소드의 조인포인트만을 제공하기 때문에 Spring 프레임워크 내에서의 조인포인트는 메소드라고 볼 수 있다. Advice가 적용될 위치, 끼어들 수 있는 지점

- 포인트컷(PointCut) : 어드바이스를 적용할 조인포인트를 선별하는 기능을 정의한 모듈을 말함.

- 애스펙트(Aspect) : 부가기능 모듈을 말한다. 애스펙트는 부가될 기능을 정의한 어드바이스와 어드바이스를 어디에 적용할지 결정하는 포인트컷을 함께 가지고 있다. (여기서 애스팩트에 대해 알았다면 다시 위의 문장으로 돌아가 AOP에 대해서 이해하자!)

- 프록시(Proxy) : 타겟을 감싸서 타겟의 요청을 대신 받아주는 랩핑 오브젝트이다. -> 한마디로 타겟이 실행되면 타겟이 바로 실행되는 게 아니라 프록시를 거쳐간다. 라고 생각하면 될 것 같다.

- 인트로덕션(Introduction) : 타겟 클래스 코드의 변경 없이 신규 메소드나 멤버변수를 추가하는 기능

- 위빙(Weaving) : 지정된 객체에 애스팩트를 적용하여 새로운 프록시 객체를 생성하는 과정

**어노테이션**

@Aspect : Aspect역할을 할 클래스에 선언

@Pointcut : 적용할 지점또는 범위 선택

@Around : 실제 부가 기능 구현

```java
@Aspect 
@Component 
public class LogAspect { 
    
    private final Logger logger = LoggerFactory.getLogger(this.getClass()); 
    
    @Pointcut("execution(public * com.example.demo.service..*(..))") // 적용 범위 지정
    private void publicTarget() { } 
    
    @Around("publicTarget()") 
    public Object calcPerformanceAdvice(ProceedingJoinPoint pjp) throws Throwable { 
        logger.info("성능 측정을 시작합니다."); 
        StopWatch sw = new StopWatch(); 
        sw.start(); 
        
        Object result = pjp.proceed(); 
        
        sw.stop(); 
        logger.info("성능 측정이 끝났습니다."); 
        logger.info("걸린시간: {} ms", sw.getLastTaskTimeMillis()); 
        return result;
    }
}
```

출처 : 자세한 AOP 코드를 보고 싶다면 [SpringBoot AOP코드](https://memostack.tistory.com/238)를 클릭하면 내가 참고했던 글이 나옵니다

다른 글들을 보다가 아래와 같이 @Pointcut을 사용하지 않고 @Around에 범위를 지정해주는 것을 봄

```java
@Aspect 
@Component 
public class LogAspect { 
    
    private final Logger logger = LoggerFactory.getLogger(this.getClass()); 
    
    @Around("execution(public * com.example.demo.service..*(..))") 
    public Object calcPerformanceAdvice(ProceedingJoinPoint pjp) throws Throwable { 
        logger.info("성능 측정을 시작합니다."); 
        StopWatch sw = new StopWatch(); 
        sw.start(); 
        
        Object result = pjp.proceed(); 
        
        sw.stop(); 
        logger.info("성능 측정이 끝났습니다."); 
        logger.info("걸린시간: {} ms", sw.getLastTaskTimeMillis()); 
        return result;
    }
}
```

AOP에 대해 더 읽으면 좋을 [AOP](https://devlog-wjdrbs96.tistory.com/398) 글은 클릭하면 나옵니다.
