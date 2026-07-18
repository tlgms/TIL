<!-- notion-page-id: 3a02cdd741ac80a2b982ee14d3cdc994 -->

# yml 파일

```yaml
jpa:
  generate-ddl: false
  hibernate:
    ddl-auto: update
  database-platform: org.hibernate.dialect.MySQL5InnoDBDialect
```

`generate-ddl: false`

• true로 설정 시, Entity어노테이션이 명시된 클래스를 찾아서 DDL(데이터베이스를 정의하는 언어)을 생성하고 실행 → false는 true의 반대겠쥬? 

`ddl-auto: update`

- create: 기존테이블 삭제 후 다시 생성 (DROP + CREATE)

- create-drop: create와 같으나 종료시점에 테이블 DROP

- update: 변경분만 반영(운영DB에서는 사용하면 안됨)

- validate: 엔티티와 테이블이 정상 매핑되었는지만 확인

- none: 사용하지 않음(사실상 없는 값이지만 관례상 none이라고 한다.)

> **주의해야할점**
  - 운영 장비에서는 절대 crate, create-drop, update 사용하면 안된다.
  - 개발 초기 단계는 create 또는 update
  - 테스트 서버는 update 또는 validate
  - 스테이징과 운영 서버는 validate 또는 none
    - 스테이징 환경이란 운영환경과 거의 동일한 환경으로 구성하여, 운영환경에 배포하기 전 여러 가지 기능(성능, 장애 등)을 검증하는 환경이다. 
    - 운영환경은 실제 서비스를 운영하는 환경이다

`database-platform: org.hibernate.dialect.MySQL5InnoDBDialect`

데이터베이스 스토리지 엔진을 설정하는 건데 여기서는 `InnoDB` 로 설정함.

[https://nomadlee.com/mysql-스토리지-엔진-종류-및-특징/](https://nomadlee.com/mysql-스토리지-엔진-종류-및-특징/)

```yaml
datasource:
  url: jdbc:mysql://localhost:3306/swith
  username: root
  password: password
  driver-class-name: com.mysql.cj.jdbc.Driver
```

`url: jdbc:mysql://localhost:3306/swith`

데이터베이스 url을 적으면 된다. 데이터베이스마다 설정하는 방법이 다르니 주의하기!

`username: root`

데이터베이스의 유저 이름을 적어주면 된다.

`password: password`

데이터베이스 비밀번호를 적어주면 된다.

`driver-class-name: com.mysql.cj.jdbc.Driver`

데이터베이스 JDBC Driver의 이름을 적어주면되는 데 데이터베이스마다 다르다!

[https://crazykim2.tistory.com/81](https://crazykim2.tistory.com/81)

mysql에서는 `com.mysql.jdbc.Driver`와 `com.mysql.cj.jdbc.Driver`두가지가 있지만 `com.mysql.jdbc.Driver`는 Deprecated이므로 `com.mysql.cj.jdbc.Driver` 을 사용
