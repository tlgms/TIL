<!-- notion-page-id: 3c02cdd741ac8030b823caed9f066fb2 -->

# ConfigService

NestJS(TypeScript)에서 ConfigService는 `.env` 파일이나 시스템 환경 변수를 관리하고 애플리케이션 전역에서 해당 값에 안전하게 접근할 수 있도록 제공되는 서비스 클래스이다.


```typescript
import { Injectable } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';

@Injectable()
export class UserService {
  // ConfigService 주입
  constructor(private configService: ConfigService) {}

  getDatabasePort(): number {
    // 'PORT' 환경 변수를 number 타입으로 가져오며, 없을 경우 3000을 기본값으로 사용
    return this.configService.get<number>('PORT', 3000);
  }
}
```
