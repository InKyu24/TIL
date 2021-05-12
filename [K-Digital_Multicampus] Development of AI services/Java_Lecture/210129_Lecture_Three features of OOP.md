# 1. 객체 지향 프로그래밍

## 1] 객체란?

**객체**란 물리적으로 존재하거나 추상적으로 생각할 수 있는 것 중에서 **자신의 속성**을 가지고 있고 **식별 가능**한 것

객체들은 서로 간에 기능(동작)을 이용하고 데이터를 주고 받는다. 즉, 개체와 객체 간의 상호작용을 한다.



>  **Object** - 객체
>
> 구체적, 추상적, 관념적 모든 사물 (Class의 구현체로 Instance라고도 할 수 있다.)

>  **Field(Attribute) - 속성**
>
> 객체의 데이터가 저장되는 곳
>
>   ex) 사람의 피부색, 나이, 이름, 자동차의 색상, 속도

>  **Method(Function) - 동작**
>
> 객체의 동작에 해당하는 실행 블록
>
>   ex) 웃다, 먹다, 자다, 달리다, 멈추다

>  **Class** - Data와 Method로 구성된 자바 프로그램의 단위

>  **Constructor** - 생성자
>
>  new 연산자와 클래스 이름으로 호출되어, 초기화를 담당하는 블록

>  **Package** - Class의 그룹



## 2] 객체 간의 관계

객체는 다른 객체와 관계를 가지게 되는데, 이를 집합 관계, 사용 관계, 상속 관계로 구분할 수 있다.

- **집합관계**: 완성품과 부품의 관계  (자동차와 바퀴)

- **사용관계**: 객체가 다른 객체를 사용하는 관계  (사람과 스마트폰)

- **상속관계**: 종류 객체와 구체적인 사물 객체 관계  (동물과 호랑이)



**객체 지향 프로그래밍**은 만들고자 하는 완성품인 객체를 모델링하고, 집합 관계에 있는 부품 객체와 사용 관계에 있는 객체를 하나씩 설계한 후 <u>조립하는 방식으로 프로그램을 개발하는 기법</u>이다.



# 2. 객체 지향 프로그래밍의 특징

객체 지향 프로그램의 특징으로는 캡슐화, 상속성, 다형성이 있다.



## 1] 캡슐화 (Encapsulation)

Data의 직접 접근을 숨기고, Method만을 사용할 수 있게끔 하는 설계 기법

객체는 각각 분리하여 메모리에 저장되며, 참조함으로써 이용할 수 있게 된다. 참조하여 객체를 사용하는 입장에서 생각해보면, 객체를 직접 생성한 것이 아니기 때문에 객체에 대한 구체적인 정보를 정확하게 파악해낼 수 없다. 따라서 오해와 실수가 빈번히 발생한다. 그렇기 때문에 객체를 생성하는 입장에서는 재사용을 유용하게 할 수 있도록 배려하는 것이 중요하다.

### 캡슐화를 바탕으로 한 코드 작성과 이해

> private으로 되어있는 변수를 다른 클래스로 사용하기 위한 getters/setters

```java
package test.encapsulation;
public class MyDate {
	private int year; 
	private int month;
	private int day;	 // Member 클래스 외 접근 불가한 int 데이터(연, 월, 일)를 선언
	
	public int getYear() {	// get 메소드 정의
		return year;		// [데이터를 반환하기 위해]
	}
	public int getMonth() { // get 메소드 정의
		return month;       // [데이터를 반환하기 위해] 
	}
	public int getDay() {   // get 메소드 정의
		return day;         // [데이터를 반환하기 위해]
	}

	public void setYear(int year) { // set 메소드 정의
		if(year>0 && year<2022) {   // [유효성 검사]
			this.year=year;			// [데이터를 입력하기 위해]
			
		}else {
			System.out.println("Invalid year");
		}
	}

	public void setMonth(int month) { // set 메소드 정의
		if(month>0 && month<13) {     // [유효성 검사]
			this.month = month;       // [데이터를 입력하기 위해]
		}else {
			System.out.println("Invalid month");
		}
	}

	public void setDay(int day) { // set 메소드 정의
		if(month==1||month==3||month==5||month==7||month==9||month==12) { // [유효성 검사]
			if(day>0 && day<32) {
				this.day = day;   // [데이터를 입력하기 위해]
			}
		}else if(month==4||month==6||month==9||month==11) {
			if(day>0 && day<31) {
				this.day = day;   
            }    
		}else if(month==2) {
			if(day>0 && day<30) {
				this.day = day;
			}
		}else
			System.out.println("Invalid day");
		}
}
```

```java
package test.encapsulation;
public class MyProfile {
	MyDate birthday=new MyDate(); // MyDate 클래스를 birthday 생성자로 가져오기
	public void setBirthday() {  // set 메소드 정의
		birthday.setYear(1991);	 // MyDate 클래스 내 setYear 메소드 호출
		birthday.setMonth(2);	 // MyDate 클래스 내 setMonth 메소드 호출
		birthday.setDay(4);		 // MyDate 클래스 내 setDay 메소드 호출

		System.out.println(birthday.getYear()+"년 "+birthday.getMonth()+"월 "+birthday.getDay()+"일");	 // getYear, getMonth, getDay 메소드 호출을 통한 결과값 출력	
	}
}
```



### Access Modifier (접근 지정자)

[![img](https://1.bp.blogspot.com/-j2r7G66UA4c/YBbJg2RUdnI/AAAAAAAAGTA/DpWEVXSlqf8ynBxzOcLCRA_QeSDm3g-xACLcBGAsYHQ/w640-h208/%25EA%25B7%25B8%25EB%25A6%25BC2.png)](https://www.blogger.com/blog/post/edit/9180050484951786848/8297003251818016501#)

> 접근 지정자를 Data에서는 private으로 Method는 public으로 하는 것이 가장 일반적인 형태!



## 2] 상속성 (Inheritance)

상속은 **Extends**라는 키워드로 **단일 상속**을 지원한다. - Java에서 부모는 엄마, 아빠가 아니라 하나의 엄빠!

**즉, 상위 객체는 단 하나!**

> 설계를 하다보면, 한 클래스가 다른 클래스와 유사성이 있는 경우가 많다.
> 그러면 그 클래스들의 유사성을 묶어야할 필요가 생긴다.

상위 객체의 속성을 하위 객체가 물려받는 것으로 이로써 하위 객체를 보다 쉽고 빠르게 설계할 수 있게끔 하는 역할을 한다. 재사용 관점에서 바라보면 비효율적인 코드 작성의 회피. 즉,반복된 코드의 중복을 줄여줄 수 있다는 것과 유지보수의 편의성에 큰 이점이 있다고 볼 수 있다.

### Object

> Object - 모든 Class의 조상 [클래스의 뿌리]
>
> data는 없고 11가지의 method들로 구성되어 있으며, 상속 유무에 관계없이 기본적으로 상속한다.
>
> Object 관련 API document : [http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html](https://www.blogger.com/blog/post/edit/9180050484951786848/8297003251818016501#)



### 상속을 바탕으로 한 코드 작성과 이해

```java
package test.inheritance;
public class Father { 			// Father 클래스 생성
	public int i=10;			// Data i를 10으로 선언
	public void printI() { 		// printI 메소드로 i값을 "A: i" 형식으로 출력하도록 정의
		System.out.println("A:"+i);
	}
}
```

```java
package test.inheritance;
public class Sun extends Father { // Sun 클래스 생성 및 Father 클래스 상속
		public int x=1000;		// Data x를 1000으로 선언
		public int i=100;		// Data i를 100으로 선언

		public void printX() {		// printI 메소드로 x값을 출력하도록 정의
			System.out.println(x);
		}
		public void printI() {		// printI 메소드로 i값을 "A: i" 형식으로 출력하도록 정의
			System.out.println("B:"+i);
		}				
}
```

```java
package test.inheritance;
public class Test {
	public static void main(String[] args) {	// main 메소드 정의
		Father dad=new Father();				// Father 클래스를 dad 생성자로 가져오기
		dad.i++;					// Father 클래스 내 i 값에 1을 더하기
		dad.printI();				// printI 메소드 호출 [A: 11 출력]
		
		Sun kid=new Sun();			// Sun 클래스를 kid 생성자로 가져오기
		kid.x++;					// Sun 클래스 내 x 값에 1을 더하기
		kid.printX();				// printX 메소드 호출 [1001 출력]
		kid.i++;					// Sun 클래스 내 i 값에 1을 더하기
		kid.printI();				// printI 메소드 호출 [B:101 출력]
		
		System.out.println(dad);			// dad 생성자가 저장된 데이터 주소위치 출력
		System.out.println(dad.toString()); // dad 생성자가 저장된 데이터 주소위치 출력

		System.out.println(kid);			// kid 생성자가 저장된 데이터 주소위치 출력
		System.out.println(kid.toString());	// kid 생성자가 저장된 데이터 주소위치 출력	
	}
}
```

> 상속 받은 클래스에서도 동일한 이름의 변수는 물론, 동일한 이름의 메소드 정의가 가능하다.
>
> 따라서 상속은 정교하고 세분화 하는 것을 **지향**한다.

### Shadow Effect (그림자 효과)

Test 클래스에서 Father dad=new Father(); 을 Object dad=new Father();으로 작성하거나, Sun kid=new Sun();을 Object kid=new Sun();로 작성하게 된다면 해당 클래스의 속성이 Object로 가려지게 되는데 이를 그림자 효과(Shadow effect)라고 한다.

즉, 상위 타입으로 선언된 객체는 상위 타입으로만 취급되어 하위 타입의 멤버가 가려지는 것이다.

> 이모티콘을 오브젝트로 변환하면 그림자가 드리워져 원만 남는 것과 비슷하다고 이해했다.

![](https://lh3.googleusercontent.com/-UdYdjDTOkb0/YBp4K0a6fXI/AAAAAAAAGUE/d5JocVkkyT4mc4SWCfUc4yzU75qHvyfsACLcBGAsYHQ/w400-h211/image.png)

## 3] 다형성 (Polymorphism)

하나의 클래스나 메소드가 다양한 방법으로 동작하는 것을 의미한다.

> ''발차기'' 라는 행위를 예로 들어보자.
>
> 태권도장에서 발차기라는 행위를 하게 되면, 열심히 운동하는 사람으로 보일 것이다.
> 자기 전에 침대 위에 누워서 발차기를 하게 된다면, 오늘 있던 부끄러운 일을 후회하는 사람처럼 보일 것이다.
>
> 이처럼 다형성은 같은 타입의 객체로 다양한 실행 결과를 만들어내며, 객체를 부품화시킨다.



### 1) 다형적 변수 (polymorphic variable)

상위 타입으로 선언된 변수를 다형적 변수라고 한다.

예를 들어 public void print(Shape s) {} 라고 메소드를 정의한다면, 여기서 s는 모양을 받는 상위 타입의 다형적 변수라 볼 수 있다. 따라서 s는 원, 삼각형, 사각형, 오각형...만이천각형까지 모든 Shape의 하위 객체를 가리키는 변수가 될 수 있다.

> 다형적 변수의 최고봉은 Object



### 2) Overloading

한 클래스 내에 동일한 이름의 메소드를 여러 개 정의하는 방법

> Object 내에는 data는 없고 메소드만 11개가 들어있다. 그 [11가지 메소드](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)를 찾아보게 되면, wait 메소드라는 동일한 이름으로 3가지나 있는 것을 찾아볼 수 있다.

하지만 overloading의 경우, 확장성과 사용성 측면에서 매우 떨어진다.



### 3) Overriding

상위 클래스의 메소드를 하위 클래스에서 재정의하여 하위 클래스의 메소드를 우선적으로 사용하는 방법으로 Shadow effect를 우회하는 것을 Overriding이라고 한다. 따라서 Overriding은  데이터가 아닌 메소드에서만 적용 가능하며, 성능과 확장성 모두 향상시킬 수 있다.