<!-- notion-page-id: 3bb2cdd741ac80e2956acb0968312dbc -->

# JWT 발급 (순수 발급만)

## 1. 의존성(Dependency) 추가

`build.gradle`에 JJWT 라이브러리를 추가한다.

```groovy
dependencies {
    // JJWT
    implementation 'io.jsonwebtoken:jjwt-api:0.12.5'
    runtimeOnly 'io.jsonwebtoken:jjwt-impl:0.12.5'
    runtimeOnly 'io.jsonwebtoken:jjwt-jackson:0.12.5'
}
```

## 2. 설정 파일(`application.yml`) 구성

토큰 서명에 사용할 **비밀키**와 **유효시간**을 설정한다. Secret Key는 암호화 알고리즘(HS256) 기준 최소 256비트(32자) 이상이어야 한다.

```yaml
jwt:
  secret: your-very-long-and-secure-secret-key-must-be-at-least-32-bytes
  expiration-ms: 3600000 # 1시간 (밀리초 단위)
```

## 3. JWT Provider (발급 클래스)

토큰을 생성하고 서명하는 로직을 담당하는 컴포넌트를 작성합니다.

```java
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.security.Keys;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

import javax.crypto.SecretKey;
import java.nio.charset.StandardCharsets;
import java.util.Date;

@Component
public class JwtProvider {

    private final SecretKey key;
    private final long expirationMs;

    public JwtProvider(
            @Value("${jwt.secret}") String secret,
            @Value("${jwt.expiration-ms}") long expirationMs
    ) {
        // String 키를 HMAC-SHA 서명용 Key 객체로 변환
        this.key = Keys.hmacShaKeyFor(secret.getBytes(StandardCharsets.UTF_8));
        this.expirationMs = expirationMs;
    }

    // JWT 토큰 발급
    public String createToken(String username, String role) {
        Date now = new Date();
        Date validity = new Date(now.getTime() + expirationMs);

        return Jwts.builder()
                .subject(username)                 // 토큰 주인 (식별자)
                .claim("role", role)              // 추가 클레임 (권한 정보 등)
                .issuedAt(now)                    // 발급 시간
                .expiration(validity)             // 만료 시간
                .signWith(key)                    // 비밀키로 서명 (알고리즘 자동 선택)
                .compact();
    }
}
```

## 4. 토큰 발급 Controller 예제

로그인 요청 시 인증을 거친 뒤, JWT를 발급하여 응답하는 예시입니다.

```java
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
@RequestMapping("/api/auth")
public class AuthController {

    private final JwtProvider jwtProvider;

    public AuthController(JwtProvider jwtProvider) {
        this.jwtProvider = jwtProvider;
    }

    @PostMapping("/login")
    public ResponseEntity<Map<String, String>> login(@RequestBody LoginRequest request) {
        // 1. 사용자 인증 로직 수행 (DB 검증 등)
        // if (!authService.authenticate(request)) { ... }

        // 2. 인증 성공 시 토큰 발급
        String token = jwtProvider.createToken(request.getUsername(), "USER");

        // 3. 클라이언트에 토큰 반환
        return ResponseEntity.ok(Map.of("accessToken", token));
    }
}
```

발급된 토큰은 클라이언트(React, 앱 등)가 저장해 두었다가, 이후 요청 시 Authorization: Bearer 헤더에 담아 보낼 수 있다!
