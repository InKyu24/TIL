## 1. Java 프로그래밍 순서

[![img](https://1.bp.blogspot.com/-lCkwpX50sCY/YBEaF1aQOmI/AAAAAAAAGKc/BevZwmUmtTUJZC47hQR4CWQbd6E0kCZSgCLcBGAsYHQ/w640-h592/%25E3%2584%25B1.png)](https://1.bp.blogspot.com/-lCkwpX50sCY/YBEaF1aQOmI/AAAAAAAAGKc/BevZwmUmtTUJZC47hQR4CWQbd6E0kCZSgCLcBGAsYHQ/s955/%E3%84%B1.png)

Java는 웹 기반 언어로 Eclipse는 보통 메모장보다 더 똑똑하게 SourceCode를 작성할 수 있게 하는 역할을 한다

> IDE : Integrated Development Environment 

SourceCode는 자연어와 유사한 언어로 작성된 코드로 .java의 확장자를 갖는다. SourceCode는 javac.exe로 번역되어 .class의 확장자를 갖는 반기계어인 ByteCode 파일이 생기게 된다. 그리고 ByteCode 파일은 JRE에 의해 실행되게 된다.

JRE 내 Class Loader가 클래스를 읽어오며, ByteCodeVerifier가 검수, MachineCode Generator가 완전한 기계어로 바꾸며, JVM에서 main method를 제외한 Static Member data를 초기화를 진행한다.

이후 상속 관계를 파악하고, main method를 실행하고, 데이터를 4byte를 기준으로 할당(register)한다.

> JVM의 역할: CPU 할당, 메모리 관리, register 제공



## 2. 데이터가 메모리에 저장되는 과정

```java
package test.datatype;   //패키지 선언
public class Test {     //클래스 선언
    	/*A 위치*/
	public static void main(String[] args) { // 시작 메소드
	    /*B 위치*/                          
    }
}
```

\- **A 위치**에 선언되는 데이터 : Member data [Eden에 저장]
\- **B 위치**에 선언되는 데이터 : Local data [Stack에 저장]



Test.java를 가진 상태에서 컴파일을 하면 Test.class라는 바이트 코드를 얻게 된다.
(참조된 파일이 있다면 그것도 자동으로 컴파일 진행)

[![img](https://1.bp.blogspot.com/-wL0eiq7Khnw/YBEVJI66ftI/AAAAAAAAGKE/qi4QOxaew1MK2SzEinyxTeRqFGRmQaLzQCLcBGAsYHQ/w640-h376/%25E3%2584%25B4.png)](https://1.bp.blogspot.com/-wL0eiq7Khnw/YBEVJI66ftI/AAAAAAAAGKE/qi4QOxaew1MK2SzEinyxTeRqFGRmQaLzQCLcBGAsYHQ/s1649/%E3%84%B4.png)



```java
[Test.java]
package test.datatype;
public class Test {
  	public static void main(String[] args) {
       	int age=31;
       	double tall=177.5D;
       	char gender='남';
       	boolean isNice=true;
       	MemberName name=new MemberName();

       	System.out.println(age);
       	System.out.println(tall);
       	System.out.println(gender);
       	System.out.println(isNice);
     	System.out.println(name.name1+""+name.name2+""+name.name3);
   	}
}
```

```java
[Membername.java]
package test.datatype;
public class MemberName {
   	char name1='최';
    char name2='인';
   	char name3='규';
}
```

****

* Stack 영역: [age, tall, gender, isNice 값]. [name으로 참조된 주소]
* Eden 영역: [name1. name2, name3 값]

>  기본형 데이터는 객체값을 가지고. 참조형 데이터는 주소값을 가진다.

 

## 3. 객체를 만들어야 하는 개연성

장구, 북, 징을 연주하는 철수가 있다. 그리고 영희는 장구와 꽹과리를 연주하려고 한다.

객체지향언어를 이용한다면, 영희는 철수의 장구.class를 객체로 호출하여 이를 재사용할 수 있다.

 

## 4. 문자열을 더욱 편리하게, String 클래스 재사용

```java
[Test.java]
MemberName name=new MemberName();

[Membername.java]
package test.datatype;
public class MemberName {
    	char name1='최';
	    char name2='인';
    	char name3='규';
}
```

Membername.java 클래스의 char 변수들을 String name=new String(“최인규”); 로 대체할 수 있게 된다.

따라서 문자열을 사용하기 위해서는 이제 개별 변수들을 하나하나 생성할 필요 없이 String 클래스를 사용한다.

> String : 주소값을 나타내지 않고, 자동으로 결과값을 찾아서 보여주는 클래스. 메모리 효율성을 위해 참조형 데이터 타입이 아닌 기본형 데이터 타입으로 사용 가능하다.



```java
package test.datatype;
public class StringTest {
    public static void main(String[] args) {
        String s1=new String("java");
        String s2=new String("java");              

        String s3="java";
        String s4="java";
    }
}
```

* new로 생성된 s1과 s2는 Instance[Eden] 영역에 저장되어 있으며, 서로 다르다. Instance 영역에서는 Garbage Collector 기능이 있기 때문에 자동으로 메모리를 효율적으로 관리한다.

+ 하지만 s3와 s4는 서로 같다. (Heap의 Method area 내 String Literal Pool 공간에 할당되고, c-value comparator에서 문자열을 서로 비교해서 같은 내용의 문자열을 중복 저장하지 않게 하기 때문이다.)

  String Literal Pool에는 Garbage Collector 기능이 없기 때문에 꽉 차게 되면 OOME 발생

 

## 5. 날짜를 더욱 편리하게, java.util.Date 클래스 재사용하기

```java
package test.datatype;
import java.util.Date;
public class Test {
	public static void main(String[] args) {
		Date birthday=new Date(1991,2,4);
		System.out.println(birthday.getYear()+"년");
    }
}
```



## 6. UI 제작을 위해, java.awt 내 클래스 재사용 (Button, Frame)

```java
package test.datatype;
import java.awt.BorderLayout;
import java.awt.Button;
import java.awt.Frame;   // import 세 라인을 import java.awt.*; 으로 대체가능

public class MyUI {
	public static void main(String[] args) {
		Button b=new Button("SEND"); //SEND라고 써있는 b버튼 생성.
		Frame f=new Frame();  	     //f프레임 생성.
		f.add(b,BorderLayout.SOUTH); //f프레임에 b버튼을 하단에 추가.
		f.setSize(500, 400);    	 //f프레임 사이즈 500*400.
		f.setVisible(true);      	 //f프레임이 보여지게 세팅.
	}
}
```



## 7. Default value 확인

```java
package Prj1.shop;
public class Customer {
	String name; 					//값 없이 name 선언.
	String address; 				//값 없이 address 선언.
	String phone;					//값 없이 phone 선언.
	char gender;					//값 없이 gender 선언.
	int age;						//값 없이 age 선언.
	double tall;					//값 없이 tall 선언.
	boolean isPretty;				//값 없이 isPretty 선언.
}
```

```java
package Prj1.shop;
public class Shop {
	public static void main(String[] args) {
		Customer c1=new Customer();
		System.out.println(c1);				//주소값
		System.out.println(c1.name);		//null
		System.out.println(c1.gender);		//빈 칸
		System.out.println(c1.age);			//0
		System.out.println(c1.tall);		//0.0
		System.out.println(c1.isPretty);	//false	
	}
}
```

