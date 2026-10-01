<!-- notion-page-id: 3ec2cdd741ac8094b651e94b23a52f5d -->

# Guard

Guard는 **요청이 라우트 핸들러까지 가도 되는지 결정하는 클래스
**Spring으로 비유하면 `HandlerInterceptor.preHandle()`이나 Spring Security의 인가 단계(`@PreAuthorize`)와 비슷한 역할입니다. 
차이점은 Guard가 `ExecutionContext`를 받기 때문에 **어떤 핸들러가 실행될지 알고 있다**는 점입니다. 그래서 핸들러에 붙은 메타데이터(예: 필요한 권한)를 읽고 판단할 수 있습니다.

## 실행 순서

```plain text
Middleware → Guard → Interceptor(before) → Pipe → Handler → Interceptor(after) → (예외 시) Exception Filter
```

## 기본 구조

`CanActivate` 인터페이스를 구현하고, `boolean`, `Promise<boolean>`, `Observable<boolean>` 중 하나를 반환합니다.

```typescript
import { CanActivate, ExecutionContext, Injectable, UnauthorizedException } from '@nestjs/common';

@Injectable()
export class AuthGuard implements CanActivate {
  constructor(private readonly jwtService: JwtService) {}

  async canActivate(context: ExecutionContext): Promise<boolean> {
    const request = context.switchToHttp().getRequest();
    const token = request.headers.authorization?.replace('Bearer ', '');
    if (!token) throw new UnauthorizedException();

    try {
      request.user = await this.jwtService.verifyAsync(token); // 이후 핸들러에서 사용
      return true;
    } catch {
      throw new UnauthorizedException();
    }
  }
}
```

반환값에 따라 동작이 달라집니다.

- `true`를 반환하면 요청이 통과합니다.

- `false`를 반환하면 자동으로 `ForbiddenException`(403)이 발생합니다.

- 401 같은 다른 응답을 원하면 위 코드처럼 직접 예외를 던지면 됩니다.

## 메타데이터 Reflector

커스텀 데코레이터로 필요한 역할을 핸들러에 붙이고, Guard에서 `Reflector`로 읽는 패턴이 가장 흔합니다.

```typescript
// roles.decorator.ts
export const Roles = Reflector.createDecorator<string[]>();

// roles.guard.ts
@Injectable()
export class RolesGuard implements CanActivate {
  constructor(private reflector: Reflector) {}

  canActivate(context: ExecutionContext): boolean {
    const roles = this.reflector.getAllAndOverride(Roles, [
      context.getHandler(),  // 메서드 레벨
      context.getClass(),    // 컨트롤러 레벨
    ]);
    if (!roles) return true;

    const { user } = context.switchToHttp().getRequest();
    return roles.some((role) => user?.roles?.includes(role));
  }
}

// controller
@Get('admin')
@Roles(['admin'])
getAdminData() { ... }
```

`getAllAndOverride`는 메서드에 설정한 값을 우선하고, 없으면 클래스에 설정한 값을 사용합니다.

## 적용 범위

```typescript
// 1. 메서드 / 컨트롤러 단위
@UseGuards(AuthGuard, RolesGuard)
@Controller('users')
export class UsersController {}

// 2. 전역 (DI 불가)
app.useGlobalGuards(new AuthGuard());

// 3. 전역 + DI 가능 (권장)
@Module({
  providers: [{ provide: APP_GUARD, useClass: AuthGuard }],
})
export class AppModule {}
```

전역 Guard에서 `JwtService`나 `Reflector` 같은 의존성이 필요하면 `APP_GUARD` 방식을 써야 합니다. 여러 Guard를 나열하면 순서대로 실행되고, 하나라도 실패하면 그 자리에서 중단됩니다.

전역 인증을 걸고 일부 라우트만 제외하고 싶을 때는 `@Public()` 같은 메타데이터 데코레이터를 만듭니다. 그리고 Guard 안에서 그 값이 있으면 `true`를 반환하게 합니다.

## Passport와 함께 쓰기

실무에서는 `@nestjs/passport`의 `AuthGuard('jwt')`를 많이 씁니다. Strategy 클래스에 검증 로직을 두고, Guard는 그 Strategy를 실행하는 역할만 합니다.

```typescript
@UseGuards(AuthGuard('jwt'))
@Get('me')
getMe(@Req() req) { return req.user; }
```
