# Django 실습

- `csrf`: POST요청 시 최소한의 신원 확인을 하도록 넣어줌

  - settings.py의 MIDDLEWARE에서 확인 가능

  ```html
  <form action="{% url 'articles:create' %}" method="POST">
          {% csrf_token %}
  </form>
  ```

  - `request.method == 'POST'`일 때만 수행하도록

  ```python
  def delete(request, pk):
      article = Article.objects.get(pk=pk)
      if request.method == 'POST':
          article.delete()
          return redirect('articles:index')
      else:
          return redirect('articles:detail', article.pk)
  ```

  

- `redirect`: view함수의 return의 경로 지정

  ```python
  # views.py
  from django.shortcuts import render, redirect
  
  def create(request):
  	...
  	return redirect('articles:index') # 다른 경로를 return
  ```

  

- 게시글 역순으로 보여주기

  ```python
  def index(request):
      articles = Article.objects.all()[::-1] # 1. python문법 이용
      articles = Article.objects.order_by('-pk') # 2. DB API 구문 이용
      context = {
          'articles': articles
      }
      return render(request, 'index.html', context)
  ```

  

- 