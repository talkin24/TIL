# Django_2

### URL 심화

- url.py 폴더에 경로를 전부 저장하는 건 유지 보수에 좋지 않음

  `from django.urls import path, include` `include()`를 사용해서 상세 경로를 구분 가능





### 상속

- 여타 웹사이트의 nav들은 페이지가 바뀌어도 유지된다. 이 경우 마다 코드를 새로 짜는 것이 아니고, 상속을 이용하면 된다

- `{% extentds 'base.html' %}`: 첫번째 줄

- template 내에 `{% block content %}` `{% endblock content %}`으로 구멍을 뚫어줌

- `settings.py`내 `TEMPLATES` 에서 `'DIRS'`를 수정해야 함

  ```python
  'DIRS': [BASE_DIR / 'first_project' / 'templates'],
  ```

  