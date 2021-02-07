# 인터페이스

인터페이스는 객체의 사용 방법을 정의한 타입이다. 단일 상속만을 지원하는 자바에서 객체 간의 교환성을 높이고 다형성을 구현하기 위해서는 인터페이스는 매우 중요한 역할을 한다. 즉, 다중 상속의 형태를 띄기 위해서 인터페이스는 존재한다.

예를 들어, Animal 클래스에는 Bird와 Human가 자식 클래스로 존재하고, Human 클래스에는 Superman과 man 클래스가 있다고 하자. 그리고 Vehicle 클래스에는 Airplane과 Car 클래스가 있다고 하자. 현재 상속 관계로서는  Bird, Superman, Airplane이라는 세 클래스에만 공통적으로 Fly라는 메소드를 부여하기에 어려움이 있다. 이러한 상황에서는 인터페이스가 필요하다. 이 상황에서 인터페이스의 메소드를 호출하면 인터페이스는 객체의 메소드를 호출시킨다. 그렇기 때문에 개발 코드는 객체의 내부 구조를 알 필요 없이 인터페이스의 메소드만 알고 있으면 된다.



> 어떨 때 extends를 하고 어떨 때 implements가 될 수 있을까? 언제든지 그만둘 수 있는 것에 implements 인터페이스로 디자인하고, 반드시 그 존재여야 하는 것 또는 합당한 것 하나를 선택하여 extends 상속한다.



## 인터페이스의 선언

인터페이스는 class 키워드 대신에 interface 키워드를 사용하여 선언하게 된다. 

```java
public interface RemoteControl {
}
```

클래스는 필드 ,생성자, 메소드를 구성 멤버로 가지는 것과 달리, 인터페이스는 상수와 메소드만을 구성 멤버로 가진다. 인터페이스는 객체로 생성할 수 없기 때문에 생성자를 가질 수 없다.

```java
package test.interface_;

public interface RemoteControl {
	int MAX_VOLUME = 10;	// 상수 필드 선언 [반드시 초기값 대입]
	int MIN_VOLUME = 0;	.	// [public, static, final 생략]
	
	void turnOn();			// 추상 메소드 선언 [실행블록 불필요_{}가 없음]
	void turnOff();			// [public abstract 생략]
	void setVolume(int volume); 
	
	default void setMute(boolean mute) { 	// 디폴트 메소드 선언
		if(mute) {							// [public 생략]
			System.out.println("무음 처리");
		} else {
			System.out.println("무음 해제");
		}
	}

	static void changeBattery() {					// 정적 메소드 선언
		System.out.println("건전지를 교환합니다."); 	 // [public 생략]
	}
}
```



## 인터페이스 구현

인터페이스를 구현하는 클래스를 구현 클래스라고 하며, 구현 클래스는 보통의 클래스와 동일한데 클래스 선언부에 `implement` 키워드를 추가하고 인터페이스명을 명시해야 한다.

인터페이스의 모든 메소드는 기본적으로 public 접근 제한을 갖기 때문에 구현 클래스에서 인터페이스의 추상 메소드에 대한 실체 메소드를 작성할 때 더 낮은 접근 제한자를 사용할 수 없다는 점에 유의할 필요가 있다.

또한, 인터페이스에서 선언한 실체 메소드를 구현 클래스가 작성하지 않는다면 구현 클래스는 자동으로 추상 클래스가 된다. 따라서 클래스 선언부에 abstract 키워드를 추가해야 한다.

```java
public class TV implements RemoteControl{
	
    
    public void turnOn() {	// 추상 메소드 turnOn();의 실체 메소드
        System.out.println("TV on");
	}	
    
	public void turnOff() {	 // 추상 메소드 turnOff();의 실체 메소드
		System.out.println("TV off");
    }
    	
	public void setVolume(int volume) { // 추상 메소드 setVolume();의 실체 메소드
		if(volume>RemoteControl.MAX_VOLUME) {
			this.volume = RemoteControl.MAX_VOLUME;
		} else if(volume<RemoteControl.MIN_VOLUME) {
			this.volume = RemoteControl.MIN_VOLUME;
		} else {
			this.volume = volume;
		}
		System.out.println("현재 TV 볼륨은 " + volume);
	}
}
```



## 인터페이스 변수 선언

인터페이스로 구현 객체를 사용하려면 인터페이스 변수를 선언하고 구현 객체를 대입해야 한다. 아래 코드에 변수를 선언하고 대입하는 두 가지의 방법을 제시했다.

```java
public class RemoteControlExample {
	public static void main(String[] args) {
		RemoteControl rc;		// 인터페이스명 변수명; 
		rc = new TV();	// 변수명 = 구현객체();
	}
}
```

```java
public class RemoteControlExample {
	public static void main(String[] args) {
		RemoteControl rc= new TV(); // 인터페이스명 변수명 = 구현객체();
	}								// 자동 타입 변환에 해당
}
```



## 인터페이스 사용

추상 메소드는 구현 객체에서 실체 메소드를 구현한대로 호출이 가능하다.

디폴트 메소드는 인터페이스에서 선언한 대로 호출이 가능하나, 구현 객체에서 재정의가 가능하다.

정적 메소드는 인터페이스로 바로 호출이 가능하다.

```java
public class Audio implements RemoteControl {
	private int volume;
    private boolean mute;  // 새로운 필드 추가

    public void turnOn() {
		System.out.println("Audio를 켭니다.");
	}	
	public void turnOff() {
		System.out.println("Audio를 끕니다.");
	}

	public void setVolume(int volume) {
		if(volume>RemoteControl.MAX_VOLUME) {
			this.volume = RemoteControl.MAX_VOLUME;
		} else if(volume<RemoteControl.MIN_VOLUME) {
			this.volume = RemoteControl.MIN_VOLUME;
		} else {
			this.volume = volume;
		}
		System.out.println("현재 Audio 볼륨: " + volume);
        
    @Override
    public void setMute(boolean mute) {  // 디폴트 메소드 재정의
        this.mute = mute;
        if(mute) {
			System.out.println("Audio 무음 처리");
		} else {
			System.out.println("Audio 무음 해제");
		}
    }
}
```

```java
public class RemoteControlExample {
	public static void main(String[] args) {
		RemoteControl rc = null;  // 인터페이스 변수 선언 
		rc = new TV();			  // TV 객체를 인터페이스 타입에 대입	
		rc.turnOn();				// 인터페이스의 추상메소드 호출 ["TV on" 출력]
		rc.setMute(true);			// 인터페이스의 디폴트메소드 호출 ["무음 처리" 출력]
		
		rc = new Audio();		// Audio 객체를 인터페이스 타입에 대입
		rc.turnOn();			// 인터페이스의 추상메소드 호출 ["TV on" 출력]
		rc.setMute(true);		// 구현 객체에서 재정의된 디폴트메소드 호출 ["Audio 무음 처리"]
				
		RemoteControl.changeBattery(); // 정적 메소드 호출	["건전지를 교환합니다." 출력]	
	}
}
```



## 인터페이스 활용하기

처음에 언급했던 Animal 클래스와 Vehicle 클래스를 통해 인터페이스를 활용해보자.

```java
public interface Fly {					// 인터페이스 선언
	public void fly();					// 추상 메소드
}
```



```java
public class Animal {
	public void eat() {	
	}
	public void sleep() {
		System.out.println("쿨쿨 잔다");
	}
}
```

```java
public class Bird extends Animal implements Fly{
	@Override				
	public void eat() {		// 부모 클래스인 Animal 메소드 재정의
		System.out.println("벌레를 먹는다");
	}
	
	public void fly() {		// fly 인터페이스 실체 메소드 정의
		System.out.println("날개로 난다");
	}
}
```

```java
public class Human extends Animal {
	@Override
	public void eat() {		// 부모 클래스인 Animal 메소드 재정의
		System.out.println("밥을 먹는다");
	}
	
	public void walk() {	// Human 메소드 정의
		System.out.println("걷는다");
	}
}
```

```java
public class Superman extends Human implements Fly{
	public void fly() {		// fly 인터페이스 실체 메소드 정의
		System.out.println("망토로 난다");
	}
}
```



```java
public class Vehicle {
	public void transfer(String start, String end) { // 메소드 정의
		String locate = start+"에서 "+end+"까지 "; 
		System.out.println(locate+" 이동합니다");
	}
}
```

```java
public class Car extends Vehicle {
	public void drive() {							// 메소드 정의
		System.out.println("부릉부릉 달립니다");
	}
}
```

```java
public class Airplane extends Vehicle implements Fly{
	public void flight() {							// 메소드 정의
		System.out.println("엔진으로 난다");
		}
    
	@Override
	public void fly() {			// fly 인터페이스 실체 메소드 정의
		flight();
	}
}
```



```java
public class Show {
	public void airShow(Fly f) {	// Fly 인터페이스를 매개변수로 airshow 메소드 정의
		f.fly();
	}
}
```

```java
public class Test {
	public static void main(String[] args) {
		Animal ah=new Human(); // Animal로 가져왔으므로 Human에서 정의된 메소드 사용 불가
		ah.eat();		// Human에서 재정의 된 메소드
		ah.sleep();		// Animal의 메소드 상속
		
		Human h=new Human();
		h.eat();	// Human에서 재정의 된 메소드
		h.sleep();	// Animal 메소드 상속
		h.walk();	// Human의 메소드
		
		Superman s=new Superman();
		s.eat();	// Human에서 재정의 된 메소드 상속
		s.sleep();	// Human이 Animal로부터 상속받은 메소드를 상속
		s.walk();	// Human의 메소드 상속
		s.fly();	// Superman에서 정의한 fly 인터페이스의 실체 메소드
        		
		Bird b=new Bird();
		b.eat();	// Bird에서 재정의 된 메소드
		b.sleep();	// Animal의 메소드 상속
		b.fly();	// Bird에서 정의한 fly 인터페이스의 실체 메소드
		
		Airplane a=new Airplane();
		a.transfer("인천", "상해"); // Vehicle의 메소드 상속
		a.flight();	// Airplane의 메소드
		a.fly();	// Airplane에서 정의한 fly 인터페이스의 실체 메소드
		
		Car c = new Car();
		c.transfer("서울", "부산");  // Vehicle의 메소드 상속
		c.drive();					// car의 메소드
		
		Show show=new Show();		// show 클래스 내 에어쇼 메소드 (매개변수)
		show.airShow(b);		
		show.airShow(s);
		show.airShow(a);
		
	}
}
```