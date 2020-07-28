# Data_Structure2

## 세트(Set)

mutable, unordered, iterable

- `.add(elem)`: 값 추가

- `.update(*others)`: 값 여러개 추가, 반드시 iterable이 인자

- `.remove(elem)` vs. `.discard(elem)`

  - remove는 없으면 KeyError 발생, discard는 에러발생 안함

- `pop()`: 임의의 원소 제거해 반환, 아무 설정 없으면 맨 뒤부터 제거

  

## 딕셔너리(Dictionary)

mutable, unordered. iterable 
Key/Value의 pair 자료구조

- `.get(key[,default])`

  - key를 통해 value를 가져옴
  - 절대 KeyError 발생하지 않음
  - key가 없으면 default 반환

- `pop.(key[,default])`

  - key가 있으면 제거 후 그 값 반환, 없으면 default 반환
  - default가 없는 상태면 없을 시 KeyError 발생

- `.update()`

  - 값을 제공하는 key, value로 덮어씀

- 딕셔너리에서 `for`를 활용하는 4가지 방법

  ```python
  # 0. dictionary 순회 (key 활용)
  for key in dict:
      print(key)
      print(dict[key])
  
  
  # 1. `.keys()` 활용
  for key in dict.keys():
      print(key)
      print(dict[key])
      
      
  # 2. `.values()` 활용    
  for val in dict.values():
      print(val)
  
      
  # 3. `.items()` 활용
  for key, val in dict.items():
      print(key, val)
  
  ```

- Dictionary comprehension을 사용 시, elif는 else if로 써야한다. 또한 for문이 뒤로 와야함
  `{키: 값 if 조건식 else 식 if 조건식 else 식 if ... else ... for 변수 in iterable}`