# Django

- 다른 framework는 MVC인데 장고만 MTV
  
  - Model, View Controller -> Model(데이터 관리), Template(인터페이스[화면]), View(중간 관리[상호 동작])
- 순서
  1. HTTP Request: 요청
  2. URLS(urls.py): URL 받아옴
  3. View(views.py)): 가장 중요 
  4. Template: 여기서 데이터 가져옴
  5. HTTP Response: 데이터 보내주기

- setting 순서
  - VScode에서 Django(가장 먼저 나오는) Extension download
  - `Ctrl`+`shift`+`p` 누르고 j.son 검색
  - `settings.json` 누르고 Django Extension에 있는 코드 2개 복붙해 넣기
- `django-admin startproject 프로젝트명`
  
  - 프로젝트 생성
- 이름에 하이픈 사용 불가, python이나 django에서 기존적으로 사용되는 이름은 사용 불가
  
- `python manage.py 명령어`
  
  - `runserver`: server 실행, server 주소 확인 가능
  
    

### 프로젝트 폴더 구성

- `__init__.py`: 특정 폴더를 패키지로 인식하게 하는 파일
- `asgi_py`: 배포할 때 쓰는 파일, 아직 안씀. 3.0version에 추가됨
- `settings.py`: 모든 세팅을 관리(중요)
- `urls.py`: 요청을 가장 먼저 받아들임(중요)
- `wsgi.py`: 배포 시 사용



### 프로젝트는 앱 여러개의 집합

- `python manage.py startapp 앱이름s`: 앱 만들기. 이름은 복수형이 좋음
- 해당 앱 폴더내
  
- `views.py`: 장고에서 가장 오래 머물고, 가장 많은 코드를 작성할 부분
  
- 프로젝트에 앱등록 해야 앱 사용 가능 -> `settting.py`

  - 순서 중요 by convention

    ```python
    INSTALLED_APPS = [
     	# 1. local apps
        'articles',
        # 2. 3rd party apps
        # 3. django apps
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]
    ```

  - django는 콤마가 마지막에 옮(trailing comma)

- 언어 변경
  
  - `settings.py`에서 `LANGUAGE_CODE`수정
  - language_code에 따라 글자 수 다르게 인식하는 문제 발생할 수 있음
- 시간 변경
  
- `settings.py`에서 `TIME_ZONE`수정
  
- 장고 import convention

  ```
  django imports style guide
  #1. standard library
  #2. 3rd party
  #3. Django
  #4. local djange 
  ```

- 공식 문서 내 검색이 구리니, 구글로 검색해서 공식문서에 접근 추천



### 중요! 앱 등록을 먼저하고 앱 생성을 하면 안됨! 항상 앱 생성 먼저!

### 앱 생성되고 등록 됐으니 이제 준비 완료!

코드 작성 순서 1. `urls.py` 2. `views.py` 3.`templates` : 데이터 흐름과 동일

위 3가지 파일은 이름이 같은게 관리하기 좋음

key와 value도 이름이 동일한 것이 관리하기 편함. 단 hypenr과 underscore는 혼용 가능
ex) `{pick: pick,}`

### 1. urls.py -> 

- `urls.py` 내에 앱과 views.py를 import

- `path('주소/', 뷰함수)  `: 특정 주소로 요청이 들어오면 해당하는 view로 연결. views.py에 작성된 뷰함수가 작동됨
  - 주소 쓸때 append slash 잊지말기

- variable routing: 변수를 받을때마다 url을 만들 순 없으니 사용
- url은 underscore보다 hypen 권장



### 2. views.py

- 뷰함수는 반드시 request를 첫인자로 받는다!

- 뷰함수의 return이 template

  - render()함수 사용

- 뷰함수 간 빈 line은 2개

- context 딕셔너리를 만들어 변수 처리

  

### 3. templates

- 자동으로 생성 안되니 앱폴더 내에 만들어 줘야함

- `templates`폴더 이름은 고정
- django에서 변수를 받을 때 `{{}}`(이중 중괄호)[django template language]



## Django Template Language(DTL)

- django template system에서 사용하는 built-in function

- 조건, 반복, 치환, 필터, 변수 등의 기능을 제공

- 프로그래밍적 로직이 목적이 아님 -> 프레젠테이션을 표현하기 위한 것

  - 프로그래밍적 로직은 view에서 하는 것

  - python처럼 if나 for를 사용할 수 있으나, 이것은 단순히 python code로 실행되는 것이 아님. 단지 문법 구조가 비슷할 뿐

    

### Syntax

- variable: `{{ }}`
  - list에서 변수 하나씩 꺼낼때 `[]`이 아닌 `.`을 이용한다
- filter: `{{ variable|filter }}` 
- tags: `{% tag %}` 
  - for, if 등..(python과 외양만 같음)
    - {% for %}{% endfor %}
    - {% if %}{% endif %}
  - `forloop.counter`: 번호 매기기
    - `counter0`: 0부터 시작
  - `{% empty %}`: if 없이 data가 비어있을 때 지정가능
- 장고에서 template system은 표현을 제어하는 도구이자 표현에 관련된 로직일뿐. 여기서는 이러한 기본목표를 넘어서는 기능을 지원해선 안됨



### URL 심화

- url.py 폴더에 경로를 전부 저장하는 건 유지 보수에 좋지 않음

  `from django.urls import path, include` `include()`를 사용해서 상세 경로를 구분 가능

- app 간 동일한 page혹은 경로를 가지고 있을 때 우선순위는 settings.py 내 app 등록 순으로 적용됨

  



### 상속

- 여타 웹사이트의 nav들은 페이지가 바뀌어도 유지된다. 이 경우 마다 코드를 새로 짜는 것이 아니고, 상속을 이용하면 된다

- `{% extentds 'base.html' %}`: 첫번째 줄

- template 내에 `{% block content %}` `{% endblock content %}`으로 구멍을 뚫어줌

- `settings.py`내 `TEMPLATES` 에서 `'DIRS'`를 수정해야 함

  ```python
  'DIRS': [BASE_DIR / 'first_project' / 'templates'],
  ```

  

### Input 받기

- html에서 `form`태그 사용

- input태그의 속성

  - type: input 방식
  - id: label과 연결
  - name: key의 name

- form의 필수속성

  - action: 어디로 보낼지
  - method: 어떤 메서드
    - GET: (default) 데이터 단순 조회 시 사용. url에 노출됨
    - POST: 데이터에 변경을 줄 때. url에 노출되지 않음

- request에 클라이언트가 요청한 데이터가 담김

  - request를 통해 변수를 받아오는 방법은 2가지
    - `request.GET['key']`: key값이 없을 때 error 발생하므로 비권장
    - `request.GET('key')`: key값이 없을 때 none 반환

  
  
  