# 지정자 (Modifier)

지정자는 클래스, 변수, 메소드의 선언부에 사용되며, 부가적인 의미를 부여한다.

하나의 대상에는 여러 개의 지정자를 조합해서 사용할 수 있으나, 접근지정자의 경우에는 단 하나만 사용할 수 있다는 점에 유의하자.



## 접근 지정자 (Access Modifier)

멤버 또는 클래스에 사용하여, 외부에서 접근하지 못하도록 제한할 수 있는 기능을 한다.

![img](https://1.bp.blogspot.com/-j2r7G66UA4c/YBbJg2RUdnI/AAAAAAAAGTA/DpWEVXSlqf8ynBxzOcLCRA_QeSDm3g-xACLcBGAsYHQ/w640-h208/%25EA%25B7%25B8%25EB%25A6%25BC2.png)



## 사용 지정자(Usage Modifier)

> 생성자에는 사용지정자를 붙일 수가 없다.

### static - 객체 생성없이 사용하도록 지정

`static`은 클래스에 고정된 멤버로서 객체를 생성하지 않고 사용할 수 있는 필드와 메소드를 말하며, '클래스의' 또는 '공통적인' 이라는 의미를 가지고 있다. 하지만 `static`을 너무 남발하게 되면 OOME 에러가 발생할 수 있기 때문에 데이터 공유가 불가피한 경우에만 사용하도록 해야한다.

`static` 멤버 데이터는 모든 객체에 공통적으로 사용되는 클래스 변수가 된다. 따라서 클래스 변수는 객체를 생성하지 않고도 사용가능하며, 클래스가 메모리에 로드될 때 생성된다.

`static` 메서드는 객체를 생성하지 않고도 호출이 가능한 메서드가 된다. `static` 메서드 내에서는 객체 내 변수들을 직접 사용할 수 없다.

```java
public class StaticTest {
	static int i=10;		// i값 static
	int j=20;
	public static void main(String[] args) {
		System.out.println(i);			// 객체 생성 없이 사용 가능
//		System.out.println(j);			// 객체 생성 없이 사용 불가
		
		StaticTest st=new StaticTest();	// st로 클래스 객체 생성
		System.out.println(st.j);		// 객체 생성하였으므로 j값 출력 가능
	}
}
```

```java
public class StaticTest1 {
	public static void main(String[] args) {
		B.j++; 			// B 클래스 생성 없이 j값 사용 가능 (j값 21)
		B.printJ();		// B 클래스 생성 없이 printJ 메소드 사용 가능
		
		B o1=new B();
		o1.i++;			// i값 11
		o1.printI();
		o1.j++;			// B.j++;과 같은 내용 (j값 22)
		o1.printJ();	// B.printJ;와 같은 내용
		
		B o2=new B();	
		o2.i++;			// i값 11
		o2.printI();
		o2.j++;			// B.j++;과 같은 내용 (j값 23)
		o2.printJ();	// B.printJ;와 같은 내용
	}
}

class B{	
	int i=10;
	static int j=20;				//객체 생성없이 사용가능한 j
	static public void printJ() {	//객체 생성없이 사용가능한 printJ 메소드
		System.out.println(j);
	}
	public void printI() {
		System.out.println(i);
	}	
}
```



### final - 변경없이 사용하도록 지정

'마지막의' 또는 '변경될 수 없는'이라는 의미를 가지고 있다. 대표적인 `final` 클래스로는 String으로 상속 불가능한 클래스이다. 따라서 String을 사용하기 위해서는 객체화를 시켜야 한다.

`final`이 붙은 변수들은 변경할 수 없는 상수가 된다. 참고로 상수 데이터는 대문자로 네이밍하는 것이 관례이다. `final` 데이터로 선언되었으나 값이 없는 경우에는, 딱 한번 값이 저장되면 변경이 불가능하다.

`final`이 붙은 메소드는 오버라이딩을 통해 재정의가 불가능하다.

`final`이 붙은 클래스는 상속될 수 없는 클래스로 다른 클래스의 조상이 될 수 없다.



### abstract - 객체 생성 불가, 상속해서 사용하도록 지정

'추상의' 또는 '미완성의'라는 의미를 가지고 있다. 메소드의 선언부에서만 작성하고 실제 수행 내용은 구현하지 않는 추상메소드를 선언하는데 사용한다.

`abstract`가 붙은 메소드는 선언부만 작성하고 호출은 하지 못하는 추상 메소드임을 의미한다. 부모 메소드를 `abstract`로 지정하게 되면 자식 클래스는 반드시 오버라이딩으로 재정의를 하여 메소드를 호출하여야 한다. 

> Dog.class, Cat.class라는 실체 클래스는 Animal.class라는 추상 클래스를 상속받는다. 만약 Animal 클래스 내에서 `abstract` 메소드를 선언했다면 Dog.class와 Cat.class에서 각각 메소드를 오버라이딩으로 재정의하여 호출해야 한다. (이 때 당연히 Animal 클래스에도 `abstract`가 붙어야 한다!)

`abstract`를 클래스에 붙이는 목적은 두 가지가 있다. 하나는 실체 클래스의 공통된 필드와 메소드의 이름을 통일할 목적이고, 다른 하나는 실체 클래스를 작성할 때 시작을 절약할 목적이다. `abstract`가 붙은 클래스는 상속을 통해서만 사용할 수 있으며, 메소드가 `abstract`이면 클래스도 반드시 `abstract`여야 한다. `abstract` 메소드가 없는데도 클래스를 `abstract`로 사용한다는 것은 본 클래스로 객체 생성하지 말고, 자식 클래스로 객체를 생성해서 사용하라는 것으로 볼 수 있다.

> 전화라는 추상 클래스에 주인이라는 필드와 켠다라는 메소드가 있다면,
>
> 그 하위 클래스의 스마트폰 클래스와 집전화 클래스에서는 주인 필드와 켠다라는 메소드를 선언할 필요가 없이 호출할 수 있다. p.332

```java
public abstract class Phone {	// Phone 클래스는 abstract [추상 클래스]
	public String owner;				// 필드
	
	public Phone(String owner) {		// 생성자 선언
		this.owner = owner;
	}	

	public void turnOn() {					// 메소드 정의
		System.out.println("power on.");
	}	
	public void turnOff() {					// 메소드 정의
		System.out.println("power off");
	}
}
```

```java
public class SmartPhone extends Phone {	// Smartphone 클래스는 Phone 클래스를 상속 [실체 클래스]
	public SmartPhone(String owner) {		// 생성자 선언
		super(owner);						// Phone 클래스의 생성자 호출
	}
	public void internetSearch() {			// 메소드 정의
		System.out.println("Search for the internet");
	}
}
```

```java
public class PhoneExample {
	public static void main(String[] args) {
		//Phone phone = new Phone();  추상 클래스는 객체 생성이 불가하고, 
		
		SmartPhone smartPhone = new SmartPhone("홍길동"); // 자식 클래스를 통해 사용 가능
		
		smartPhone.turnOn();
		smartPhone.internetSearch();
		smartPhone.turnOff();
	}
}
```



## 지정자의 조합

+ 클래스 사용 가능 지정자 - <u>public</u>, <u>default</u>, **final**, abstract
  + 클래스에 final과 abstract를 함께 사용할 수 없다.

+ 메소드 사용 가능 지정자 - <u>public</u>, protected, <u>default</u>, private, static, **final**, abstract
  + 메서드에 static과 abstract를 함께 사용할 수 없다.
  + 메서드에 private과 abstract를 함께 사용할 수 없다.
  + 메서드에 private과 final은 같이 사용할 필요는 없다.

+ 멤버 변수 사용 가능 지정자 - <u>public</u>, protected, <u>defalut</u>, private, static, **final**

+ 지역 변수 사용 가능 지정자 - **final**

