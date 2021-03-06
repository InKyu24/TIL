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



## Java 문서 보는 법

Java에서는 더 쉽게 프로그램을 만들 수 있도록 여러 가지 부품들을 제공한다. 화면에 무언가 출력하고 싶을 때는 System, 날짜를 알고 싶을 때는 Date, 수학적인 것들을 이용하기 위해서는 Math를 사용하는 것처럼 말이다. 이렇게 Java가 기본적으로 내장하고 있는 기능들을 기본 라이브러리라고 부른다. 기본 라이브러리의 조작방법을 Java Application Programming Interface(Java API)라고 부른다. 프로그램을 잘 만들기 위해서는 어떤 API가 있고, 그 API는 어떻게 조작하는가를 풍부하게 알고 사용할 수 있게 되는 것이 좋은 프로그래머가 되는 초석이라고 할 수 있겠다.  이렇게 만들어진 결과물이 누군가에게 사용된다면  User Interface(UI)라고 할 수 있다. 또한 결과물이 또 다른 프로그램을 위해 이용될 수도 있다. 그런 경우에는 새로운 API가 되는 것이다.



### API Document

Java의 API Document는 Java의 공식 사용설명서로 Java를 공부하는 것에서 자립하기 위한 핵심적인 기술이라고 할 수 있다. API Document에는 Java가 기본적으로 제공하는 부품들인 라이브러리에 대한 설명들을 확인할 수 있다. 검색 엔진을 통해 Api documentation java를 검색하면 Java API Document를 볼 수가 있다. 최초 화면의 좌측 하단에 All Classes에서 약 4천 개 정도의 모든 클래스들을 확인할 수 있다. 각 클래스들은 하나의 프로그램이라고 인식하자.

#### Package

만약 수학과 관련된 작업을 해야한다면, Math 클래스를 검색해서 클릭하게 되면, 우측 화면에서 Math  클래스에 대한 상세정보를 볼 수 있게 된다. Math 클래스 우측 화면에서 java.lang을 살펴보자. 이것은 math라는 클래스 속해있는 패키지라고 하는 것이다. 클래스가 엄청나게 많아지면, 수많은 클래스를 정리해야 할 필요성을 느낄 것이다. 게다가 이미 존재하는 이름의 클래스를 만들고자 한다면 서로 충돌하기 때문에 같은 곳에 둘 수 없을 것이다. 이러한 문제를 해결하기 위한 것이 패키지다.

좌측 상단에서는 java가 기본적으로 제공하는 패키지들의 목록을 볼 수가 있다. java.lang 패키지를 찾아서 선택하게 되면 좌측 하단에는 이제 java.lang 패키지에 속한 클래스들이 나타나게 된다. String도 java.lang 패키지에서 찾아볼 수 있다. 이렇게 패키지는 서로 연관된 성격의 클래스들을 모아 이름을 붙인 것이라는 것을 알게 되었다.

#### Class

이제 클래스를 다시 정의해보면 클래스는 서로 연관된 변수와 메소드라는 것들을 모아서 이름을 붙인 것이다. 다시 정리해보자. 여러 개의 클래스들을 그룹화하여 이름을 붙인 것이 바로 패키지이고, 각각의 클래스는 변수들과 메소드들을 그룹화하여 이름 붙인 것이다.

클래스가 무엇인가를 알아보기 위한 실습을 시작해보자. 수학과 관련된 작업이 필요한 상황이라면 java 기본 라이브러리에서 제공하는 Math라는 클래스를 이용할 수 있다. Math를 적고 .을 누르면 Math 클래스에 소속되어있는 변수나 메소드라고 하는 것들의 리스트들을 확인할 수 있다. 만약 파이 값이 필요하다면 PI를 선택할 수 있을 것이다. 그렇게 되면 파이의 구체적인 값이 저장되어 있는 변수 PI를 가져올 수 있게 되는 것이다. Math 클래스를 다시 이용해보자. 소수점의 내림과 올림이 필요한 경우에는 어떨까? Math 클래스에 소속되어있는 floor와 ceil 메소드를 가져오면 쉽게 처리할 수 있을 것이다.

```java
public class ClassApp {
    public static void main(String[] args) {         
        System.out.println(Math.PI);
        System.out.println(Math.floor(1.6));
        System.out.println(Math.ceil(1.6));
    }
}
```
#### Instance

클래스는 서로 연관된 변수와 메소드를 모아서 이름을 붙인 것이라는 것을 알게 되었다. 이번엔 PrintWriter라는 클래스를 통해 인스턴스라는 것을 파악해보자. PrintWriter 클래스는 이전에 배운 Math 클래스와는 사용법이 다르다. PrinterWriter 클래스는 소괄호가 들어있으며, 그 안에는 내가 저장하고 싶은 파일의 이름이 들어간다. 그 앞에 new를 붙여서 PrintWriter의 복제본을 만들 수 있게 된다. 따라서 p1은 PrintWriter의 인스턴스가 되는 것이다. 그리고 p1이 PrintWriter의 클래스의 인스턴스만 받는다는 규제의 의미에서 p1의 앞부분에 PrintWriter라고 적게 된다.

왜 PrintWriter 클래스는 Math 클래스와 달리 인스턴스를 생성하는 것일까? 인스턴스는 내부적으로 각자의 상태를 가지게 된다. p1 인스턴스는 "result1.txt"라는 상태를, p2 인스턴스는 "result2.txt"라는 상태를 내장하고 있는 것처럼 말이다. Math 클래스는 1회성의 작업을 위해 고안된 클래스라면, PrintWriter 클래스는 후속적인 여러 작업을 할 수도 있고, 동시에 다양한 인스턴스를 생성해 작업할 수도 있도록 고안된 클래스이다.

#### Constructor

API에서 Math 클래스와 PrintWriter 클래스를 찾아보면, PrintWriter 클래스에서만 생성자라고 하는 Constructor를 확인할 수 있다. Constructor가 있다는 것은 이를 이용해 인스턴스를 만드는 것이 허용되어 있다고 볼 수 있다. 또한 구체적으로 API를 찾아보면 Constructor의 괄호 안에 입력값으로 들어올 수 있는 값에 대한 설명, 해당 클래스를 사용하는 과정에서 생길 수 있는 오류들 등을 알아볼 수 있게 된다.

```java
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.PrintWriter;
public class InstanceApp {

    public static void main(String[] args) throws IOException{
		PrintWriter p1 = new PrintWriter("result1.txt");
		p1.write("Hello 1");
		p1.close();
		
		PrintWriter p2 = new PrintWriter("result2.txt");
		p2.write("Hello 2");
		p2.close();	
	}
}
```

#### Inheritance

이번에는 Java에서 굉장히 중요한 상속이라는 것을 알아보자. 앞서 알아본 PrintWriter 클래스를 API에서 확인해보면, java.io.PrintWriter 클래스는 java.io.Writer라는 클래스를 상속받았고, java.io.Writer라는 클래스는 java.lang.Object 클래스를 상속받은 것을 알 수 있다.

```java
public abstract class PrintWriter extends Writer
```

```java
public abstract class Writer extends Object
```

어떤 기능을 만들 때, 처음부터 끝까지 다 만드는 것은 어렵기에 Writer라는 클래스가 가지고 있는 메소드와 변수들을 그대로 물려받으면서, 거기에다 자신이 원하는 메소드와 변수들을 추가한 것이 PrintWriter 클래스가 된다는 것이다. 마찬가지로 Writer라는 클래스도 Object 클래스가 가지고 있는 메소드와 변수들을 그대로 물려받으면서, Writer만이 필요로 하는 메소드와 변수들을 추가한 것으로 볼 수 있다.

이클립스에서 Open Type Hierarchy를 이용하면, 상속 관계를 파악할 수 있다. Object 클래스에서는 toString 메소드를 확인할 수 있고, Writer 클래스와 PrintWriter 클래스에서는 toString 메소드를 확인할 수 없지만 Object 클래스가 부모 클래스(상속하고 있는 상위 클래스)로 위치하고 있기 때문에 toString 메소드를 사용할 수 있다. 여기서 알 수 있는 것은 Java의 모든 클래스는 Object 클래스를 상속받고 있다. 즉, Object 클래스가 최상위 클래스이다. PrintWriter의 인스턴스를 생성하여 toString 메소드를 사용하게 되면, PrintWriter 클래스에 toString 메소드가 있는지 확인하고 없으면, 부모 클래스인 Writer 클래스에서 확인하게 된다. 다시 Writer 클래스에도 없다면, 부모 클래스인 Object 클래스에서 확인하게 된다. 만약에 Object 클래스에도 없다면 오류가 발생하게 되고, 있다면 toString 메소드가 실행되는 것이다.

#### Override

다시 Open Type Hierarchy를 통해 상속 관계를 파악해보자. Write 클래스에는 입력값을 String으로 받는 write 메소드가 정의되어 있다. 그런데 PrintWriter 클래스에도 입력값을 String으로 받는 write 메소드가 정의되어 있다.  쉽게 말하면, 상속받는 PrintWriter 클래스에서 부모 클래스에 있는 메소드를 덮어쓰기 한 것이다. PrintWriter의 인스턴스를 생성하여 write 메소드를 사용하게 되면, PrintWriter 클래스에 write 메소드가 있기 때문에 부모 클래스인 Writer 클래스에 write 메소드가 있다 하더라도, 해당 클래스의 메소드를 사용하게 되는 것이다. 이러한 것을 부모 클래스에 있는 메소드를 자식 클래스에서 Override 했다라고 표현한다.

```java
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.PrintWriter;
public class InstanceApp {
 
    public static void main(String[] args) throws IOException{
         
        PrintWriter p1 = new PrintWriter("result1.txt");
        p1.write("Hello 1");
        p1.close();
         
        PrintWriter p2 = new PrintWriter("result2.txt");
        p2.write("Hello 2");
        p2.close();
        System.out.println(p1.toString());
        p2.toString();
        p2.write("Hello 2");

    } 
}
```



## 나의 앱 만들기 1

내가 물건을 판매하는 사업을 하고 있다고 상상해보자. 세금, 인건비, 유통비와 같은 비용도 발생하고, 그리고 비용을 제한 그 이익을 동업자와 공평하게 분배를 해야한다. 이런 작업을 위한 프로그램을 직접 만들어보려 한다. 이에 필요한 기본 기능들을 시스템 출력 메소드로 구현한다면 아래와 같다.

```java
Public class AccountingApp {
    public static void main(String[] args) {
        System.out.println("Value of supply : "+10000.0);
        System.out.println("VAT : "+ (10000.0 * 0.1));
        System.out.println("Total : "+ (10000.0 + 10000.0 * 0.1);
		System.out.println("Expense : "+ (10000.0 * 0.3));
        System.out.println("Income : "+ (10000.0 - 10000.0 * 0.3));
        System.out.println("Dividend 1: "+ (10000.0 - 10000.0 * 0.3) * 0.5);
        System.out.println("Dividend 2: "+ (10000.0 - 10000.0 * 0.3) * 0.3);
        System.out.println("Dividend 3: "+ (10000.0 - 10000.0 * 0.3) * 0.2);      
    }
}
```



이제 위 코드에 변수를 도입해보려 한다. 각각의 데이터들이 어떤 의미를 갖는지를 변수를 통해 이름을 붙여주면 아래와 같이 더 보기 좋은 코드가 되었다. 이로 인해 계산할 숫자의 변화가 생겼을 때, 더욱 손쉽게 변경하고 변화를 확인할 수 있게 되었다.

```java
Public class AccountingApp {
    public static void main(String[] args) {
        double valueOfSupply = 10000.0
        double varRate = 0.1;
        double expenseRate= 0.3;
        double vat = valueOfSupply * varRate;
        double total = valueOfSupply + vat;
        double expense = valueOfSupply * expenseRate;
        double income = valueOfSupply - expense;
        double dividend1 = income * 0.5;
        double dividend1 = income * 0.3;
		double dividend1 = income * 0.2;           
        
        System.out.println("Value of supply : "+valueOfSupply);
        System.out.println("VAT : "+ vat);
        System.out.println("Total : "+ total);
		System.out.println("Expense : "+ expense);
        System.out.println("Income : "+ income);
        System.out.println("Dividend1: "+ dividend1);
        System.out.println("Dividend2: "+ dividend1);
        System.out.println("Dividend3: "+ dividend1);      
    }
}
```



보통 프로그래머들이 부끄러워하는 일이 있다.  데이터가 바뀌었다고 코드를 바꾸고, 데이터가 바뀌었다고 로직을 바꾸는 일들이다. 따라서 데이터의 입력값이 변화하여도 출력값이 나타날 수 있도록 Run configuration에서 arguments의 값을 통해 valueOfSupply의 변수값을 넣어주었다. 그리고 args의 배열은 String 객체로 저장되기 때문에 이를 Double 객체로 타입을 변경해주었다.

만약 기존 데이터 입력값을 바꾸지 않고, 다른 데이터 입력값을 넣고 싶다면 Run configuration에서 Java Application을 Duplicate하게 되면 복사된 Application이 생성하여, 새롭게 생성된 Application에 arguments 값에 다른 데이터 입력값을 넣을 수 있게 된다.

또한 이클립스 없이 Java application을 실행할 수 있다. cmd를 실행하여 해당 경로로 이동한 뒤, `javac AccountingApp.java`를 실행하게 되면 클래스 파일이 컴파일된다. 하지만 `java AccountingApp`를 입력하면 에러가 발생한다. 왜냐하면 arguments를 세팅하지 않았기 때문이다. 이를 해결하기 위해서는 뒤에 arguments 값을 넣어, `java AccountingApp 10000.0` 처럼 실행하게 되면 결과를 출력받을 수 있게 된다.

컴파일된 클래스 파일을 가지고 있다면, JRE 또는 JVM이 설치되어 있는 디바이스 어디에서나 이와 같이 Application을 실행할 수 있게 된다. 만약 JRE 또는 JVM도 설치가 되어 있지 않은 어떤 컴퓨터에서 Application을 실행하고 싶다면, `launch4j`와 같은 소프트웨어를 찾아서 이용하면 된다.

```java
Public class AccountingApp {
    public static void main(String[] args) {
        double valueOfSupply = Double.parseDouble(args[0]);
        double varRate = 0.1;
        double expenseRate= 0.3;
        double vat = valueOfSupply * varRate;
        double total = valueOfSupply + vat;
        double expense = valueOfSupply * expenseRate;
        double income = valueOfSupply - expense;
        double dividend1 = income * 0.5;
        double dividend1 = income * 0.3;
		double dividend1 = income * 0.2;           
        
        System.out.println("Value of supply : "+valueOfSupply);
        System.out.println("VAT : "+ vat);
        System.out.println("Total : "+ total);
		System.out.println("Expense : "+ expense);
        System.out.println("Income : "+ income);
        System.out.println("Dividend1: "+ dividend1);
        System.out.println("Dividend2: "+ dividend1);
        System.out.println("Dividend3: "+ dividend1);      
    }
}
```



제어문을 통해서 위의 AccountingApp 클래스를 좀 더 개선을 시켜보자.

현재는 income을 5:3:2 비율로 나누고 있다. 하지만 어떠한 이유로 인해서 income이 10,000원 보다 작은 경우에는 10:0:0으로 Dividend1에게 전부 몰아주고, 10,000원 보다 큰 경우에는 5:3:2 비율로 나누고 싶다는 필요성이 생겼다고 생각해보자. 

조건문을 사용하지 않는다면 두 개의 프로그램을 만들어서 상황에 따라 프로그램을 선택하여 실행해야 할 것이다. 하지만 조건문을 사용함으로써 프로그램이 알아서 자신의 상황을 판단해 동작하기 때문에 프로그램을 제작자도 편리하고, 사용자도 프로그램에 대한 이해없이 쉽게 사용이 가능하다.

```java
public class AccountingIFApp {
    public static void main(String[] args) {
 
        double valueOfSupply = Double.parseDouble(args[0]);
        double vatRate = 0.1;
        double expenseRate = 0.3;
        double vat = valueOfSupply * vatRate;
        double total = valueOfSupply + vat;
        double expense = valueOfSupply * expenseRate;
        double income = valueOfSupply - expense;
         
        double dividend1;
        double dividend2;
        double dividend3;
         
        if(income > 10000.0) {
            dividend1 = income * 0.5;
            dividend2 = income * 0.3;
            dividend3 = income * 0.2;
        } else {
            dividend1 = income * 1.0;
            dividend2 = income * 0;
            dividend3 = income * 0;
        }
 
        System.out.println("Value of supply : " + valueOfSupply);
        System.out.println("VAT : " + vat);
        System.out.println("Total : " + total);
        System.out.println("Expense : " + expense);
        System.out.println("Income : " + income);
        System.out.println("Dividend 1 : " + dividend1);
        System.out.println("Dividend 2 : " + dividend2);
        System.out.println("Dividend 3 : " + dividend3);
 
    }
}
```



다시 조건문을 사용하기 이전의 AccountingApp 클래스를 가지고 배열을 배워보려 한다. 

수익을 나누는 비율인 5:3:2를 rate1, rate2, rate3이라는 변수로 선언하여 사용할 수 있다. 하지만 비율 선언문과 호출문 사이에 많은 코드들이 쌓이게 되면 중간에 데이터가 변할 가능성도 있고, 쉽게 알아보지 못하는 불편함도 생긴다. 이로 인해 배열 이용의 필요성이 생긴다.

배열은 `[]`를 사용해 선언한다. 배열을 도입함으로써 각각의 값들이 연관되어 있다는 것을 한 눈에 알 수 있고, 한 줄의 변수 선언문만을 필요로 하기 때문에 오염될 가능성을 현저히 줄일 수 있게 되었다.

```java
public class AccountingArrayApp {
    public static void main(String[] args) {
 
        double valueOfSupply = Double.parseDouble(args[0]);
        double vatRate = 0.1;
        double expenseRate = 0.3;
        double vat = valueOfSupply * vatRate;
        double total = valueOfSupply + vat;
        double expense = valueOfSupply * expenseRate;
        double income = valueOfSupply - expense;
         
        double[] dividendRates = new double[3];
        dividendRates[0] = 0.5;
        dividendRates[1] = 0.3;
        dividendRates[2] = 0.2;
         
        double dividend1 = income * dividendRates[0];
        double dividend2 = income * dividendRates[1];
        double dividend3 = income * dividendRates[2];
 
        System.out.println("Value of supply : " + valueOfSupply);
        System.out.println("VAT : " + vat);
        System.out.println("Total : " + total);
        System.out.println("Expense : " + expense);
        System.out.println("Income : " + income);
        System.out.println("Dividend 1 : " + dividend1);
        System.out.println("Dividend 2 : " + dividend2);
        System.out.println("Dividend 3 : " + dividend3);
    }
}
```



배열과 반복문은 같이 사용하게 되면 엄청난 시너지 효과를 내게 된다. 따라서 반복문을 공부해보려 한다.

현재 수익의 분배를 셋이서 하고 있으나, 셋보다 훨씬 많은 사람들과 수익이 분배할 필요가 있다고 상상해보자.

그렇다면 엄청나게 많은 코드가 생겨나게 된다. 만약 코드에 오류가 발생한다면 수많은 코드를 확인해야 할 것이다. 하지만 반복되는 작업들을 반복문을 사용해 하나의 코드로 작성한다면 오류의 가능성은 줄고, 오류 수정은 더욱 용이해질 것이다.

```java
public class AccountingArrayLoopApp {
    public static void main(String[] args) {
 
        double valueOfSupply = Double.parseDouble(args[0]);
        double vatRate = 0.1;
        double expenseRate = 0.3;
        double vat = valueOfSupply * vatRate;
        double total = valueOfSupply + vat;
        double expense = valueOfSupply * expenseRate;
        double income = valueOfSupply - expense;
         
         
 
        System.out.println("Value of supply : " + valueOfSupply);
        System.out.println("VAT : " + vat);
        System.out.println("Total : " + total);
        System.out.println("Expense : " + expense);
        System.out.println("Income : " + income);
         
        double[] dividendRates = new double[3];
        dividendRates[0] = 0.5;
        dividendRates[1] = 0.3;
        dividendRates[2] = 0.2;
         
             
        int i = 0;
        while(i < dividendRates.length) {
            System.out.println("Dividend : " + (income*dividendRates[i]) );
            i = i + 1;
        }
    }
}
```



이제 메소드를 AccountingApp 클래스에 도입하면서 공부해보자. 메소드는 서로 연관된 코드를 그룹화하여 이름을 붙인 정리정돈의 상자이다.

메소드에 매개변수를 작성하지 않고 사용하기 위해서는 지역변수로 선언된 변수를 전역변수로 지정해서, 모든 메소드에서 접근할 수 있도록 할 수 있다.

```java
public class AccountingMethodApp {
    public static double valueOfSupply;
    public static double vatRate;
    public static double expenseRate;
    public static void main(String[] args) {
        valueOfSupply = 10000.0;
        vatRate = 0.1;
        expenseRate = 0.3;
        print();
    }
    
    public static void print() {
        System.out.println("Value of supply : " + valueOfSupply);
        System.out.println("VAT : " + getVAT());
        System.out.println("Total : " + getTotal());
        System.out.println("Expense : " + getExpense());
        System.out.println("Income : " + getIncome());
        System.out.println("Dividend 1 : " + getDiviend1());
        System.out.println("Dividend 2 : " + getDiviend2());
        System.out.println("Dividend 3 : " + getDiviend3());
    }
    
    public static double getDiviend1() {return getIncome() * 0.5;}
    public static double getDiviend2() {return getIncome() * 0.3;}
    public static double getDiviend3() {return getIncome() * 0.2;}
    public static double getIncome() {return valueOfSupply - getExpense();}
    public static double getExpense() {return valueOfSupply * expenseRate;}
    public static double getTotal() {return valueOfSupply + getVAT();} 
    public static double getVAT() {return valueOfSupply * vatRate;}
}
```



클래스는 서로 연관된 변수와 메소드를 그룹화하여 이름을 붙인 또 다른 정리정돈의 상자이다. 우리가 소프트웨어를 만드는 것에 있어서 메소드와 클래스가 구조를 결정하기 때문에 중요한 것이다.

Accounting 클래스를 생성하여, 변수들과 메소드를 Accounting 클래스 멤버로 이동시켰다. 그리고 기존 클래스에서 Accounting 클래스를 호출하면, Accounting 클래스에 소속된 변수들과 메소드를 이용할 수 있게 된다. 그리고 `.`을 찍어 구분함으로써, 같은 이름에 변수나 메소드가 선언되어도 구분지어 사용할 수 있다. 이것이 바로 객체지향의 핵심이라고 할 수 있는 클래스이다.

```java
class Accounting{
    public static double valueOfSupply;
    public static double vatRate;
    public static double expenseRate;
    public static void print() {
        System.out.println("Value of supply : " + valueOfSupply);
        System.out.println("VAT : " + getVAT());
        System.out.println("Total : " + getTotal());
        System.out.println("Expense : " + getExpense());
        System.out.println("Income : " + getIncome());
        System.out.println("Dividend 1 : " + getDiviend1());
        System.out.println("Dividend 2 : " + getDiviend2());
        System.out.println("Dividend 3 : " + getDiviend3());
    }
    
    public static double getDiviend1() {return getIncome() * 0.5;}
    public static double getDiviend2() {return getIncome() * 0.3;}
    public static double getDiviend3() {return getIncome() * 0.2;}
    public static double getIncome() {return valueOfSupply - getExpense();}
    public static double getExpense() {return valueOfSupply * expenseRate;}
    public static double getTotal() {return valueOfSupply + getVAT();} 
    public static double getVAT() {return valueOfSupply * vatRate;}
}

public class AccountingClassApp {  
    public static void main(String[] args) {
        Accounting.valueOfSupply = 10000.0;
        Accounting.vatRate = 0.1;
        Accounting.expenseRate = 0.3;
        Accounting.print();
    }
}
```



객체지향의 양대산맥은 클래스와 인스턴스이다. 인스턴스는 하나의 클래스를 복제해서 서로 다른 데이터의 값과 서로 같은 메소드를 가진 복제본을 만드는 것이다. 

Accounting 클래스의 복제본인 인스턴스를 a1과 a2로 복제하였다. 그리고 서로 다른 데이터 값을 부여하였고, 서로 같은 메소드를 이용하였다.

```java
class Accounting{
    public double valueOfSupply;
    public double vatRate;
    public double expenseRate;
    public static void print() {
        System.out.println("Value of supply : " + valueOfSupply);
        System.out.println("VAT : " + getVAT());
        System.out.println("Total : " + getTotal());
        System.out.println("Expense : " + getExpense());
        System.out.println("Income : " + getIncome());
        System.out.println("Dividend 1 : " + getDiviend1());
        System.out.println("Dividend 2 : " + getDiviend2());
        System.out.println("Dividend 3 : " + getDiviend3());
    }
    
    public static double getDiviend1() {return getIncome() * 0.5;}
    public static double getDiviend2() {return getIncome() * 0.3;}
    public static double getDiviend3() {return getIncome() * 0.2;}
    public static double getIncome() {return valueOfSupply - getExpense();}
    public static double getExpense() {return valueOfSupply * expenseRate;}
    public static double getTotal() {return valueOfSupply + getVAT();} 
    public static double getVAT() {return valueOfSupply * vatRate;}
}

public class AccountingClassApp {   
    public static void main(String[] args) {
        // instance (a1)
        Accounting a1 = new Accounting();
        a1.valueOfSupply = 10000.0;
        a1.vatRate = 0.1;
        a1.expenseRate = 0.3;
        a1.print();
        
        // instance (a2)
        Accounting a2 = new Accounting();
        a2.valueOfSupply = 20000.0;
        a2.vatRate = 0.05;
        a2.expenseRate = 0.2;
        a2.print();
         
        a1.print();
    }
}
```