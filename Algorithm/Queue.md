# Queue

### 큐

- 선형
- FIFO
- 구조
  - 머리 Front: 출구
  - 꼬리 Rear: 입구
- 연산
  - enQueue: 삽입 
  - deQueue: 삭제
  - createQueue(): 공백 큐 생성
  - isEmpty()
  - isFull(): 포화상태인지 확인
  - Qpeek(): front 원소 삭제 없이 반환



### 우선순위 큐(Priority Queue)

- FIFO가 아니라, 우선순위가 높은 순서대로 먼저 나가게 됨
- 값이 큰 기준 or 값이 작은 기준