<!-- notion-page-id: 3b92cdd741ac8096a1f3d104f336a9ab -->

# 비동기 처리 2 - Promise 객체

Promise 객체는 비동기 작업 결과를 약속(Promise)으로 관리하는 객체이다.

---

## 상태 3가지

Promise 객체에는 3가지 상태가 있다.


| 상태 | 의미 |
|---|---|
| pending | 대기중 |
| fulfilled | 성공 |
| rejected | 실패 |

---

## 기본 구조

```javascript
const promise = new Promise((resolve,reject) => {
    resolve("성공");
});
```

[pending] ──성공──▶ [fulfilled]    → .then() 실행
          └────실패──▶ [rejected]   → .catch() 실행

- resolve() → 성공

- reject() → 실패

---

# 성공 예시

```javascript
const work = new Promise((resolve,reject) => {
		resolve("작업 완료");
});

work.then(result => {
    console.log(result);
});
```

출력:

```plain text
작업 완료
```

# 실패 처리 예시

```javascript
const work = newPromise((resolve,reject) => {
    reject("오류 발생");
});

work
.then(result => console.log(result))
.catch(error => console.log(error));
```

출력:

```plain text
오류 발생
```

---

## Promise.all()

Promise.all()으로 한 번에 처리도 가능하다!

```plain text
Promise.all([
Promise.resolve("A"),
Promise.resolve("B"),
Promise.resolve("C")
]).then(result =>console.log(result));
```

출력:

```plain text
["A", "B", "C"]
```

---

## 프로미스 체이닝(`then`이 이어질 때)에서의 `result`

```javascript
new Promise((resolve) => resolve(10))
  .then((result) => {
    console.log(result); // 10 (초기 resolve 값)
    return result * 2;   // 20을 반환
  })
  .then((result) => {
    console.log(result); // 20 (이전 .then이 return한 값)
    return result + 5;   // 25를 반환
  })
  .then((result) => {
    console.log(result); // 25
  });
```

- 첫 번째 .then()의 result: `new Promise` 안에서 `resolve(값)`으로 넘겨준 값

- 이후 이어지는 .then()의 result: 바로 이전 `.then()`의 콜백 함수가 `return`한 값
