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



### 2차원 배열

**델타를 이용한 2차원 배열**

- 4방향 경계 체크 시 일반화하면 연산에 부담이 될 수 있음. 연산 속도를 생각했을 때, 4가지 경우를 나눠서 경계 조건을 확인하는게 더 빠름



### 순열

- N개의 요소에 대해서 N!개의 순열들이 존재 -> 12! 만해도 5억, 10! 정도를 마지노선으로 생각할 것
- 인덱스 순열을 만들면 순열 생성은 한번만 하면 되기 때문에 상대적으로 연산에서 이득

```java
numbers[] : 순열 저장 배열. 매번 함수를 호출하기 때문에 이전 단계의 숫자들을 저장할 공간이 필요
isSelected[] : 인덱스에 해당하는 숫자가 사용중인지 저장하는 배열. 비교 횟수 감소. 메모리 사용

perm(cnt)
	if cnt == 3
		순열 생성 완료
	else
		for i from 1 to 3
			if isSelected[i] == true then continue
			numbers[cnt] <- i
			isSelected[i] <- true
			perm(cnt+1)
			isSelected[i] <- false
		end for
```

- 재귀 매개변수를 결정하는데 보통 어려움을 겪음. 재귀메소드에 대한 정의를 명확히 하고, 매개변수를 결정 요인으로 이해할 것
- 가변 길이의 순열을 만들 때 기저 조건만 바꾸면 되기 때문에 이용됨. 단 고정 길이 순열의 경우 반복문이 더 유리
- isSelected를 빼면 **중복순열**

### 조합

- 순서가 의미가 없기 때문에 오히려 순서대로 구현하면 됨

```java
comb(cnt, cur) // cnt: 현재까지 뽑은 조합 원소 개수, cur: 조합에 시도할 원소의 시작 인덱스
	if cnt == r
		조합 생성 완료
	else
		for i from cur to n-1
				numbers[cnt] <- input[i]; //isSelected처럼 중복을 확인하는 과정이 필요 없음
				comb(cnt + 1, i + 1);
		end for
end comb()
```

- 다음 조합의 시작 위치를 현재 위치랑 같게 하면 **중복조합**

### 부분집합

