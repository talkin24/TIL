# Auth

- authentication(인증)
- authorization(권한)
- 장고는 이 두개를 합하여 하나로 취급 -> authentication system(인증시스템)



- 인증은 크게 2가지

  1. User

     - 보통 accounts라는 앱으로 진행

     - 절차

       1. 회원가입

          - 회원가입 페이지 / 회원가입 로직

          - Authemtication Built-in Forms 활용
          - UserCreationForm
            - 모델폼!
          - Create랑 상당히 유사

       2. 로그인

          - AuthenticationForm
            - 그냥 폼!

          - 로그인 페이지 / 로그인 로직

          - http는 연결성이 없음, 그 연결성을 만들어 주는 것이 쿠키와 세션

            - 쿠키

              - 클라이언트 로컬에 저장되는 키-값의 작은 데이터 파일
              - 아이디 자동완성, 공지 하루 안보기, 팝업 체크, 비로그인 장바구니 담기 등
              - 편의를 위하되 유출되어도 크게 상관없는 정보들

            - 세션

              - 서버에 저장(이때 session id는 쿠키의 형태로 클라이언트 로컬에 저장)
              - 사이트와 특정 브라우저 사이의 state를 유지시키는 것
              - 클라이언트가 서버에 접속하면 서버가 session id를 발급
              - 클라이언트는 session id를 쿠키에 저장
              - 장고는 특정 session id를 포함하는 쿠키를 사용하여 각 브라우저와 사이트가 연결된 세션을 알아냄. 세션정보는 장고 db의 django_session 테이블에 저장
              - 주로 로그인 상태 유지에 사용

            - **HTTP 쿠키는 상태가 있는 세션을 만들도록 해준다!**

            - 로그인 하면 db에 저장됨(sqlite3 내django_session)

            - 로그아웃 함수 사용하면 session 쿠키 삭제(db에서도 삭제)

              - 단 쿠키를 개발자도구에서 직접 지우면 db에서 삭제 안됨(유효기간이 다 지워지면 삭제될 것)

            - 로그인 사용자에 대한 접근 권한

              - `is_authenticated`

                - html 에 if문으로 적용

                  ```django
                  {% if request.user.is_authenticated %}
                  	<a href="{% url 'accounts:logout' %}">Logout</a>
                  {% else %}  
                  	<a href="{% url 'accounts:signup' %}">Signup</a>
                  <a href="{% url 'accounts:login' %}">Login</a>
                  ```

                - 단, 본질적으로 로그인이나 회원가입을 막은 건 아니다(렌더링만 바꾼 것)

              - views.py에서도 막아줘야 함

                ```python
                def signup(request):
                    if request.user.is_authenticated:
                        return redirect('articles:index')
                        ...
                        
                def login(request):
                    if request.user.is_authenticated:
                        return redirect('articles:index')
                        ...
                ```

              - 글쓰기, 수정, 삭제도 로그인 여부를 확인해야 함

                - decorator로 매우 간단하게 처리 가능
                - `from django.contrib.auth.decorators import login_required`
                - 이때 로그인 없이 권한 없는 페이지에 접근하면 아래와 같은 주소로 이동
                  - http://127.0.0.1:8000/accounts/login/?next=/articles/create/
                  - 로그인 하면 new키의 값으로 보내준다는 뜻
                  - 데코레이터 2개 사용 자체는 문제가 안되나, 특정 데코레이터들의 경우 문제가 생길 수 있음

       ```
       회원가입 User create
       로그인 session create
       로그아웃 session delete
       최원탈퇴 user delete
       ```

  2. Request



### User object

- django 인증시스템의 핵심
- User가 django 인증시스템에서 표현되는 모델
- 일반적으로 사이트와 상호작용 하는 사람들을 나타냄
- django 인증 시스템에서는 오직 하나의 User Class만 존재
- AbstractUser Class의 상속을 받음
  - AbstractUser
    - User model을 구현하는 완전한 기능을 갖춘 클래스

