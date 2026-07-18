<!-- notion-page-id: 3a02cdd741ac80b88debd3ae28109136 -->

# Entity 연관관계

Entity끼리는 연관관계를 맺을 수 있는데 이를 '관계형 데이터베이스'라고 한다.

1:1(일대일) 관계
일대일 관계는 하나의 Entity는 연관된  Entity와 단 하나의 관계를 맺는 것을 말한다.
예) 학생 - 성적

## 1 : 1 연관관계
@OneToOne : 1:1 Entitiy매핑을 할 때 사용하는 어노테이션
@JoinColumn : 1:1 매핑할 Entity의 외래키를 설정하는 어노테이션
User Entity
```java
public class UserEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, length = 10)
    private String name;

    @Column(nullable = false)
    private String pwd;

    @OneToOne(cascade = CascadeType.ALL)
    @JoinColumn(name = "GAME_ID")
    private GameEntity gameEntity;

}

```
Game Entity
```java
public class GameEntity {

    @Id
    @Column(name = "GAME_ID") // 위에서 설정 해 주었던 외래키 이름 넣기
    @GeneratedValue(strategy = GenerationType.IDENTITY)
		// 외래키도 생성전락을 선택 해 주어야함.
    private Long id;

    @Column(nullable = false, length = 2)
    private Integer Sstage;

    @Column(nullable = false, length = 2)
    private Integer Cstage;

    @Column(nullable = false, length = 2)
    private Integer Jstage;

}

```
```java
// UserEntity를 통해 GameEntity에 접근 할 수 있음.
UserEntity.getGameEntity().getCstage();


// 빌더패턴에 적용
UserEntity userDto = UserEntity.builder()
                .id(userEntity.getId())
                // 해당 id값을 넘겨주지 않으면 새로운 레코드가 생성되니 유의할 것!
                .name(userEntity.getName())
                .pwd(userEntity.getPwd())
                .gameEntity( 
									// 연결된 Entity를 빌더 패턴으로 접근할 때는 이런식으로 해야함.
                        GameEntity.builder()
                                .id(userEntity.getGameEntity().getId())
                                .Cstage(userEntity.getGameEntity().getCstage())
                                .Jstage(userEntity.getGameEntity().getJstage())
                                .Sstage(Sstage)
                                .build()
                )
                .build();
```

1:N(일대다) 관계
일대다 관계는 하나의 Entity가 연관된 Entity의 객체를 여러개를 가질 수 있는 것을 말한다.
예) 반 - 학생
-> 보충 설명을 하자면 Entity를 가질 수 있는 것이 아니라 연관된 Entity의 '객체'를 가질 수 있는 것이다.
1반 이라는 하나의 Entity에 여러명의 학생이 학생 Entity에서 객체로 생성되어 연관된다.

N:N(다대다)관계
다대다 관계는 두 Entity모두 여러개의 객체를 가지고 있는 것이다. 주 Entity도 연관된 Entity도 서로의 객체가 연관되어있다.
-> 여기서 1:N이랑 N:N이 헷갈리는데 그림을 그리면 바로 이해가 된다. 1:N은 한쪽만 많은 것이라고 생각하면 된다. 딱 한쪽만 많이 연관된것이다. 근데 N:N은 둘다 많은 객체를 가지고 있는 것이다. 1:N에서 예로 든 반 - 학생을 통해 설명하자면 학생은 1반 말고 다른 반을 가질 수 없기 때문에 N:N관계가 될 수 없다.
예)  학원 - 학생 (학생은 많은 학원을 다닐 수 있으며, 학원은 많은 학생을 수용한다)
