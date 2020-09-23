# DB

- terminal 약어 등록
  - `vi ~./bashrc` > `E` > `alias 약어='원래명령어'` > `ESC` > `:wq!` > `source ~./bashrc`

## SQLite3

- 실행

  - `winpty sqlite3` -> `sqlite3`로 약어 설정
  - DB 생성 및 실행
    -  `sqlite3 DB이름.sqlite3`

- 외부 csv import

  ```sqlite
  .mode csv
  .import 파일 테이블
  ```

- 데이터 조회

  ```sqlite
  SELECT * FROM 테이블;
  ```

  ```sqlite
  SELECT rowid, name FROM classmates; 				    보고싶은 칼럼만
  SELECT rowid, name FROM classmates LIMIT 1; 		    최상단 값 하나 가져오기
  SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;    세번째 값 하나 가져오기
  SELECT rowid, name FROM classmates WHERE address="서울"; 특정 조건의 값만 가져오기
  SELECT DISTINCT age FROM classmates;					중복 없이 조회
  ```

  

- 이쁘게 보이게 하기

  ```sqlite
  .headers on
  .mode column
  ```

- 테이블 생성

  ```sqlite
  CREATE TABLE classmates(
  ...> id INTEGER PRIMARY KEY,
  ...> name TEXT
  ...> 변수명 자료형
  ...> );
  
  CREATE TABLE classmates(
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INT NOT NULL,
  address TEXT NOT NULL
  );
  ```

  - NOT NULL을 넣어주면 반드시 입력해야 함

- 전체 테이블 확인

  `.tables`

- schema 확인

  `.schema 테이블`

- 데이터 삽입

  ```sqlite
  INSERT INTO classmates(name, age) VALUES('홍길동', 23);
  INSERT INTO classmates VALUES('홍길동', 23, '서울');
  ```

  - column명은 항상 들어가진 않아도 됨

- id까지 출력

  ```sqlite
  SELECT rowid, * from 테이블;
  ```

  - rowid를 굳이 스키마에 적기보다 위와 같이 조회하는게 편함

- PK는 integer만 가능

- 데이터 삭제

  - 중복이 불가능한 rowid를 기준으로 삭제

  ```sqlite
  DELETE FROM table WHERE rowid=?;
  DELETE FROM classmates WHERE rowid=4;
  ```

- SQLite는 기본적으로 삭제된 값의 rowid를 재사용한다

  - 단 AUTOINCREMENT 사용 시 재사용하지 못하게 만들 수 있음

    ```sqlite
    CREATE TABLE tests(id INTEGER PRIMARY KEY AUTOINCREMENT,
       ...> name TEXT NOT NULL);
    ```

  - 중간 항목이 삭제된 경우 재사용하진 않는다

    ex) id가 4번까지 있을 때, 2번을 삭제한 후 데이터를 추가하면 5번으로 추가됨

- 데이터 수정

  ```sqlite
  UPDATE classmates SET name = '홍길동', address='제주' WHERE rowid=4;
  ```

- 레코드 개수 반환

  `count(column)`

  ```sqlite
  SELECT COUNT(*) FROM users;
  ```

- 레코드 평균 반환

  ```sqlite
  SELECT AVG(age) FROM users WHERE age>=30;
  ```

- 레코드 최댓값 반환

  ```sqlite
  SELECT first_name, MAX(balance) FROM users;
  ```

- LIKE; 정확한 값에 대한 비교가 아닌, 패턴을 확인하여 해당하는 값 반환

  - 와일드카드 2가지 패턴

    - _ : 반드시 이 자리에 <u>한 개</u>의 문자가 존재
    - % : <u>한 개 이상</u>의 문자가 존재

    ```sqlite
    SELECT * FROM users WHERE age like '2_';
    SELECT * FROM users WHERE phone like '02-%';
    SELECT * FROM users WHERE phone like '%-5114-%';
    ```

- 정렬

  ```sqlite
  SELECT * FROM users ORDER BY age ASC LIMIT 10;
  SELECT * FROM users ORDER BY age, last_name ASC LIMIT 10;
  SELECT * FROM users ORDER BY age DESC LIMIT 10;
  SELECT * FROM users ORDER BY age, last_name DESC LIMIT 10; # DEFAULT가 오름차순이므로 이 경우 age는 오름차순, last_name은 내림차순 정렬이 됨
  ```

- GROUP_BY

  - 지정된 기준에 따라 행 세트를 그룹으로 결합

  - 데이터를 요약하는 상황에 주로 사용

    ```sqlite
    SELECT last_name, COUNT(*) FROM users GROUP BY last_name;
    ```

- 테이블 이름 변경

  ```sqlite
  ALTER TABLE articles RENAME TO news;
  ```

- 칼럼 명 변경

  ```sqlite
  ALTER TABLE news RENAME COLUMN content TO comment;
  ```

- 칼럼 추가

  ```sqlite
  ALTER TABLE news ADD COLUMN created_at TEXT NOT NULL;
  Error: Cannot add a NOT NULL column with default value NULL  # 기존 데이터에 NULL값이 존재하면 NOT NULL 옵션 줄 수 없음
  
  ALTER TABLE news ADD COLUMN subtitle TEXT NOT NULL DEFAULT 1;
  # DEFAULT 값을 주면 NOT NULL 옵션 부여 가능
  
  ```



### shell_plus에 sql 함께 표시하기

```shell
$python manage.py shell_plus --print-sql
```

