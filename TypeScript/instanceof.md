<!-- notion-page-id: 3ec2cdd741ac80738bf7e07ccbdd7348 -->

# instanceof

특정 클래스의 인스턴스인지 확인하는 예약어

## 기본 사용법과 타입 좁히기 (Type Narrowing)

조건문에서 instanceof를 사용하면 타입스크립트 컴파일러가 해당 블록 내부에서 변수의 타입을 클래스 타입으로 자동 추론합니다.

```typescript
class Dog {
  bark() {
    console.log("멍멍!");
  }
}

class Cat {
  meow() {
    console.log("야옹~");
  }
}

function handlePet(pet: Dog | Cat) {
  if (pet instanceof Dog) {
    pet.bark(); // 여기서 pet은 Dog 타입으로 자동 확정됨
  } else {
    pet.meow(); // 여기서 pet은 Cat 타입으로 자동 확정됨
  }
}
```
