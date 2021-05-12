# Chapter 7

## Oracle의 데이터 형식

### 숫자 데이터 형식

+ NUMBER(p,s)

  5~21바이트 전체 자릿수(p)와 소수점 이하 자릿수(s)를 가진 숫자형 데이터.
  NUMBER(5,2)는 전체 자릿수를 5자리로 하되, 그 중 소수점 이하를 2자리로 하겠다는 의미

> NUMBER						  >		1234567.888 [그대로 표현]
>
> NUMBER (9)					>		1234568 [소수점 아래 반올림]
>
> NUMBER (9,2)				 >		1234567.89 [소수점 아래 두자리까지 표현]
>
> NUMBER (9,1)				 >		1234567.9 [소수점 아래 두자리에서 반올림]
>
> NUMBER (*,1)				 >		1234567.9 [p의 전체 자리수(최대 38) 표현 및 소수점 아래 두자리에서 반올림
>
> NUMBER (7,-2)				>		1234600 [십의 자리에서 반올림]



### 문자 데이터 형식

+ CHAR[(n)]

  고정길이 문자형으로 n을 1~2,000바이트까지 지정.
  n없이 사용하면 CHAR(1)과 동일.

+ NCHAR[(n)]

  유니코드 고정길이 문자형. n을 1~1,000바이트까지 지정.
  한글을 저장할 수 있으므로 한 글자당 2바이트가 사용.
  n없이 사용하면 NCHAR(1)과 동일.

+ VARCHAR2(n)

  가변길이 문자형으로, n은 1~4000바이트까지 지정.

+ NVARCHAR2(n)

  유니코드 가변길이 문자형으로, n은 1~2000바이트까지 지정.
  한글을 저장할 수 있으므로 한 글자당 2바이트가 사용.

+ CLOB

  대용량의 영문 텍스트 데이터 타입. 최대 128TB.

+ NCLOB

  대용량 유니코드 텍스트 데이터 타입. 최대 128TB.



### 이진 데이터 형식

+ BLOB

  대용량 이진 데이터를 저장할 수 있는 데이터 타입. 최대 128TB

+ BFILE

  운영체제에 외부 파일 형태로 대용량 이진 데이터를 저장. 운영체제에서 허용하는 크기까지.



### 날짜와 시간 데이터 형식

+ DATE

  BC 4712부터 AC 9999년까지 저장. 연, 월, 일, 시, 분, 초까지 7바이트로 저장됨.

+ TIMESTAMP

  DATE와 같으나, 밀리초 단위까지 저장. 11바이트.

+ TIMESTAMP WITH TIME ZONE

  날짜 및 시간대 형태의 데이터 형식. 13바이트.

+ TIMESTAMP WITH LOCAL TIME ZONE

  날짜 및 시간대 형태의 데이터 형식. 11바이트
  조회 시에는 클라이언트의 시간대로 보여짐.

  

> 날짜 형식은 주로 DATE 형식을 사용한다.

```sql
-- 현재 날짜 출력
SELECT SYSDATE FROM DUAL;

-- 현재 날짜를 형식에 맞춰 출력
SELECT TO_CHAR(SYSDATE, 'YYYY/MM/DD HH:MM:SS') "현재 날짜" FROM DUAL;

-- 문자열을 날짜 형식으로 변환
SELECT TO_DATE('20201231235959', 'YYYYMMDDHH24MISS') "날짜 형식" FROM DUAL;
```



# Chapter 8

## 테이블 생성 및 삭제 (CREATE & DROP)

```sql
-- test 테이블 생성
Create table test (idNum number(5));

-- 테이블 내 데이터 삽입
insert into test (idNum) values(1);

-- 테이블 삭제
drop table test;
```

> DDL

> DML

```sql
-- userTBL 생성 (열 데이터 형식 지정 및 Null 유무)
Create table userTBL
(   userID      CHAR(8) NOT NULL,
    userName    NVARCHAR2(10) NOT NULL,
    bitthYear   NUMBER(4) NOT NULL,
    addr        NCHAR(2) NOT NULL, 
    mobile1     CHAR(3) NULL, 
    mobile2     CHAR(8) NULL, 
    height      NUMBER(3) NULL, 
    mDate       DATE NULL
);
```

> NOT NULL   : 반드시 값을 입력
>
> NULL			: 빈 값을 허용



## 기본 키 지정 (PRIMARY KEY)

```sql
-- userTBL 생성 및 기본키 지정 (1)
Create table userTBL
(   userID      CHAR(8) NOT NULL PRIMARY KEY,
    userName    NVARCHAR2(10) NOT NULL,
    bitthYear   NUMBER(4) NOT NULL,
    addr        NCHAR(2) NOT NULL, 
    mobile1     CHAR(3) NULL, 
    mobile2     CHAR(8) NULL, 
    height      NUMBER(3) NULL, 
    mDate       DATE NULL
);

-- userTBL 생성 및 기본키 지정 (2)
Create table userTBL
(   userID      CHAR(8) NOT NULL,
    userName    NVARCHAR2(10) NOT NULL,
    bitthYear   NUMBER(4) NOT NULL,
    addr        NCHAR(2) NOT NULL, 
    mobile1     CHAR(3) NULL, 
    mobile2     CHAR(8) NULL, 
    height      NUMBER(3) NULL, 
    mDate       DATE NULL,
 	PRIMARY KEY (userID)
);

-- userTBL 생성 및 기본키(기본키 제약조건 이름 포함) 지정
Create table userTBL
(   userID      CHAR(8) NOT NULL,
    userName    NVARCHAR2(10) NOT NULL,
    bitthYear   NUMBER(4) NOT NULL,
    addr        NCHAR(2) NOT NULL, 
    mobile1     CHAR(3) NULL, 
    mobile2     CHAR(8) NULL, 
    height      NUMBER(3) NULL, 
    mDate       DATE NULL,
 	CONSTRAINT PK_userID PRIMARY KEY (userID)
);
```

> PRIMARY KEY 기본키 설정 시 NOT NULL 생략 가능



## 외래 키 지정 (FOREIGN KEY)

```sql
-- buyTBL 생성 및 외래키 지정
Create  table buyTBL
(   idNum       NUMBER(8) NOT NULL PRIMARY KEY,
    userID      CHAR(8) NOT NULL,
    prodName    NCHAR(6) NOT NULL,
    groupName   NCHAR(4) NULL,
    price       NUMBER(8) NULL,
    amount      NUMBER(3) NOT NULL,
 	FOREIGN KEY(userID) REFERENCES userTBL(userID)
);

-- buyTBL 생성 및 외래키(외래키 제약조건 이름 포함) 지정
Create  table buyTBL
(   idNum       NUMBER(8) NOT NULL,
    userID      CHAR(8) NOT NULL,
    prodName    NCHAR(6) NOT NULL,
    groupName   NCHAR(4) NULL,
    price       NUMBER(8) NULL,
    amount      NUMBER(3) NOT NULL,
 	PRIMARY KEY (idNum),
 	CONSTRAINT FK_userID FOREIGN KEY (userID) REFERENCES userTBL(userID)
);
```



## 시퀀스 생성 (SEQUENCE)

```sql
-- 시퀀스 생성
Create sequence idSEQ;

-- 시퀀스 삭제
Drop sequence idSEQ;

-- userTBL에 데이터 삽입
insert into userTBL values ('LSG','이승기',1987,'서울','011','1111111',182,'2008-8-8');
insert into userTBL values ('KBS','김범수',1979,'경남','011','2222222',173,'2012-4-4');
insert into userTBL values ('KKH','김경호',1971,'전남','019','3333333',177,'2007-7-7');

-- buyTBL에 데이터 삽입
insert into buyTBL values (idSEQ.NEXTVAL,'KBS','운동화',NULL,30,2);
insert into buyTBL values (idSEQ.NEXTVAL,'KBS','노트북','전자',1000,1);
insert into buyTBL values (idSEQ.NEXTVAL,'JYP','모니터','전자',200,1); -- parent key not found 에러
```

idSEQ 시퀀스를 생성한 후에, idSEQ.NEXTVAL로 데이터를 입력하게 되면 순차적으로 1번부터 데이터가 입력이 된다. 하지만 마지막인 세번째 데이터는 parent key not found 에러로 입력이 되지 않았기 때문에, 그 다음에 들어가는 데이터는 4번을 부여받게 된다.



## 제약조건 (CONSTRAINTS)

제약조건이란 데이터의 무결성을 지키기 위한 제한된 조건을 의미한다. 특정 데이터를 입력할 때 무조건적으로 입력되지 않고, 어떠한 조건을 만족했을 때 입력될 수 있도록 제약할 수 있는 것이다. 동일한 ID나 EMAIL로 회원가입이 안되는 것도 동일한 데이터를 입력할 수 없는 제약 조건이 설정되어 있는 것이다.

모든 제약조건은 이름을 가지게 되는데, 제약 조건의 이름은 임의로 지정받을 수도 직접 지정할 수도 있다.

```sql
-- 제약 조건 확인
select * from user_constraints where table_name='USERTBL' and constraint_type='P';

-- 제약 조건이 있더라도 테이블 삭제
drop table userTBL CASCADE CONSTRAINTS;
```



대부분의 DBMS는 6가지의 제약조건(PRIMARY KEY 제약조건, FOREIGN KEY 제약조건, UNIQUE 제약조건, CHECK 제약 조건, DEFAULT 정의, NULL 값 허용)을 제공한다.

### PRIMARY KEY 제약조건

기본 키에 입력되는 값은 중복될 수 없으며, NULL 값이 입력될 수 없다.
기본 키로 생성한 것은 자동으로 인덱스가 생성된다.
기본 키는 하나의 열에만 설정할 수도 있으며, 두 개의 열을 합쳐서 기본 키로 설정할 수도 있다.

```sql
-- 테이블 생성과 동시에 두 개의 열에 기본키 설정
Create table prodTBL
(   prodCODE    CHAR(3) NOT NULL,
    prodID      CHAR(4) NOT NULL,
    prodDate    DATE    NOT NULL,
    prodCur     CHAR(10)    NULL,
    CONSTRAINT PK_prodTBL_prodCODE_prodID PRIMARY KEY (prodCODE, prodID)
);

-- 테이블 생성 후, 두 개의 열에 기본키 설정
Create table prodTBL
(   prodCODE    CHAR(3) NOT NULL,
    prodID      CHAR(4) NOT NULL,
    prodDate    DATE    NOT NULL,
    prodCur     CHAR(10)    NULL
);
ALTER TABLE prodTBL
    ADD CONSTRAINT PK_prodTBL_prodCODE_prodID
    PRIMARY KEY (prodCODE, prodID);
```



### FOREIGN KEY 제약조건

외래 키를 정의하는 테이블인 buyTBL을 '외래 키 테이블'이라고 하고, 외래 키에 의해 참조가 되는 테이블인 userTBL을 '기준 테이블'이라고 하면 더 이해하기 쉬울 것이다. 외래 키 테이블에 데이터를 입력할 때는 기준 테이블을 참조해서 입력하므로, 기준 테이블에 데이터가 존재하지 않는다면 데이터를 입력할 수 없다. 따라서 시퀀스 생성에서 작성된 마지막 코드는 에러가 발생하여, 데이터가 삽입되지 않았던 것이다.

외래 키 테이블이 참조하는 기준 테이블의 열은 반드시 Primary Key이거나, Unique 제약 조건이 설정되어 있어야 한다.

```sql
-- 테이블 생성 후, 외래키 설정
Create  table buyTBL
(   idNum       NUMBER(8) NOT NULL PRIMARY KEY,
    userID      CHAR(8) NOT NULL,
    prodName    NCHAR(6) NOT NULL,
    groupName   NCHAR(4) NULL,
    price       NUMBER(8) NULL,
    amount      NUMBER(3) NOT NULL
);
ALTER table buyTBL
	ADD CONSTRAINT FK_uesrID
	FOREIGN KEY (userID)
	REFERENCES userTBL(userID)
	ON DELETE CASCADE; -- 기준 테이블 데이터 삭제 시 외래 키 테이블 데이터도 자동 삭제되는 외래 키 옵션
	
-- 외래키 제거
ALTER table buyTBL
	Drop CONSTRAINT FK_uesrID
```



### UNIQUE 제약조건

UNIQUE 제약 조건은 '중복되지 않는 유일한 값'을 입력해야 하는 조건이다. PRIMARY KEY와 유사하나 UNIQUE 제약조건은 NULL값을 허용한다는 것에 차이가 있다.



```sql

```

```sql

```



### CHECK 제약 조건

CHECK 제약 조건은 입력되는 데이터를 점검하는 기능을 한다. 예로 '마이너스 값이 들어올 수 없다' 등의 조건을 지정한다. CHECK 제약 조건이 설정된 후에는 제약 조건에 위배되는 값은 입력이 안된다. ALTER TABLE 옵션에서 ENABLE NOVALIDATE 옵션이 있는데, 이는 기존에 입력된 데이터가 제약 조건을 위배하더라도 무시하고 넘어간다는 옵션이다.

```sql

```

```sql


	
```



### DEFAULT 정의

DEFAULT는 값을 입력하지 않았을 때, 자동으로 입력되는 기본 값을 정의하는 방법이다.

출생년도를 입력하지 않으면 -1을 입력하고, 주소를 입력하지 않았다면 '서울'이 입력되며, 키를 입력하지 않으면 170이라고 입력되도록 하고 싶다면 아래와 같이 정의할 수 있다.

```sql
-- 테이블 생성과 동시에 DEFALUT 정의
create table userTBL
( userId char(8) NOT NULL Primary key,
  userName     nvarchar2(10) not null,
  birthYear    number(4) default -1 not null,
  addr         nchar(2) default '서울' not null, 
  mobile1      char(3) null, 
  mobile2      char(8) null,
  height       number(3) default 170  null,
  mDate        date null
);

-- 테이블 생성 후 DEFAULT 정의
create table userTBL
( userId 	   char(8) NOT NULL Primary key,
  userName     nvarchar2(10) not null,
  birthYear    number(4) not null,
  addr         nchar(2) not null, 
  mobile1      char(3) null, 
  mobile2      char(8) null,
  height       number(3) default 170  null,
  mDate        date null  
);
Alter Table userTBL
    MODIFY birthyear DEFAULT -1;
Alter Table userTBL
    MODIFY addr DEFAULT '서울';
Alter Table userTBL
    MODIFY height DEFAULT 170; 

-- DEFAULT 값을 포함하는 데이터 입력
insert into userTBL values
('LSG','이승기',default,default,'011','1111111',default,'2008-8-8');
insert into userTBL(userID,userName,mobile1,mobile2,mdate) values
('CIK', '최인규','010','7777777','2021-2-17');
```



### NULL 값 허용

Null 값은 '아무 것도 없다'라는 의미이다. 즉, `space`를 누른 공백(' ')이나 0과 같은 값들과는 다르다.

```sql
-- NULL 값 테스트
insert into userTBL values ('KBS','김범수',1979,'경남','011',NULL,173,'2012-4-4');
insert into userTBL values ('KKH','김경호',1971,'전남','019','',177,'2007-7-7');
insert into userTBL values ('LSG','이승기',1987,'서울','011',' ',182,'2008-8-8');
```

따라서 위의 두 코드의 mobile2 열의 값은 (NULL)로 표현된다. 하지만 마지막 코드의 mobile2 열의 값은 공백으로 입력이 되어 빈 칸으로 나타난다.