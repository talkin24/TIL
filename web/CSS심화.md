## Float

- 레이아웃을 위해 도입
- 이미지가 아닌 다른 요소들에도 적용 가능
- 속성: `none, left, right`

cf) `lorem`: dummy data 생성, ex) lorem100

- 특정 태그 다음에 가상요소로 내용이 빈 블럭 추가 (사용할 땐 after 빼고, float된 태그의 부모에 적용)

  ```css
  .클래스::after {
        content: "";
        display: block;
        clear: both;
      }
  ```



## Flexbox

### **항상 메인축을 기준으로 생각할 것**

- `display: flex` or`inline-flex;`
- 가장 중요한 2가지: 요소, 축
- 요소
  - Flex Container(부모 요소)
  - Flex Item(자식 요소)
- 축
  - main axis(메인 축)
  - cross axis(교차 축)
- 속성
  - `flex-direction:` 메인 축 방향 변경(메인축에 수직하는게 교차 축)
  - `justify-content:` 메인 축 정렬
    - `flex-start` `flex-end` `center`
    - `space-evenly`: 내부 요소 공백과 외부 요소 공백 동일
    - `space-around`: 내부 요소 공백이 외부 요소 공백의 2배
  - `align`: 교차 축 정렬
    - `-content`: 여러 줄
    - `-items`: 한 줄
    - `-self`: 각 아이템 한 개ㄹ
  - `flex-wrap`: item이 flex영역을 벗어날 때 개행을 해서라도 안쪽으로 넣어주는 것이 wrap, 안 넣는 것이 nowrap
  - `flex-flow`: `flex-direction`과 `flex-wrap`의 shorthand
    ex) `flex-flow: column wrap;`
  - `stretch`: 늘어뜨리기
  - `order`: 기본값은 0, 어떤 값이 든 상대적으로 비교(음수 가능)
  - `flex-grow`: 남은 여백을 어떻게 분배할 것인가. 숫자 비율대로 분배. 단 남은 여백을 쪼개서 분배하는 것이기 때문에 원래 차지하고 있던 분배는 포함되지 않는다(주의)



## Bootstrap

- Quickly, Responsive, Mobile-first, The world's most popular front-end open source toolkit
- 웹페이지에서 기본적으로 쓰는 요소들은 다 가지고 있는 라이브러리
  - 디자인 요소에 사용하는 시간 단축
  - 크롬 뿐이 아닌 어떤 브라우저로 접근하더라도 같은 화면을 보여줌(reboot)
    <CSS 초기화 방법>
    - Reset: 공격적, '브라우저 너네 자체 스타일 다 없앨거야'
    - Normalize: 젠틀, 웹표준에 다 맞춤; 최근에는 reset.css보다 normalize.css 선호
- 파일 다운로드 안해도, 온라인에서 가져와 사용할 수 있음
- m: margin, p: padding
  t: top, b: bottom, l:left, r:right, x: 수평, y: 수직
- breakpoint: sm, md, lg, xl, 화면 크기에 따라 특정요소 보이거나 안보이게 하기
- sticky-top은 fixed-top과 다르게 다음 sticky를 만나면 겹쳐짐



### Grid system

- Responsive web을 만들기 위해 필요
- flexbox 기반, **5 breakpoints**, **12 column system**
- `container`로 시작
- doc에 있는 거 직접 해보기
- cf) `alt + shift + 아래 방향키`: 복사
- cd) `ctrl + alt + 방향키`: 다중커서

- 한 칼럼을 다시 12개로 쪼갤 수 있음