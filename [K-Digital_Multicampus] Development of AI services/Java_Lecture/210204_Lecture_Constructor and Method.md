# 생성자 (constructor)

객체 생성에 관여하는 특별한 메소드인 생성자에 대해서 알아보자. 생성자는 객체를 생성할 때 호출되며, 객체의 초기화를 담당한다.

이미 나는 생성자에 대해서 알고 있다. 그것은 바로 new를 통해 생성자를 호출하고 있기 때문이다. new를 통해 생성자를 호출하게 되면 Heap(Eden) 영역에 객체가 생성되고 객체의 주소값이 클래스 타입 변수에 리턴되어 객체에 접근할 때 이용된다.

생성자는 메소드와 비슷한 모양이지만 리턴 타입은 없고, 클래스 이름과 동일한 형태를 가지고 있다.



## 기본 생성자 (Default Constructor)

생성자는 메소드와 비슷한 모양이지만 리턴 타입이 없고, 클래스 이름과 동일하다.

모든 클래스는 생성자가 반드시 존재하며, 하나 이상을 가질 수 있는 것이 기본이다. 만약 내가 클래스 내부에 생성자 선언을 하지 않았다면 어떻게 될까?

컴파일러는 생성자 선언이 되어있지 않다면 눈에 보이지는 않지만 `[해당 클래스 접근지정자] 해당 클래스 이름 () { super();}`을 기본 생성자가 있는 자동 추가 시킨다. 여기서 super();에 대해서는 따로 다루도록 하자.

만약 기본 생성자를 명시적으로 선언하게 되면 컴파일러는 기본 생성자를 추가하지 않는다.

```java
public class Choi {  
/*	public Computer () { 
	super();
	}				눈에는 보이지 않지만 생성되어 있는 기본 생성자 */
}
```

이렇게 기본 생성자가 있기 때문에 `new`를 통해 생성자를 호출하여 객체를 생성할 수 있게 되는 것이다.

```java
Choi family = new Choi(); // 기본 생성자를 호출
```

그러나 만약 명시적으로 선언한 생성자가 하나라도 있다면, 컴파일러는 기본 생성자를 추가하지 않는다. 그러면 굳이 명시적으로 생성자를 선언하는 이유는 뭘까?



## 생성자 선언

결과부터 말하면, 명시적으로 생성자를 선언하는 이유는 다양하게 객체를 초기화하기 위해서이다. 생성자 선언의 구조는 아래와 같다.

클래스이름 (`매개변수선언`) {
 `객체의 초기화 코드` 
}

생성자는 메소드와 비슷한 모양을 가지고 있지만, 리턴 타입이 없고 클래스 이름과 동일한 형태를 띄고 있다. `매개변수선언` 부분은 생략이 가능하며, 여러 개를 선언할 수도 있다.

```java
public class Choi {
    Choi (String name, int age, char gender) {
      // 객체의 초기화 코드
    }
}
```

```java
Choi family = new Choi("인규", "31", '남');
Choi family = new Choi // 매개변수 없이 생성자 호출 불가능한 상황
```

여기서 매개변수는  `String`, `int`, `char`타입으로 세 가지로 구성되어 있다. 

이처럼 클래스에 명시적으로 생성자를 선언하고, 매개변수까지 구체적으로 선언한 경우에는 반드시 매개변수를 함께 작성해서 호출해서 객체를 생성해야 한다.



생성자에 대한 이해가 끝나면 아래 코드에서 `a1`, `a2`, `a3` 객체들은 어떤 생성자를 호출하는 것인지 추측이 가능하다.

```java
public class A {
	public A() {
		System.out.println("A() 생성자 호출");
	}
    
	public A(int i) {
		System.out.println("A(int i) 생성자 호출");
	}
    
	public A(int i, String s) {
		System.out.println("A(int i,String s) 생성자 호출");
	}
```

```java
public static void main(String[] args) {
	A a1=new A();
	A a2=new A(10);
	A a3=new A(20, "java");
	}
}
```

생성자가 하나 뿐이라면 다양한 데이터들을 수용할 수 없기 때문에 위와 같이 생성자를 다양하게 생성하면, 외부에서 제공되는 다양한 데이터들을 이용할 수 있게 된다. 또한 이를 통해, 생성자도 오버로딩(overloading)이 가능하다는 것을 알 수 있게 된다.

이제 모든 클래스는 생성자가 반드시 존재하며, 하나 이상을 가질 수 있다는 것이 다시금 확인되었다.



## `this();` `super();`

> 자신을 가리키면 this, 부모를 가리키면 super!

this라는 키워드 : 자신 객체를 가리키는 참조 키워드
this()라는 메소드 : 자신의 생성자를 호출하는 구문
super라는 키워드 : super 객체를 가리키는 참조 키워드
super()라는 메소드 : super 생성자를 호출하는 구문



### `this` 키워드

`super();` 메소드에 대해 알아보기 전에 우선 `this ();` 메소드와 `this` 키워드에  대에서 알아보도록 하자.

생성자 오버로딩을 많이 할 경우에는 생성자 간에 반복되는 코드가 발생할 수 있다.

```java
public class Smartphone {
    String company;
    String model;
    
    Smartphone () {									// 생성자1 선언
        this.company="Samsung";
        this.model="Galaxy";			// this 키워드를 통한 생성자2 자신의 객체 참조
    }

    Smartphone (String model) {						// 생성자2 선언
        this.company="Samsung";
        this.model=model;				// this 키워드를 통한 생성자2 자신의 객체 참조
    }
    
    Smartphone (String company, String model) { 	// 생성자3 선언
        this.company=company;
        this.model=model;        		// this 키워드를 통한 생성자3 자신의 객체 참조
    }
}
```

```java
public class SmartphonePrint {
	public static void main(String[] args) {
	    Smartphone s1 = new Smartphone();						// 생성자1 호출
	    Smartphone s2 = new Smartphone("Galaxy");				// 생성자2 호출
	    Smartphone s3 = new Smartphone("Samsung", "Galaxy");	// 생성자3 호출
	    
		System.out.println(s1.company+s1.model);
		System.out.println(s2.company+s2.model);
		System.out.println(s3.company+s3.model);
    }
}	
```

위의 코드를 살펴보면 다양한 생성자들을 선언했으나, 세 생성자 모두 같은 내용을 담고 있는 것을 알 수 있다.

### `this();` 메소드

이 경우에는 자기 자신의 또 다른 생성자를 호출하는 `this();` 메소드를 이용하면 중복 코드를 최소화할 수 있으며, 더 다양한 내용을 쉽게 담아낼 수 있다.

```java
public class Car {
	String company="현대자동차";
	String model, color;
	int maxSpeed;
		
	public Car() {						// 생성자1 정의
	}

	public Car(String model) {			// 생성자2	정의
		this(model, "은색", 250);		// **this 메소드를 통해 또 다른 생성자(생성자4)를 호출**
	}

	public Car(String model, String color) {	// 생성자3 정의
		this(model,color,250);		 // **this 메소드를 통해 또 다른 생성자(생성자4)를 호출**
	}

	public Car(String model, String color, int maxSpeed) {  // 생성자4 정의
		this.model = model;
		this.color = color;
		this.maxSpeed = maxSpeed;	// this 키워드를 통한 생성자4 자신의 객체 참조
	}
}
```

```java
public class CarExample {
	public static void main(String[] args) {
		Car car1 = new Car();
		System.out.println(car1.company);
		System.out.println();
	
		Car car2 = new Car("자가용");
		System.out.println(car2.company);
		System.out.println(car2.model);
		System.out.println();
		
		Car car3 = new Car("택시","검정");
		System.out.println(car3.company);
		System.out.println(car3.model);
		System.out.println(car3.color);
		System.out.println();
		
		Car car4 = new Car("택시","검정",200);
		System.out.println(car4.company);
		System.out.println(car4.model);
		System.out.println(car4.color);
		System.out.println(car4.maxSpeed);
	}	
}
```



### `super` 키워드

 `super ();` 메소드와 `super` 키워드에  대에서 알아보도록 하자.

`this` 키워드가 스스로 객체 자신을 가리키기 위해 사용하는 참조 변수라면, `super` 키워드는 부모 클래스로부터 상속받은 필드나 메소드를 자식 클래스에서 참조하는 데 사용하는 참조 변수이다.

```java
class Parent {
    int a = 10;
}
```

```java
public class Child extends Parent {  // parent 클래스를 상속
    int a = 20;

    public void printA() {
    	System.out.println(this.a);	  // 해당 클래스의 a값 출력
    	System.out.println(super.a);  // 부모 클래스의 a값 출력
    } 
}	
```

```java
public class Super {
	public static void main(String[] args) {
		Child c=new Child();
		c.printA();
	}
}
```



### `super();` 메소드

`this();` 메소드가 같은 클래스 내의 다른 생성자를 호출하기 위해 사용된다면, `super();` 메소드는 부모 클래스의 생성자를 호출할 때 사용된다. 괄호 내에 매개변수가 있다면 그에 맞는 부모 클래스 내 생성자를 호출하겠지만, 매개변수를 입력하지 않거나, `super();` 메소드를 생략하게 되면 부모 클래스의 기본 생성자를 호출하게 된다.

자식 클래스에서 객체를 생성하면, 해당 객체에는 자식 클래스 뿐만 아니라 부모 클래스 멤버까지도 포함하고 있다. 따라서 부모 클래스 멤버를 초기화하기 위해서는 자식 클래스의 생성자에서 부모 클래스의 생성자까지 호출해야만 한다. 이는 모든 클래스의 조상인 Object까지 거슬러 올라가며 수행하게 된다. 따라서 컴파일러는 클래스에 생성자가 하나도 정의되어 있지 않으면 자동으로 기본 생성자로 `super();` 메소드를 생성하게 된다.

생성자는 `Source` > `Generate Constructor using Fields...`를 통해 쉽게 명시적 생성이 가능한데, 여기서면, `super();`라는 메소드를 자동으로 선언하는  것을 알 수 있다.



> `this();` 메소드, `super();` 메소드는 생성자의 첫 줄에서만 사용 가능하기 때문에,
>
> 동시에 둘 다 사용은 불가능하며, 기본 생성자는 `super();` 이다.



# 메소드 (method)

메소드는 동작과 행위이며, 항상 소괄호를 갖는 특징이 있다. 소괄호 뒤에 { }가 있으면 메소드 정의를 뜻하고 있으며, 소괄호 뒤에 ;이 있으면 메소드 호출을 의미한다. 또한 생성자와 달리 리턴타입을 가지고 있다.

메소드 정의 시 매개변수를 선언하게 되면, 메소드를 호출할 때 매개변수 값을 함께 전달해주어야 한다.



## 리턴값이 있는 메소드

메소드 선언에 리턴 타입이 있는 메소드는 반드시 리턴문을 사용해서 리턴값을 지정해야 한다.

```java
int plus(int x, int y) {	// 리턴 타입이 int
    int result = x+y;
    return result;
 // System.out.println(result);  // return 이후 실행문은 결코 실행되지 않기에 컴파일 오류
}
```



## 리턴값이 없는 메소드 (void)

void로 선언되어 리턴값이 없는 메소드에서도 리턴문을 사용할 수 있다. `return;`을 사용하면 메소드 실행을 강제 종료 시킬 수 있다.



## 메소드 오버로딩

클래스 내에 같은 이름의 메소드를 여러 개 선언하는 것을 메소드 오버로딩이라고 한다. 메소드 오버로딩을 위해서는 매개 변수의 타입, 개수, 순서 중 하나가 달라야 한다.

