<!-- notion-page-id: 3a02cdd741ac809f9949c65d9737e273 -->

# URI, URL, URN

> 이걸 왜 정리하게 되었는지의 서사를 풀자면, 솔직히 말해서 URL, URI, URN이 뭔지 구분이 제대로 되지 않았다. 아직도 3개를 구분하지 못한다는 것이 부끄러워서 다시 정리하게 되었다…

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/691f90fd-6dc5-4eaa-8c76-f263b46c80de/d1ea6c4c-ee3f-45f7-bdb8-88ae8a526426/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BMEZIND%2F20260717%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260717T160343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC4PHIqO7vV7H8P1ctm4aOkOr9HfZhHloFCHHMb9WYb%2BgIgdRAwuUAIcTdC7tyzRloB9qYvS7CsC2bW5SyydAWu0Ycq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDJwdws05F5kIwFp6ISrcA%2Ber04XTtKEfmEQB5nMeGssyOF9RJiO66ggoVSyUl4ewu0bSxirF3n%2BRA4tgPOIAeJC5%2BwPiujbg74DRpkiPW21yoIRESNjTq2qbCG4WHivl9d6VKV4aSKsXYnKWRUXhBhUXCo0eXMRzAElCbK6XRJC7vEAWPSP9cwmGMzYegRiA5SP8%2Fif%2FBz3Nl%2F%2BjANOTfMHKJbQz2998a1QH4839IkdIfkzHno84%2FsQObfXgQfkNUgoUg%2FLkXhhWbWPYsBCNvcRr17dLfocmb28YDj7Iuiu2ZmLTzS5o3lxwVEy2fp%2Fc%2FaTfTRLqu5IO6iTINBPURVnkXmMeqewApYyaDRRRRLMb2FoisLjupl%2FENOCrkOtJdvQyC1pvKMUFVH3EnmGfoxQjKcefaxMsJn7QGzJlJXyHaNZVqajuuxUiisq4Gf0OIAo7sa6X0zMlflqN7vtzHIV7R%2BGTCaFWySuNBb8xTWOvplRJOm3aEfVI5dcrqFY9I7lS2%2BkthNTDwpII4oTpiSu75V3%2F9minNQuf9YsCDBLbG4LbCjAIU48U4dJZ6d2XccgD80wJAVL8cHpwZ5BkhqR9TzsYujUQPwJ4rPMiWNJs89q7ftTM6SATQy4sabkhyTF0FNGt1VP6GzjQMN%2BT6dIGOqUB1GOLa%2Fqc6vMxqvivrNiLqvw7wDdC%2BS7SJqJd3i0tRCtDZpdGgjGdLksxu3m4P2OFZDzr0lcZ7RAI%2F2Z%2BhApTGPLKjgBtLqmA8C57z91r2MbtqBUreG128ze448hQJUqDtFOh8gkZDSFlHb8KGRqo6JFYbuhC98NGZtmW%2BxGqr2xJ6SGQA1dYXhhWT4%2F97VuTITsbV1IJoBq9hjyGRarx9ic%2BjczM&X-Amz-Signature=92dfbc838a7a3cfc0217e3b1d8c3ff85468a5aa1ba0e6b32eea28cd86e85c801&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- Scheme : 통신 프로토콜 

- Host : 웹서버, 도메인 또는 IP

- Port : 웹 서버에 접속하기 위한 통로

URI, URL, URN을 검색하면 이런 그림이 아주 많이 나온다. 나는 이 그림이 URI, URL, URN을 알기 가장 적합한 그림이라고 생각된다.

### URI : 인터넷에 있는 자원을 나타내는 유일한 주소

URI는 Uniform Resource Identifier, 통합 자원 식별자의 줄임말로 자원을 나타내는 주소를 말한다.

### URL : 네트워크 상에서 자원이 어디있는 지 알려주는 규약 -> 웹페이지의 주소

URL은 Uniform Resource Locator의 줄임말로, 네트워크 상에서 웹 페이지, 이미지, 동영상등의 파일이 위치한 정보를 알려준다.

URL은 웹 상의 주소를 나타내기 때문에 효율적으로 리소스에 접근하기 위한 방법론이 생겨났는데 그 중 하나가 REST API이다.

### URN : 자원의 이름을 나타냄

URN은 Uniform Resource Name의 줄임말로, 이름으로 리소스를 특정하는 URI이다.

URN에는 리소스 접근방법과, 웹 상의 위치가 표기되지 않으며, 실제 자원을 찾기 위해서는 URN을 URL로 변환하여 이용한다.

URL과 URN의 차이점

- URL은 어떻게 리소스를 얻을 것이고 어디에서 가져와야하는지 명시하는 URI이다.

- URN은 리소스를 어떻게 접근할 것인지 명시하지 않고 경로와 리소스 자체를 특정하는 것을 목표로하는 URI이다.
