<!-- notion-page-id: 3ba2cdd741ac801bb082cceb2cb2d28e -->

# TypeORM

# 01.

터미널에서 다음 명령어를 입력해 설치한다.

```bash
# install TypeORM
npm i typeorm

# 만약 nest.js에서 typeorm을 사용하기를 원한다면, 이 패키지도 함께 설치해 주어야 합니다.
npm i @nestjs/typeorm

# TypeORM과 MySQL을 연동하기 위해서 mysql2 엔진을 설치해줍니다.
# 그냥 mysql을 설치하면 안됩니다. mysql2로 설치해주세요.
npm i mysql2
```

따로따로 설치하기 귀찮다면, 아래와 같이 입력해도 됨

```bash
npm i typeorm @nestjs/typeorm mysql2
```

# 02.

루트폴더에 `data-source.ts` 파일을 생성한다

```javascript
// data-source.ts

import * as path from 'path';
import { DataSource } from 'typeorm';

export const dataSource = new DataSource({
  type: 'mysql',  // 어떤 DB를 사용할 것인지
  host: 'localhost',  // 우리는 본인 컴퓨터에 깔린 mysql을 사용할 예정이니, localhost로 해줍니다.
  port: 3306,  // MySQL의 기본 포트는 3306 입니다.
  database: 'study',
  username: 'root', // MySQL 설치시 설정한 유저네임을 입력하면 됩니다,
  password: '0000', // MySQL 설치시 설정한 비밀번호를 입력하면 뒵니다.,
  entities: [  // entity는 DB의 테이블을 지칭합니다. 따라서 어떤 테이블이 사용되는지. 테이블에 대한 정보를 가져오는 것.
    path.join(__dirname, 'src/entities/**/*.entity.ts'),
    path.join(__dirname, 'dist/entities/**/*.entity.js'),
  ],
  synchronize: false, // 이건 무조건 false로 해둡시다. 
  logging: true,  // typeorm 쿼리가 실행될 때, 터미널에 MySQL쿼리가 어떻게 짜여졌는지 보여줍니다.
});
```

- `import path from 'path';`가 아닌 `import * as path from 'path';`로 설정해줍시다. import에서 문제가 터지면 대부분 이 문제일 가능성이 큽니다. 

- 엔티티 생성은 이따 설명함. [엔티티 설계](/p/3ba2cdd741ac801bb082cceb2cb2d28e#3ba2cdd741ac80ac8d8bed23afb39378)

# 03.

Package.json에 schema관련 scripts추가

```json
// "schema:sync": "ts-node ./node_modules/typeorm/cli.js schema:sync -d [dataSource파일 위치]"

"schema:drop": "ts-node ./node_modules/typeorm/cli.js schema:drop -d ./data-source.ts",
"schema:sync": "ts-node ./node_modules/typeorm/cli.js schema:sync -d ./data-source.ts",
```

- schema:sync 명령은 DB에 entity파일과 동일한 테이블들을 생성해주는 명령어입니다. (정확히 생성은 아니고 수정... 느낌 이긴합니다)

- schema:drop 명령은 DB에 테이블을 모두 삭제하는 명령어입니다. 테이블을 수정할 일이 생기면, 삭제를 하고 schema:sync를 하는게 에러가 잘 안나기 때문입니다.

- 터미널에서 npm run schema:sync 와 같이 명령어를 치면 실행됩니다.

# 04.

```javascript
// app.module.ts
import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import * as path from 'path';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { UserModule } from './res/user/user.module';

@Module({
  imports: [
    TypeOrmModule.forRootAsync({
      useFactory: () => ({
        retryAttempts: 10, // 연결에 실패했을 경우, 연결 재시도 횟수를 의미합니다.
        type: 'mysql', // 어떤 DB를 사용할 것인지
        host: 'localhost', // 우리는 본인 컴퓨터에 설치된 DB를 사용할 것이디 localhost로 설정
        port: 3306,  // MySQL의 기본 포트는 3306 입니다.
        database: 'study',  // 위에서 만든 study 데이터베이스로 설정
        username: 'root',  // 설정한 username입력, 기본은 root
        password: '0000', // 설정한 password입력
        entities: [
          path.join(__dirname, '/entities/**/*.entity.{js, ts}'),
        ],
        synchronize: false, // 무조건 false로 해두세요.
        logging: true,  // typeorm 쿼리 실행시, MySQL의 쿼리문을 터미널에 보여줍니다.
        timezone: 'local',
      }),
    }),
    UserModule,
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
```

- NestJS프로젝트와 TypeORM, DB를 연동하기 위해서는 **app.module.ts** 파일에 해당 정보를 넣어주어야 합니다.

# 05.

TypeORM 엔티티 설계

---

## **엔티티 및 컬럼 데코레이터**

## **@Entity(name?, options?)**

클래스를 DB 테이블과 매핑합니다.

## **@Column(options)**

일반 컬럼을 정의하며, 다양한 데이터 형식을 지정하는 옵션을 지원합니다.

- **`type`**: `varchar`, `int`, `text`, `boolean` 등 DB 데이터 타입을 지정합니다.

- **`nullable`**: `true`로 설정하면 `NULL` 값을 허용합니다. (기본값 `false`)

- **`default`**: 기본값을 지정합니다.

- **`unique`**: `true`로 설정하면 유니크 제약조건이 추가됩니다.

## **@PrimaryGeneratedColumn(strategy)**

자동 생성되는 기본 키(PK)입니다.

- **`increment`**: 1부터 시작해 자동으로 증가하는 정수형 PK (기본값)

- **`uuid`**: 중복 확률이 없는 고유 문자열(UUID)을 PK로 사용

---

## **관계(Relation) 데코레이터**

## **@OneToOne / @JoinColumn (1:1 관계)**

- **`@OneToOne`**: 두 엔티티가 서로 고유하게 연결됩니다. (예: 사용자 1명 - 프로필 1개)

- **`@JoinColumn`**: 외래 키(FK) 컬럼을 실제로 소유하는 엔티티 쪽에 **반드시** 작성해야 합니다.

## **@ManyToOne / @OneToMany (N:1 / 1:N 관계)**

- **`@ManyToOne`**: 자식 엔티티에 작성하며, DB에 외래 키 컬럼이 생성됩니다.

- **`@OneToMany`**: 부모 엔티티에 작성하며, 반대편 매핑 정보를 명시합니다. (`@JoinColumn`을 쓰지 않음)

- **`cascade`**: `true` 설정 시, 부모 엔티티를 저장/삭제할 때 연관된 자식 엔티티도 함께 저장/삭제됩니다

---

## Gemini산 예제

## **📂 profile.entity.ts (1:1 관계의 대상)**

```typescript
import {Entity,PrimaryGeneratedColumn,Column }from'typeorm';

@Entity('profiles')exportclassProfile {
  @PrimaryGeneratedColumn()id:number;

  @Column({type:'varchar',nullable:true })bio:string;

  @Column({type:'varchar',nullable:true })avatarUrl:string;
}
```

## **📂 post.entity.ts (N:1 관계의 자식)**

```typescript
import {Entity,PrimaryGeneratedColumn,Column,ManyToOne,CreateDateColumn }from'typeorm';import {User }from'./user.entity';

@Entity('posts')exportclassPost {
  @PrimaryGeneratedColumn('uuid')// UUID 형식의 PK 생성id:string;

  @Column({type:'varchar',length:150 })// 최대 길이 150 자 제한title:string;

  @Column({type:'text' })content:string;

  @CreateDateColumn()// 게시글 작성일 자동 기록createdAt: Date;// N:1 관계 설정 (게시글은 한 명의 작성자에게 속함)
  @ManyToOne(() => User, (user) => user.posts, {onDelete:'CASCADE' })user: User;
}
```

## **📂 user.entity.ts (메인 엔티티: 1:1 및 1:N 관계 포함)**

```typescript
import {Entity,PrimaryGeneratedColumn,Column,CreateDateColumn,UpdateDateColumn,DeleteDateColumn,OneToOne,JoinColumn,OneToMany,BeforeInsert
}from'typeorm';import {Profile }from'./profile.entity';import {Post }from'./post.entity';

@Entity('users')exportclassUser {
  @PrimaryGeneratedColumn()id:number;

  @Column({type:'varchar',unique:true })// 중복 이메일 가입 방지email:string;

  @Column({type:'varchar',select:false })// 보안을 위해 조회(Find) 시 기본 제외password:string;

  @Column({type:'int',default:20 })// 기본값 20 설정age:number;// 공통 라이프사이클 컬럼
  @CreateDateColumn()createdAt: Date;

  @UpdateDateColumn()updatedAt: Date;

  @DeleteDateColumn()// Soft Delete용 컬럼 (데이터를 실제로 지우지 않고 삭제일만 기록)deletedAt: Date;// 1:1 관계 설정 (회원은 하나의 프로필을 가짐)// FK 컬럼(profileId)을 user 테이블에 생성하므로 @JoinColumn을 붙입니다.
  @OneToOne(() => Profile, {cascade:true })
  @JoinColumn()profile: Profile;// 1:N 관계 설정 (회원은 여러 개의 게시글을 작성할 수 있음)
  @OneToMany(() => Post, (post) => post.user)posts: Post[];// 라이프사이클 이벤트: DB에 저장되기 직전에 실행
  @BeforeInsert()toLowerCaseEmail() {this.email =this.email.toLowerCase();// 저장 전 이메일을 소문자로 강제 변환
  }
}
```

- `createdAt`, `updatedAt`은 개발자가 직접 `new Date()`를 넣지 않아도 TypeORM이 자동으로 시간을 관리해 주므로 편하게 로깅할 수 있습니다.
