<!-- notion-page-id: 3ba2cdd741ac80a691dade7ed6790836 -->

# Prisma

Prisma는 NestJS에서 데이터베이스와 상호작용하기 위한 ORM 도구중 하나이다.

# **Prisma 설치**

```bash
npm install prisma --save-dev
```

- 설치가 완료되면, 아래 명령어를 실행해 사용가능한 prisma 명령어를 확인할 수 있다.

```bash
npx prisma
```

- prisma 기본 설정 및 prisma 폴더 생성
  - 아래 명령어를 실행하면 프로젝트 내에 프리즈마라는 새 폴더가 생성되고, 이 폴더 안에는 `schema.prisma` 라는 파일이 자동으로 생성된다.
  - 데이터베이스는 기본적으로 postgresql 를 지원한다.

```bash
npx prisma init
```

`prisma/schema.prisma`

```javascript
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}
```

- `.env` 파일도 생성되는데, 그 파일 안에 `DATABASE_URL`가 정의되어 있다.
  - DB 정보에 맞게 수정해준다.

```javascript
DATABASE_URL="postgresql://[USERNAME]:[PASSWORD]@localhost:5432/[DATABASE]"
```

# Prisma Client

- Prisma Client는 개발자가 복잡한 SQL 쿼리를 작성하는 대신 간결하고 직관적인 API를 사용하여 데이터베이스 작업을 수행할 수 있게 해주는 도구이다.
  - 이는 코드의 가독성을 높이고, 타입 안정성을 통해 오류를 줄이며, 특히 타입스크립트와 잘 호환되어 강력한 타입 체킹과 자동완성 기능을 제공한다.

- Prisma Client 가 설정되면 스키마에 정의된 모델에 접근할 수 있다.
  - 이 모델들을 사용하여 데이터 생성, 조회, 업데이트, 삭제 등의 작업을 수행할 수 있다.

- Prisma Client 설치

```javascript
npm install @prisma/client
```

## PrismaService 생성

- NestJS에서 PrismaClient 를 사용하여 DB에 연결하기 위해 전역으로 사용할 Prisma Service를 생성한다.

`src/prisma/prisma.module.ts`

```javascript
import { Global, Module } from '@nestjs/common';
import { PrismaService } from './prisma.service';

@Global()
@Module({
  providers: [PrismaService],
  exports: [PrismaService],
})
export class PrismaModule {}
```

`src/prisma/prisma.service.ts`

```javascript
import { Injectable, OnModuleInit } from '@nestjs/common';
import { PrismaClient } from '@prisma/client';

@Injectable()
export class PrismaService extends PrismaClient implements OnModuleInit {
  async onModuleInit() {
    await this.$connect();
  }
}
```

- 정의한 PrismaService 는 API 생성에 필요한 Service 정의 시 다음과 같이 사용하여 DB에 접근할 수 있다.

`user.service.ts`

```javascript
import { Injectable } from '@nestjs/common';
import { PrismaService } from 'src/prisma/prisma.service';

@Injectable()
export class UserService {
  constructor(private readonly prismaService: PrismaService) {}

  async findAll() {
    return this.prismaService.user.findMany();  // DB의 USER 테이블에 접근
  }
}
```

# 데이터 모델 정의

```javascript
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model User {
  id        Int      @id @default(autoincrement())
  createdAt DateTime @default(now())
  email     String   @unique
  name      String?
}
```

- 데이터 모델 DB 에 적용

```javascript
npx prisma db push
```
