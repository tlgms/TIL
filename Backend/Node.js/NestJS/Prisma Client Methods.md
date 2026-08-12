<!-- notion-page-id: 3ba2cdd741ac80bf8df5f212f198ee2c -->

# Prisma Client Methods

## Read (데이터 찾기) Method


| 메서드 | 하는 일(요약) | 언제 쓰나(예시) | 주요 파라미터 |
|---|---|---|---|
| `findUnique` | 조건에 맞는 **하나의 데이터**만 찾음 | 고유값(ID 등)으로 정확히 1개 조회할 때 | `where` **(필수, 유니크 필드만)** · `select` · `include` · `omit` ※ 없으면 `null` 반환. 예외를 던지려면 `findUniqueOrThrow` |
| `findFirst` | 조건에 맞는 **첫 번째 데이터 1개**만 찾음 | 정렬/필터 결과 중 **맨 앞 1개**만 필요할 때 | `where` · `orderBy` · `skip` · `cursor` · `distinct` · `select` · `include` · `omit` ※ 예외 버전은 `findFirstOrThrow` |
| `findMany` | 조건에 맞는 **여러 데이터**를 모두 찾음 | 조건에 맞는 **목록(list)**을 가져올 때 | `where` · `orderBy` · `take` · `skip` · `cursor` · `distinct` · `select` · `include` · `omit` ※ 결과 없으면 빈 배열 `[]` |

## Create (데이터 만들기) Method


| 메서드 | 하는 일(요약) | 언제 쓰나(예시) | 주요 파라미터 |
|---|---|---|---|
| `create` | 새로운 **데이터 1개** 생성 | 단일 레코드 생성 | `data` **(필수)** · `select` · `include` · `omit` ※ `data` 안에서 관계 `create` / `connect` 중첩 쓰기 가능 |
| `createMany` | **여러 데이터**를 한 번에 생성 | 여러 레코드 **일괄 생성** | `data` **(필수, 객체 배열)** · `skipDuplicates` ※ 반환값은 레코드가 아니라 `{ count }`. 중첩 쓰기 불가 |
| `createManyAndReturn` | 여러 데이터를 만들고 **생성된 레코드까지 반환** | 일괄 생성 후 생성된 값(자동 id 등)이 필요할 때 | `data` **(필수)** · `skipDuplicates` · `select` · `omit` ※ PostgreSQL / SQLite 등 일부 DB만 지원 |

## Update (데이터 고치기) Method


| 메서드 | 하는 일(요약) | 언제 쓰나(예시) | 주요 파라미터 |
|---|---|---|---|
| `update` | 기존 **데이터 1개**를 찾아 수정 | 특정 레코드 1개 수정 | `where` **(필수, 유니크 필드)** · `data` **(필수)** · `select` · `include` · `omit` ※ 대상이 없으면 에러 발생 |
| `updateMany` | 조건에 맞는 **여러 데이터**를 한 번에 수정 | 조건부로 여러 레코드 **일괄 수정** | `where` · `data` **(필수)** · `limit` ※ 반환값은 `{ count }`. 중첩 쓰기 불가 |
| `upsert` | 있으면 **수정**, 없으면 **생성** | “없으면 만들고, 있으면 갱신” 패턴 | `where` **(필수)** · `create` **(필수)** · `update` **(필수)** · `select` · `include` |

## Delete (데이터 지우기) Method


| 메서드 | 하는 일(요약) | 언제 쓰나(예시) | 주요 파라미터 |
|---|---|---|---|
| `delete` | 기존 **데이터 1개** 삭제 | 특정 레코드 1개 삭제 | `where` **(필수, 유니크 필드)** · `select` · `include` ※ 대상이 없으면 에러 발생, 삭제된 레코드를 반환 |
| `deleteMany` | 조건에 맞는 **여러 데이터** 삭제 | 조건부로 여러 레코드 **일괄 삭제** | `where` · `limit` ※ `where`를 생략하면 **전체 삭제**. 반환값은 `{ count }` |

## Aggregation (개수/연산) Method


| 메서드 | 하는 일(요약) | 언제 쓰나(예시) | 주요 파라미터 |
|---|---|---|---|
| `count` | 조건에 맞는 **개수**를 셈 | 총 개수/조건부 개수 계산 | `where` · `select` (필드별 개수, `_all`) · `orderBy` · `take` · `skip` · `cursor` |
| `aggregate` | 합계/평균/최댓값 등 **계산값** 반환 | 통계(합, 평균, min/max 등) 필요할 때 | `_count` · `_avg` · `_sum` · `_min` · `_max` · `where` · `orderBy` · `take` · `skip` · `cursor` ※ `_avg`/`_sum`은 숫자 필드에만 사용 |
| `groupBy` | 특정 기준으로 **그룹화**해서 계산 | 그룹별 통계(예: 카테고리별 개수/합계) 필요할 때 | `by` **(필수, 그룹 기준 필드 배열)** · `where` (그룹화 **전** 필터) · `having` (그룹화 **후** 필터) · `orderBy` · `_count` 등 집계 · `take` · `skip` |

---

# 공통 파라미터

## `where` — 어떤 행을 고를지 (필터)


| 구분 | 연산자 | 설명 |
|---|---|---|
| 비교 | `equals` · `not` · `in` · `notIn` | 같다 / 아니다 / 목록 안에 있다 / 목록 밖이다 |
| 크기 | `lt` · `lte` · `gt` · `gte` | 미만 / 이하 / 초과 / 이상 (숫자·날짜) |
| 문자열 | `contains` · `startsWith` · `endsWith` · `mode` | 포함 / 시작 / 끝. `mode: 'insensitive'`로 대소문자 무시(PostgreSQL 등) |
| 논리 | `AND` · `OR` · `NOT` | 조건 조합. 같은 객체 안 필드들은 기본적으로 AND |
| 관계 | `some` · `every` · `none` · `is` · `isNot` | 1:N 관계는 `some`/`every`/`none`, 1:1은 `is`/`isNot` |

```typescript
const users = await prisma.user.findMany({
  where: {
    email: { endsWith: '@dsm.hs.kr' },
    age: { gte: 18, lt: 30 },
    OR: [{ role: 'ADMIN' }, { verified: true }],
    posts: { some: { published: true } }, // 게시글 중 하나라도 공개면
  },
})
```

## `select` / `include` / `omit` — 어떤 필드를 받을지


| 파라미터 | 설명 | 주의 |
|---|---|---|
| `select` | **포함할 필드만** 명시 (화이트리스트) | `include`와 **동시 사용 불가** (같은 레벨에서) |
| `include` | 기본 스칼라 필드 + **관계 필드까지** 함께 조회 | 중첩 `include`는 N+1/과다 조인 주의 |
| `omit` | **제외할 필드만** 명시 (블랙리스트) | 비밀번호 같은 민감 필드 빼는 데 유용 |

```typescript
// select: 필요한 것만
await prisma.user.findUnique({
  where: { id },
  select: { id: true, email: true, posts: { select: { title: true } } },
})

// include: 관계까지 통째로
await prisma.user.findUnique({
  where: { id },
  include: { posts: true, profile: true },
})

// omit: 민감 필드 제외
await prisma.user.findMany({ omit: { password: true } })
```

## `orderBy` / `take` / `skip` / `cursor` / `distinct` — 정렬·페이지네이션


| 파라미터 | 값 | 설명 |
|---|---|---|
| `orderBy` | `{ field: 'asc' \| 'desc' }` 또는 배열 | 정렬 기준. 배열로 다중 정렬. `{ sort, nulls }`로 NULL 위치 지정 가능 |
| `take` | 숫자 (음수 가능) | 가져올 개수. **음수면 뒤에서부터** |
| `skip` | 숫자 | 건너뛸 개수. offset 페이지네이션용 |
| `cursor` | 유니크 필드 값 | 커서 기반 페이지네이션. 보통 `skip: 1`과 같이 씀 (커서 자기 자신 제외) |
| `distinct` | 필드명 배열 | 지정 필드 기준 중복 제거 |

```typescript
// offset 방식 — 뒤로 갈수록 느려짐
await prisma.post.findMany({ orderBy: { createdAt: 'desc' }, skip: 20, take: 10 })

// cursor 방식 — 대용량에 유리
await prisma.post.findMany({
  take: 10,
  skip: 1,
  cursor: { id: lastSeenId },
  orderBy: { id: 'asc' },
})
```

## `data` — 무엇을 쓸지 (중첩 쓰기 · 원자적 연산)


| 구분 | 키워드 | 설명 |
|---|---|---|
| 관계 중첩 쓰기 | `create` · `connect` · `connectOrCreate` · `disconnect` · `set` · `update` · `upsert` · `delete` | 부모와 자식을 **한 트랜잭션**에서 같이 처리. `create` / `update` / `upsert`에서만 사용 가능 |
| 숫자 원자적 연산 | `increment` · `decrement` · `multiply` · `divide` · `set` | 읽고-쓰기 없이 DB에서 바로 연산 → **경쟁 상태(race condition) 방지** |

```typescript
// 중첩 쓰기
await prisma.user.create({
  data: {
    email: 'a@b.com',
    posts: {
      create: [{ title: '첫 글' }],
      connect: [{ id: existingPostId }],
    },
  },
})

// 원자적 증가 (조회 후 +1 하는 것보다 안전)
await prisma.post.update({
  where: { id },
  data: { viewCount: { increment: 1 } },
})
```

---

# 헷갈리기 쉬운 포인트

> 
  - `findUnique`의 `where`에는 **유니크 필드(@id, @unique, @@unique)만** 넣을 수 있음. 일반 필드로 찾으려면 `findFirst`.
  - `create` / `update` / `upsert`는 **레코드를 반환**하지만, `createMany` / `updateMany` / `deleteMany`는 `{ count: n }`만 반환.
  - `delete` / `update`는 대상이 없으면 **에러**, `deleteMany` / `updateMany`는 `count: 0`으로 조용히 끝남.
  - `deleteMany({})`처럼 `where`를 비우면 **테이블 전체가 삭제**됨.
  - `groupBy`에서 `take` / `skip`을 쓰려면 `orderBy`가 **필수**.
  - `where`는 그룹화 **전** 필터, `having`은 그룹화 **후**(집계 결과) 필터.
  - `createMany`의 `skipDuplicates`는 일부 DB(SQLite, MongoDB 등)에서 미지원.
  - 같은 레벨에서 `select`와 `include`는 함께 쓸 수 없음.
