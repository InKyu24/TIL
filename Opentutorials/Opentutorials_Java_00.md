## Java

Write once, Run anywhere [한번 작성하면, 어디서든 실행된다.]



## 기초

### 온라인 편집기를 개발환경으로 이용하기

Java를 설치하기 이전에`JAVA online editor`를 검색하면 여러가지 좋은 도구들이 나온다. 그 중에서 https://jdoodle.com이라는 도구를 이용해서 익혀보자. 



### Java 설치 (Windows)

Oacle 홈페이지에서 JDK(Java Development Kit)를 다운로드 하여 설치한다. 이후 윈도우에서 cmd를 실행하고, `java -version`과 `javac -version`을 입력해서 버전 정보가 출력되면 제대로 설치된 것이다. 만약 제대로 버전 정보가 나타나지 않는다면 Path를 수정해주어야 한다. 

윈도우 탐색기에서 JDK가 설치된 경로를 확인 및 복사(bin 디렉토리 이전까지)하고, 내 컴퓨터에서 속성, 고급 시스템 설정, 환경 변수 순으로 들어가서 새로 만들기를 통해`JAVA_HOME`이라는 변수 이름과 복사한 설치 경로를 변수 값으로 붙여넣기한다. 또한 시스템 변수 내 `Path`를 편집해서 `%JAVA_HOME%\bin`을 추가한다. 그 후에 다시 cmd를 실행하여 다시 한 번 버전을 확인해서 버전 정보가 출력된다면 JAVA의 설치가 완료된다.



### 이클립스 설치

Java를 이용해서 프로그램을 만들려면, 기본적인 도구가 필요하다.  많은 도구들 중에서 가장 많은 Java 개발자들이 사용하는 이클립스를 설치해서 이용해보자. 이클립스 홈페이지에서 Eclipse IDE를 다운로드하여 설치하면 된다. workspace는 프로젝트들이 저장되는 경로를 지정하면 된다.



### 이클립스 실행

'HelloWorld'라는 Java Project를 생성하고, 'HelloWorldApp'이라는 클래스를 생성한 뒤에 아래와 같이 작성한다.

```java
public class HelloWorldApp{
	public static void main(String[] args) {
		System.out.println("Hello world!!");
	}
}
```

그리고 오른쪽 클릭하고, `Run as` 버튼을 클릭하여 코드를 실행한다. Console창에 결과값이 출력된 것을 확인한다.



### Java의 동작원리

원인과 결과가 있다. 원인이라는 같은 대상을 source, code, language라는 단어로 관점에 따라 다르게 불리며, 결과는 application, program이라는 단어로 불린다.

확장자가 .java인 파일(Java Source Code)은 인간이 Java라는 컴퓨터 언어로 작성하고 이해할 수 있는 언어로 작성되어 있다. 기계가 확장자가 .java인 파일을 이해하기 위해서 컴파일이라고 불리는 전환하는 단계를 거쳐 확장자가 .class인 파일(Java application)을 생성한다. 그리고 이클립스를 통해 Run as 버튼을 클릭하면, JVM(Java Virtual Machine)이 확장자가 .class인 파일을 읽어서 컴퓨터를 동작시킨다.



### Java로 할 수 있는 일



#### Java로 데스크탑 앱 만들기

Java를 이용하면 데스크랍 애플리케이션을 만들어 낼 수 있다.

아래 코드들을 살펴보면서, 조금씩 코드에 익숙해지자.

```java
import javax.swing.*;   
import java.awt.Dimension;
import java.awt.Toolkit;
public class HelloWorldGUIApp{
    public static void main(String[] args){
        javax.swing.SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                JFrame frame = new JFrame("HelloWorld GUI");
                frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
                frame.setPreferredSize(new Dimension(800, 300));
                JLabel label = new JLabel("Hello World!!", SwingConstants.RIGHT);
                frame.getContentPane().add(label);
                Dimension dim = Toolkit.getDefaultToolkit().getScreenSize();
                frame.setLocation(dim.width/2-400/2, dim.height/2-300/2);

                frame.pack();
                frame.setVisible(true);
            }
        });
    }
}
```



#### Java로 사물 제어하기 (IoT)

Java를 이용해서 라즈베리파이에 연결된 각종 부품을 제어할 수 있다. 점점 더 작아지고 저렴해지고 빨라지는 컴퓨터가 등장하면서 그 컴퓨터를 Java를 통해 제어하게 되면 사물 인터넷이 가능해진다.



#### Java로 안드로이드 앱 만들기

Java를 이용해서 안드로이드 앱을 제작할 수 있다. 인터넷 브라우저에 `android development documentation`을 검색하게 되면, android studio를 다운로드 받을 수 있게 된다. 이를 설치하고 실행한 뒤에, 프로젝트를 실행하게 되면 언어 선택을 통해 Java언어로 안드로이드 앱을 제작할 수 있다.

```java
package com.example.myjavaworld;
import ...
public class MainActivity extends AppcompatActivity {
    @Override
    protected void onCreate (Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}
```



## 데이터와 연산

각각의 데이터마다 그 데이터의 특성에 맞는 처리 방식이 존재한다. 숫자 데이터는 더하고, 곱하고, 빼고, 나누기에서부터 미적분까지, 문자 데이터는 특정 문자의 개수, 특정 문자를 없애기, 특정 문자 검색 등의 다양한 처리 방식이 존재한다.

```java
public class Datatype{
    public static void main(String[] args) {
        System.out.println(6); 					// Number
        System.out.println("six"); 				// String     
        System.out.println("6"); 				// String 6
         
        System.out.println(6+6); 				// 12
        System.out.println("6"+"6"); 			// 66   
        System.out.println(6*6); 				// 36
//      System.out.println("6"*"6"); -- 문자 데이터는 곱셉이 불가능
         
        System.out.println("1111".length()); 	// 4
//      System.out.println(1111.length()); -- 숫자 데이터는 길이를 파악 불가능
         
        System.out.println("Hello World"); 		// String 문자열
        System.out.println('H'); 				// Char 문자
        System.out.println("H");				// String 문자
    }
}
```



### 숫자와 연산

```java
public class Number {
 
    public static void main(String[] args) {
        // Operator
        System.out.println(6 + 2); 				// 8
        System.out.println(6 - 2); 				// 4
        System.out.println(6 * 2); 				// 12
        System.out.println(6 / 2); 				// 3
 
        System.out.println(Math.PI); 			// 3.141592653589793
        System.out.println(Math.floor(Math.PI));// 3 [소수점 버림]
        System.out.println(Math.ceil(Math.PI));	// 4 [소수점 올림]
    }
}
```



### 문자열 다루기

```java
public class StringApp {
 
    public static void main(String[] args) {
         
        // Character VS String 
        System.out.println("Hello World"); 		// String
        System.out.println('H'); 				// Character [오직 한글자]
        System.out.println("H"); 				// String
     
        System.out.println("Hello "				
                           + "World");			// Hello World 출력
         
        // new line
        System.out.println("Hello \nWorld");	// Hello
       											// World 출력    
        // escape
        System.out.println("Hello \"World\"");// Hello "World" 출력
    }
 
}
```

 문자열이라는 데이터 타입을 표현할 수 있게 되면, 문자열과 관련된 Java에 내장되어 있는 여러 가지 문자열을 처리할 수 있는 기능들을 활용할 수 있게 된다.

```java
public class StringOperation {
 
    public static void main(String[] args) {
         
        System.out.println("Hello World".length()); // 11
        System.out.println("Hello, [[[name]]] ... bye. ".replace("[[[name]]]", "duru")); // Hello, duru ... bye.
 
    }
 
}
```



## 변수

### 변수의 정의

변수란 데이터에 붙이는 이름이다. 이름을 붙이기 전까지 우리는 그 데이터를 부르기 어렵고, 기억하기 어렵고, 이해하기 어렵다. 변수에 대해 알아보자. 

```java
public class Variable {
 
    public static void main(String[] args) {
         
        int a = 1; 		// integer(정수)     ... -2, -1, 0, 1, 2 ...
        System.out.println(a);
         
        double b = 1.1;	// double(실수)   ... -2.0, -1.0, 0.0, 1.0, 2.0 ...
        System.out.println(b);
         
        String c = "Hello World"; // String(문자열)
        System.out.println(c);
    }

}
```

왜 변수에 데이터 타입을 항상 정의를 해주어야만 하냐면, 변수의 데이터 타입을 지정하면 값의 의미를 빨리 파악할 수 있기 때문이다.



### 변수의 효용

작성된 코드는 미래의 내가 또는 다른 누군가가 보게 될 코드이다. 따라서 그 코드의 의미를 빨리 파악할 수 있도록 작성하는 것은 매우 중요하다. 그 때 사용하는 가장 중요한 수단 중 하나가 변수이다. 변수는 값의 이름을 부여하는 것이기 때문이다.

```java
public class Letter {
 
    public static void main(String[] args) {
        String name = "leezche";
        System.out.println("Hello, "+name+" ... "+name+" ... egoing ... bye");
        	// Hello, leezche ... leezche ... egoing bye
        
        double VAT = 10.0;
        System.out.println(VAT);
    }
 
}
```



### 데이터 타입의 변환 (Casting)

Casting은 데이터 타입을 다른 데이터 타입으로 변환하는 방법이다.

```java
public class Casting {
 
    public static void main(String[] args) {
        double a = 1.1;
        double b = 1;
        double b2 = (double) 1;
         
        System.out.println(b);
         
        // int c = 1.1; -- 정수 데이터 타입인 Integer에는 실수 데이터를 넣을 수 없다.
        double d = 1.1;
        int e = (int) 1.1;	   // 실수 데이터를 Integer 데이터 타입으로 강제 변환하면 정수 데이터 1로
        System.out.println(e); 
         
        // 1 to String 
        String f = Integer.toString(1); // 정수 데이터 1을 String 데이터 타입으로 강제 변환하면 문자열 1로
        System.out.println(f.getClass()); // String 출력[f의 데이터 타입 확인]
 
    }
}
```



https://opentutorials.org/course/3930/26661부터 진행