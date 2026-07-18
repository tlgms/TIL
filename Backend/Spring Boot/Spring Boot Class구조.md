<!-- notion-page-id: 3a02cdd741ac80e98778d529597ec841 -->

# Spring Boot Class구조

Client - Controller - Service - Repository - DB

<--------------- Dto ---------------><- Entity ->

**Controller**

클라이언트에서 요청을 받고 그에 따른 응답을 해 주는 곳이며, 요청에 따라 어떤 처리를 할 것인가를 결정하고 (실질적 처리는 하지 않는다.) 응답을 보내준다.

```java
@PostMapping("/join") // POST 방식으로 URL이 /join이었다면 이 메소드를 수행한다.
    @ResponseStatus (HttpStatus.CREATED)
        // 성공적으로 요청을 수행했다면 201상태코드로 응답을 보낸다.
    public void join (@RequestBody @Valid UserDto dto) {
                        // Body에서 UserDto 형식으로 데이터를 받는다.
        userService.saveData(dto);
        // Service를 호출하여 데이터에 대한 처리를 한다.
    }
```

만약, Service가 없었다면 위의 메소드는 내용이 많아지고 가독성도 떨어지게된다. 또한 Service가 없다면 유지와 보수가 힘들어지게 된다.

**Service**

데이터의 처리를 담당한다. Controller이 불러내면 그에 맞는 메소드를 수행한다.

```java
// Service Class중 한 부분
public UserEntity saveData(UserDto userdto){

        UserEntity userEntity = UserEntity.builder()
                .name(userdto.getName())
                .pwd(passwordEncoder.encode(userdto.getPwd()))
                .gameEntity(
                        GameEntity.builder()
                                .Jstage(0)
                                .Cstage(0)
                                .Sstage(0)
                                .build()
                )
                .build();

        userRepository.save(userEntity);

    }
```

이런식으로 Service안에 여러 기능들을 하는 메소드를 넣어서 그 기능을 사용하고 싶을 때마다 꺼낼 수 있도록 하기 때문에 중복되는 코드를 줄일 수 있다. 또한 재사용성이 좋아진다.

**DTO**

Data Transfer Object의 약자로, 계층간의 데이터 교환 역할을 하는 객체이다. Dto를 사용하는 이유는 Entity의 외부 노출을 막기 위해서이며, Entity만 있다면 Entity가 복잡해진다.

**Entity**

실제 DB테이블과 매칭될 클래스로 DB의 테이블의 값들과 같은 필드를 가지고 있다.

```java
@Entity
@Table(name = "user")
public class UserEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String name;

    @Column(nullable = false)
    private String pwd;

}
```

위의 코드대로 Entity를 만들면

**테이블**
| id | name | pwd |
|---|---|---|
| 1 | 김태균 | qwer1234 |

이런식으로 DB테이블이 만들어지게 된다.

**Repository**

DB의 데이터들을 CRUD할 수 있는 인터페이스로 스프링 프레임워크에서 제공하는 jpa처리를 담당하는 Repository를 상속받아 사용한다.

```java
public interface UserRepository extends CrudRepository<UserEntity, Long> {
                                // Repository를 상속받음. 또한 Entity와 매칭된다.

    Optional<UserEntity> findByname(String name);
    boolean existsByname(String name);

}
```
