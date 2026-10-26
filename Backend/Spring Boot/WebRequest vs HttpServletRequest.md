<!-- notion-page-id: 4052cdd741ac80828dddffd31a03f863 -->

# WebRequest vs HttpServletRequest

**1. HttpServletRequest**

**정의**: 자바 표준 Servlet API의 일부로, 서블릿 컨테이너(Tomcat 등)가 HTTP 요청을 받을 때 직접 생성하는 객체입니다. [[1](https://barnabas-kim8618.tistory.com/206), [2](https://crushed-taro.tistory.com/164)]

- **정의**: 자바 표준 Servlet API의 일부로, 서블릿 컨테이너(Tomcat 등)가 HTTP 요청을 받을 때 직접 생성하는 객체입니다. [[1](https://barnabas-kim8618.tistory.com/206), [2](https://crushed-taro.tistory.com/164)]

**특징**:
    ◦ 서블릿 API에 완전히 종속적입니다.
    ◦ HTTP 요청의 모든 상세 정보(IP, 헤더, 바디, 쿠키, 세션, 파라미터 등)를 직접 다룰 수 있습니다.
    ◦ 서블릿, 필터, 인터셉터, 컨트롤러 등에서 주로 사용됩니다. [[1](https://wonyong-jang.github.io/web/2020/02/15/Web-HttpServletRequest-HttpServletResponse.html), [2](https://crushed-taro.tistory.com/164), [3](https://barnabas-kim8618.tistory.com/206)]

- **특징**:
  - ◦ 서블릿 API에 완전히 종속적입니다.
  - ◦ HTTP 요청의 모든 상세 정보(IP, 헤더, 바디, 쿠키, 세션, 파라미터 등)를 직접 다룰 수 있습니다.
  - ◦ 서블릿, 필터, 인터셉터, 컨트롤러 등에서 주로 사용됩니다. [[1](https://wonyong-jang.github.io/web/2020/02/15/Web-HttpServletRequest-HttpServletResponse.html), [2](https://crushed-taro.tistory.com/164), [3](https://barnabas-kim8618.tistory.com/206)]

**2. WebRequest**

**정의**: 스프링 프레임워크(Spring Framework)에서 제공하는 추상화 인터페이스입니다. [[1](https://velog.io/@dainel/HttpServletRequest-vs-WebRequest-%EB%AC%B4%EC%97%87%EC%9D%84-%EC%96%B8%EC%A0%9C-%EC%8D%A8%EC%95%BC-%ED%95%A0%EA%B9%8C)]

- **정의**: 스프링 프레임워크(Spring Framework)에서 제공하는 추상화 인터페이스입니다. [[1](https://velog.io/@dainel/HttpServletRequest-vs-WebRequest-%EB%AC%B4%EC%97%87%EC%9D%84-%EC%96%B8%EC%A0%9C-%EC%8D%A8%EC%95%BC-%ED%95%A0%EA%B9%8C)]

**특징**:
    ◦ 서블릿 API에 종속적이지 않은 형태를 취합니다.
    ◦ 내부적으로 `HttpServletRequest`의 정보를 대부분 캡슐화하여 제공합니다.
    ◦ 서블릿 외의 다른 환경(예: 포틀릿 등)에서도 공통으로 요청을 다룰 수 있도록 설계되었습니다.
    ◦ `getParameter()`, `getHeader()` 등 기본적인 요청 정보 조회는 가능하지만, 서블릿 전용 세부 기능을 쓰려면 `getNativeRequest(HttpServletRequest.class)` 등으로 원본 객체를 꺼내 써야 할 때가 있습니다. [[1](https://jhkang-tech.tistory.com/50), [2](https://crushed-taro.tistory.com/164), [3](https://velog.io/@dainel/HttpServletRequest-vs-WebRequest-%EB%AC%B4%EC%97%87%EC%9D%84-%EC%96%B8%EC%A0%9C-%EC%8D%A8%EC%95%BC-%ED%95%A0%EA%B9%8C)]

- **특징**:
  - ◦ 서블릿 API에 종속적이지 않은 형태를 취합니다.
  - ◦ 내부적으로 `HttpServletRequest`의 정보를 대부분 캡슐화하여 제공합니다.
  - ◦ 서블릿 외의 다른 환경(예: 포틀릿 등)에서도 공통으로 요청을 다룰 수 있도록 설계되었습니다.
  - ◦ `getParameter()`, `getHeader()` 등 기본적인 요청 정보 조회는 가능하지만, 서블릿 전용 세부 기능을 쓰려면 `getNativeRequest(HttpServletRequest.class)` 등으로 원본 객체를 꺼내 써야 할 때가 있습니다. [[1](https://jhkang-tech.tistory.com/50), [2](https://crushed-taro.tistory.com/164), [3](https://velog.io/@dainel/HttpServletRequest-vs-WebRequest-%EB%AC%B4%EC%97%87%EC%9D%84-%EC%96%B8%EC%A0%9C-%EC%8D%A8%EC%95%BC-%ED%95%A0%EA%B9%8C)]
