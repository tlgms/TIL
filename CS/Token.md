<!-- notion-page-id: 3a02cdd741ac80caba46fe554206ee81 -->

# Token

토큰은 세션과 쿠키보다 비교적 보안이 좋다. 하지만 중간에 토큰을 탈취한다면 보안에 큰 취약점이 생긴다. 그러므로 토큰은 유효기간을 설정한다. 

JWT 토큰

JSON Web Token의 약자로, Header.Payload.Signature으로 구성되어 있다.

**토큰의 구조**

Header.Payload.Signature

- Header(헤더)
  typ과 alg 두가지 정보로 구성, alg는 헤더를 암호화하는 것이 아닌 signature를 해싱하기 위한 알고리즘을 지정하는 것이다.
  - typ : 토큰의 타입을 지정
    ex)  JWT
  - alg : 알고리즘 방식을 지정, 서명및 토큰 검증에 사용
    ex)  HS256(SHA256) 또는 RSA

- Payload(페이로드)
  토큰에서 사용할 정보의 조각인 클레임이 담겨 있음
  - claim
    - 등록된 클레임 : 토큰의 정보를 표현하기 위해 이미 만들어진 종류의 데이터
      iss : 토큰 발급자		sub : 토큰 제목		aud : 토큰 대상자		jti : 토큰 식별자(중복 방지, accass토큰등에 사용)
      exp : 토큰 만료 시간		nbf : 토큰 활성날짜		iat : 토큰 발급 시간
    - 공개 클레임 : 사용자 정의 클레임으로 공개용 정보를 위해 사용, 충돌방지를 위해 URI포맷 사용
    - 비공개 클레임 : 사용자 정의 클레임으로 서버와 클라이언트 사이에 임의로 지정한 정보 저장

- Signature(서명)
  토큰을 인코딩하거나 유효성을 검증할때 사용한다. 헤더와 페이로드를 각각 BASE64로 인코딩하고 인코딩한 값을 비밀키를 이용해 헤더에서 정의한 알고리즘으로 해싱하고 이를 다시  BASE64로 인코딩하여 생성한다.

**토큰 생성**

```plain text
Jwts.builder()
  .setHeaderParam(Header.TYPE, Header.JWT_TYPE) // 헤더의 타입을 지정
  .setExpiration(new Date(System.currentTimeMillis() + AccessToken * 1000)) // exp
  .setIssuedAt(new Date()) // iat
  .setSubject(authentication.getName()) // sub
  .signWith(SignatureAlgorithm.HS256, SecretKey) // 해싱 알고리즘과 시크릿키를 설정할 수 있다.
  .compact();
```

**토큰의 단점**

- JWT는 상태를 저장하지 않기 떄문에 한번 만들어지면 제어가 불가능하다. 즉, 임의로 토큰을 삭제 하지 못하므로 해커에게 토큰을 빼앗기면 토큰을 무효화 할 방법이 없다. 그러므로 토큰의 만료시간을 넣어줘야 한다.

→ 토큰은 Access Token과 Refresh Token이 있다. Access Token은 유효시간이 설정되어 있는 토큰으로 설정되어 있던 시간이 다 되면 자동으로 소멸된다.

- 페이로드 자체는 암호화 된 것이 아니라 인코딩이 된 것이므로 중간에 탈취당하면 데이터를 볼 수 있으므로 중요한 데이터는 넣지 않는다.

**인증, 인가**

Authentication(인증) ---인증후---> Authoriztion(인가)

- 인증 : 해당 사용자가 본인이 맞는지 확인하는 절차

- 인가 : 인증된 사용자가 요청된 자원에 접근가능한지 결정하는 절차
