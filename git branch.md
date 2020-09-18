# git 심화

### branch

- 나무가지라는 의미로 코드의 분기를 의미함



- `git branch`

  - 현재 가지들의 목록을 보여줌

  

- `git branch <new branch name>`

  - 브랜치 생성
  - 이름은 기능별로 작성(혹은 버전별로)

  

- `git switch <branch>`

  - 움직이고자 하는 곳으로 브랜치 이동
  - master에서 다른 브랜치로 이동 가능!



- `git branch -d <branch>`
  - 삭제



- `git log --all --oneline`
  - 현재 위치 상관없이 전체 log보기
  - `--graph`
    - 시각적으로 분기 보여줌



- `git merge <branch>`
  - 합치기!
  - master에서 다른 branch를 합쳐야 함
  - 충돌 시에는 충돌을 해결하고 다시 merge해야함