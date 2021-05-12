# 열거 타입 (Enumeration)

데이터 중에는 몇 가지로 한정된 값만을 갖는 경우가 흔히 있다. 요일에 대한 데이터는 일곱 개의 한정된 값을 갖고, 계절에 대한 데이터는 네 개의 값만을 가진다. 이와 같이 한정된 값만을 갖는 데이터 타입이 열거 타입(Enum)이다. 

만약 class로 선언되는 부분에 enum이라고 선언되어 있다면, 이 객체는 상수의 집합으로 구성된 Enumeration이라는 사실을 알아차려야 한다. enum의 선언은 `public` `enum` `이름` {`상수 선언`} 으로 구성되어 있다. 상수들은 선언 시 모두 대문자로 작성하는 것이 관례이다. 

```java
public class Week { 					// class를 통해 상수를 열거한 경우
	public static final char MON='월';
	public static final char TUE='화';
	public static final char WED='수';
	public static final char THU='목';
	public static final char FRI='금';
	public static final char SAT='토';
	public static final char SUN='일';
}
```

```java
public enum Week {						// Enum을 통해 상수를 열거한 경우
	MON,
	TUE,
	WED,
	THU,
	FRI,
	SAT,
	SUN
}
```



모든 enum은 컴파일될 때 java.lang.Enum 클래스를 상속하게 되어 있다. 여기에는 몇 가지의 메소드들이 선언되어 있기 때문에 enum에서는 해당 매소드를 사용할 수 있게 되는 것이다.

* name() 메소드 - enum이 가지고 있는 문자열을 리턴 (String)
* ordinal() 메소드 - 몇 번째 열거 객체인지 리턴 (int)
* compareTo() 메소드 - 열거 객체들 간의 순번 차이를 리턴 (int)
* valuesOf() 메소드 - 동일한 문자열을 가지는 열거 객체를 리턴
* values() 메소드 - enum 내  열거 객체들을 배열로 리턴

```java
public class EnumMethod {
	public static void main(String[] args) {	
		Week today = Week.일요일;	// today에 열거 객체 `일요일` 참조
		
		//name() 메소드
		String dayOfWeek = today.name(); // String dayOfWeek에 참조된 '일요일' 문자열 리턴
		System.out.println(dayOfWeek);	// [일요일 출력]
		
		//ordinal() 메소드
		int order = today.ordinal();	// int값 order에 열거 객체 '일요일'의 순번값 리턴
		System.out.println(order);		// [6 출력}

		//compareTo() 메소드
		Week day1 = Week.월요일;		// day1에 열거 객체 '월요일' 참조
		Week day2 = Week.수요일;		// day2에 열거 객체 '수요일' 참조
		int result1 = day1.compareTo(day2);	// int값 result1에 ('월요일' 순번값- '수요일' 순번값) 리턴 
		int result2 = day2.compareTo(day1); // int값 result2에 ('수요일' 순번값- '월요일' 순번값) 리턴 
		System.out.println(result1); // [0-2 값 출력]
		System.out.println(result2); // [2-0 값 출력]

		//valueOf() 메소드
		Week weekDay = Week.valueOf("일요일"); // weekDay에 "일요일"과 동일만 문자열을 가진 열거 객체 '일요일' 참조
		if(weekDay == Week.토요일 || weekDay == Week.일요일) {
			System.out.println("주말이군");		// [주말이군 출력]
		} else {
				System.out.println("평일이군");
		}
		
		//values() 메소드
		Week[] days = Week.values(); // 열거 타입의 열거 객체들을 배열 days로 만들어 리턴 
		for(Week day : days) {		 // 향상된 for문 = days배열에서 day를 차례대로 가져와 실행문 반복
			System.out.println(day);
		}
	}
}
```



# 어노테이션 (Annotation)

어노테이션은 컴파일러에게 코드 문법 에러를 체크하도록 정보를 제공하거나, 소프트웨어 개발 툴이 코드를 자동으로 생성할 수 있도록 정보를 제공하거나, 실행 시 특정 기능을 실행하도록 정보를 제공하는 역할을 한다.

가장 대표적인 예로, 메소드가 오버라이드되었을 경우에는 컴파일러에게 오버라이드(재정의)된 것임을 알려주어 정확히 오버라이드가 되었는지 검사를 할 수 있게끔 하는 것이다. 

```java
public abstract class Animal {
	public String kind;
	public abstract void sound();
}
```

```java
public class Dog extends Animal { // Dog는 Animal을 상속받는다.
	public Dog() {
		this.kind = "포유류";
	}

	@Override						// 대표적인 어노테이션의 사용!
	public void sound() {
		System.out.println("멍멍");
	}
}
```

