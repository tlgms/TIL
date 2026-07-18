<!-- notion-page-id: 3a02cdd741ac800b8b37c33cbe0a421a -->

# JPA의 작동원리

[https://stylishc.tistory.com/150?category=846114](https://stylishc.tistory.com/150?category=846114)

[https://ttl-blog.tistory.com/183](https://ttl-blog.tistory.com/183)

### **트랜잭션 범위의 영속성 컨텍스트**

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/691f90fd-6dc5-4eaa-8c76-f263b46c80de/520ada2a-9a69-4595-8b63-b83345620114/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NXY7EVY%2F20260717%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260717T160429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBTC%2FZE7sW9HsR258ElxSRuLrkNlXdZucGOeADhlepeTAiAzCNfrmqZD43fyAnzi9EL0S%2FXSljBL9KQnFfEmOH%2FpWCr%2FAwhhEAAaDDYzNzQyMzE4MzgwNSIMD%2BlKqWfBto7ljgC2KtwDDvL%2F8%2BcNnQoXlRBeirdi9%2FtH7xx9U4X0VhgXbHk6mlQP0TlbdoTGjs6%2BRI2D8wGEgrECLPIWFBI0gmgCu19odUxRHZLrNJUt9fuw7dUEC%2BQCK6xK0XbvZPd56Vuwa670uMiwFtg%2FJ1HyEYpsqta8L36NYXnO0gIxOHL6ESo49f%2Faq39uZbgDXsA4rygLrjjLj6BZu%2FIUbiKK0Ry65j%2B2VfZrgLzMrxALVJk4c7Dw3RvdR8yeBu4ZHiHQN1M7%2BHr7yMlxCZMHzpxOoycFgI42CaaY%2Bd7E4eUYvjI48%2Bv%2FMMsOmQG%2BHFcH1V6GH0lwvPCaAecVt5OPNjtCzNKgSUK2lXA7qF%2BiHorxDLfO8NsMgLtUNsPGLu2VGO5k8d4xpiObivip7RIGUX9667Gj8J5iGwvjxw4Dwp5sljd2AcLz4tc%2FyARRNpYFDY4l3d8X9qcjHCBpilvSTYKudNTHIH2EnvXO5aikypHQXUzdbon97Dl1l0DRg8jB6znKX9c006Pa3b%2FxsLAhOFSN4J4CTW55yCKf%2Fn3ogMvcXR0KC6qkjIioaAH1Hr4CPdciXZpgZOd8PUWF%2FVWAX2SdaCJxpP20UDnx6vIbGndTLqp7B%2B22bfMh90hueDcx7rIV1j8w3JTp0gY6pgGOiLN6oVYJ7PC4kC7NSPPhs3UPyLseMj0a63dCepiHxCAbjlCYmgBQMy21KHkaebfSuZi3kM7NROAVIMwo9XyW%2FwMZX6WFBm1Z3KniEyJoz8YZPyaIIwM3zfHpcF0NZJ9XuEath%2FsFFid0ONqcG9kphkv2ry04hs5Aj1Gok6swBsuqsuvlSb4eYy9hyUZirHqu0l%2B7x2pmHzWEy4%2FR5k0la9dwQGz4&X-Amz-Signature=18325a107b414a7a1e8f3cfc0d38f73779a8da2c34f8c6304bad4d095c9ee6b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

스프링에서 JPA를 사용하면 스프링 컨테이너가 제공하는 전략을 따라야 한다. 스프링 컨테이너는 트랜잭션 범위의 영속성 컨텍스트를 기본 전략으로 사용한다.

트랜잭션 범위의 영속성 컨텍스트는 말 그대로 트랜잭션과 영속성 컨텍스트의 생존 범위가 같다는 것을 말한다.

스프링 어플리케이션에서는 @Transactional을 사용하여 트랜잭션을 시작하게 되는데, 이때  스프링 트랜젝션 AOP가 먼저 작동하게 된다. 먼저 대상 메소드 호출 직전에 트랜잭션을 시작하여 호출이 정상적으로 종료되면 트랜잭션을 커밋하고 종료한다. 여기서 트랜젝션 커밋 시 JPA는 영속성 컨텍스트를 플러시하여 변경 내용을 DB에 반영한 후 DB 트랜잭션을 커밋한다.
(예외가 발생하면 트랜잭션을 종료하고 롤백을 한다. 이때 영속성 컨텍스트를 플러시 하지 않는다.)

- 트랜잭션이 같으면 같은 영속성 컨텍스트를 사용한다.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/691f90fd-6dc5-4eaa-8c76-f263b46c80de/d76d7bdf-213b-4fe8-84a7-3b7469c02693/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLY3256C%2F20260717%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260717T160430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRrkVwHfgoeiK3d3P%2F2v8fg%2BHW%2FwRSVO2E7L1FvQNr9gIhALCtgL9xQNaHfE8AASkFGNjkPVh46wtMKE8Qk9Td1i%2FQKv8DCGEQABoMNjM3NDIzMTgzODA1IgyD54oNvWlT115laSEq3APrE3%2BpOKC8M2UOCsTBcAuT0%2FvDgZuZvGdOzg5qK8VMJrq5oDiIJAQrdQ%2Fpj6K4S8Fgjw4uogFA2og7yR2Axu0gfhXosrei7iS7oL21R1aeNzGo%2Bk0DYILdvPPCYkabsmfVaLd6Wv%2BeMtVqUf2TEjWCmGAsPbNmw3BK5EcZPo0gAKnrtgwDOYP5HhS1XOjOr%2BDnIKpJ5i1qiP%2FQLrshVbhtQMUiFjPYzAtzrneP63bUyw5y1R9pvI0ckd1RH%2Fnw1bBLK1zaMMAZ8zvuo0%2BIMKdpsTQ%2B5W3yWsmejFrhvOgLBv8ZM4JSnPd9tMuKpiMC2bvCTTgh5bFyvTqDk9X8rwxfiSUsDNhr6o2XGYXk52G1f7vsQhOAWfdemT3XOpHX4JbrWAybnjdS28s19c%2BT4VyPLCoJ9HDCmDkKww6TYsw4COlJfPd8ksWjqhe19t9PfNKdBAdxV1VPJlUnN1MSLC7xR%2BTwa%2BUODU%2FjmbM%2FBCWUzZJdr3oaU5SNNHHVTDu6brQHrKX4I2tn0e975U6gJkMChVvThVLCkjRXdr8YDVkpDTCQBoAmeglJlDwv4pA7XwxVOfT3vjwX%2BSna%2BdLwFw8fI9tlBi77WCsn3KhwykaH6IrC9PSHPfKuR0IgjDC2k%2BnSBjqkAZs%2Bmu8Sw5hgdzjZj4aEYxGkKumn4pib5SnJasu%2FgQkWblHhC3aZ7N9V8ScIMOluBCOJ0zhpBV6Do1ioCeic26ZafHk2kXARa2to0k%2FOGEWTVdnkvmGk4XeChFWyxZR2enlep1z12bvjWt%2FEGDT9DQ3tBoQF37F%2BVTqMzcF%2Fy4ICruZNCPQP4F765YODX2THzO580AQgqTqqzy511JxpypahxkVK&X-Amz-Signature=1b00d6636b264b9b4e44774f399d3d39a9970d8e19b151b229e40b18b8b1846f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
  트랜잭션 범위의 영속성 컨텍스트 전략은 다양한 위치에서 엔티티 메니저를 주입받아 사용하더라도 동일한 트랜잭션 내에서는 항상 같은 영속성 컨텍스트를 사용하게끔 구현되어있다.
  - 그렇다는 것은 트랜잭션이 다를 경우 다른 영속성 컨택스트를 상용한다는 것이다.
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/691f90fd-6dc5-4eaa-8c76-f263b46c80de/04b05f43-749d-4b28-9e51-630137c12071/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PHBUFHA%2F20260717%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260717T160431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBHBnNJQflSVClDyvgzkB%2FESfFknq3g7hZwn0wUk5pzRAiEAtpBd57zJebH7kJx6koX0CiFgYaGifEZEU1GAJSf9VJUq%2FwMIYRAAGgw2Mzc0MjMxODM4MDUiDHcyLrP3j96gGJ2ZaircA8l02Mtrf74a6vfKCFtfw2ZzvoECm%2Bpr%2F6m2bL38hjGdKxpbkVv12d98lsFBviZoGkfvj5J7VisGAXusaRnh9glhhdawpNQ3qgzkQbWNHX9KDZy4LqfaVnIIYoDvbIIPkMax6e5r15MWw5T5kFD5J%2F7j95qRGlZ7i47OWbg0NmfGr%2B%2FyU%2B%2B7WpP1CQZsgWMSz9qJBjTOyIQi7FhqtN%2B3OlhaSQTc3O%2F9tupIIEZndprREhmbKhNJ%2BDKSRY%2BN%2BfiNGTTiDg25KIGz9DXX2VGcLqgqbcB5hqQv6gaeAIXPaOSyB2S1jyCpCV4J%2F%2FCLxoJyl%2BzSlSEHKiVqdQiKbkwEz6OcMKKMC1vRKmdv4WwXny8ZIXrBFrMoEHCo8H2DV2WBuMBcZh%2BCNPt55vzTNxs7OvHpaIa67K3TWG9r086syJERpVvnn29WZ4pncOzQXjIklrnHsx69wKDbRN%2FrPlC3XQFTVq%2Bm%2BmBRYDyNpayeB%2BUX5f4EvZ6nAnMDV4OVvibyJ4qH7NEZa0EZ34pCaa7VMYakOPZ7HSDo3Gv59nA%2FjZPljsyoeRC8xgS9rbln07vVuEqIxtK1hP0cHruQeoqJzNNvJY%2B6hD8LF6OrA972XoEa%2BukwurOZNpgII5onMMaT6dIGOqUBmdJuj1QsObT259CEd073uGRjvfiC6wAHpHFlSi%2BDirEEIjGmffkjOrpeWH9qRNyXlsdIz1KbiaH%2BtC%2FclTeveKhFypqLrDht9K9nDi7dsKPeuE3Q1fVvQwofnaNLvArER3s418LlruFsMjxcfojo4Psg9DkvkICiWLKCRYnmTkiEM%2Fwtp%2BCguudYXUuLyB8he5OHPIiqjtV5BYyqXAC7ECJKJxEa&X-Amz-Signature=b7a2dba35dee355cb80019c252ce895e803f7f7073055f1255b6d3a07a5d6421&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
    이것도 여러 스레드에서 동시에 같은 엔티티 메니저를 사용하는 요청이 오더라도 트랜잭션이 다르다면 접근하는 영속성 컨텍스트 또한 달라진다.
    스프링 컨테이너에서는 스레드별로 각기 다른 트랜잭션을 할당하므로 엔티티 매니저를 호출해도 영속성 컨텍스트가 다르기 때문에 멀티스레드 환경에도 안전하다.

### **준영속 상태와 지연 로딩**

트랜잭션은 보통 서비스 계층에서 시작하므로 서비스 계층이 시작되는 순간 트랜잭션이 생성되고, 서비스 계층이 끝나는 시점에 트랜젝션이 종료되면서 영속성 컨텍스트도 함께 종료가 된다. 그러므로  Service와 Repository계층에서는 영속성 컨텍스트에 관리되지만, Controller나 VIw같은 프리젠테이션 계층에서는 준영속 상태가 된다.

준영속 상태에서는 영속상태가 아니기 때문에 영속성 컨텍스트에서 제공하는 기능을 사용하지 못한다. 지연로딩이나 변경감지를 사용하지 못한다.

준영속 상태일때의 가장 큰 문제점은 지연로딩을 사용하지 못한다는 점이다. 뷰를 렌더링 할때 연관 엔티티도 함께 조회했다고 한다면, 초기화가 되지 않은 상태로 프리젠테이션 계층에 반환되고 이후 데이터를 불러오려고 초기화를 시도할 경우, 준영속 상태이므로 예외가 발생한다.

**해결 방법**

1. 뷰가 필요한 엔티티를 미리 로딩해두는 방법
  1-1. 글로벌 페치 전략 수정 (즉시로딩)
  1-2. 강제로 초기화
  1-3. JPQL 페치 조인 사용

1. OSIV를 사용해서 엔티티를 항상 영속 상태로 유지하는 방법

### **1. 뷰가 필요한 엔티티를 미리 로딩해두는 방법**

**1-1. 글로벌 페치 전략 수정 (즉시로딩)**

```plain text
@ManyToOne(fetch = FetchType.EAGER)
```

즉시로딩을 사용하게 된다면 필요없는 엔티티를 로딩하는 문제가 생기며, JPQL을 사용하게 될 경우에 JPQL자체만을 사용하기 때문에 N+1문제가 발생한다.

이러한 이유로 즉시로딩을 사용하지 않는 것이 좋다.

**1-2. 강제로 초기화**

영속성 컨텍스트가 살아있을 때, 프리젠테이션 계층이 필요한 엔티티를 강제로 초기화하여 반환하는 방법이다. 하지만 이 방법은 프리젠테이션 계층이 서비스 계층을 침범한다. 이를 해결하기 위해서는 퍼사드 패턴을 도입해서 퍼사드 계층에서 프록시 초기화를 담당하게 하면 된다.

퍼사드 계층을 통해 초기화하는 방법은 중간에 계층이 하나 더 끼어들기 때문에 많은 코드를 작성해야한다는 단점이 존재한다.

**1-3. JPQL 페치 조인 사용**

JPQL 페치 조인을 사용해서 해결하는 방법도 있지만, 페치조인을 무분별하게 사용한다면 리포지토리 메소드가 증가하여 프레젠테이션 계층이 데이터 접근 계층을 침범해버린다. 이를 해결하기 위해서는 Member만 조회하는 메소드와 Member과 Team을 같이 조회하는 메소드가 있다고 한다면 Member만 조회하는 메소드에 페치조인을 이용하여 Team까지 같이 조회하도록 한다.

하지만, Member만 조회하면 되는 데 Team까지 조회하는 경우 약간의 로딩시간이 길어질 수 있다.

### **2. OSIV를 사용해서 엔티티를 항상 영속 상태로 유지하는 방법**

첫번째 방법은 번거롭고 실수할 가능성이 있다. 문제의 원인은 엔티티가 프리젠테이션 계층에서 준 영속 상태이기 때문에 발생한다. 여기서 OSIV는 영속성 컨텍스트를 뷰까지 살아있게 만들어준다.

OSIV는 Open Session In View의 약자로 영속성 컨텍스트를 뷰까지 열어두겠다는 의미이다.
(OSIV는 사실 하이버네이트에서 사용되는 용어이고, JPA에서는  OEIV(Open EntityManager In View)라고 한다. 하지만, 관례상 OSIV로 부른다고 한다.)

과거의 OSIV는 클라이언트의 요청이 들어오자마자 서블릿 필터나 스프링 인터셉터에서 트랜잭션을 시작하고 요청이 끝날때 트랜잭션을 끝내는 방식인 요청당 트랜잭션 방식을 사용했다. 하지만 이 방식은 프리젠테이션 계층이 엔티티를 변경 할 수 있다. 이를 방지하기 위해서는 프리젠테이션 계층에서 엔티티를 수정하지 못하도록 막으면 된다. 하지만 수정하지 못하도록 막는 방법을 사용할때 코드량이 증가한다는 단점이 있다. 그래서 요즘은 거의 사용하지 않는다.

이러한 문제점을 보안하여 만들어진것이 스프링 프레임워크가 제공하는 OSIV이다.

스프링이 제공하는 OSIV는 비지니스계증에서만 트랜잭션을 유지하는 방식을 사용한다. 스프링은 다양한 OSIV를 제공한다. 원하는 클래스를 선택해서 사용하면 된다.

- 하이버네이트 OSIV 서블릿 필터

- 하이버네이트 OSIV 스프링 인터셉터

- JPA OEIV 서블릿 필터

- JPA OEIV 스프링 인터셉터

동작 원리

1. 클라이언트 요청이 들어오면 서블릿 필터 혹은 스프링 인터셉터에서 영속성 컨텍스트를 생성한다. 이때 트랜잭션은 시작하지 않는다.

1. 서비스 계층에서 @Transactional로 트랜잭션을 시작할 때 미리 생성해둔 영속성 컨텍스트를 찾아와서 트랜잭션을 시작한다.

1. 서비스 계층이 끝나면 트랜잭션을 커밋하고 영속성 컨텍스트를 플러시한다. 이때 트랜잭션은 끝나지만 영속성 컨택스트는 종료하지 않는다.

1. 컨트롤러와 뷰까지 영속성 컨텍스트가 유지되므로 조회한 엔티티는 영속 상태를 유지한다.

1. 서블릿 필터나 스프링 인터셉터로 요청이 돌아오면 영속성 컨텍스트를 종료한다. 이때 플러시를 호출하지 않고 바로 종료한다.

→ 프리젠테이션 계층까지 영속성 컨텍스트를 살려두면서 변경은 불가능하게 만들었다.

영속성 컨텍스트를 통한 모든 변경은 트랜잭션 안에서 이루어져야하지만 단순한 조회인 경우에는 트랜잭션 없이 가능하다.

단점

- 같은 영속성 컨텍스트를 여러 트랜잭션이 공유할 수 있다는 점을 주의해야한다.

- 프리젠테이션 계층에서 엔티티를 수정하고 난 후 비지니스 로직을 수행한다면 엔티티가 수정될 수 있다.

- 프리젠테이션 계층에서 지연 로딩에 의한 SQL이 실행되기에 성능 튜닝시 확인해야할 부분이 넓어진다.

- 너무 오랜시간 동안 데이터베이스 커넥션 리소스를 사용하기 때문에 실시간 트래픽이 중요한 애플리케이션에서는 커넥션이 모자랄 수 있다.

### **결론**

- 실시간 트레픽이 중요한 경우 DTO로 직접 조회하기

- 어드민 페이지같이 실시간 트레픽이 중요하지 않는 경우 OSIV사용하기
