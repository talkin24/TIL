# module

- 함수명 역시 변수에 넣어 이름을 바꿀 수 있음

  ```python
  check_odd = check.odd
  check_odd(10)
  >> False
  ```



- 패키지 = 모듈 여러개
- `__init__.py`는 해당 폴더가 python패키지라는 것을 표시해주기 위한 파일. 최근 버전(3.3이상)에는 필요 없으나, 과거 버전과 일부 프레임워크에 package가 사용될 수도 있으므로 생성해줌
- 'module.변수'를 통해 모듈 안에 있는 변수를 불러올 수도 있음
- modul 안에 뭐가 있는지 모를때는 `dir()` 활용