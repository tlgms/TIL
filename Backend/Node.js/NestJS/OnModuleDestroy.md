<!-- notion-page-id: 3c22cdd741ac80c4b3cdddd576669b51 -->

# OnModuleDestroy

`OnModuleDestroy`는 NestJS 생명주기 훅(Lifecycle Hook) 중 하나로, **애플리케이션이 종료 신호(SIGTERM 등)를 받을 때 실행**됩니다. 데이터베이스 연결 해제, 타이머 정지, 외부 서버와의 연결 종료 등 자원을 정리(Cleanup)하는 코드를 작성할 때 사용합니다.

## 01.

- **인터페이스 구현**: 클래스에 `OnModuleDestroy`를 임포트하고 `onModuleDestroy()` 메서드를 작성합니다.

```typescript
import { Injectable, OnModuleDestroy } from '@nestjs/common';

@Injectable()
export class DatabaseService implements OnModuleDestroy {
  async onModuleDestroy() {
    // 앱이 꺼질 때 실행할 정리 작업
    await this.closeDatabaseConnection();
    console.log('데이터베이스 연결이 닫혔습니다.');
  }

  private async closeDatabaseConnection() {
    // 연결 해제 로직
  }
}
```

## 02.

- **종료 훅 활성화 필수**: `main.ts`에서 `app.enableShutdownHooks()`를 호출해야 정상 작동합니다.

```typescript
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  // 핵심: 애플리케이션 종료 훅 활성화 (이 설정을 해야 OnModuleDestroy가 실행됩니다)
  app.enableShutdownHooks();

  await app.listen(3000);
}
bootstrap();

```

## 03.

- **실행 순서**: `onModuleDestroy` → `beforeApplicationShutdown` → `onApplicationShutdown` 순서로 진행됩니다.
