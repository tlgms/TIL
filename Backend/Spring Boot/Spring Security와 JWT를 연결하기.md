<!-- notion-page-id: 3bb2cdd741ac8074b6e6d2666cf781d4 -->

# Spring Security와 JWT를 연결하기

## 1. JWT 검증 및 Authentication 객체 생성 로직 추가 (`JwtProvider`)

[기존 ](/p/3bb2cdd741ac80e2956acb0968312dbc)[`JwtProvider`](/p/3bb2cdd741ac80e2956acb0968312dbc)에 토큰 검증 로직과 인증 객체를 생성하는 메서드를 추가한다.

```java
import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.authority.SimpleGrantedAuthority;

import java.util.Collections;

// (기존 JwtProvider 클래스 내에 추가)

    // 1. 토큰 유효성 검증
    public boolean validateToken(String token) {
        try {
            Jwts.parser()
                    .verifyWith(key)
                    .build()
                    .parseSignedClaims(token);
            return true;
        } catch (Exception e) {
            // ExpiredJwtException, MalformedJwtException 등 예외 처리
            return false;
        }
    }

    // 2. 토큰에서 인증 정보(Authentication) 추출
    public Authentication getAuthentication(String token) {
        Claims claims = Jwts.parser()
                .verifyWith(key)
                .build()
                .parseSignedClaims(token)
                .getPayload();

        String username = claims.getSubject();
        String role = claims.get("role", String.class);

        // Security가 인식할 수 있는 Authority 객체 생성
        var authorities = Collections.singletonList(new SimpleGrantedAuthority("ROLE_" + role));

        // UserDetails 구현체 대신 간단히 UsernamePasswordAuthenticationToken 생성
        return new UsernamePasswordAuthenticationToken(username, "", authorities);
    }
```

## 2. JWT 인증 필터 구현 (`JwtAuthenticationFilter`)

요청당 한 번만 실행되는 `OncePerRequestFilter`를 상속받아 HTTP 요청 헤더에서 JWT를 추출하고 검증한다.

```java
import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.util.StringUtils;
import org.springframework.web.filter.OncePerRequestFilter;

import java.io.IOException;

public class JwtAuthenticationFilter extends OncePerRequestFilter {

    private final JwtProvider jwtProvider;

    public JwtAuthenticationFilter(JwtProvider jwtProvider) {
        this.jwtProvider = jwtProvider;
    }

    @Override
    protected void doFilterInternal(HttpServletRequest request,
                                    HttpServletResponse response,
                                    FilterChain filterChain) throws ServletException, IOException {

        // 1. Request Header에서 토큰 추출
        String token = resolveToken(request);

        // 2. 토큰 유효성 검증 후 SecurityContext에 저장
        if (StringUtils.hasText(token) && jwtProvider.validateToken(token)) {
            Authentication authentication = jwtProvider.getAuthentication(token);
            SecurityContextHolder.getContext().setAuthentication(authentication);
        }

        // 3. 다음 필터로 진행
        filterChain.doFilter(request, response);
    }

    // Header("Authorization: Bearer <TOKEN>")에서 순수 토큰만 추출
    private String resolveToken(HttpServletRequest request) {
        String bearerToken = request.getHeader("Authorization");
        if (StringUtils.hasText(bearerToken) && bearerToken.startsWith("Bearer ")) {
            return bearerToken.substring(7);
        }
        return null;
    }
}
```

## 3. Spring Security 설정 (`SecurityConfig`)

작성한 필터를 Spring Security 체인에 등록한다. JWT 환경에서는 **세션을 사용하지 않으므로 STATELESS로 설정한**다.

```java
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configurers.AbstractHttpConfigurer;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;

@Configuration
@EnableWebSecurity
public class SecurityConfig {

    private final JwtProvider jwtProvider;

    public SecurityConfig(JwtProvider jwtProvider) {
        this.jwtProvider = jwtProvider;
    }

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            // 1. CSRF, Form Login, Basic Auth 비활성화 (JWT 사용 시 불필요)
            .csrf(AbstractHttpConfigurer::disable)
            .formLogin(AbstractHttpConfigurer::disable)
            .httpBasic(AbstractHttpConfigurer::disable)

            // 2. 세션 미사용 설정 (Stateless)
            .sessionManagement(session ->
                session.sessionCreationPolicy(SessionCreationPolicy.STATELESS))

            // 3. URL별 권한 설정
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/api/auth/**").permitAll() // 로그인/회원가입은 허용
                .requestMatchers("/api/admin/**").hasRole("ADMIN") // 관리자 전용
                .anyRequest().authenticated() // 그 외 모든 요청은 인증 필요
            )

            // 4. JWT 필터를 UsernamePasswordAuthenticationFilter 이전에 배치
            .addFilterBefore(new JwtAuthenticationFilter(jwtProvider),
                            UsernamePasswordAuthenticationFilter.class);

        return http.build();
    }
}
```

## Gemini가 요약해준 작동 흐름

1. **클라이언트 요청**: `Authorization: Bearer eyJhbGci...` 헤더를 포함하여 요청 전송.

1. **`JwtAuthenticationFilter`**** 작동**:
  - Header에서 `Bearer `를 제외한 토큰 파싱.
  - `JwtProvider`로 토큰 검증.
  - 검증 성공 시 `SecurityContextHolder`에 `Authentication` 객체 저장.

1. **인증 완료**: 컨트롤러나 서비스 레이어에서 `@AuthenticationPrincipal` 또는 `SecurityContextHolder`를 통해 로그인한 사용자 정보 조회 가능.
