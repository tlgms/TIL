<!-- notion-page-id: 3a02cdd741ac80f883afe4cb1e0e545a -->

# Repository

### 스프링 프레임워크에서 JPA를 편하게 지원하도록 도와줌

**CRUD** 처리를 위한 공통 인터페이스 제공

- **C**reate(생성), **R**ead(읽기), **U**pdate(갱신), **D**elete(삭제)

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/691f90fd-6dc5-4eaa-8c76-f263b46c80de/e7d3bb81-993b-479e-90e0-4ea83adb5bfd/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KO563B6%2F20260717%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260717T160432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC0z0VxsJGfFJuACXSDxgN8nS9gMHqvUytYlVm2xt2fkAiEA5TKVzyEMenHc4ian1P6DaLaT3MFmFHwc3qT5GxF8JEQq%2FwMIYRAAGgw2Mzc0MjMxODM4MDUiDJm0dlIeNVnYKto%2BnircAybIRRVelhOFz6D%2FsokrDwH9H%2BaRE%2Fq5p%2F91s4RiqdWSUXNtWEmXn5AcR%2FIiQou5ldSdggamv6aPPQpX5UJ7V%2FYackcgtEHwVDKcWnvML9zj2RiE3NzrTN53ZNO5%2Ftp7r1L4u8N0OBkG%2BWtHZCjo9cElU8s2lToCW2KOPhaEgM1u2sclEz6hlhcxzTQOAyFeybUltbCvWe6oBWmmGnkBOzn5KE149DkuswQB6cxqT4OMqg4UxXJ%2FBJY1lY0FRDOYRfu7EYvBwwmnqDtEnRpWjuehrkOxOtPjnDT50c5XuciTELuYOKKW1EIK8TmygZs0Uo7cc2aaafoipLzYXuOQ2gJfBKR5dL5eSIGIu80v6aYJZmQ5bNn57oAAuK1O1DSv28tZkURzigqzp%2Fb%2Btm7%2FjTmI2zaE5b5jaCEe%2F1mQFls1YPXt6tBcrl%2Fu3iiK%2FJn0AG7HRRvaUtOItuVMzA1mHz5LRyuJAKKp69y9EWcqRka%2FeckufHIvHlPr3JOMnbszD%2BZqkyxZjyDV5xLL5UivxXiHX0%2F8NKiWq0R69Wf0jDA6HQqJhaXQilNFdJLcmJyxv9ZFSMzwsgyUWe6FxNBRjVTGwb5hQc9zajofITTx232KSQ3Z3eOjFUMd%2FHx0MLOT6dIGOqUBKGeaL6tbCBq9%2BVGVZi81yHz558djw3pVZE1OjLvoOlT6gD7OPNffl3pskIbnCA8z4dQ26NQ90AGO5kkcE8jORr4qvcgBR16uIrUSJoiH1GqJGR2E%2BA5oxYm7rsGgvh7InrNZ9xHM2o9JIau8yPvm9GukvNxAXB9gdMa5592jgvg1n58nTGjZvY5bQhyFUjQh0Yu6%2FUc2lLTJNBI2csfyjZ97Pl%2BW&X-Amz-Signature=f2e0eb432f19970eeeb3059edddd7a6434831fa5420e24a2bc56af4bbedc217a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
    ### Repository의 종류
    - Repository<T, ID>
    - CrudRepository<T, ID>
    - PagingAndSortingRepository<T, ID>  
      페이징 처리를 위한 메소드를 제공한다.
    - JpaRepository <T,ID>

Repository의 상속 관계는 그림과 같다. 

> Repository에서 멀어질수록 더 많은 기능들을 담고 있는 인터페이스이다. 
그러므로 JpaRepository를 사용하면 많은 기능들을 사용할 수 있다. 하지만, 개발자가 선언하지 않은 메소드들이 외부에 노출 될 수 있다. 
  기본적인 기능들은 CrudRepository만으로도 가능하기 때문에 작은 기능들을 사용하는 프로젝트는 CrudRepository를 사용하는 것이 좋다.
  - 다른 차이점
![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/691f90fd-6dc5-4eaa-8c76-f263b46c80de/058c00f3-74c2-4734-a332-efad00997e05/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-12-13_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_4.55.39.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RESGSIZ%2F20260717%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260717T160432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEQhu5IzALqWVsORmplPs8mtiDCN7%2FZdD2uT%2Bg8u3lgXAiBnZdnjp0olwXYHbWoXuFGHENNpz3LsAzM91O3QXvJbxir%2FAwhhEAAaDDYzNzQyMzE4MzgwNSIM%2FquNcpTXiLuQv%2F7%2BKtwDgrOSWxZ80DSBn%2FuN4tB0HuCRwm%2FvZTJXjs7F0aaIeRU7jerf5XwnDDdrsqegy%2FCrLBTdTxyxI15HGAbsgUof6wugBkB2gdLl4uXLp7cPkfEytdBKmwpB4UC8005HA8zVqBx4WA9u%2Fov2gnuovhpcN8e4i30VmwuodPUGoTSXzf0omRvYhhKNZePynxJ6qnQ0jYRG2OMq%2FI2wWJcaO%2B0BKjw%2FD1pO9%2FiWvAWiZxK3oS76oYAN7EGp1uanc%2BeZy6RMyaGuVA7SlPX9onRVwZWvtAYpHnHUmSE7WAzMXBq8Pgy8AFnwph%2FpwRQyhBJN17AP9O7BU1u4Efl6ZMxOpnyLCZcSs9p8%2BgvPwQv4P%2FilymXoyk50NP6F90XdMaqTSQXuNh5xgIceTv2zBRJU1KLDNIxhk1FtTO90FGYfgs97Un8YZ73www2EX5uSoGxq2aHn89lgxRHauAnYoOXJYkONf9eI01L8gYqaUHbrLVY4aUtXKvTgdT5FcNSLaobeVO8TE8YxD7E8wphtHw8vPMCZ7JPTXUJU1PYJjyNT0T1THBceKSMwhINMDTZgBCacKc%2BmC%2Bj0N6ZaxXiL%2FnKBhk%2FKdmhNKSay1Cf%2BDqWo9Rpw5UOx3ULBUuF7S5v3eR0wn5Tp0gY6pgFeIs2XiO5nXR6JCnkJnrasKumPoTvtXaMt0o9Q7YQ0r5xW2fYIbCI4eoi3Ewfj2arT1wy2b5xomTs0v90htzPUvEdQwWxFLt0h%2Fz4OD3gyoYvHw3AeKanivnQNhP4IvIfXWRmDB0U14LYC4sCC7Wz7pBlXYad%2Fq36%2BKSqyCJE9IiW1iQC62qLqSQu%2F5Yues%2FqmJD2Jjy7HezEPuClFyGijnz94k0Pc&X-Amz-Signature=3a775e9bd28aa7f07b1d2d418c4d7c1e49a3686bceb74552c9a3ce48150e0788&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### |  Repository interface 정의

```java
@Repository //어노테이션을 꼭 붙이지 않아도 된다.
public interface PersonRepository extends CrudRepository<엔티티 타입, 식별자 타입> {
}
```

### |  Repository 메소드 

findBy

- 퍼지검색 : 검색키워드가 정확하지 않아도 예상하여 적절한 단어를 찾는 검색 방식
