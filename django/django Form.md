# django Form



- django 프로젝트의 주요 유효성 검사도구

- 공격 및 우연한 데이터 손상에 대한 중요한 방어수단

1. 렌더링을 위한 데이터 준비 및 재구성
2. 데이터에 대한 HTML forms 생성
3. 클라이언트로부터 받은 데이터 수신 및 처리

- Form Class
  - django Form 관리 시스템의 핵심
  - form 내 field, filed 배치, 디스플레이, widget, label, 초깃값, 유효하지 않은 field에 관련된 에러메시지 결정
  - 사용자 데이터를 받을 때 과중한 반복작업을 줄여줌

- Model form
  - 모델에 있는 것을 form에서 반복하는 것은 낭비
  - 이미 있는 모델을 상속받아 사용

### view 함수 대격변!

- new함수와 create함수 합병

  ```python
  def create(request):
      if request.method == 'POST':
          form = ArticleForm(request.POST)
          if form.is_valid():
              article = form.save()
              return redirect('articles:detail', article.pk)
      else: # new
          form = ArticleForm()
      context = {
          'form': form,
      }
      return render(request, 'articles/new.html', context)
  ```

  의문점 2가지

  1. 왜 if문에 'GET'이 아니고 굳이 'POST'가 올까?

     - POST일 때는 DB에 영향을 주는 중요한 코드를 실행해야함. 악성 사용자가 이상한 요청을 보내도 문제 없도록

  2. context는 왜 if, else와 동일선상에 있는 것일까?

     - 똑같이 form을 받긴하지만, 유효성 검사를 통과하지 못한 경우, 오류 메시지도 발생.

       

- Moedl form이 훨씬 편한데 form은 언제 쓰냐? 

  - model에 연관되지 않는 데이터를 받을 때 사용



- NoReverseMatch 에러는 딱 한 가지랑 관련됨
  - url tag



-  form은 models.py에 같이 작성될 수도 있음.
  - 그러나 유지보수 고려 시 파일을 따로 관리하는게 나음

- form이 편하긴 한데 디자인할 때 불편함

  - 하나씩 다 뽑아주기

    ```django
    <form action="" method="POST">
        {% csrf_token %}
        <div>
          {{ form.title.errors }}
          {{ form.title.label_tag }}
          {{ form.title }}
        </div>
        <div>
          {{ form.content.errors }}
          {{ form.content.label_tag }}
          {{ form.content }}
        </div>
        <input type="submit">
      </form>
    ```

    

  - for문 사용(개수 많을때)

    ```django
    <form action="" method="POST">
        {% csrf_token %}
        {% for field in form %}
            {{ field.errors }}
            {{ field.label_tag }}
            {{ field }}
        {% endfor %}
        <input type="submit">
    </form>
    ```

- Form에도  bootstrap을 먹이고 싶은 경우

  1. bootstrap에서 class 찾아서 직접 태그에 입력
  2. `django-bootstrap4` 설치
     - `pip install django-boostrap4`
     - settings.py의 INSTALLED_APPS에 추가



### View decorator

- decorator 

  - 어떤 함수에 기능을 추가하고 싶을 때, 함수는 수정하지 않고 기능을 연장하게 해주는 함수

- Allowed HTTP methods

  

- server는 client한테 왜 에러가 나는지 정확히 알려줘야 함!