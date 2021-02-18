# JDBC 

JDBC는 Java DataBase Connectivity의 약자로, Java에서 DB 프로그래밍을 하기 위해 사용되는 API의 일종이다. JDBC API는 `java.sql` 패키지에 의해 구현되고, 이 패키지를 통해 여러 종류의 데이터베이스에 접근할 수있다.

쉽게 말하면 JDBC는 DB에 데이터를 삽입, 수정, 삭제할 때 SQL Developer를 사용하지 않더라도, Java에서 SQL문을 이용하여 DB에 작업을 할 수 있도록 하는 다리 역할을 한다는 것이다. JDBC는 DBMS의 종류에 관계없이 독립적으로 사용이 가능하다는 장점이 있다. 즉, 다양한 벤더들도 JDBC를 이용하면 동일하에 SQL문을 Java에서 사용할 수 있다. 

> `java.sql` 패키지 : RDBMS의 데이터에 접속해 처리할 수 있는 단일 API를 제공.



![img](https://lh3.googleusercontent.com/-Xcu4ovgAzhY/YC3JydZTFrI/AAAAAAAAGXQ/jA-MAvWrcT8KMUheJOP9U_O6fRkmQTycwCLcBGAsYHQ/w640-h202/%25EA%25B7%25B8%25EB%25A6%25BC1.png)



## JDBC 프로그래밍 절차 6단계

### 1단계 : 드라이버 등록 (Driver Loading)

드라이버 클래스에 객체 생성

```java
Class.forName("Driver");
```

>  Java Build Path > Libraries > Add External JARs 를 통해 Oracle 홈페이지에서 다운로드 한 .jar 확장자의 드라이버를 가져온다.



### 2단계 : 연결 (Connection)

```java
Connection con = DriverManager.getConnection("URL", "User", "Password");
```

>jdbc.driver = **oracle.jdbc.driver.OracleDriver**
>jdbc.url=**jdbc:oracle:thin:@localhost:1521:xe**
>jdbc.username = **shop**
>jdbc.password = **1234**



### 3단계 : 생성 (Statement)

반환된 Connection 객체를 이용해서 SQL문을 실행하고 그 결과를 반환 받을 수 있는 Statement 객체를 생성하는 단계.

```java
Statement stmt = con.createStatement();
```



### 4단계 : SQL문 전송

```java
ResultSet rs = stmt.executeQuery("SQL문");
```



### 5단계 : 결과 얻기

```java
while (rs.next()) {
    int id = rs.getInt("id");
    String name = rs.getString("name");
    String address = rs.getString(3) // 컬럼 순서를 통해 결과를 얻기도 가능
}
```



### 6단계: 자원 닫기

진행 했던 순서의 역순으로 자원을 닫는 것이 안전하다.

```java
rs.close();
stmt.close();
con.close();
```



## JDBC 6단계 실습

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class Test {
	public static void main(String[] args) {
		Connection con = null;
		Statement stmt =null;
		ResultSet rs = null;
		
		try {	
		// 1. Driver Loading
			Class.forName("oracle.jdbc.driver.OracleDriver");
			System.out.println("Loading Success");
		
		// 2. Connection
			con = DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe", "SHOP", "1313");
			System.out.println("Connection Success");
		
		// 3. Statement
			stmt = con.createStatement();
			System.out.println("Statement Success");
			
		// 4. SQL 전송
			rs = stmt.executeQuery("select * from memberTBL");
			
		// 5. 결과 얻기
			System.out.println("This is the Result");
			while(rs.next()) {
				String id = rs.getString("MEMBERID");
				String name = rs.getString("MEMBERNAME");
				String addr = rs.getString(3);
				System.out.println(id+":"+name+":"+addr);
			}	
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		} catch (SQLException e) {
			e.printStackTrace();
			
		// 6. 자원종료 [finally 블럭에서!]
		} finally {
			try {
				if(rs!=null) {rs.close();}
				if (stmt!=null) {stmt.close();}
				if (con!=null) {con.close();}
			} catch (SQLException e) {
				e.printStackTrace();
			} 	
		}
	}
}
```



## Statement의 확장

Statement을 상속하고 있는 PreparedStatement, 그리고 PreparedStatement을 상속하고 있는 CallableStatement이 있다. 

여기서는 Statement와 PreparedStatement를 알아보고자 한다. 이 둘의 가장 큰 차이는 SQL문이 들어가는 위치와 SQL문 실행 메소드 작성 시 argument 유무에 있다.



> SQL문을 실행하기 위해서는 execute(), executeQuery(), executeUpdate()  메소드를 이용한다.
>
> execute(); 			 	실행해야 할 SQL문의 종류를 모르는 경우 사용
> executeQuery();   	주로 Select와 같이 DB에 변경을 주지 않는 SQL문을 실행할 경우 사용
> executeUpdate(); 	DB 값이나 구조에 변경을 주는 SQL문을 실행할 경우 사용 [숫자 데이터 반환]



### Statement

Statement 인터페이스에서 가장 최상위에 위치하고 있으며, Connection 객체에서 createStatement() 메소드 호출로 생성된다. 가장 쉽게 이용할 수 있는 인터페이스이기 때문에 단순한 SQL 문장을 보낼 때 사용되며, 성능이나 효율성이 낮다는 단점이 있다.

```java
Statement stmt = con.createStatement();
	ResultSet rs = stmt.executeQuery("SQL문");
	while(rs.next()) {
		String id = rs.getString(1);
		String name = rs.getString(2);
		String date = rs.getString(3);
		String phone = rs.getString(4);
    }
```



### PreparedStatement

PreparedStatement는 높은 성능 향상, 빠른 처리 속도로 Statement의 단점을 보완해준다. Connection 객체에서 prepareStatement() 메소드로 생성하며, 여러 번 반복해서 사용되는 SQL을 다루는 경우에 더욱 편리하다. 

PreparedStatement는 메소드 생성과 동시에 SQL문 작성이 이루어지며, execute 메소드 내에 argument를 넣지 않는다는 특징이 있다. 가장 큰 특징은 데이터 바인딩 변수를 사용한다는 것이다. SQL문에 물음표가 있으면 값을 대입하여 실행이 된다.

```java
PreparedStatement stmt = con.prepareStatement("Insert into member values (?,?,?,?,?) ");
	stmt.setString(1, m.getMemid());
	stmt.setString(2, m.getName());
	stmt.setDate(3, new Date(m.getmDate().getTime()));
	stmt.setString(4, m.getPhone());
	stmt.setInt(5, m.getPoint());
```

>  Stored Procedure : 클라이언트에서 SQL 문을 실행하는 것과 달리 DB 쪽에서 Procedure로 존재하기 때문에, 클라이언트에서 저장된 프로시저를 실행만 하면 바로 처리가 될 수 있어, 빠른 속도를 낼 수 있다.



#### PreparedStatement를 통한 Insert문

```java
PreparedStatement stmt = null;
stmt = con.prepareStatement("insert into member values(?,?,?,?,?)"); 
	stmt.setString(1,args[0]);
	stmt.setString(2,args[1]);
	java.util.Date today = new java.util.Date();
	Date now = new Date(today.getTime());
	stmt.setDate(3, now);

	int i = stmt.executeUpdate();
```



#### PreparedStatement를 통한 Update문

```java
PreparedStatement stmt = null;
stmt = con.prepareStatement("update member set address=? where name=?");
	stmt.setString(1, args[0]); 
	stmt.setString(2, args[1]);
	
	int i = stmt.executeUpdate();
```



#### PreparedStatement를 통한 Delete문

```java
PreparedStatement stmt = null;
stmt = con.prepareStatement("Delete from member where memid=?");
	stmt.setString(1, args[0]); 
```



#### PreparedStatement를 통한 Create문

```java
PreparedStatement stmt = null;
stmt = con.prepareStatement("Create table Product(Pno integer, Pname varchar(20), Price integer)");
```



#### PreparedStatement를 통한 Drop문

```java
PreparedStatement stmt = null;
stmt = con.prepareStatement("Drop table Product");
```

