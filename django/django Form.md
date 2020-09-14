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

- Model from
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
  2. context는 왜 if, else와 동일선상에 있는 것일까?