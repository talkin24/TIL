# CSS

### 웹 관련 자료는 MDN에서 확인할 것

- css는 selector와 함께 시작된다

- css구문은 하나 이상의 선언들로 구성됨

- 선언 = 속성: 값

  ex) `h1{color: blue; font-size: 15px}`

- CSS 정의방법

  1. 인라인: 해당태그에 직접 style 속성을 활용
  2. 내부참조: `head` 태그 내에 직접 작성 -> 수업에서 활용
  3. 외부참조: css파일을 `<head>`내 `<link>`를 통해 불러오기  -> 현업에서 가장 일반적

- 선택자

  1. 기초 선택자
  2. 고급 선택자
  3. 의사 클래스(pseudo class)



- `.class명`: class선택자
- `#id명`: id선택자
- `>`:  직계 자식 가리키기, 자손은 공백



- class 여러개 주고 싶을땐 따옴표 안에 클래스간 공백을 주면 됨

  

- CSS 적용 우선순위
  - `!important`: 무조건 가장 높은 우선순위(사용시 주의)
  - 인라인 / id선택자 / class선택자 / 요소 선택자
  - CSS 내 순서가 후에 적힌 것이 우선적용됨. 선택자 내 클래스 간 순서는 의미 없음
  - 코드 유지보수 할때는 거의 모든 CSS selector가 class인게 낫다. 되도록 id 셀럭터는 지양
- CSS 상속은 되는것도 있고 안되는 것도 있음



- (상대)크기 단위

  - px(픽셀)
  - %
  - em: 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐(부모 기준)
  - rem: 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐(최상위 기준)
  - Viewport 기준단위: 보이는대로 -> 스마트폰 또는 태블릿에서 주로 사용

- 색상

  - 색상 키워드

  - RGB색상(16진수 표기법, rgb함수형 표기법)

  - HSL색상

  - a는 투명도 추가

    

- img: 디자인 + 컨텐츠
- background-image: 디자인



- boxmodel 축약형은 2개일때, 3개일때 4개일때 다름
  - 2개일때 : 상하 좌우
  - 3개일때: 상 좌우 하
  - 4개일때: 상->우->하->좌(clockwise)
- 개발자도구에서 먼저 테스트 해보고 코드를 수정하는게 좋음



- 기본적으로 모든 요소의 box-sizing은 content-box(padding 제외 한 것이 기준). 다만 우리가 일반적으로 영역을 볼 때는 border까지의 너비를 100px로 보는 것을 원함
  -> box-sizing을 border-box로 설정
  - 일반적으로 항상 border-box로 바꾸고 시작함
- block 요소 정렬과 inline요소 정렬은 다름
- inline-block은 block과 inline 레벨 요소의 특징을 모두 갖는다. inline처럼 한줄에 표시 가능하며, block처럼 width, height, margin 등 속성을 모두 지정 가능



- position
  - absolute는 원래 위치를 기억하지 않음
  - relative는 부모를 기준으로 움직임