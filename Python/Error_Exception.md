# Error_Exception

- try-except에서 except는 여러개 사용할 수 있음

  ```python
  try:
      num = input('100으로 나눌 값을 입력하시오: ')
      (100/int(num))
  except ValueError:
      print('글자가 아닌 숫자를 입력해주세요.')
  except ZeroDivisionError:
      print('0으로는 나눗셈을 할 수 없습니다.')
  ```

  

- 이때 에러는 순차적으로 수행되므로, 가장 작은 범주부터 시작해야 함

  ```python
  try:
      num = input('100으로 나눌 값을 입력하시오: ')
      100/int(num)
  except Exception:
      print('에러가 났어요')
  except ValueError:
      print('글자가 아닌 숫자를 입력해주세요.')
  except ZeroDivisionError:
      print('0으로는 나눗셈을 할 수 없습니다.')
  ```

  

- `else`는 `try` 블럭에서 에러가 발생하지 않을때 실행되어야 하는 코드에 사용됨. `except`뒤에 와야함. 보통 성공했을 때 실행될 코드를 사용. 가독성 향상 시킴

- `finally`는 어떤 경우에든 반드시 실행되어야 하는 코드에 사용. 예외발생 여부와 무관

- `raise` : 예외 강제로 발생시키기

- `assert`: 예외 발생시키는 다른 방법. 보통 상태검증?시 사용. 무조건 `AssertionError`가 발생

  ```python
  assert Boolean expression, error message
  
  assert type(1) == int, '문자열을 입력하였습니다.'
  ```

  