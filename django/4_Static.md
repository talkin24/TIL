### static

### homeworkshop/0915 참고 

- app 폴더 내에 static 폴더 생성

  - 그 내부에 앱이름 다시 생성
  - 해당 폴더에 이미지 저장
  - server를 재가동해야 적용가능

- html 파일 상단에 `{% load static %}` 꼭 작성

  ```django
  {% load static %}
  ...
  <img src="{% static 'articles/images/mac_pro_13.jpg' %}" alt="sample">
  ```

- 다른 폴더를 static 경로로 지정하고 싶다면 `settings.py`에서 `STATIC_URL` 아래에 경로 추가

  ```python
  ...
  STATIC_URL = 
  
  STATICFILES_DIRS = [
  	BASE_DIR / 'static'
  ]
  ```

  

- 이미지가 아니어도 적용 가능 ex) css



### 이미지 입력 받기

- `models.py`에  field 추가

  ```python
  from django.db import models
  
  class Article(models.Model):
      title = models.CharField(max_length=20)
      content = models.TextField()
      image = models.ImageField(blank=True) # 반드시 입력되지 않아도 됨
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  ```

- 단 Pillow 설치 해야함

- model이 변경되었으니, `makemigrations`, `migrate` 해줘야 함

- 모델 폼 사용하면 자동으로 적용됨



- 전송받는 image를 인코딩해야하므로,  html의 form 태그에 `enctype="multipart/form-data"` 추가

  ```django
  <form action="{% url 'articles:create'%}" method='POST' enctype="multipart/form-data">
      {% csrf_token %}
      {{ form.as_p }}
      <input type="submit">
    </form>
  ```

- request로 받을때 파일도 받아야 하므로 view함수에서 request 받아올 때 FILES 추가, 

  `        form = ArticleForm(request.POST, request.FILES)`

  ```python
  def create(request):
      if request.method == 'POST':
          form = ArticleForm(request.POST, request.FILES)
          if form.is_valid():
              article = form.save()
              return redirect('articles:detail', article.pk)
      else:
          form = ArticleForm()
      context = {
          'form': form,
      }
      return render(request, 'articles/create.html', context)
  ```

### 사용자가 추가한 파일을 저장하여 이용하는 루트 필요

- `settings.py`

  ```python
  MEDIA_ROOT = BASE_DIR / 'media'
  MEDIA_URL = '/media/'
  ```

- `urls.py`(앱 보다 상위에 존재하는 파일)

  -  `settings` `static` import
  - `+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)` 추가

  ```python
  from django.contrib import admin
  from django.urls import path, include
  from django.conf import settings
  from django.conf.urls.static import static
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('articles/', include('articles.urls')),
  ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
  ```



### html에 if문 삽입

- image 파일이 없는 경우, error 발생 할 수 있으므로 img 태그에 if 문 사용

  `{% if article.image %}
      <img src="{{ article.image.url }}" alt="{{ article.image }}">
    {% endif %}`

  ```django
  {% extends 'base.html' %}
  
  {% block content %}
    <h1>CRUD with ModelForm</h1>
    <hr>
    <h2>Detail</h2>
    <hr>
    <p><h3>글 번호: {{ article.pk }}</h3></p>
    <p><h3>글 제목: {{ article.title }}</h3></p>
    {% if article.image %}
      <img src="{{ article.image.url }}" alt="{{ article.image }}">
    {% endif %}
    <p>글 내용: {{ article.content }}</p>
    <p>글 생성시각: {{ article.created_at }}</p>
    <p>글 수정시각: {{ article.updated_at }}</p>
    <a href="{% url 'articles:update' article.pk %}">EDIT</a><br>
    <form action="{% url 'articles:delete' article.pk %}" method="POST">
          {% csrf_token %}
          <button class="btn btn-danger">DELETE</button>
    </form>
    <hr>
    <a href="{% url 'articles:index' %}">BACK</a><br>
  {% endblock content %}
  ```

### 사용자가 저장한 파일이 저장되는 경로 설정

- `models.py`에서 upload_to 속성

```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='%Y/%M/%d') # 반드시 입력되지 않아도 됨 / 저장 경로 지정(일단 날짜로)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```



### 파일 크기 지정

- `pilkit` `django-imagekit` install

- `settings.py`, INSTALLED_APPS에 `'imagekit'` 추가

  ```
  
  ```

- models.py에 

  - import `from imagekit.models import ProcessedImageField`

  ​								`from imagekit.processors import Thumbnail`

  - `image = ProcessedImageField(`
            `blank=True,`
            `processors=[Thumbnail(200,300)],`
            `format='JPEG',`
            `options={'quality', 90} # 원본 이미지의 90% 퀄리티`
            `upload_to='%Y/%m/%d',`
        `)` 추가

  ```python
  from django.db import models
  from imagekit.models import ProcessedImageField
  from imagekit.processors import Thumbnail
  
  class Article(models.Model):
      title = models.CharField(max_length=20)
      content = models.TextField()
      # image = models.ImageField(blank=True, upload_to='%Y/%m/%d') # 반드시 입력되지 않아도 됨 / 저장 경로 지정(일단 날짜로)
      image = ProcessedImageField(
          blank=True,
          processors=[Thumbnail(200,300)],
          format='JPEG',
          options={'quality': 90}, # 원본 이미지의 90% 퀄리티
          upload_to='%Y/%m/%d',
      )
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  ```

  