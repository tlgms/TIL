<!-- notion-page-id: 3a02cdd741ac803fa9c9f3cb3724f158 -->

# Jackson 라이브러리

Jackson 라이브러리는 json 데이터 구조를 처리해주는 라이브러리이다. Jackson 라이브러리는 크게 3가지 라이브러리로 구성되어 있다.

- Jackson-core : low-level 스트리밍 API 정의 및 JSON 별 구현

- Jackson-databind : 스트리밍 패키지에 대한 데이터 바인딩 지원 구현. 스트리밍 및 annotation 패키지에 의존

- Jackson-annotations : 표준 Jackson annotation 포함

Jackson 라이브러리를 사용하기 위해서는 의존성을 추가해주어야 한다.

```plain text
implementation "com.fasterxml.jackson.core:jackson-core:2.9.9"
implementation "com.fasterxml.jackson.core:jackson-annotations:2.9.9"
implementation "com.fasterxml.jackson.core:jackson-databind:2.9.9"
implementation "com.fasterxml.jackson.module:jackson-module-kotlin:2.9.9"

```

Spring Boot에서는 spring-boot-starter-web 의존성을 추가해주면 Jackson 라이브러리가 포함된다.

```plain text
implementation 'org.springframework.boot:spring-boot-starter-web'

```

Jackson 라이브러리는 JSON을 표현하기 위해 JsonNode라는 추상클래스를 제공한다. JSON 조작은 추상 클래스를 상속한 자식 클래스의 메소드를 통해서 이루어진다. 이러한 자식 클래스의 인스턴스는 ObjectMapper 클래스를 통해서 편리하게 생성 가능하다.

### Jackson의 동작과정

Jackson은 JSON 데이터를 출력하기 위한  MappingJacksonHttpMessageConverter를 제공하는데 스프링 MessageConverter를  MappingJacksonHttpMessageConverter으로 등록한다면, controller가 리턴하는 객체를 자바 Reflection을 사용하여 Jackson의 ObjectMapper API로 JSON 객체를 완성한다.

**자바 Reflection이란?**
구체적인 클래스 타입을 알지 못해도 그 클래스의 메소드, 타입, 변수들에 접근할 수 있도록 해주는 자바 API

내가 Jackson 라이브러리에 대해 정리하게 된 이유는 Response에서 Getter 어노테이션을 제거 했을 때 발생한 오류 때문이었다. 실행도 잘 되고, 데이터베이스에 값이 잘 저장이 되지만 값을 반환할 때 문제가 발생하였다. controller에서 JSON을 반환할때 @ResponseBody를 사용했는데 당시 나는 Jackson 라이브러리를 몰랐기 때문에 생긴 실수였다.

아래는 Jackson 공식문서의 일부분이다.

---

**How Jackson ObjectMapper Matches JSON Fields to java Fields**
어떻게 Jackson ObjectMapper가 JSON의 필드와 java의 필드와 일치시키는 가

**To read Java objects from JSON with Jackson properly, it is important to know how Jackson maps the fields of a JSON object to the fields of a Java object, so l will explain how Jackson does that.**
Jackson으로 JSON에서 자바 객체를 올바르게 읽기 위해서 Jackson이 JSON 필드와 Java 필드를 매핑하는 방법을 아는 것이 중요합니다. Jackson이 어떻게 하는 지 설명해드리겠습니다.

**By default Jackson maps the fields of a JSON object to finds in a Java object by matching the JSON field to the getter and setter methods in the Java object.**
기본적으로 Jackson은 JSON 필드의 이름을 Java 객체의 getter과 setter 메소드와 일치시켜 JSON 객체 필드를 Java 객체 필드에 매칭 시킨다.

**Jackson removes the “get” and “set” part of the names of the names of the getter and setter methods, and converts the first character of the remaining name to lowercase.**
Jackson은 getter 및 setter 메소드 이름 중 "get"과 "set" 부분을 제거하고 나머지 이름의 첫 문자를 소문자로 변환합니다.

---

response를 JSON으로 변환할 때 Jackson 라이브러리를 사용하는데 json 문자열로 Serialize 할때, Getter 또는 Setter이 필요하다. 그러므로 Getter 어노테이션이 꼭 필요했던 것이었다.
