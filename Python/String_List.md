# Data_Structure1

- 데이터를 저장하거나 조작하는 방법



### 문자열(String)

특징: immutable, ordered, iterable

- `.find(x)` vs. `.index(x)` 
  - x의 첫번째 위치를 반환하는 공통점
  - 단 후자는 x가 없을때 오류 발생, 전자는 `-1` 반환
- `.replace(old, new[, count])`
- `.strip([chars])`: `lstrip()`, `rstrip()`
- `'separator'.join(iterable)`: 문자열로 반환
- `.capitalize()`, `.title()`
- `.swapcase()`



### 리스트(List)

**mutable**, ordered, iterable

- `.append(x)` vs. `.extend(iterable)`

  -  extend는 덧셈(+)과 같은 역할(list concatenate). 즉 리스트 간의 덧셈. 
  - 따라서 extend 안에는 **iterable**이 입력되어야함.

  ```
  ['starbucks', 'tomntoms', 'hollys', 'banapresso', 'wcafe', '빽다방', 'mc_cafe', 'droptop', ['coffeenie'], 'twosome_place']
  -------------------------------------------------------------------------------------------------------------------------
  ['starbucks', 'tomntoms', 'hollys', 'banapresso', 'wcafe', '빽다방', 'mc_cafe', 'droptop', ['coffeenie'], 'twosome_place', 'e', 'd', 'i', 'y', 'a']
  ```

  

- `.insert(i,x)`: 위치 i에 x를 추가, <u>인덱스(i)가 길이를 넘어서도 오류 X</u>

- `.remove(x)`: 리스트에서 x값 삭제. <u>삭제할 값이 없으면 오류 발생</u>

- **shallow copy** vs. **deep copy**

  - mutable한 자료형은 복제된 데이터가 바뀌면 원본도 바뀜
  - 단, slice 사용하면 원본과 달라짐

- map 사용시 첫번째 인자는 함수의 호출이 아닌, 함수의 이름