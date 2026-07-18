<!-- notion-page-id: 3a02cdd741ac808cab75dd69bcc7d59c -->

# Spring Security

[https://twer.tistory.com/entry/Security-%EC%8A%A4%ED%94%84%EB%A7%81-%EC%8B%9C%ED%81%90%EB%A6%AC%ED%8B%B0%EC%9D%98-%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98%EA%B5%AC%EC%A1%B0-%EB%B0%8F-%ED%9D%90%EB%A6%84](https://twer.tistory.com/entry/Security-%EC%8A%A4%ED%94%84%EB%A7%81-%EC%8B%9C%ED%81%90%EB%A6%AC%ED%8B%B0%EC%9D%98-%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98%EA%B5%AC%EC%A1%B0-%EB%B0%8F-%ED%9D%90%EB%A6%84)

스프링 시큐리티는 스프링 기반의 애플리케이션의 보안(인증과 권한, 인가 등)을 담당하는 스프링 하위 프레임워크이다. 
스프링 시큐리티에서는 주로 서블릿 필터와 이들로 구성된 필터 체인으로 구성된 위임모델을 사용한다. 그리고 보안과 관련하여 많은 옵션을 제공해주기 때문에 일일이 보안관련 로직을 작성하지 않아도 되어 편하다.

- 스프링 시큐리티는 필터기반으로 동작하기 때문에 스프링 MVC와 분리되어 관리 및 동작한다.

- 스프링 시큐리티 3.2부터는 XML설정을 이용하지 않아도 되며, 빈으로 설정할 수 있다.

**기본 용어**

- 접근 주체(Principal) : 보호된 리소스에 접근하는 대상

- 인증(Authentication) : 보호된 리소스에 접근한 대상이 누구인지, 애플리케이션의 작업을 수행해도 되는 주체인지 확인하는 과정

- 인가(Authorize) : 해당 리소스에 대해 접근 가능한 권한을 가지고 있는 것을 확인하는 과정(인증 이후)

- 권한 : 어떠한 리소스에 대한 접근 제한, 모든 리소스는 접근 제어 권한이 걸려있기 때문에 인가 과정에서 해당 리소스에 대한 최소한의 권한을 가졌는 지 확인한다.

### **스프링 시큐리티의 구조**

스프링 시큐리티는 기본적으로 쿠키&세션 방식으로 인증한다.

스프링 시큐리티의 구조는 많이 찾아볼 수 있는데 내가 이해하기 쉬운 방식으로 이해하자면, 일단 로그인을 시도한다면 DB에서 유저를 찾고 DB에 있는 유저라면 유저의 세션을 생성한다. 그리고 SecurityContextHolder에 저장후 클라이언트에게 세션 아이디를 보내준다. 로그인 이후의 요청이라면, 인증 관리자(Authentication Manager)와 접근 결정 관리자(Access Decision Manager)를 통해 사용자의 리소스 접근을 관리한다. 인증관리자는 UsenamePasswordAuthenticationFilter, 접근 결정 관리자는 FilterSecurityInterceptor가 수행한다.

- HTTP기본 인증을 요청하면 BasicAuthenticationFilter를 통과한다.

- HTTP Digest 인증을 요청하면 DigestAuthenticationFilter를 통과한다.

- 로그인 폼에 의해 요청된 인증은 UseerPasswordAuthenticationFilter를 통과한다.

- x509 인증을 요청하면 X509AuthenticationFilter를 통과한다.

**스프링 시큐리티 필터**

1. SecurityContextPersistenceFilter
  SecurityContextRepository에서 SecurityContext를 로드하고 저장하는 일을 담당함

1. LogoutFilter
  설정된 로그아웃 URL로 오는 요청을 감시하며, 해당 유저를 로그아웃 처리

1. UsernamePasswordAuthenticationFilter
  설정된 로그인 URL로 오는 요청을 감시하며, 유저 인증 처리
  AuthenticationManager를 통한 인증 실행
  - 인증 성공 시, 얻은 Authentication 객체를 SecurityContext에 저장 후 AuthenticationSuccessHandler 실행
  - 인증 실패 시, AuthenticationFailureHandler 실행

1. DefaultLoginPageGeneratingFilter
  폼기반 또는 오픈 아이디 기반 인증에 사용하는 가상 URL에 대한 요청을 감시하고 로그인 폼 기능을 수행하는 데 필요한 HTML을 생성함

1. BasicAuthenticationFilter
  HTTP 기본 인증 해더를 감시하고 이를 처리함

1. RequestCacheAwareFilter
  로그인 성공 이후 원래 요청 정보를 재구성하기 위해 사용된다.

1. SecurityContextHolderAwareRequestFilter
  HttpServletRequestWrapper를 상속한 SecurityContextHolderAwareRequestWapper 클래스로 HttpServletRequest 정보를 감싼다. SecurityContextHolderAwareRequestWrapper 클래스는 필터 체인상의 다음 필터들에게 부가정보를 제공한다.

1. AnonymousAuthenticationFilter
  이 필터가 호출되는 시점까지 사용자가 아직 인증을 받지 목했다면 요청 관련 인증 토큰에서 사용자가 익명 사용자로 나타나게 된다.

1. SessionManagementFilter
  인증된 사용자와 관련된 모든 세션을 추적한다.

1. ExceptionTranslationFilter
  보호된 요청을 처리하는 중에 발생할 수 있는 예외를 위임하거나 전달하는 역할을 한다.

1. FilterSecurityInterceptor
  AccessDecisionManager 로 권한부여 처리를 위임함으로써 접근 제어 결정을 쉽게해준다.
