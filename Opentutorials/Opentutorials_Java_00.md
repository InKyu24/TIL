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



## 프로그래밍

프로그램의 어원에는 시간의 순서에 따라 공연이 순차적으로 진행이 되는 것에서 출발한다. 그 이후로 시간의 순서에 따라 무언가가 일어나는 성격의 것들을 프로그램이라고 부른다. 컴퓨터가 가지고 있는 각각의 작업의 하나하나들이 시간의 순서에 따라 실행되게 할 수 있게, 자동화된 처리를 할 수 있게 된다. 따라서 이를 프로그램이라고 부를 수 있게 되는 것이다.

```java
public class Program {
    public static void main(String[] args) {
        System.out.println(1);
        System.out.println(2);
        System.out.println(3);
    }
}
```

상상력을 통해 위의 단순한 코드가 매우 중요한 길고 복잡한 코드이고, 많은 사람들이 함께 쓰는 코드라고 생각해보자. 내가 하고 싶은 취지에 맞게 코드를 배치하면 순차적으로 컴퓨터가 가진 하나하나의 기능들이 자동화되어 작동된다. 게다가 각각의 작업들이 언제 끝나게 될 지 예측할 수 없는 작업이라고 가정해본다면, 순차적으로 실행되는 프로그램을 통해 이를 쉽게 통제할 수 있다. 그리고 다양한 프로그래밍 언어 중에 대표적인 언어가 바로 Java인 것이다.

프로그램을 만드는 경우에 혼자서 처음부터 끝까지 모두 만드는 것은 매우 드문 경우이다. 다른 사람이 만든 어떤 부품을 가지고 와서 나의 완제품을 만드는 것이고, 나의 완제품은 또 누군가의 부품이 될 수 있는 형태이다. 

누군가가 프로그램을 만들었다고 가정하자. 그 프로그램을 이용하면 엘리베이터를 호출할 수 있고, 시큐리티를 해제할 수 있고, 전자제품의 전원을 켜고 끌 수 있으며, 나아가서는 냉장고에 무엇이 들었는 지까지 알 수 있다고 하자. 그리고 나는 그 코드의 사용자가 되어, 내가 원하는 일에 따라 그리고 시간에 흐름에 따라 코드를 배치하여 원하는 애플리케이션을 제작하고자 할 것이다. 

나는 집에 도착하기 전에 엘리베이터를 부르고, 현관문의 잠금장치가 자동으로 해제되고, 전등이 자동으로 켜지도록 할 것이다. 이러한 각각의 실행들이 순서대로 이뤄지도록 할 것이다. 그렇게 제작된 프로그램의 예시는 아래와 같다. 실제로 그렇게 실행이 되는 것은 아니지만 프로그래밍을 이해하기 위한 용도로 생각해두자.

 ```java
// 나에게 필요한 클래스를 불러오기
import org.opentutorials.iot.Elevator;
import org.opentutorials.iot.Lighting;
import org.opentutorials.iot.Security;
 
public class OkJavaGoInHome {
 
    public static void main(String[] args) {
        // 집 주소를 문자열 데이터 타입으로, 변수명 id 생성
        String id = "JAVA APT 507";	
        
        // Elevator call 
        // 엘리베이터라는 데이터 타입으로, 변수명 myElevator 생성
        Elevator myElevator = new Elevator(id);
        // myElevator를 1층으로 호출하는 실행문 호출
        myElevator.callForUp(1); 
         
        // Security off 
        // 시큐리티라는 데이터 타입으로, 변수명 
        Security mySecurity = new Security(id); mySecurity 생성
        // mySecurity를 끄는 메소드 호출
        mySecurity.off(); 
         
        // Light on
        // 라이팅이라는 데이터 타입으로, 변수명 hallLamp 생성
        Lighting hallLamp = new Lighting(id+" / Hall Lamp"); 
        // hallLamp를 끄는 메소드 호출.
        hallLamp.on(); 
        // 라이팅이라는 데이터 타입으로, 변수명 floorLamp 생성 
        Lighting floorLamp = new Lighting(id+" / floorLamp"); 
        // floorLamp를 끄는 메소드 호출
        floorLamp.on(); 
    }
}
 ```



## 디버거

코딩이 편해질 수 있는 지름길 중 하나는 디버거라는 것이다. 내가 짠 코드에 의도하지 않은 문제를 버그라고 하고, 이를 잡는 행위를 디버깅, 그리고 디버깅을 할 때 사용하는 도구를 디버거라고 부른다. 여러 가지 현대적인 개발 도구들은 디버거를 내장하고 있다. 이클립스에서 디버거를 다루게 된다면 어떤 개발 도구에서도 디버거를 다루기가 쉬워질 것이다.

만약 코드에서 문제가 발생했다면 첫 번째로 취해야하는 행동은 실행을 멈추는 것이다. 멈추고 싶은 코드를 더블클릭하게 되면 좌측에 푸른 점이 생기는 데, 이를 브레이크 포인터라고 부른다. 그 다음, 벌레 모양의 버튼을 누르게 되면 Perspective가 Switching되고, 브레이크 포인트에서 실행이 멈추게 된다. 그리고 Stepover 버튼(`F6`)을 클릭하면, 브레이크 포인트 다음 코드 하나하나씩을 실행시킬 수 있으며, 실행되는 순간마다 애플리케이션 내의 변수의 상태를 하나하나 확인할 수 있게 된다.

만약 브레이크 포인트를 2개 이상 설정해 놓았다면, Resume 버튼(`F8`)로 다음 브레이크 포인트까지 바로 이동할 수도 있으며, StepInto(`F5`)와 StepReturn(`F7`) 버튼으로 구체적인 메소드의 코드를 확인하고, 다시 원래 코드로 돌아올 수 있게 된다.



## 입력과 출력

프로그램은 입력(Input)을 처리해서 출력(Output)을 만들어 내는 기계라고 할 수 있다. Java에서는 Argument, File, Network, Audio, Program 등 다양한 방식으로 입력값을 줄 수 있다. 가장 일반적인 것은  Argument라고 해서 프로그램을 실행할 때 어떤 텍스트를 주는 것이다. 이렇게 입력을 받아서 결과를 출력할 수 있게 된다. 출력의 방식은 Monitor 화면에 띄어질 수도 있으며, File, Audio, Program 등의 다양한 형태가 될 수 있다.

```java
// swing에 속한 JOptionPane API 가져오기
import javax.swing.JOptionPane;

import org.opentutorials.iot.DimmingLights;
import org.opentutorials.iot.Elevator;
import org.opentutorials.iot.Lighting;
import org.opentutorials.iot.Security;
 
public class OkJavaGoInHomeInput {
    public static void main(String[] args) {
        // 값을 입력할 수 있는 JOptionpane 생성
        String id = JOptionPane.showInputDialog("Enter a ID");
        String bright = JOptionPane.showInputDialog("Enter a Bright level");
        
        Elevator myElevator = new Elevator(id);
        myElevator.callForUp(1); 
         
        Security mySecurity = new Security(id); mySecurity 생성
        mySecurity.off(); 
         
        Lighting hallLamp = new Lighting(id+" / Hall Lamp");  
        hallLamp.on(); 
        Lighting floorLamp = new Lighting(id+" / floorLamp"); 
        floorLamp.on(); 
        
        DimmingLights moodLamp = new DimmingLights(id+" moodLamp");
        // Double.parseDoublce(bright)만큼의 밝기로 조절
        // 변수 bright의 데이터 타입을 String에서 double로 변환
        moodLamp.setBright(Double.parseDouble(bright));
        moodLamp.on();
    }
}
```

보편적으로 사용되는 방법이 있다. 명령어로 실행되는 프로그램에 파라미터를 통해서 Arguments를 전달하는 방식이다. `Run Configurations`에서 해당하는 Java Application을 선택하고, Arguments에 입력값을 넣을 수 있게 된다. Arguments에 값을 넣을 때는 띄어쓰기로 구분하기 때문에 띄어쓰기가 포함된 데이터를 입력할 경우에는 따옴표를 이용하여, 하나의 값이라는 표시를 해주어야 한다. Arguments에 입력한 값들을 코드 내에서 입력값으로 사용하기 위한 방법은 args[0], args[1]....을 해당하는 위치에 넣으면 된다.

```java
import org.opentutorials.iot.DimmingLights;
import org.opentutorials.iot.Elevator;
import org.opentutorials.iot.Lighting;
import org.opentutorials.iot.Security;
 
public class OkJavaGoInHomeInput {
    // paramter, 매개변수
    public static void main(String[] args) {
        
        // 문자열 데이터 타입으로, 변수명 id 생성 (값은 첫번째 Argument)
        String id = args[0];
        // 문자열 데이터 타입으로, 변수명 bright 생성 (값은 두번째 Argument)
        String bright = args[1];

        Elevator myElevator = new Elevator(id);
        myElevator.callForUp(1);

        Security mySecurity = new Security(id);
        mySecurity.off();

        Lighting hallLamp = new Lighting(id+" / Hall Lamp");
        hallLamp.on();
         
        Lighting floorLamp = new Lighting(id+" / floorLamp");
        floorLamp.on();
         
        DimmingLights moodLamp = new DimmingLights(id+" moodLamp");
        moodLamp.setBright(Double.parseDouble(bright));
        moodLamp.on();
    }
}
```



## 이클립스 없이 컴파일

이클립스 없이도 Java가 설치되어 있고, 환경변수(Path)가 설정되어 있다면 Source 코드를 실행시킬 수 있게 된다.

`Java Source code (Program.java)`가 있고, 컴파일을 통해서 `Java Application (Program.class)`로 변환시킨 뒤, JVM을 통해 이를 실행시킬 것이다.

1. 윈도우에서 cmd를 실행시키고, Source code가 저장되어 있는 디렉토리로 이동한다.

   명령어 `cd 경로`를 통해 이동하고, 명령어 `dir`로 디렉토리 내 파일들을 확인할 수 있다.

2. Program.java 파일을 Program.class 파일로 변환한다.

   명령어`javac Program.java`를 통해 컴파일한 뒤, 명령어 `dir`로 Program.class 파일이 생성된 것을 확인할 수 있다.

3. Program.class 파일을 실행시킨다.

   명령어 `java Program`을 통해 실행시킨다.

   

만약에 나의 프로그램이 타인이 만든 것을 재사용한 프로그램이라면 조금은 더 복잡해진다. Import를 통해 Elevator, Lighting, Security 클래스들을 불러와 사용한 코드들을 이클립스 없이 컴파일하고 실행시켜보자.

1. 윈도우에서 cmd를 실행시키고, Source code가 저장되어 있는 디렉토리로 이동한다.

   명령어 `cd 경로`를 통해 이동하고, 명령어 `dir`로 디렉토리 내 파일들을 확인할 수 있다.

2. OKJavaGoInHome.java 파일을 OKJavaGoInHome.class 파일로 변환한다.

   명령어`javac OKJavaGoInHome.java`를 통해 컴파일하게 되면, 명령어 `dir`로 OKJavaGoInHome.class 파일이 생성된 것은 물론이고, Import 되어 있던 소스 파일들도 .class 파일로 변환된 것을 알 수 있다.

   > OKJavaGoInHome.java 파일과 같은 디렉토리 내에 Import하기 위한 패키지가 없고, lib라는 디렉토리 안으로 패키지가 이동되었다면, 명령어 `javac -cp ".;lib" OKJavaGoInHome.java`로 컴파일해야 한다.

3. Program.class 파일을 실행시킨다.

   명령어 `java Program`을 통해 실행시킨다.

   > OKJavaGoInHome.java 파일과 같은 디렉토리 내에 Import하기 위한 패키지가 없고, lib라는 디렉토리 안으로 패키지가 이동되었다면, 명령어 `java -cp ".;lib" OKJavaGoInHome`를 실행해야 한다.



그렇다면 Arguments를 입력값으로 넣은 소스 코드를 이클립스 없이 어떻게 실행하는지에 대해서도 알아보자. 컴파일 후 실행할 때, 명령어 `java OKJavaGoInHomeInput "JAVA APT 507" 15.0` 를 입력해 Arguments 값을 넣어주면 된다.







