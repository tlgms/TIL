<!-- notion-page-id: 3a02cdd741ac80cc8ea5c9dbaac6b388 -->

# HTTP

[https://velog.io/@entrydsm/내가-알던-HTTP가-맞냐](https://velog.io/@entrydsm/내가-알던-HTTP가-맞냐)

서버와 클라이언트 간의 통신을 하기 위한 통신 규약
  통신 방법
  - TCP : 연결 통신을 한다. 1 : 1 통신
  - UDP : 비연결 통신을 한다. 신뢰도가 떨어지고 흐름제어와 혼잡 제어가 힘들다.

**HTTP 메소드**
| 메소드 | 설명 |
|---|---|
| PUT | 클라이언트가 서버의 리소스를 수정 할 때 사용 ( CRUD에서 Update : 전체 수정 ) |
| POST | 클라이언트가 서버의 리소스를 새로 만들 때 사용 ( CRUD 에서 Create ) |
| GET | 클라이언트가 서버에 리소스를 요청할 때 사용 ( CRUD 에서 Read ) |
| DELETE | 클라이언트가 서버의 리소스를 삭제 할 때 사용 ( CRUD에서 Delete ) |

### <Http 상태코드 정리>

[https://hocheon.tistory.com/68](https://hocheon.tistory.com/68)

언제 어떤 상태코드를 주어야 할까?

[https://tecoble.techcourse.co.kr/post/2020-08-31-http-status-code/](https://tecoble.techcourse.co.kr/post/2020-08-31-http-status-code/)

**상태코드**
| 상태코드 | 설명 | 태그 |
|---|---|---|
| 500 | 서버 오류 | Internal Server Error |
|  |  |  |
| 429 | 너무 많은 요청을 보냄 | Too Many Requests |
| 409 | 서버와 요청이 충돌함 | Conflict |
| 405 | 클라이언트가 보낸 메소드가 해당 URI에서 지원하지 않음 | Method Not Allowed |
| 404 | 요청한 URI을 찾을 수 없음 | Not Found |
| 403 | 클라이언트가 요청한 컨텐츠에 대해 접근할 권리가 없음 | Forbidden |
| 401 | 요청을 위해 권한 인증이 필요함 | Unauthorized |
| 400 | 잘못된 요청 | Bad Request |
|  |  |  |
| 204 | 서버가 요청을 성공적으로 처리했지만 제공할 컨텐츠는 없음 | No Content |
| 201 | 성공적으로 생성에 대한 요청을 받았으며 자원이 생성되었음 | Created |
| 200 | 요청을 정상적으로 처리함 | OK |

401과 403의 차이)

401은 허가되지 않은 것을 의미하고, 403은 금지됨을 의미한다. 401은 인증이 되지 않은 사용자일떄, 403은 인증은 되었으나 권한이 없는 사용자일때 사용한다.

[https://mangkyu.tistory.com/146](https://mangkyu.tistory.com/146)

**<http의 특성>**
| 특성 | 단점 | 장점 |
|---|---|---|
| 비연결성 (Connectionless)  비상태성 (Stateless) | 같은 사용자가 요청을 여러번 하더라도 매번 새로운 사용자로 인식한다.  즉, 로그인 상태가 유지되지 않는다. | 서버의 자원을 크게 절약할 수 있다. |

모든 사용자의 요청마다 연결과 해제의 과정을 거치면서 연결상태를 유지하지 않고 연결 해제 후에도 상태 정보를 저장하지 않음
