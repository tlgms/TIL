<!-- notion-page-id: 3bd2cdd741ac80e99f3fde5b7398bb4b -->

# SEQUENCE

SEQUENCE는 PostgreSQL에서 지원하는 순차적인 고유번호를 생성하는 기능이다.

### 1. 수명 주기 관리

- SEQUENCE는 ID가 테이블과 분리된 별도 데이터베이스 객체로 관리된다.
```sql
-- 1. 시퀀스라는 독립된 객체를 만듦
CREATE SEQUENCE my_custom_seq;

-- 2. 테이블을 만들고 기본값으로 시퀀스를 연결함
CREATE TABLE users (
    id BIGINT DEFAULT nextval('my_custom_seq') PRIMARY KEY,
    name VARCHAR(50)
);
```
  - 나중에 `users` 테이블이 필요 없어져서 `DROP TABLE users;`로 테이블을 삭제하더라도, 데이터베이스에는 `my_custom_seq`라는 시퀀스 객체가 계속 남아 있다. → 고아 객체(Orphaned Object)가 됨.

IDENTITY: 컬럼의 하위 속성으로 귀속되어 있어 테이블을 삭제하면 관련 시퀀스도 함께 깔끔하게 제거된다.

### 2. Spring Boot(JPA) 환경에서 SEQUENCE가 갖는 성능적 이점

- JDBC Batch Insert 지원: IDENTITY는 INSERT 실행 후에만 ID를 알 수 있어 Batch Insert가 불가능하지만, SEQUENCE는 사전 채번이 가능하여 대량 INSERT를 한 번에 처리할 수 있다.

- 네트워크 I/O 최적화: @SequenceGenerator의 allocationSize(기본값 50)를 활용해 ID 범위를 메모리에 미리 할당받음으로써 DB 호출 횟수를 대폭 줄입니다.

- persist() 즉시 ID 할당: DB에 flush하기 전에도 메모리상에서 엔티티 ID가 채번되므로 로깅, 연관관계 처리, 외부 API 전달 등에 바로 활용할 수 있다.

- 쓰기 지연(Write-Behind) 유지: JPA 영속성 컨텍스트의 기본 메커니즘(트랜잭션 커밋 시점 플러시)을 깨뜨리지 않는다.

### 3. 선택 기준

IDENTITY

- 단순 CRUD 위주의 애플리케이션, 표준 SQL 준수가 중요한 환경, DB 관리 부담을 줄이고 싶을 때.

SEQUENCE

- 대량 데이터 저장(`saveAll`)이 많거나 성능 최적화가 중요한 Spring Boot / JPA 프로젝트, 저장 전 ID 활용이 필요한 경우.
