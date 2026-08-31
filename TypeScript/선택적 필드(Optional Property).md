<!-- notion-page-id: 3cc2cdd741ac809face5ce07dcf55b2a -->

# 선택적 필드(Optional Property)

이 문법을 사용하면 해당 필드가 **필수가 아닌 선택 사항**임을 컴파일러에게 알린다.
쉽게 설명하자면 값이 할당되지 않아도 컴파일되게 설정하는 방법입니다.

---

```typescript
classUser {name:string;// 필수 필드age?:number;// 선택적 필드 (? 사용)constructor(name:string) {this.name = name;// age는 선택 사항이므로 생성자에서 초기화하지 않아도 컴파일 에러가 나지 않습니다.
  }
}// 1. age를 생략하고 객체 생성 (가능)constuser1 =new User("홍길동");// 2. age를 포함하여 객체 생성 (가능)constuser2 =new User("이순신");
user2.age =30;
```

- `age?: number`는 실제 컴파일 시 `number | undefined` 타입으로 해석된다. 값을 넣지 않으면 기본적으로 `undefined`가 들어간다.

- TypeScript는 클래스 필드를 선언하면 생성자(`constructor`)에서 반드시 초기화하도록 강제한다. 하지만 `?`를 붙이면 초기화를 생략해도 에러가 발생하지 않음.
