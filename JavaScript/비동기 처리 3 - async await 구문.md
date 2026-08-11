<!-- notion-page-id: 3b92cdd741ac800590bdd9f8bd645335 -->

# 비동기 처리 3 - async await 구문

Promise도 좋아졌지만 `.then().then().then()` 계속 쓰면 복잡하다.
그래서 더 쉽게 만든 문법이 **`async / await`**이다!

---

# 기본 문법

```javascript
async function hello() {
    return "안녕하세요";
}
```

실행:

```javascript
hello().then(console.log);
```

출력:

```plain text
안녕하세요
```

---

- async는 이 함수의 return값을 Promise로 자동 포장해주는 키워드이다
  - return "안녕"                 → Promise { '안녕' }
  - return 42                        → Promise { 42 }
  - return { name: "andy"} → Promise { { name: 'andy' } }

---

# `async/await`를 사용하는 이유

## Promise `.then()` 방식

```javascript
function loadData() {
  fetchData()
    .then(user => {
      return fetchOrders(user.id);
    })
    .then(orders => {
      console.log(orders);
    })
    .catch(error => {
      console.error(error);
    });
}
```

## `async / await` 방식

```javascript
async function loadData() {
  try {
    const user = await fetchData();
    const orders = await fetchOrders(user.id);
    console.log(orders);
  } catch (error) {
    console.error(error);
  }
}
```

---

# `Promise.all`로 병렬 처리하기

두 비동기 작업을 동시에(병렬로) 시작하고, 두 작업이 모두 끝날 때까지 기다린다..!

```javascript
async function getFruits() {
  // 두 Promise를 동시에 시작하고 Promise.all로 묶어서 기다림
  const [apple, banana] = await Promise.all([getApple(), getBanana()]);
  return `${apple} + ${banana}`;
}
```

---

# 에러 처리하는 법… 전에 reject 반환하는 법

`async`를 사용하면 반환값이`Promise`객체로 감싸져 반환되지만, 그럼 싹다 fulfilled(성공) 상태의 Promise로 처리된다.
그렇기 떄문에 따로 이를 Rejected(거부) 상태의 `Promise`를 반환하도록 처리해야한다.

## 1. `throw` 문 사용하기


```javascript
async function checkAge(age) {
  if (age < 20) {
    // throw를 사용하면 해당 에러 객체가 reject의 사유(reason)가 됩니다.
    throw new Error("미성년자는 접근할 수 없습니다.");
  }
  
  return "접근 허용"; // 정상 동작 시 Resolve
}
```

- `async` 함수 내부에서 `throw`를 사용해 에러를 던지면, JavaScript는 자동으로 해당 함수가 Rejected 상태의 Promise를 반환하도록 알잘딱해준다!

## 2. `return Promise.reject()` 사용하기

```javascript
async function checkAge(age) {
if (age < 20) {
return Promise.reject(new Error("미성년자는 접근할 수 없습니다."));
}

return "접근 허용";
}
```

- `Promise.reject()`를 명시적으로 `return`해 주는 방법도 있다.

```javascript
async function fetchUserData() {
  try {
    const response = await fetch('https://api.example.com/data');
    const data = await response.json();
    return data;
  } catch (error) {
    // 네트워크 에러나 응답 처리 중 발생한 에러를 여기서 잡아냄
    console.error("데이터를 가져오는 중 에러 발생:", error);
  }
}
```

---

# 에러 처리하기

```javascript
async function fetchUserData() {
  try {
    const response = await fetch('https://api.example.com/data');
    const data = await response.json();
    return data;
  } catch (error) {
    // 네트워크 에러나 응답 처리 중 발생한 에러를 여기서 잡아냄
    console.error("데이터를 가져오는 중 에러 발생:", error);
  }
}
```

- `async/await` 구문에서는 JavaScript의 표준 예외 처리 구문인 `try...catch`를 사용하여 에러를 처리한다.

`Promise.all()` 도 마찬가지로 `try...catch`를 사용하여 에러를 처리할 수 있다.

```javascript
async function fetchAllData() {
  try {
    // 세 비동기 작업을 동시에 실행
    const results = await Promise.all([
      fetchUser(),
      fetchPosts(),
      fetchComments()
    ]);
    
    // 모두 성공했을 때 실행 (results는 각 작업의 결과 배열)
    console.log("성공 데이터:", results);
  } catch (error) {
    // 하나라도 실패(Reject)하면 즉시 이곳으로 이동
    console.error("하나 이상의 요청 실패:", error.message);
  }
}
```

- `Promise.all`은 전달된 Promise 중 하나만 실패해도 나머지 작업의 결과를 기다리지 않고 즉시 catch 블록으로 이동해버린다.

- 일부만 실패해도 전체가 멈추지 않게 하려면 이또한 따로 처리를 해주어야한다… 미친 js

```javascript
async function fetchAllData() {
  // Promise.allSettled는 성공/실패 여부를 불문하고 모든 결과가 나올 때까지 기다림
  const results = await Promise.allSettled([
    fetchUser(),
    fetchPosts(),
    fetchComments()
  ]);

  results.forEach((result, index) => {
    if (result.status === 'fulfilled') {
      console.log(`${index}번 작업 성공:`, result.value);
    } else {
      console.error(`${index}번 작업 실패:`, result.reason);
    }
  });
}
```

- `Promise.allSettled()`는 여러 비동기 작업을 병렬로 실행하고, 성공·실패 여부와 상관없이 모든 작업이 끝날 때까지 기다린 후 각 작업의 결과를 담은 배열을 반환하는 함수이다.
