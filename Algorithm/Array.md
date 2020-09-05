# Array

### 반복

### 재귀

- 처리하고 난 나머지가 전체와 동일한 모양이다 -> 재귀 구현 가능
- 직접 혹은 간접적으로 자기 자신을 호출
- '기본 부분'과 '유도 파트'로 구성

- 팩토리얼

  ```
  Basic rule:
  	N <= 1 경우, n = 1
  Inductive rule:
  	N > 1, n! = n X (n - 1)!
  ```

- 전체를 한번에 짜려고 하지말고, 현재 할 수 있는 일과 나머지를 구분하라

- 피보나치

  ```java
  fibo(n)
  	if (n <= 1) then
  		return n;
  	else
  		return fibo(n-1) + fibo(n-2);
  end fibo(n)
  ```

  - 엄청난 중복 호출이 발생하는 문제 => 메모이제이션

- 메모이제이션

  - 적절한 자료구조를 활용하여 먼저 계산된 값을 저장하여 활용
  - 동적 계획법의 핵심

  ```
  fibo(n)
  	if n >= 2 and memo[n] is zero then
  		memo[n] <- fibo(n-1) + fibo(n-2);
  	return memo[n]
  end fibo(n)
  ```

- 입력 값 n이 커질수록 재귀 알고리즘은 반복에 비해 비효율적