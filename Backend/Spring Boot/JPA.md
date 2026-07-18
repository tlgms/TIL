<!-- notion-page-id: 3a02cdd741ac8017bf8ce37e3aa0d2f4 -->

# JPA

## JPA

Java Persistence API의 약자로 java OMR기술에 대한 표준 명세로 java에서 제공하는 API이다.

- OMR
  Object-Relation Mapping의 약자로, 객체-관계 매핑이다.
  - DB데이터 <--Mapping--> Object 필드
    - 객체를 통해 간접적으로 디비 데이터를 다룬다.
  - 객체와 데이터베이스의 데이터를 자동 매핑해준다.

**JPA의 동작과정**

JPA는 애플리케이션과 JDBC 사이에서 동작한다. 개발자가 JPA를 사용하면 JPA 내부에서 JDBC API를 사용하여 SQL를 호출하여 DB와 통신한다.

- JDBC
  DB에 접근할 수 있도록 자바에서 제공하는 API이다.

**특징**

- 데이터를 객체지향적으로 관리할 수 있기 때문에 비지니스로직에 집중 할 수 있고, 객체지향 개발이 가능하다.

- 자바 객체와 DB 테이블 사이의 매칭 설정을 통해 SQL을 생성한다.

- 객체를 통해 쿼리를 작성할 수 있는 JPQL를 지원

- JPA는 지연 로딩이나 즉시 로딩과 같은 몇가지 기법을 제공하는데 이것을 활용하면 SQL을 직접 사용하는 것과 유사한 성능을 얻을 수 있다.

JPA를 사용하는 이유는 sql 중심적인 개발에서 객체 중심적인 개발이 가능하며, 간단한 메소드만으로 CRUD작업이 가능하다. 또한 유지보수가 쉽다. 필드 하나가 변경이 된다면 sql모두를 수정해야 했지만, JPA는 필드만 추가하면 SQL은 JPA가 처리하기 때문에 손댈 것이 없다.

[https://velog.io/@adam2/JPA는-도데체-뭘까-orm-영속성-hibernate-spring-data-jpa](https://velog.io/@adam2/JPA는-도데체-뭘까-orm-영속성-hibernate-spring-data-jpa)

[https://gmlwjd9405.github.io/2019/08/04/what-is-jpa.html](https://gmlwjd9405.github.io/2019/08/04/what-is-jpa.html)
