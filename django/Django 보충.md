# Django 보충

- CRUD는 수업자료를 안보고도 짤 수 있을 정도로 연습해야 함



## 가상환경

- 파이썬 인터프리터, 라이브러리 및 스크립트가 "시스템 파이썬"(글로벌 환경)에 설치된 모든 라이브러리와 격리 되어 있는 파이썬 환경
- 각 가상환경은 고유한 파이썬 환경을 가지며 독립적으로 설치된 패키지 집합을 가짐
- 대표 가상환경 지원 시스템
  - venv, virtualenv, conda, pyenv

- 왜 사용할까?

  - 프로젝트 마다 다른 버전의 라이브러리가 필요할 수 있음. 그러나 파이썬에서는 한 라이브러리에 대해 하나의 버전만 설치 가능
  - 라이브러리 간 서로 의존성이 다르기 때문에 충돌 가능성 방지

- 가상 환경 만들기

  ```shell
  $python -m venv 가상환경이름(보통 venv)
  ```

  - 프로젝트와 동일한 위치에 가상환경을 만들기 때문에 이름을 항상 venv로 만들어도 괜찮음

- 활성화

  ```shell
  #Windows(git bash): 
  source 가상환경이름/Scripts/activate
  #macOS: 
  source 가상환경이름/bin/activate
  >>(가상환경이름)
  ```

- 비활성화

  `deativate`

  cf) 파이썬 위치 확인

  ```shell
  $which python
  ```

- VS code에서 사용
  - ctrl(command) + shift + p
  - select interpreter에서 가상환경 선택
  - bash open

- 가상환경과 동일한 폴더에 프로젝트 만들기

  ```
  $django-admin startproject 프로젝트이름 .
  ```

- db, 가상환경, (.vscode)는 github에 올리지 않는다

  - add 전에 ignore 설정해야 함

  - db는 그렇다 치고 가상환경은 어떻게 동기화?

  - gitignore.io

    ```
    OS, IDE, Language, Framework, virtual environment
    ```

    ex) windows(내 os), maxOS(팀원 os), VisualstudioCode(IDE), Python(언어), Django(framework), venv(가상환경) 입력 후 생성

### 패키지 관리(git)

- `pip freeze` : 현재 환경에 설치된 패키지를 requirements format으로 출력. 각 패키지들은 대소문자 구분하지 않는 순서

- ```shell
  $ pip freeze > requirements.txt # 패키지 목록 저장
  ```

- ```shell
  $ pip install -r requirements.txt # 패키지 한번에 설치
  ```



### fixtures

- db도 git에 안올림. 그러나 초기 데이터는 필요
- fixtures는 Django가 데이터베이스로 import 할 수 있는 데이터 모음
- `dumpdata`: 특정 앱에 관련된 db의 모든 데이터를 출력
- `loaddata`: dumpdata를 통해 만들어진 fixtures 파일을 db로 import
- **fixtures 파일은 반드시 app디렉토리 안에 fixtures디렉토리에 위치**

- ```shell
  $ python manage.py dumpdata app_name.ModelName [--options] > fixturesname.json # dumpdata
  $ python manage.py dumpdata articles.Article --indent4 > articles.json # 사용 예시
  ```

- ```shell
  $ python manage.py loaddata fixtures_path # loaddata
  $ python manage.py loaddata articles/articles.json # 사용 예시
  ```

  - 출력물인 json파일은 직접 만드는게 아님. 큰 초기 데이터가 필요한 경우 csv를 import해서 dumpdata하면 됨

- admin 계정 fixtures 만들기

  ```shell
  $ python manage.py dumpdata auth.User --indent 4 > users.json
  ```

- loaddata 전에 `migrate`로 db생성해야함