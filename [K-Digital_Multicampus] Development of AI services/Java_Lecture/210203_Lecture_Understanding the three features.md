# 캡슐화, 상속성, 다형성을 활용한 프로그래밍



> 세 가지 도형 (Circle, Rectangle, Triangle)의 넓이를 출력(Printer)하기 위한 프로그래밍(Test)을 한다고 가정한다면 아래와 같은 코드를 작성할 수 있다.

```java
public class Circle {
	int radius;
	public void areaCircle() {		// 원의 넓이를 출력하는 areaCircle 메소드 정의
		System.out.println("원의 넓이="+(3.14*radius*radius));
	}
}
```

```java
public class Rectangle {
	int w,h;
	public void areaRec() {			// 사각형의 넓이를 출력하는 areaRec 메소드 정의
		System.out.println("사각형의 넓이="+(w*h));
	}
}
```

```java
public class Triangle {
	int w,h;
	public void areaTri() {			// 삼각형의 넓이를 출력하는 areaTri 메소드 정의
		System.out.println("삼각형의 넓이="+(w*h/2));
	}
}
```

```java
public class Printer {
	public void print(Circle c) {	// [Circle c를 매개변수로 받는 메소드 정의]
			c.radius=5;				// radius 값을 5로 입력
			c.areaCircle();			// 원의 넓이 출력 메소드 호출
    }
  	public void print(Rectangle r) { // [Circle c를 매개변수로 받는 메소드 정의]
			r.h=3;			// h 값을 3으로 입력
			r.w=4;			// w 값을 4로 입력
			r.areaRec();	// 사각형의 넓이 출력 메소드 호출
    }    
    public void print(Triangle t) { // [Circle c를 매개변수로 받는 메소드 정의]
			t.h=8;	// h 값을 8로 입력
			t.w=2;  // w 값을 2로 입력
			t.areaTri(); // 삼각형의 넓이 출력 메소드 호출
		}
	}
}
```

```java
public class Test {
	public static void main(String[] args) {
		Circle c=new Circle();		 // Circle 클래스로 c라는 객체를 생성
		Rectangle r=new Rectangle(); // Rectangle 클래스로 r이라는 객체를 생성
		Triangle t=new Triangle();	 // Triangle 클래스로 t라는 객체를 생성
		Printer out=new Printer();   // Printer 클래스로 out이라는 객체를 생성
		out.print(c);			// 매개변수에 Circle을 넣어 print 메소드 실행
		out.print(r);			// 매개변수에 Rectangle을 넣어 print 메소드 실행
		out.print(t);			// 매개변수에 Triangle을 넣어 print 메소드 실행
	}
}
```



> 위와 같은 코드처럼 클래스(Printer)에 같은 이름의 메소드(print)를 반복하여 넣는 것을 overload라고 한다.
>
> 이러한 방식은 새로운 도형이 추가되는 것에 너무 많은 수고로움을 느낄 것이다.
>
> 따라서 다른 방식으로 새롭게 다시 작성해보자.



```java
public class Shape {
    public void area() { 				// area 라는 메소드 정의
}
```

```java
public class Circle extends Shape{ // Shape 클래스를 상속받는 Circle 클래스
	int radius;
	public void area() { 				// area 메소드를 재정의
		System.out.println("원의 넓이="+(3.14*radius*radius));
	}
}
```

```java
public class Rectangle extends Shape{ // Shape 클래스를 상속받는 Rectangle 클래스
	int w,h;
	public void area() { 			// area 메소드를 재정의
		System.out.println("사각형의 넓이="+(w*h));
	}

}
```

```java
public class Triangle extends Shape{ // Shape 클래스를 상속받는 Triangle 클래스
	int w,h;
	public void area() { 			// area 메소드를 재정의
		System.out.println("삼각형의 넓이="+(w*h/2));
	}
}
```

```java
public class Printer {
    public void print(Shape s) {	// Shape s를 매개변수로 하는 print 메소드 정의
			s.area();					// 매개변수 s를 활용한 area 메소드 실행
	}
}
```

```java
public class Test {
	public static void main(String[] args) {
		Circle c=new Circle();		 // Circle 클래스로 c라는 객체를 생성
		Rectangle r=new Rectangle(); // Rectangle 클래스로 r이라는 객체를 생성
		Triangle t=new Triangle();	 // Triangle 클래스로 t라는 객체를 생성
		Printer out=new Printer();   // Printer 클래스로 out이라는 객체를 생성
		
		out.print(c); // 매개변수에 Circle에서 재정의 된 메소드 실행
		out.print(r); // 매개변수에 Rectangle에서 재정의 된 메소드 실행
		out.print(t); // 매개변수에 Triangle에서 재정의 된 메소드 실행
	}
}
```



> 이렇게 작성한 클래스들의 재사용될 수 있도록 하기 위해서는 데이터의 직접 접근을 불가능하게 하고, 메소드만을 사용할 수 있게끔 캡슐화를 진행해야 한다.



```java
public class Shape {
	public void area() {
	}
}
```

```java
public class Circle extends Shape{
	private int radius;		// 데이터의 직접 접근을 숨기기 위해, private 접근지정자 사용 
    
	public int getRadius() { // get 메소드 정의
		return radius;
	}
    
	public void setRadius(int radius) { // set 메소드 정의
		if (radius>0) {					// 조건문을 통한 유효성 검사
			this.radius = radius;
		}else {
			System.out.println("반지름은 0보다 클 것");
		}
	}

	public void area() {
		System.out.println("원의 넓이="+(3.14*radius*radius));
	}
}
```

```java
public class Rectangle extends Shape{
	private int w,h;	// 데이터의 직접 접근을 숨기기 위해, private 접근지정자 사용
	
	public int getW() { 	// get 메소드 정의
		return w;
	}
	public void setW(int w) { // set 메소드 정의
		if (w>0) {				// 조건문을 통한 유효성 검사
			this.w = w;
		}else {
			System.out.println("밑변은 0보다 클 것");
		}
		
	}

	public int getH() {			// get 메소드 정의
		return h;
	}

	public void setH(int h) {	// set 메소드 정의
		if (h>0) {				// 조건문을 통한 유효성 검사
			this.h = h;
		}else {
			System.out.println("높이는 0보다 클 것");
		}
		
	}

	public void area() {
		System.out.println("사각형의 넓이="+(w*h));
	}

}
```

```java
public class Triangle extends Shape{
private int w,h;		// 데이터의 직접 접근을 숨기기 위해, private 접근지정자 사용
	
	public int getW() {			// get 메소드 정의
		return w;
	}

	public void setW(int w) {	// set 메소드 정의
		if (w>0) {				// 조건문을 통한 유효성 검사
			this.w = w;
		}else {
			System.out.println("밑변은 0보다 클 것");
		}
		
	}

	public int getH() {			// get 메소드 정의
		return h;
	}

	public void setH(int h) {	// set 메소드 정의
		if (h>0) {				// 조건문을 통한 유효성 검사
			this.h = h;
		}else {
			System.out.println("높이는 0보다 클 것");
		}
		
	}
	public void area() {
		System.out.println("삼각형의 넓이="+(w*h/2));
	}
}
```

```java
public class Printer {
	
	public void print(Shape s) {
			s.area();
	}
}

```

```java
public class Test {
	public static void main(String[] args) {
		Circle c=new Circle();
		Rectangle r=new Rectangle();
		Triangle t=new Triangle();
		Printer out=new Printer();
		
        c.setRadius(3);		// Circle 클래스 radius 값 입력
		r.setW(4);			// Rectangle 클래스 w 값 입력
		r.setH(5);			// Rectangle 클래스 h 값 입력
		t.setW(6);			// Triangle 클래스 w 값 입력
		t.setH(7);			// Triangle 클래스 h 값 입력
        
		out.print(c);
		out.print(r);
		out.print(t);
	}
}
```

