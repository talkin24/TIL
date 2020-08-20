# Django Model

- django는 model을 통해 데이터에 접속하고 관리

- Model이 DB를 관리

  

### Schema

- 자료의 구조, 표현방법, 관계 등을 정의한 구조

  

### 테이블

- 필드 = 컬럼
- 행 = 레코드
- PK(Primary Key): 기본키, 각 레코드의 고윳값(id)



ORM(Object-Relational-Mapping)

![image-20200819102422581](C:\Users\cresc\AppData\Roaming\Typora\typora-user-images\image-20200819102422581.png)

- 객체지향 프로그래밍 언어를 사용하여, 호환되지 않는 유형의 시스템 간에 (Django-SQL) 데이터를 변환하는 프로그래밍 기술. 가상 DB 생성
  - 장점 : SQL을 몰라도 DB에 접근 가능, SQL의 절차적 접근이 아닌 객체 지향적 접근으로 인한 높은 생산성

- 단점: ORM만으로 완전한 서비스를 구현하기 어려운 경우가 있음

- BUT: 현대 대부분의 framework는 ORM 사용. why? **생산성**

  => DB를 객체로 활용하기 위해 ORM을 사용한다!



### 

### 핵심 Flow

```
1. models.py: 변경사항(최초작성 포함) 발생
2. makemigrations: 설계도 만들기
3. migrate: DB에 적용
```



### models.py

- 보통 모델은 class 사용
- class의 이름은 보통 어플 명의 단수형

- models 안의 Model 클래스를 상속받아 사용

- PK는 자동으로 생성

- 스키마 작성

  - `CharField(max_length=None)`
    - 길이의 제한이 있는 문자열 넣을 때 사용
    - max_length가 필수 인자
    - 필드의 최대 길이, DB와 django의 유효성 검사에서 사용
  - `TextField()`
    - 글자의 수가 많을 때 사용
  - `DateTimeField()`
    - 최초 생성 일자: `auto_now_add=True`
      - django ORM이 최초 데이터 입력시에만 현재 날짜와 시간으로 갱신
    - 최종 수정 일자: `auto_now=True`
      - django ORM이 save를 할 때마다 현재 날짜와 시간으로 갱신

  ```python
  # 각 줄이 필드
  title = models.CharField(max_length=10) # 최대 길이 10
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True) # 최초 생성시간 변하지 않음
  ```

  

### Migrations

- model에 생긴 변화를 반영하는 방법
- `makemigrations`: 새로운 마이그레이션 생성
  - 모델 활성화 전에 DB 설계도 작성
  - git의 commit과 유사, 모델의 변경 사항을 쌓아나아감
- `migrate`: table 생성
  - db.sqlite3라는 데이터베이스 파일에 테이블을 생성
  - 모델에서의 변경 사항들과 DB의 스키마가 동기화를 이룸
- `sqlmigrate`: 마이그레이션에 대한 sql 구문 확인
  - `python manage.py sqlmigrate articles(앱이름) 0001(번호)`
- `showmigrations`: migration 상태 확인
  - X표시가 migrate 되었다는 뜻
  - 모델에 문제가 생겼을 때 확인



cf) sqlite extention을 사용하면 vscode 내 explorer에서 db확인 가능



### DB API(database-abstract API)

- C(create), R(read), U(update), D(delete)

- sql 통제를 python 구문으로 하기

- Making Queries 문법

  ```
  Article.objects.all()
  Class Name / Manager/ QuerySet API
  ```

- Manager

  - query 작업이 제공되는 인터페이스
  - 기본적으로 모든 django 모델 클래스에 `objects`라는 manager 추가

- QuerySet

  - DB로부터 전달받은 객체 목록
  - 조회, 필터 정렬 등 수행
  - 이것의 객체는 0개, 1개 혹은 여러개 일 수 있음