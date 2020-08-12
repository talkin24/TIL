# git

- Commit은 항상 신중하게 하는 것이 좋음

- `git init` : git 시작

  

- `git status` : 상태 보기

- `git diff`: 과거의 기록과 최근 수정된 기록이 어떻게 다른지 보여줌

  

- `git add .` : tracking이 가능한 상태로 변경(임시저장)

- `git restore --staged 파일명`: staged된 파일을 취소

  - add된 것을 staged,  add한 걸 취소하는 걸 unstaging이라고 함

  - 과거엔 `reset` 커맨드였음

    

- `git commit -m "변경사항"`  / commit 횟수 기준으로 쌓임

- `git commit --amend`: (맨마지막 commit만) 수정. commit message 수정 가능. 만약 다른 파일 add 후 amend한다면 add된 파일까지 포함하여 commit하게 됨

  

- `git config --global.email '이메일'`

- `git config --global. name '이름'`

- `git config --global --list`

  

- `git log` : 지금까지 작성한 사항

- `git log --oneline` : 간단하게 한줄로

  

- `git remote add origin https://github.com/talkin24/TIL.git` : origin이라는 이름으로 원격 저장소 추가. 뒤에 주소 알려줌

- `git remote -v` : 원격 연결 상태 확인

- `git push origin master` : origin이라는 원격저장소에 master 브랜치에 있는 모든 것을 push해줘

- `git clone 주소` : 원격 repo에 있는 것 clone

- `git pull origin master` : 원격저장소에서 땡겨오기

- `git push origin master` : 원격저장소에 보내기

  

  

