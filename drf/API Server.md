# API Server

GUI처럼 사용자 요청에대한  응답 처리를 해주는 server



# RESTful API

### REST란

- 상태 전송 표현?
- **자원과 주소의 지정 방법**에 대한 설계 방법론
- 구성
  - 자원 URI
  - 행위 HTTP Method
  - 표현 Representations
- 중심규칙
  1. URI는 정보의 자원을 표현해야 한다.
  2. 자원에 대한 어떠한 행위는 HTTP로 표현한다.



### URI

- URL(Uniform Resource Location): 자원의 위치
- URI(Uniform Resource Location): 통합 자원 식별자; 가장 흔한 URI는 URL!
- URL 구성(계층적)
  - Scheme/Protocol; `http://`
  - Host; `localhost`
  - Port; `3000`
  - Path; `/posts/3`
  - Query
  - fragment;  브라우저에서 제공



### HTTP Method

- HTTP(Hypter Text Transfer Protocol)
  - Stateless: 상태 정보가 저장되지 않음
  - Connectless: 서버에 요청을 하고 응답한 이후에 연결 끊어짐
- Method
  - GET; 지정 리소스의 표시를 요청, 오직 데이터를 받기만 함
  - POST; 클라이언트 데이터를 서버로 보냄
  - PUT/PATCH; 서버로 보낸 데이터를 저장/ 지정 리소스의 부분만을 수정
  - DELETE; 지정 리소스를 삭제



### Representations

- 메타데이터; 데이터를 설명하는 데이터

- JSON
  - 언어 독립적인 텍스트 교환 형태 -> 쉽게 변환 가능



### 목적: 프로그래밍을 통해 요청에 <u>RESTful한 방식</u>으로 <u>JSON을 응답</u>하는 서버를 만들자!



### Django REST Framework(DRF)

- Response: JSON(DRF), HTML(Django )
- Model: ModelSerializer(DRF), ModelForm(Django)



