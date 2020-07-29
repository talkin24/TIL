# OOP

- 파이썬에서 모든 것은 객체이고, 모든 객체는 특정 타입의 인스턴스

- `isinstance(a, b)`: a가 b타입의 인스턴스인지 확인

- 속성(attribute)은 객체의 상태/데이터

- 메서드(Method)는 특정 객체에 적용할 수 있는 행위(behavior)

- 클래스의 이름은 `PascalCase`로 정의

- `.__doc__`: 클래스 내에 정의한 내용(주석)이 출력됨

- 생성된 인스턴스가 다른 변수로 바뀌면 기존 인스턴스는 제거됨

  ```python
  class Person:
      def __init__(self):
          print('응애!')
          
      def __del__(self):
          print('갈게..')
          
  p1 = Person()
  >> 응애!
  del Hanbin
  >> 갈게..
  p1 = Person()
  >> 응애!
  p1 = 'hello'        
  >> 갈게..
  ```

  

- `self`의 의미: 객체가 가지고 있는 변수

- 매직메서드(=스페셜메서드)

  - 특별한 일을 하기위해 만들어진 메서드. 더블언더스코어로 표시 `__something__`
  - `__add__`는 `+` 연산자와 동일(기타 연산자도 정의되어 있음)
  - `__str__`: 객체 출력 시 보여주는 내용 정의 가능(그 전엔 object이름만 출력됨)

- `self`: 파이썬은 인스턴스에서 메서드 호출 시 인스턴스 자신이 전달됨

  ```python
  hanbin = Person('Hanbin')
  hanbin.talk()
  
  Person.talk()
  >> TypeError
  Person.talk(hanbin)
  >> '안녕, 나는 Hanbin'
  ```

- 인스턴스 변수 vs. 클래스 변수

  ```python
  class Person:
      species = 'human'
      
      def __init__(self, name):
          self.name = name
  john = Person('john')
  eric = Person('eric')
  
  print(john.species)
  >> human
  print(eric.species)
  >> human
  print(john.name)
  >> john
  print(eric.name)
  >> eric
  ```

  - 클래스 변수는 `class.변수명` `instance.변수명` 2가지 방법으로 접근 가능

  - 인스턴스를 통해 접근하여 클래스변수를 수정한다고 해서, 모든 인스턴스의 클래스 변수가 바뀌는 건 아님

    ```python
    print(john.species)
    >> developer
    print(eric.species)
    >> human
    ```

  - 같은 이름일 시 인스턴스 속성이 우선

    ```python
    class Person:
        name = '김싸피'
    
        def __init__(self, name='ssafy'):
            self.name = name
        
        def talk(self):
            return f'안녕, 나는 {self.name}'
        
    p1 = Person()
    p1.talk()
    >> '안녕, 나는 ssafy'
    
    Person.name
    >> '김싸피'
    ```

  - 클래스와 인스턴스의 공간은 구분됨. 인스턴스에서 변수가 조회되지 않으면 클래스에서 확인함. 변수 속성뿐만 아니라 메서드도 마찬가지

- 클래스 메서드

  - 클래스가 사용하는 메서드
  - `@classmethod` 이후 정의
  - 속성과 마찬가지로 인스턴스를 통해 접근 가능

- 생성자 안에서도 연산 가능(ex. 인스턴스 발생할 때마다 population 1씩 증가)

  ```python
  class Puppy:
      population = 0
      
      def __init__(self, name, breed):
          self.name = name
          self.breed = breed
          Puppy.population += 1
  ```

- 스태틱 

  - 어떤 속성에도 접근하지 즉 변하지 않음!(변수를 사용하지 않음
  - `@staticmethod` 이후 정의

- 클래스와 인스턴스는 각각 모두 `인스턴스 메서드`, `클래스 메서드`, `정적 메서드`에 접근 가능함. 하지만 호출 가능성과 별개로 인스턴스가 할 행동은 모두 인스턴스 메서드로 한정지어 설계하고, 클래스가 할 행동은 클래스 메서드와 정적 메서드로 한정하여 정의하는 것이 좋음

- `issubclass(자식, 부모)`: 상속 여부 확인

- `isintance(인스턴스, 자식 클래스)` = `isintance(인스턴스, 부모 클래스)`

- 내장 타입들에도 상속 관계가 있음

  ```python
  print(issubclass(bool, int))
  >> True
  print(issubclass(float, int))
  >> False
  ```

  

- `super()`: 상속을 했음에도 불구하고 중복되는 내용 발생 가능. 부모 클래스의 내용을 바로 사용해서 중복을 제거하고자 할 때 사용

  ```python
  class Student(Person):
      def __init__(self, name, age, number, email, student_id):
          # Person()
          super().__init__(name, age, number, email)
          self.student_id = student_id
  ```

- 다중상속

  - 여러개 클래스로부터 상속받을 수 있음
  - 이때 상속 순서가 중요. 왼쪽에 있는 속성, 메서드가 우선적으로 적용됨



