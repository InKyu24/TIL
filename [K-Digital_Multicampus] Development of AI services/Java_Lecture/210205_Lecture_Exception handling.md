# Exception

하드웨어의 오동작, 고장으로 인해 프로그램 실행 오류가 발생하는 것을 에러(error)라고 한다. 이는 결국 JVM 실행에 문제가 생긴 것으로 개발자는 이런 에러에 대처할 방법이 전혀 없다.

자바에서는 에러 이외에 예외(exception)라고 부르는 오류가 있다. 예외란 사용자의 잘못된 조작이나 개발자의 잘못된 코딩으로 발생하는 프로그램 오류를 말한다. 예외가 발생되면 프로그램 실행 오류가 발생하는 것은 에러와 같지만 예외는 예외 처리(exception handling)를 통해 프로그램을 종류하지 않고 정상 실행 상태를 유지시킬 수 있다.

예외를 처리하는 방법을 알게 되면 보다 안전하고 유연한 프로그래밍을 할 수 있게 된다.

예외는 일반 예외와 실행 예외로 나뉜다. 일반 예외는 소스 코드를 컴파일하는 과정에서 예외 처리 코드가 필요한지 검사하는 과정이 필요하기 때문에 컴파일러 체크 예외라고 불린다. 만약 예외 처리 코드가 없다면 컴파일 오류가 발생하게 된다. 실행 예외는 컴파일하는 과정에서 예외 처리 코드를 검사하지 않는 예외를 말한다. 두 가지 예외는 컴파일 시 예외처리를 확인하는 지에 대한 여부에 따라 차이가 있을 뿐, 모두 예외 처리가 필요하다.

자바에서는 예외를 클래스로 관리한다. 즉, 예외를 클래스 중 하나로 보고 있다는 것이다. 실행 도중에 예외가 발생하면 해당 예외 클래스로 객체를 생성하고, 예외 처리 코드에서 예외 객체를 이용할 수 있도록 해준다. 모든 예외 클래스들은 java.lang.Exception 클래스를 상속받고 있다.



+ 컴파일러가 직접 체크를 해주는 Checked Exception(일반 예외)

+ 컴파일러가 직접 체크를 안해주는 Unchecked Exception(실행 예외)

  

[![img](https://lh3.googleusercontent.com/-zDCQRCUZ4Ps/YB-LmMLZTWI/AAAAAAAAGVs/FNESMeo8h2gW44FMpK0-_BhhNywg-4jtwCLcBGAsYHQ/w640-h270/image.png)](https://lh3.googleusercontent.com/-zDCQRCUZ4Ps/YB-LmMLZTWI/AAAAAAAAGVs/FNESMeo8h2gW44FMpK0-_BhhNywg-4jtwCLcBGAsYHQ/image.png)

실행 예외는 자바 컴파일러가 체크를 하지 않기 때문에 개발자의 경험에 의해서 예외 처리 코드를 삽입해야 한다. 만약 예외 처리 코드를 넣지 않았을 경우, 해당 예외가 발생하면 프로그램은 곧바로 종료된다.



## 실행 예외

### NullPointerException

자바에서 가장 빈번하게 발생하는 실행 예외는 java.lang.NullPointerException일 것이다. 이것은 객체 참조가 없는 상태를 의미한다. null 값을 갖는 참조 변수로 객체 접근 연산자인 도트(.)를 사용했을 때 발생한다.

즉, 객체가 없는 상태에서 객체를 사용하려 할 때 발생하는 것이다.

```java
public class NPE {
    public static void main(String[] args) { 
		String data = null;
		System.out.println(data.toString());	// NullPointerException 발생
	}
}
```



### ArrayIndexOutOfBoundsException

배열에서 인덱스 범위를 초과하여 사용할 경우에는 실행 예외인 java.lang.ArrayIndexOutOfBoundsException이 발생한다. 따라서 배열값을 읽기 전에 배열의 길이를 한 번 더 확인해야 한다.

```java
public class AIOOBE {
	public static void main(String[] args) {
		int[] array= {10, 20};
		System.out.println(array[3]);	// ArrayIndexOutOfBoundsException 발생
	}							
}
```



### NumberFormatException

문자열로 되어 있는 데이터를 숫자로 변경하는 경우가 있다. 이 때 문자열이 숫자로 변환될 수 없다면 java.lang.NumberFormatException이 발생하게 된다.

예시를 보기 전에 문자열을 숫자 데이터로 변경하는 법에 대해 숙지할 필요가 있다.
`Integer.parseInt(String s)`는 문자열 s를 정수로 변환해서 리턴하는 메소드이고, `Double.parseDouble(String s)`는 문자열을 실수로 변환해서 리턴하는 메소드임을 기억하자.

```java
public class NFE {
	public static void main(String[] args) {
		String data="삼";	
		int value = Integer.parseInt(data); // NumberFormatException 발생
		System.out.println(value);	
	}					
}
```



### ClassCastException

부모 클래스와 자식 클래스에서, 인터페이스와 구현 클래스에서 타입 변환(casting)이 발생한다. 이러한 관계가 갖춰지지 않는다면 클래스는 다른 클래스로 타입 변환을 할 수 없게 된다. 억지로 타입 변환을 시도하는 경우에는 java.lang.ClassCastException이 발생한다.



Animal 클래스를 부모 클래스로 하는 Cat 클래스와 Dog 클래스가 있다고 가정해보자. 그리고 Power 인터페이스에 Radio 클래스와 Audio 클래스가 구현 클래스로 있다고 가정해보자.

```java
Animal ad = new Dog(); 	// Dog 클래스를 부모 객체로
Dog dd = (Dog) ad; 		// 부모 객체로 생성된 Dog 클래스를, 클래스 본래 타입으로 변환

Power pr = new Radio(); // Radio 클래스를 인터페이스로
Radio rr = (Radio) pr;	// 인터페이스로 선언된 pr을 구현 클래스 본래 타입으로 변환
```

그러나 아래와 같이 타입 변환을 하게 되는 경우 java.lang.ClassCastException이 발생한다.

```java
Animal ad = new Dog(); 	// Dog 클래스를 부모 객체로
Cat c = (Cat) ad; 		// 대입된 객체가 아닌 다른 클래스 타입으로 변환 [ClassCastException 발생]
						
Power pr = new Radio(); // Radio 클래스를 인터페이스로
Radio r = (Radio) pr;	// 대입된 객체가 아닌 다른 클래스 타입으로 변환 [ClassCastException 발생]
```

이러한 오류를 발생시키지 않기 위해서는 타입 변환 전에 타입 변환이 가능한 지 여부를 확인하는 것이 좋다. 타입 변환 가능 여부는 `instanceof` 연산자로 확인하는 것이 좋다. `instanceof` 연산의 결과가 true이면 좌측 객체를 우측 타입으로 변환이 가능하다는 의미이다.

```java
Animal ad = new Dog();
if (ad instanceof Dog) {				// if 조건문 true
    Dog dd = (Dog) ad;
} else if(ad instanceof Cat) {
    Cat c = (Cat) ad;
}

Power pa = new Audio();
if (pa instanceof Radio) {
    Radio r = (Radio) pa;
}else if(pa instanceof Audio) {			// else if 조건문 true
    Audio aa = (Audio) pa;
}
```



## 예외 처리하기

프로그램에서 예외의 발생으로 갑작스러운 종료가 발생할 우려가 있다. 따라서 정상적인 실행을 계속 유지할 수 있도록 처리하는 코드를 예외 처리 코드라고 한다. 예외 처리 코드는 `try` - `catch` - `finally` 블록을 이용한다. `try` - `catch` - `finally` 블록은 생성자 내부와 메소드 내부에서 작성되어 일반 예외와 실행 예외가 발생할 경우 예외 처리를 할 수 있도록 해준다. 



### `try` - `catch` - `finally` 블록

`try` - `catch` - `finally` 블록의 구성은 아래와 같다.

```java
try {
    예외 발생 가능 코드
} catch (예외클래스 e) {
    예외 처리
} finally {
    항상 실행;
}
```

`try` 블록의 코드가 정상 실행되면 `catch` 블록은 건너 뛰고 `finally` 블록의 코드를 실행하게 된다. 하지만 만약에 `try` 블록의 코드에서 예외가 발생한다면, 즉시 실행을 멈추고  `catch` 블록으로 이동하여 예외 처리 코드를 실행한다. 그리고 `finally` 블록의 코드를 실행하게 된다. `fianlly` 블록은 예외 발생 여부와 상관없이 항상 실행할 내용이 있는 경우에만 작성해주면 되는 선택 사항으로 생략이 가능하다. `try` - `catch` 블록에서 return문을 사용하더라도 `finally` 블록은 항상 실행된다.



### 예외 처리 코드 작성

앞에서 알아본 실행 예외가 발생하는 코드들을 가지고, `try` - `catch` - `finally` 블록으로 예외 처리를 해보자.

```java
public class NPE {
	public static void main(String[] args) { 
		String data = null;
		try {
			System.out.println(data.toString());
		} catch (NullPointerException e) {
			System.out.println("객체가 없는 상태");
		}
	}
}
```

```java
public class AIOOBE {
	public static void main(String[] args) {
		int[] array= {10, 20};
      	try {
        	System.out.println(array[3]);
        }catch (ArrayIndexOutOfBoundsException e) {
        	System.out.println("인덱스 범위를 초과");
        }	
	}							
}
```

```java
public class NFE {
	public static void main(String[] args) { 
    	String data="삼";	
		try {
	        int value = Integer.parseInt(data); // NumberFormatException 발생
			System.out.println(value);	        
        }catch (NumberFormatException e) {
            System.out.println("숫자로 변환 불가");	        
        }finally {
            System.out.println("다시 시도하세요");
        }
	}					
}
```



### 다중 catch

`try` 블록 내부에서는 다양한 종류의 예외가 발생할 수 있다. 발생되는 예외별로 예외 처리 코드를 다르게 하기 위해서는 `catch` 블록을 다중으로 작성해야 한다. 하나의 예외가 발생하면 즉시 실행을 중단하고 `catch` 블록으로 이동하기 때문에 `catch` 블록이 여러 개라 할지라도 단 하나의 catch 블록만 실행된다.

다중의 `catch` 블록을 작성할 때는 상위 예외 클래스가 하위 예외 클래스보다 먼저 나오지 않도록 해야 한다. 예외가 발생했을 때, 예외를 처리해줄 `catch` 블록은 위에서부터 찾아서 들어가기 때문이다.

```java
public class Test {
	public static void main(String[] args) {
		try {
			int x=100;
			args[0]=null;
			int y=Integer.parseInt(args[0].trim());		
					
			System.out.println(x/y);
		}catch(ArithmeticException e) {
			System.out.println("0으로 나눌 수 없음");
		}catch(NumberFormatException e) {
			System.out.println("숫자로 변환 불가");
		}catch(ArrayIndexOutOfBoundsException e) {
			System.out.println("인덱스 범위를 초과");
		}catch(Exception e) {						// 예외 클래스의 조상으로 마지막까지 catch!
            System.out.println(e.getMessage()); // 예외 메시지 출력
			e.printStackTrace(); 	// 예외 추적 내용 출력
		}
		
		System.out.println("중요한 일 시작!");
	}
}
```



### 예외 떠넘기기

메소드 내부에서 예외가 발새할 수 있는 코드를 작성할 때 `try` - `catch` 블록으로 예외를 처리하는 것이 기본이지만, 경우에 따라서는 메소드를 호출한 곳으로 예외를 떠넘길 수도 있다. 이 때 사용하는 키워드가 바로 `throws`이다. `throws` 키워드는 메소드 선언부 끝에 작성되어 메소드에서 처리하지 않은 예외를 호출한 곳으로 떠넘기는 역할을 한다.

[![img](https://lh3.googleusercontent.com/-BaOuvSU9fNw/YB-sPrCh0nI/AAAAAAAAGV8/DaWdNtQZ_doUTctbEtJc_ApjS-Uf8TLNgCLcBGAsYHQ/w640-h150/image.png)](https://lh3.googleusercontent.com/-BaOuvSU9fNw/YB-sPrCh0nI/AAAAAAAAGV8/DaWdNtQZ_doUTctbEtJc_ApjS-Uf8TLNgCLcBGAsYHQ/image.png)



### 사용자가 직접 예외 정의

```java
public class Calculator {
// 정수 x와 y를 매개변수로 하는 divide 메소드 선언 [MyException 클래스로 떠넘기기]
	public int divide (int x, int y) throws MyException { 
        int z=0;
		if(y==0) {		// y 값이 0일 때 문자열을 가지고 MyEception 클래스에 떠넘긴다. 
			throw new MyException("y는 0으로 입력 안됨"); 
        }
        z=x/y;		// y값이 아닌 경우에 x를 y로 나누어 z값에 결과 저장
		return z;	// z값 리턴
	}
}
```

```java
public class MyException extends Exception{ // MyException에서 Exception 클래스 상속
	public MyException(String message) {	// Exception의 message 문자열을 매개변수로 하는 생성자 정의
		super(message);
	}
	
}
```

```java
public class Test {
	public static void main(String[] args) {
        
		Calculator c=new Calculator();	// Calculator 클래스 호출
		int result=0;
        
		try {
			result = c.divide(100, 0);	// throws가 붙은 메소드는 반드시 try 블록 내에서 호출
		} catch (MyException e) {	// throws를 통해 떠넘긴 예외 클래스
			System.out.println(e.getMessage());
		}finally {
  	      System.out.println(result);
          System.out.println("중요한 일 시작");
	}
}
```

