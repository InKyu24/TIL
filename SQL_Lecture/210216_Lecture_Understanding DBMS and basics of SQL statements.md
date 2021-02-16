# Chapter 1

## DB vs. DBMS

Data Base vs. Data Base Management System

DB를 '데이터의 집합'이라고 정의한다면 DBMS는 이 DB를 관리 및 운영하는 역할을 한다. 쉽게 말해, 가수와 기획사의 사이라고 할 수 있다. 정보 자체를 일컫을 때에는 DB라고 하며, 대용량 데이터를 관리하고 사용자 간 공유하는 역할을 한다면 DBMS로 보는 것이다

DBMS는 DB를 관리하는 역할을 하는 소프트웨어의 개념이다. 지금부터 배울 Oracle은 DBMS이다. Oracle에서는 DB를 스키마라고 부르는 것이 더 적절하다고 볼 수 있다. 



## DBMS의 종류

DBMS에는 Oracle, MySQL, SQL Server, MariaDB, PostgreSQL, DB2, Access, SQLite 등 다양하게 있으며, Oracle은 가장 많이 사용하는 DBMS이다.



## DB, DBMS의 중요한 특징

+ 데이터의 무결성 - DBMS 내 데이터는 오류가 있어서는 안 된다. 이 무결성을 위해서 DB는 제약 조건이라는 특징을 가진다. 예를 들어, 모든 학생은 학번이 반드시 있어야 하고 중복되어서는 안된다는 제약 조건이 있을 수 있다.
+ 데이터의 독립성 - DB의 크기를 변경하거나 저장소를 변경하더라도, 기존에 작성된 응용프로그램은 전혀 영향을 받지 않아야 한다. 즉, 의존적 관계가 아닌 독립적 관계여야 한다. 예를 들어, DB가 저장된 디스크가 새 것으로 변경되어도 기존에 사용하던 응용 프로그램은 아무 변경없이 계속 사용되어야 한다.
+ 보안 - DB 안의 데이터에는 어떠한 권한을 가진 사람들만이 접근할 수 있어야 한다.
+ 데이터 중복 최소화 - 동일한 데이터가 여러 개 중복되어 저장하는 것을 최소화하는 것을 말한다. 예를 들어, 학생 정보를 이용하는 교직원이 여러 명 있다고 하면, 각각의 교직원마다 별도의 엑셀 파일을 사용하게 된다. 그렇게 되면 한 명의 학생 정보가 각각의 엑셀 파일에 중복되어 관리된다. DBMS를 이용하면 하나의 테이블에 데이터를 저장하고 이를 공유하므로써 데이터 중복을 최소화할 수 있다.
+ 응용 프로그램 제작 및 수정이 용이 - 각각 파일 포맷에 맞춰 개발해야하는 응용 프로그램을 DB를 이용함으로써 통일된 방식으로 응용 프로그램을 작성할 수 있고, 유지보수 또한 쉬워진다.
+ 데이터의 안전형 향상 - 대부분의 DBMS가 제공하는 백업 및 복원 기능을 이용함으로써, 데이터가 손상되는 문제가 발생할 경우에 원상태로 복원 및 복구하는 방법이 명확해진다.



## DBMS의 분류

DBMS의 유형은 크게 계층형(Hierarchical), 망형(Network), 관계형(Relational), 객체지향형(Object-Oriented), 객체관계형(Object-Relational) DBMS로 분류된다.

관계형 DBMS는 RDBMS라고도 하며, 대다수의 DBMS는 관계형 DBMS이다. Oracle도 관계형 DBMS 중 하나이다.



### 관계형 DBMS

RDBMS의 핵심 개념은 'DB는 테이블이라 불리는 최소 단위로 구성되어 있다. 그리고 테이블은 하나 이상의 열로 구성되어 있다.' 이다. 

> 테이블을 칭하는 다른 용어로 '릴레이션', '엔티티' 등이 있다. 

관계형 DBMS에서 모든 데이터는 테이블에 저장되므로, 테이블이라는 구조가 가장 기본적이고 중요한 구성이 된다. 그러므로 테이블에 대한 이해가 중요하다. 테이블은 데이터를 효율적으로 저장하기 위한 구조이다. 정보를 저장하기 위해서 하나의 테이블이 아닌 여러 개의 테이블로 나누어서 저장함으로써, 불필요한 공간의 낭비를 줄이고 데이터 저장의 효율성을 보장해 줄 수 있다. 또, 이렇게 나뉜 테이블의 관계를 기본 키(Primary Key)와 외래 키(Foreign Key)를 사용해 맺어 줌으로써, 두 테이블은 부모와 자식의 관계로 묶어 줄 수 있다. 추후에 부모 테이블과 자식 테이블을 조합해서 결과를 얻고자 할 경우에는 SQL의 조인 기능을 이용하면 된다.



## SQL

SQL(Structured Query Language)은 관계형 데이터베이스에서 사용되는 언어로, '에스큐엘' 또는 '시퀄'로 읽는다.

관계형 DBMS를 배우기 위해서는 SQL을 익히는 것이 필수다. SQL이 비록 DB를 조작하는 '언어'이다. 국제 표준화 기관에서 표준화된 내용을 계획 발표해 왔으며, 일반적인 프로그래밍 언어와는 다른 특성을 갖고 있다.

+ DBMS 제작회사와 독립적 - SQL은 모든 DBMS 제작회사에 공통적으로 공개되고, 각 제작회사는 이 표준 SQL에 맞춰서 DBMS를 개발한다. 그러므로 표준 SQL은 대부분의 DBMS 제품에서 공통적으로 호환된다. 
+ 다른 시스템으로의 우수한 이식성 - SQL 표준은 서버용, 개인용, 휴대용 장비에서 운영되는 DBMS마다 상호 호환성이 뛰어나다. 그렇기에 어느 곳에서 사용된 SQL을 다른 시스템으로 이식하는데 별 문제가 없다.
+ 계속 발전하는 SQL 표준 - SQL 표준은 계속 개선된 표준안이 발표되고 있다.
+ 대화식 언어 - 기존 프로그래밍 언어는 '프로그램 작성, 컴파일, 디버깅, 실행'이라는 과정을 거쳐야만 그 결과를 확인할 수 있으나, SQL은 이와 달리 바로 질의하고 결과를 얻는 대화식 언어로 구성되어 있다.
+ 분산형 클라이언트/서버 구조 - SQL은 분산형 구조인 클라이언트/서버 구조를 지원한다. 즉, 클라이언트에서 질의를 하면 서버에서 그 질의를 받아서 처리 한 후, 다시 클라이언트에게 전달하는 구조를 가진다.

> 주의할 점은 모든 DBMS의 SQL문이 완벽하게 동일하지 않다는 것이다. 그래서 각 회사는 표준 SQL을 지키면서 자신의 제품에 특화시킨 SQL을 사용한다.

<img src="https://lh3.googleusercontent.com/-R_AIW2Ccbi0/YCuXKYEuYSI/AAAAAAAAGXA/cOWtpmjRGOIXDJQfO9aJSqfbcHBsPW-5gCLcBGAsYHQ/image.png" alt="img" style="zoom:50%;" />



> CRUD - 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능인 Create, Read, Update, Delete를 묶어서 일컫는 말
>
> JDBC - 자바 프로그램 내에서 DBMS에 구애받지 않고 SQL문을 실행하기 위한 표준 DB 인터페이스 API



# Chapter 3

## DBMS 필수 용어

* 데이터 - 하나하나의 단편적인 정보로, 체계화되지 못한 상태의 정보
* 테이블 - 데이터 입력을 위해 표 형태로 표현한 것
* 스키마 - 테이블, 뷰 등이 저장되는 저장소를 말하거나 여러 테이블, 뷰 등의 묶음으로도 말한다. 또한 스키마는 사용자 이름과 동일하게 취급된다. 스키마는 사용자별 고유 공간이며, 주로 원통 모양으로 표시된다. 각 스키마는 서로 다른 고유한 이름을 가지고 있어야 한다.
* 데이터베이스(DB) - 여러 개의 스키마가 저장되는 저장 공간이다. Oracle XE는 XE라는 이름의 데이터베이스를 기본적으로 제공하며, 단 1개의 데이터베이스만이 운영 가능하다. Oracle EE나 SE에서는 여러 개의 데이터베이스를 생성하고 동시에 운영할 수 있다.
* DBMS - 스키마를 관리하는 시스템 또는 소프트웨어를 말한다. Oracle이 대표적인 DBMS이다.
* 열(=컬럼, 필드) - 각 테이블은 열로 구성된다.
* 열 이름 - 각 열을 구분하기 위한 이름으로, 각 테이블 내에서 열 이름은 중복되지 않고 고유해야 한다.
* 행(=로우, 레코드) - 실질적인 데이터를 말한다.
* 기본 키(Primary Key) 열 - 각 행을 구분하는 유일한 열을 말한다. 모든 행이 가지고 있는 데이터이면서 동시에 모든 행이 서로 다른 데이터라면 해당 열은 기본 키로 지정되기에 충분한 조건이 될 수 있다.
* 외래 키(Foreign Key) 필드 - 두 테이블의 관계를 맺어주는 키를 말한다.
* SQL - DBMS가 알아 들을 수 있는 언어가 SQL이다.



## 스키마 구축 실습

```SQL
CREATE TABLE "my testTBL" (id NUMBER(3));
	-- my testTBL을 이름으로 하는 테이블 생성[열 이름 ID이고, 숫자 3자리 형식]
	-- ""을 하면 띄어쓰기한 이름, 대소문자 구분하는 이름 생성이 가능

Drop Table "my testTBL";
```



# Chapter 4

## 정보시스템 구축 절차

정보시스템 구축을 위해서는 분석, 설계, 구현, 시험. 유지보수의 5단계를 거친다. 먼저 분석 단계는 구현하고자 하는 프로젝트의 가장 첫 번째 단계로, 시스템 분석 또는 요구사항 분석이라고 부른다. 프로젝트의 첫 단추를 끼우는 중요한 단계로, 현재 우리가 '무엇을' 할 것인지를 결정한다. 설계는 주로 시스템 설계 또는 프로그램 설계라는 용어로 부르는데, 우리가 구축하고자 하는 시스템을 '어떻게' 할 것인지를 결정한다. 설계까지 완료되면 가장 큰 작업이 끝난 것으로 간주된다. 대부분의 프로젝트에서 분석과 설계 과정이 전체 공정의 50% 이상을 차지하기 때문이다. 분석과 설계 과정에서 가장 중요한 과정 중 하나가 'DB 모델링'이다. DB 모델링이란 현실세계에서 사용되는 데이터를 Oracle에 어떻게 옮겨 놓을 것인지를 결정하는 과정이라고 생각하면 된다. 



> 폭포수 모델
>
> 가장 오래되고 전통적으로 사용되는 소프트웨어 개발 모델로 프로젝트 계획, 업무 분석, 시스템 설계, 프로그램 구현, 테스트, 유지보수 순으로 진행된다. 단계가 명확히 구분되어서 진행 단계가 명확해지는 장점이 있으나 폭포수처럼 이전 단계로 다시 거슬러 올라가는 것이 어렵다는 단점도 있다. 여기서 가장 핵심적인 단계는 분석과 설계이다. 데이터베이스 모델링은 분석과 설계 단계에서 가장 중요한 작업 중 하나라는 점을 기억하자



## 데이터베이스 모델링

데이터베이스 모델링은 현 세계에서 사용되는 작업이나 사물들을 DBMS의 데이터베이스 개체로 옮기기 위한 과정이라고 말할 수 있다. 쉽게 말하자면, 현실에서 쓰이는 것을 테이블로 변경하기 위한 작업이라 할 수 있다. 또한 현실세계에서 실체가 없는 '물건을 산다'라는 행위도 테이블로 변환된다는 점을 주의해서 볼 필요가 있다.

데이터베이스 모델링을 하는 사람이 어떤 사람이냐에 따라서 각기 다른 결과가 나올 수밖에 없다. 중요한 것은 좋은 모델링과 나쁜 모델링이 존재한다는 점이다. 즉, 정답은 없더라도 좋은 답안은 존재한다.

데이터베이스 모델링을 하기 위해서는 업무에 대한 폭넓고 정확한 지식과 이해가 필요하고, 데이터베이스 시스템에 대한 지식과 경험도 요구되기 때문이다.

데이터베이스 모델링은 크게 3단계를 거쳐서 완성되는 것이 보편적이다. 개념적 모델링, 논리적 모델링, 물리적 모델링으로 나뉠 수 있다. 일반적으로 개념적 모델링은 주로 업무 분석 단계에 포함되며, 논리적 모델링은 업무 분석의 후반부와 시스템 설계의 전반부에 걸쳐서 진행된다. 그리고 물리적 모델링은 시스템 설계의 후반부에 주로 진행된다.



>  Oracle SQL Developer : GUI 환경에서 SQL 명령을 사용할 수 있도록 제공되어, 고급 SQL문의 작성을 한결 수월하게 해준다.

>  SQL*Plus : Oracle의 가장 오래되고 기본적인 유틸리티로, 텍스트 기반으로 명령어가 처리된다.

> Oracle Application Express : 웹 기반으로 오라클을 관리하거나, 웹 환경의 접근을 개발하는데 유용하게 사용된다.



# Chapter 6

## PL/SQL

Oracle에서 자신의 제품의 특성을 반영하는 SQL에 PL/SQL이라는 별도의 이름을 붙였다.



## SELECT FROM

가장 많이 사용되는 구문으로, 데이터베이스 내의 테이블에서 원하는 정보를 추출하는 명령이다.

```sql
-- SELECT문의 형식
SELECT 열 FROM 테이블 WHERE 조건
```



```sql
-- SELECT문의 예시(1)
SELECT * FROM HR.employees;
	-- employees 테이블에서 모든 열에 데이터 추출
SELECT * FROM employees;
	-- HR 스키마 내 employees 테이블에서 모든 열 데이터 추출
```

> 원칙적으로는 테이블 이름 앞에 스키마 이름을 넣어야하지만, 현재 연결된 스키마를 자동으로 붙여서 실행된다.



```sql
-- SELECT문의 예시(2)
SELECT department_name FROM departments;
	-- departments 테이블에서 departments_name열 데이터 추출
SELECT department_id, department_name FROM departments;
	-- departments 테이블에서 department_id, departments_name 열 데이터 추출
```

> 열이름을 콤마(,)로 구분하여 작성하면, 선택된 열이 순서에 맞춰 추출된다.



```sql
-- SELECT문의 예시(3)
SELECT * FROM userTBL WHERE username = '김경호';
	-- userTBL 테이블에서 username이 김경호인 모든 열 데이터 추출
SELECT * FROM employees WHERE employee_id >= 120;
	-- employees 테이블에서 employee_id가 120보다 크거나 같은 모든 열 데이터 추출
	
-- <, <=, >, >=, AND, OR 활용 예시
SELECT userName, height FROM userTBL WHERE height >= 180 AND =< 183
	-- userTBL 테이블에서 height가 180 이상 183 이하인 userName, height 열 데이터 추출
SELECT userName, addr FROM userTBL WHERE addr='경남' or addr='전남' or addr='경북';
	-- userTBL 테이블에서 addr이 경남,전남,경북인 데이터의 userName, addr 열 데이터 추출

-- BETWEEN AND, IN 활용 예시
SELECT userName, height FROM userTBL WHERE height BETWEEN 180 AND 183
	-- userTBL 테이블에서 height가 180 이상 183 이하인 userName, height 열 데이터 추출
SELECT userName, addr FROM userTBL WHERE addr IN ('경남','전남','경북');
	-- userTBL 테이블에서 addr이 경남,전남,경북인 데이터의 userName과 addr 열 데이터 추출

-- %, _ 활용 예시	
SELECT userName, height FROM userTBL WHERE userName LIKE '김%';
	-- userTBL 테이블에서 userName이 김으로 시작하는 데이터의 userName, height 열 데이터 추출
SELECT userName, height FROM userTBL WHERE userName LIKE '_종신';
	-- userTBL 테이블에서 userName의 맨 앞이 한 글자이고, 종신인 데이터의 userName, height 열 데이터 추출
```

```sql
-- 오름차순, 내림차순 정렬
SELECT userName, mDate FROM userTBL ORDER BY mDate;
	-- userTBL 테이블에서 userName, mDate 열을 mdate 기준 오름차순으로 추출
SELECT userName, mDate FROM userTBL ORDER BY mDate ASC;
	-- userTBL 테이블에서 userName, mDate 열을 mdate 기준 오름차순으로 추출
SELECT userName, mDate FROM userTBL ORDER BY mDate DESC;
	-- userTBL 테이블에서 userName, mDate 열을 mdate 기준 내림차순으로 추출
SELECT userName, mDate FROM userTBL ORDER BY mDate DESC, userName ASC;
	-- userTBL 테이블에서 userName, mDate 열을 mdate 기준 내림차순, userName 기준 오름차순 추출
```

> 기본적으로 오름차순 정렬이기 때문에, ASC는 기본값으로 생략 가능하다.



```sql
-- DISTINCT
SELECT DISTINCT addr FROM userTBL;
	-- userTBL 테이블에서 addr 열을 중복된 것도 1개씩만 추출

-- ROWNUM
SELECT employee_id, hire_date FROM employees WHERE ROWNUM <= 5;
	-- employees 테이블에서 employee_id, hire_date 열을 전체 테이블에 저장된 상위 5건 추출
SELECT * FROM (SELECT userName, mDate FROM userTBL ORDER BY mDate ASC) WHERE ROWNUM <= 5;
	-- userTBL 테이블에서 userName, mDate 열을 mdate 기준 오름차순으로 상위 5건만을 추출

-- SAMPLE
SELECT employee_id, hire_date FROM employees SAMPLE(5);
	-- employees 테이블에서 employee_id, hire_date 열에서 무작위로 5%만을 추출
```



## INSERT INTO

INSERT는 테이블에 데이터를 삽입하는 명령어이다.

```sql
-- INSERT문의 형식
INSERT INTO 테이블(열1, 열2, ...) VALUES (값1, 값2, ...)
```



```sql
-- INSERT문의 예시
INSERT INTO memberTBL VALUES ('cik','최인규','서울 성북구 돈암동');
	-- memberTBL 테이블에 데이터 삽입
INSERT INTO memberTBL(memberName, memberAddress, memberID) VALUES ('최인규','서울 성북구 돈암동','Cik');
	-- memberTBL 테이블에 데이터 삽입
```

>  테이블 이름 뒤에 소괄호를 통해 열 이름을 적는 것이 원칙이나, 생략할 경우에는 VALUES 뒤에 나오는 값들의 순서 및 개수가 테이블이 정의된 열 순서 및 개수와 동일해야 한다.



## UPDATE SET

기존에 입력되어 있는 값을 변경하기 위해서는 UPDATE문을 사용한다.

```sql
-- UPDATE문의 형식
UPDATE 테이블 SET 열1=값1, 열2=값2, ... WHERE 조건
```



```sql
-- UPDATE문의 예시
UPDATE productTBL SET amount=100 WHERE productName='컴퓨터';
	-- productTBL 테이블에 productName이 컴퓨터인 데이터의 amount를 100으로 변경
```

> 만약 WHERE 조건을 작성하지 않음으로 인해, 희망하지 않는 데이터의 값이 바뀌었다면 롤백 기능을 사용하여 되돌릴 수 있다. 다만, 커밋한 이후 데이터를 롤백할 수 없게 된다.

## DELETE FROM

DELETE는 UPDATE와 거의 비슷한 개념으로, DELETE는 행 단위로 데이터를 삭제한다.

```sql
-- DELETE문의 형식
DELETE FROM 테이블 WHERE 조건
```



```sql
-- DELETE문의 예시
DELETE FROM productTBL WHERE productName='컴퓨터'
	-- productTBL 테이블에 productName이 컴퓨터인 데이터의 모든 행을 삭제 
```



## 기본 SQL문 예시 [CRUD]

```sql
회원가입
INSERT INTO memberTBL (id, pw, name) VALUES ('InKyu24','________','최인규')
```

```sql
로그인
SELECT * FROM memberTBL WHERE id='InKyu24' and pw='******'
```

```sql
회원정보 수정 (비밀번호 변경)
UPDATE memberTBL SET pw='******' WHERE id='InKyu24'
```

```sql
회원 탈퇴
DELETE FROM memberTBL WHERE id='InKyu24';
```



