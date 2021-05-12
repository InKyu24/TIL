# 1. Data Setting Method

메소드를 통해 데이터의 입력과 출력을 보다 쉽게 할 수 있다.

메소드의 정의(선언)은 `리턴타입` `메소드이름` (`매개변수선언`) {`실행코드`;}로 구성되어 있으며, 메소드 호출(실행)은 `메소드이름`  (`매개변수 값`); 으로 구성되어 있다. 만약 다음과 같이 클래스 외부에서 메소드를 호출하기 위해서는 `클래스이름` `참조변수` = new `클래스이름` (`매개변수값`);으로 클래스를 객체화하여 불러온 뒤, `참조변수`.`클래스참조변수`  `메소드이름`  (`매개변수 값`); 으로 메소드를 호출할 수 있게 된다.

```java
package test1;
public class MyProfile {
	String name;
	int age;
	double tall;

	public void setProfile(String name, int age, double tall) { // 메소드1 정의
		this.name=name;
		this.age=age;
		this.tall=tall;
	}
	public void printProFile() {				// 메소드2 정의
		System.out.println(name);
		System.out.println(age);
		System.out.println(tall);
	}
}
```

```java
package test1;
public class Test {
	public static void main(String[] args) {
		MyProfile m1=new MyProfile();
		m1.setProfile("최인규", 31, 177.5);	// 메소드1 호출
		System.out.println(m1);
		m1.printProFile();								// 메소드2 호출
		MyProfile m2=new MyProfile();
		m2.setProfile("홍길동", 28, 185.5);	// 메소드1 호출
		System.out.println(m2);
		m2.printProFile();								// 메소드2 호출	
	}
}
```



# 2. 산술 연산자

기본적인 산술 연산자는 5가지로 더하기, 빼기, 곱하기, 몫, 나머지가 있다.



```java
int c=a+b; // a와 b 더하기
int c=a-b; // a에서 b 빼기
int c=a*b; // a와 b 곱하기
int c=a/b; // a에서 b 나눈 몫
int c=a%b; // a에서 b 나눈 나머지
```

나아가서, 하나의 변수에 계속해서 연산을 누적하는 경우에는 간략하게 연산자를 사용할 수 있다.

```java
int d+=e;	// d=d+e; 와 같은 의미
int d-=e;	// d=d-e; 와 같은 의미
int d*=e;	// d=d*e; 와 같은 의미
int d/=e;	// d=d/e; 와 같은 의미
int d%=e;	// d=d%e; 와 같은 의미
```

마지막으로 1씩 증감을 할 수 있는 연산자가 있는데, 변수이름과 연산자의 순서에 따라 선후가 달라진다.

```java
int i=100;
	System.out.println(++i);	// 1만큼 증가하고 출력
	System.out.println(i++);	// 출력하고 1만큼 증가
	// System.out.println(--i); 	--1 1만큼 감소하고 출력
	// System.out.println(i--); 	1-- 출력하고 1만큼 감소
```



# 3. 논리 연산자

논리 연산자는 변수 값을 서로 비교하거나, 조건 여부를 확인하는데 사용된다.

[<img src="https://lh3.googleusercontent.com/-MQ0Ov4t34_M/YBqZwSsOQSI/AAAAAAAAGUg/es75BawcICM-DnRGT7La8Pv_YZQjJW1YQCLcBGAsYHQ/w640-h485/image.png" alt="img" style="zoom: 67%;" />](https://lh3.googleusercontent.com/-MQ0Ov4t34_M/YBqZwSsOQSI/AAAAAAAAGUg/es75BawcICM-DnRGT7La8Pv_YZQjJW1YQCLcBGAsYHQ/image.png)

```java

//			삼항 연산자_조건식
//				(조건식) ? A:B	조건이 true 이면 A를 수행, false이면 B를 수행
////		
		int d=-1;		
		System.out.println(Integer.toBinaryString(d));
		System.out.println(~d);			// b의 보수 출력
		System.out.println(d);
		d=d>>1;							// b를 오른쪽으로 한 비트 밀기
		System.out.println(d);
		System.out.println(Integer.toBinaryString(d));		
//		
	}
}
```





# 4. 비트 연산자

```java

```



정수 타입만 비트 연산이 가능

\* 부호 비트(MSB)

 a<<b, a>>b, a>>>b : a를 왼쪽, 오른쪽으로 b만큼 비트 밀기

\* >>와 >>>의 차이: >>는 정수 a의 최상위 부호 비트와 같은 값으로 채워지는 반면에, >>>는 빈자리를 0으로 채운다는 점에서 차이가 있다.



# 5. 삼항 연산자

삼항 연산자는 조건을 제시하고, 조건에 충족 여부에 따라 결과값을 다르게 입력할 수 있는 연산자이다.

(`조건`) ? `'true값'` : `'false값' `

```java
int score=90;

char grade=(score>=90)? 'A':'B'; // score가 90 이상이면 A 문자열 입력, 아니면 B 문자열 입력
System.out.println(grade);	// 따라서 grade에 A가 출력된다
```



# 6. 제어문의 종류



## 1] 조건문

두 가지 조건문(if & switch)을 통해 입력된 month 데이터의 값에 맞는 마지막 날짜를 출력하고, 1부터 12까지 범위 내에 없으면 에러메시지를 출력시키는 조건문을 연습.



### 1) if 조건문

if 조건문의 형태는 다음과 같다.

if (`조건1`) {
`조건1이 true일 때 실행문`;
} else if(`조건2`) {
`조건2가 true일 때 실행문`;
}else {
`모든 조건이 충족되지 않을 때 실행문`;
}



```java
package test.stmt;
public class IfTest {
	public static void main(String[] args) {
		int month=10;
		if(month==1||month==3||month==5||month==7||month==8||month==10||month==12) {
            																// 조건문1
			System.out.println(month+"월은 31일까지 있지.");	// 조건문1 해당 시 수행
		}else if(month==2) {									// 조건문2
			System.out.println(month+"월은 보통 28일까지 있지."); // 조건문2 해당 시 수행
		}else if(month==4||month==6||month==9||month==11) {		// 조건문3
			System.out.println(month+"월은 30일까지 있지."); 	// 조건문3 해당 시 수행
		}else {													// 나머지 조건
			System.out.println("잘못된 입력입니다.");		// 나머지 조건에 대한 수행
		}
	}
}
```



### 2) switch 조건문

switch 조건문의 형태는 다음과 같다.
`데이터` 내에는 `byte`, `short`, `int`, `char` 데이터만 가능하다는 점에 유의한다.

switch (`데이터`) {
case `값(1)`:
	`데이터와 값(1)이 일치하는 경우, 실행문`;
break;
case `값(2)` :
	`데이터와 값(2)이 일치하는 경우, 실행문`;
break;
default : `모든 조건이 충족하지 않는 경우, 실행문`;
}



```java
package test.stmt;
public class SwitchTest {
	public static void main(String[] args) {
		int month=10;
		switch(month) {
		case 1: 
		case 3:
		case 5:
		case 7:
		case 8:
		case 10:
		case 12:													// 조건문1
			System.out.println(month+"월은 31일까지");				// 조건문1 해당 시 수행
		break;														// 조건문1 탈출
		
		case 2:													 // 조건문2
            System.out.println(month+"월은 보통 28일까지");		// 조건문2 해당 시 수행
		break;													 // 조건문2 탈출
		
		case 4:
		case 6:
		case 9:
		case 11:												// 조건문3
			System.out.println(month+"월은 30일까지");			// 조건문3 해당 시 수행
		break;													// 조건문3 탈출
		
		default: System.out.println("잘못된 입력입니다."); // 조건에 해당하지 않는 경우
		}
	}
}
```

 

## 2] 반복문

반복문에는 while 반복문과 for 반복문이 있다. 0부터 99까지 출력하는 반복문을 연습.



### 1) while 반복문

while 반복문은 형태는 다음과 같다.

while (`조건`) {
`조건 충족 시 실행문`;
`반복 위한 증감치 제시`;
}

```java
package test.stmt;
public class WhileTest {
	public static void main(String[] args) {
		int i=0;
		while (i<100) {
			System.out.println(i);
			i++;
		}	// 결과적으로 0에서부터 99까지 나타나며, 현재 i값은 100이 된다.
		System.out.println("i="+i); // [i=100]
	}
}
```



### 2) do ~ while 반복문 [최소 한 번은 수행]

do ~ while 반복문은 조건에 충족되지 않더라도 한 번은 실행문을 수행할 수 있도록 하는 형태로 되어있다.

do {
	실행문;
	증감치 제시;
} while (조건) ;

```java
package test.stmt;
public class DoWhileTest {
	public static void main(String[] args) {
		int i=1000;
		do{
			System.out.println(i);
			i++;
		}while (i<100);
	}	// i가 100 이상임에도 불구하고 1000이 출력되었으며, 현재 i 값은 1001이 되어있다.
}
```



### 3) For 반복문

for 반복문은 형태는 다음과 같다.

for (`초기값`;`조건`;`증감치`)  {
`조건 충족 시 실행문`;
}

> 초기값이 중복된다면 공백으로 비워두고 작성하지 않을 수 있다.

```java
package test.stmt;
public class ForTest {
	public static void main(String[] args) {
		int i=0;
		for( ;i<100;i++) {
			System.out.println(i);
		}	// 결과적으로 0에서부터 99까지 나타나며, 현재 i값은 100이 된다.
		System.out.println("i="+i); // [i=100]
	}
}
```



## 3] break, continue 키워드

### 1) break;

```java
package test.stmt;
public class BreakTest {
	public static void main(String[] args) {
		int i=0;
		for( ;i<10;i++) {		// 0부터 9까지 i값을 계속 키워나가면서 출력하는 반복문 실행
			if(i==5) {			// i 값이 5가 되었을 때
				break;			// 반복문 탈출
			}
			System.out.println(i); // 0, 1, 2, 3, 4 출력
		}
		System.out.println("i="+i); // [i=5]가 출력
	}
}
```



### 2) continue;

```java
package test.stmt;
public class ContinueTest {
	public static void main(String[] args) {
		int i=0;
		for( ;i<10;i++) {	// 0부터 9까지 i값을 계속 키워나가면서 출력하는 반복문 실행
			if(i==5) {		// i 값이 5가 되었을 때
				continue;	// 실행문을 폴짝 건너뛰고, 다시 반복문 진행
			}
			System.out.println(i); // 0, 1, 2, 3, 4, 6, 7, 8, 9 출력
		}
		System.out.println("i="+i); // [i=10]이 출력
	}
}
```
