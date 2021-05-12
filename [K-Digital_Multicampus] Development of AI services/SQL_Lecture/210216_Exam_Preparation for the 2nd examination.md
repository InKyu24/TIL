1. 변수의 타입을  확인할 수 있는 함수는?

   1) function() 	2) int() 	<u>***3) type()***</u> 	4) check()

   

2. 다음과 같은  테이블이 있을 때 데이터를 추가하기 위한 표준 SQL 문장으로 옳은 것은?

   [![img](https://lh3.googleusercontent.com/-P0AAUWUjrJE/YCuXFSqAJkI/AAAAAAAAGW8/RnJd1X358s0aLS8aohnIj49oqH_ZnpkVACLcBGAsYHQ/image-20210216183125727.png)](https://lh3.googleusercontent.com/-P0AAUWUjrJE/YCuXFSqAJkI/AAAAAAAAGW8/RnJd1X358s0aLS8aohnIj49oqH_ZnpkVACLcBGAsYHQ/image-20210216183125727.png)

   <u>***1)	insert into stock values ("sun",  10.5);***</u> 

   2)	insert into stock values (~~sun~~, 10.5); 

   3)	insert into stock (symbol, price) values ("sun"~~);~~ 

   4)	insert into stock values ("sun"~~);~~ 

   

3. 다음과 같은 테이블을 만들기 위한 표준 SQL문장으로 옳은 것은?

   [![img](https://lh3.googleusercontent.com/-P0AAUWUjrJE/YCuXFSqAJkI/AAAAAAAAGW8/RnJd1X358s0aLS8aohnIj49oqH_ZnpkVACLcBGAsYHQ/image-20210216183125727.png)](https://lh3.googleusercontent.com/-P0AAUWUjrJE/YCuXFSqAJkI/AAAAAAAAGW8/RnJd1X358s0aLS8aohnIj49oqH_ZnpkVACLcBGAsYHQ/image-20210216183125727.png)

​		1)	CREATE  TABLE stock ( symbol char(20) not null, price float(10,2) default 0.00 );

​		***2)	CREATE  TABLE stock ( symbol char(20) <u>primary key</u>, price float(10,2) default 0.00  );*** 

​		3)	CREATE ~~stock TABLE~~ ( symbol char(20) not null,  price float(10,2) default 0.00 );

​		4)	CREATE  ~~stock TABLE~~ ( symbol char(20) primary key, price float(10,2) default 0.00 );



4. 다음과 같은 테이블에서 price 필드의 값이 10인 모든 행에 대해  price필드의 값을 20으로 변경하기 위한 표준 SQL 중 적절한 것은?

   [![img](https://lh3.googleusercontent.com/-P0AAUWUjrJE/YCuXFSqAJkI/AAAAAAAAGW8/RnJd1X358s0aLS8aohnIj49oqH_ZnpkVACLcBGAsYHQ/image-20210216183125727.png)](https://lh3.googleusercontent.com/-P0AAUWUjrJE/YCuXFSqAJkI/AAAAAAAAGW8/RnJd1X358s0aLS8aohnIj49oqH_ZnpkVACLcBGAsYHQ/image-20210216183125727.png)

   ​	1)	update  stock set price=20 where ~~symbol="sun";~~ 

   ​	2)	update stock set symbol="sun"  where price=~~20~~; 

   ​	3)	update  stock (price=20) where ~~symbol="sun";~~

   ​	***<u>4)	update stock set price=20 where price=10;</u>***

   

5. 다음과 같은 테이블에서 price 필드의 값이 10인 모든 행을 삭제하기 위한 표준 SQL 중 적절한 것은?

   [![img](https://lh3.googleusercontent.com/-P0AAUWUjrJE/YCuXFSqAJkI/AAAAAAAAGW8/RnJd1X358s0aLS8aohnIj49oqH_ZnpkVACLcBGAsYHQ/image-20210216183125727.png)](https://lh3.googleusercontent.com/-P0AAUWUjrJE/YCuXFSqAJkI/AAAAAAAAGW8/RnJd1X358s0aLS8aohnIj49oqH_ZnpkVACLcBGAsYHQ/image-20210216183125727.png)

   ​	***<u>1)	delete  from stock where price=10;</u>*** 

   ​	2)	delete  ~~set~~ symbol="sun" where price=10; 

   ​	3)	delete  from stock ~~set~~ symbol="sun";. 

   ​	4)	delete  from stock where ~~symbol="sun";~~

   

6. 다음과 같은 테이블에서 symbol필드의 값이 sun 인 데이터의 가격(price)만을 조회하기 위한 표준 SQL 중 적절한 것은?

   [![img](https://lh3.googleusercontent.com/-P0AAUWUjrJE/YCuXFSqAJkI/AAAAAAAAGW8/RnJd1X358s0aLS8aohnIj49oqH_ZnpkVACLcBGAsYHQ/image-20210216183125727.png)](https://lh3.googleusercontent.com/-P0AAUWUjrJE/YCuXFSqAJkI/AAAAAAAAGW8/RnJd1X358s0aLS8aohnIj49oqH_ZnpkVACLcBGAsYHQ/image-20210216183125727.png)

   ​	1)	select ~~*~~  from stock; 

   ​	2)	select ~~*~~  from stock where price=10; 

   ​	*<u>**3)	select  price from stock where symbol="sun";**</u>* 

   ​	4)	select  price from stock where symbol ~~"sun";~~

   

7. 다음 중  JDBC를 사용했을 때의 효용성에 대한 설명으로 틀린 것은?

   ​	1)	사용하는  RDBMS에 독립적인 프로그래밍이 가능하다. 

   ​	2)	몇 개의 변수에  대한 조작으로 RDBMS의 교체가 가능하다. 

   ​	*<u>**3)	표준의 SQL 문장~~만~~을 지원함으로써 범용성을 증대시킨다.**</u>* 

   ​	4)	자바는 단순히  문자열로 query를 전달할 뿐이고 해석은 각각의 벤더가 구현한 driver에서 담당한다. 

   

8. 다음은  JDBC를 이용한 일반적인 조회 과정이다. 순서대로 나열한 것은?

   `1.ResultSet 획득` `2.접속 close` `3.Driver Loading` `4.Statement 생성` `5.Connection 생성`

   ​	1)	5-3-4-2-1 

   ​	***<u>2)	3-5-4-1-2</u>*** 

   ​	3)	3-4-5-1-2 

   ​	4)	5-4-3-1-2 

   

9. 적절한 JDBC  드라이버를 로딩하여 con 이라는 이름으로 JDBC Connection 객체를 생성하였다.

   다음 중 생성한 Connection으로부터  질의를 위한 Statement를 얻는 내용은?.

   ​	1)	Statement  stmt = con.getStatement(); 

   ​	2)	Statement stmt =  Connection.createStatement(); 

   ​	***<u>3)	Statement  stmt = con.createStatement();</u>*** 

   ​	4)	Statement  stmt = Connection.getStatement(); 

   

10. 성능과 보안을  위해서는 Statement보다 PreparedStatement가 좋다.

    다음 중 PreparedStatement를 얻는  Connection의 메소드는?

    ​	1)	PreparedStatement(String  sql)

    ​	2)	preparedStatement(String  sql)

    ​	3)	PrepareStatement(String  sql)

    ​	***<u>4)	prepareStatement(String  sql)</u>***

    

11. 다음은  PreparedStatement를 이용해서 DB에 질의하는 SQL을 표현한 것중 옳은 것은?

    ​	***<u>1)	"insert  into members values( ?, ?, ? )"</u>*** 

    ​	2)	"insert  into members values( a, b, c )"

    ​	3)	"insert  into members values( &, &, &)"

    ​	4)	("insert  into members values( "?", "?", "?" )" 

    

12. 다음은  java.sql.ResultSet 클래스에 관한 설명입니다. 틀린 것을 고르시오.

    ​	1)	RDBMS에  select에 관련된 질의를 했을 경우 리턴되어지는 타입이다.

    ​	***<u>2)	최초에 리턴  되었을 때는 커서는 ~~결과의 첫 번째 데이터~~를 가리킨다.</u>*** 

    ​	3)	다음 행(row)으로 이동할 때에는 next() 메서드를 이용한다. 

    ​	4)	특정 컬럼의  데이터를 조회하기 위해서는 getXXX(int index) 또는 getXXX( String column_name)을 사용한다. 이때  XXX는 컬럼의 타입과 매핑된다. 

     

13. SQL 구문  가운데 insert, delete와 update를 실행하려고 한다. Statement 인터페이스에서 어떤 메소드를 사용해야 하는가?

    ​	1)	getConnection()

    ​	2)	getResultSet()

    ​	3)	executeQuery(String  sql)

    ​	***<u>4)	executeUpdate(String  sql)</u>***

    

14. Statement의  executeQuery의 리턴타입으로 옳은 것은?

    ​	1)	Connection

    ​	***<u>2)	ResultSet</u>***

    ​	3)	ResultSetMetaData

    ​	4)	int

    

15. Statement의  executeUpdate의 리턴타입으로 옳은 것은?

    ​	1)	Connection

    ​	2)	ResultSet

    ​	3)	ResultSetMetaData

    ​	***<u>4)	int</u>***

    

16. DriverManager  클래스가 속해있는 패키지는?

    ​	1)	java.util

    ​	2)	java.lang

    ​	***<u>3)	java.sql</u>***

    ​	4)	javax.sql

    

17. DriverManager의  getConnection에 들어 갈 데이터베이스 URL의 첫번째 문자열은 무엇인가?

    ​	1)	db,

    ​	2)	db:

    ​	3)	jdbc,

    ​	***<u>4)	jdbc:</u>***

    

18. 다음 코드의  여기 부분에 들어갈 SQL로 가장 알맞은 것은? 

    ```java
    int floor =1;
    String sql = " /*여기*/   ";  
    psmt =  con.prepareStatement(sql);   
    psmt.setInt(1, floor);  
    rs = psmt.executeQuery();     
    while(rs.next()) {     
        int a = rs.getInt("deptno"); 
        String b =  rs.getString("deptname"); 
        int c =  rs.getInt("floor");     
        System.out.println("deptno은  "+a+"deptname은 "+b+"floor은 "+c);     
    }
    ```

    ​	1)	select *  from department 

    ​	2)	select ?  from department 

    ​	***<u>3)	select *  from department where floor=?</u>***

    ​	4)	select *  from department where floor=1

    

19. notice  라는 이름의 테이블에서 조회수(hit)가 10초과의 행만 조회하기 위한 SQL은?

    ​	***<u>1)	select *  from notice where hit > 10</u>***

    ​	2)	select *  from notice where hit over 10

    ​	3)	select *  from notice where ~~hit >= 10~~

    ​	4)	select *  from notice where hit ?= 10

    

20. 다음 코드의  여기 부분에 들어갈 알맞은 코드는?    

    ```java
    String sql = "insert into department(deptno, deptname, floor) values  (?,?,?)";
    int deptno = 1;      
    String deptname =  "deptname";  
    int floor = 1;            
    psmt =  con.prepareStatement(sql);       
    /*여기*/
    psmt.executeUpdate();
    ```

    ​	1)	psmt.setInt(~~0~~,  deptno);       psmt.setString(~~1~~, deptname);       psmt.setInt(~~2~~, floor);

    ​	2)	psmt.setInt(~~0~~,  deptno);       psmt.set~~Int(1~~, deptname);       psmt.setInt(~~2~~, floor);

    ​	***<u>3)	psmt.setInt(1,  deptno);       psmt.setString(2, deptname);       psmt.setInt(3, floor);</u>***

    ​	4)	psmt.setInt(1,  deptno);       psmt.set~~Int~~(2, deptname);       psmt.setInt(3, floor);

    

21. PreparedStatement의  선언부로 바른 것은?

    ​	1)	public  interface PreparedStatement implements Statement

    ​	***<u>2)	public  interface PreparedStatement extends Statement</u>*** 

    ​	3)	public  class PreparedStatement implements Statement

    ​	4)	public  class PreparedStatement extends Statement 

    

22. 다음 중 반납과 상관없는 자원은?

    ​	***<u>1)	DriverManager</u>***

    ​	2)	Connection

    ​	3)	PreparedStatement

    ​	4)	ResultSet

    

23. 자바 독립형 어플리케이션이 다른 서버나 미들웨어 없이 데이터베이스와 연결하고 있다면 다음 중 어떤 구조인가?

    ​	1)	1-tier  architecture

    ​	***<u>2)	2-tier  architecture</u>***

    ​	3)	3-tier  architecture

    ​	4)	4-tier  architecture

    

24. SQL 타입으로  VARCHAR형의 데이터를 받을 수 있는 메소드 이름은?

    ​	1)	getVarchar

    ​	2)	getCharacter

    ​	3)	getChar

    ​	***<u>4)	getString</u>***

    

25. 퀴리의 결과 데이터를 얻을 수 있는 인터페이스는?

    ​	1)	Connection

    ​	2)	PreparedStatement

    ​	***<u>3)	ResultSet</u>***

    ​	4)	DriverManager

    

26. Connection의  close 메소드가 들어가기에 가장 적당한 블락은?

    ​	1)	try { 여기 }

    ​	2)	catch(Exception  e) { 여기 }

    ​	***<u>3)	finally {  여기 }</u>***

    ​	4)	main( ) {  여기 }

