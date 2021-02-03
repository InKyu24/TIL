#  참조 타입

데이터 타입에는 두 가지 종류가 있다. 이 둘은 메모리의 사용방법이 서로 다르다.

+ 기본 타입(Primitive type) : 실제 값을 변수 안에 저장

+ 참조 타입(Reference type) : 참조된 데이터 위치 주소 저장



## 1) null

참조 타입 변수는 객체를 참조하지 않는다는 뜻으로 null 값을 가질 수 있다.

null로 초기화 된 참조 변수는 Stack 영역에 생성된다.



## 2) String 타입

String은 참조 변수의 가장 대표적인 클래스로 문자열을 저장한다.

편의성을 위해 주소값이 아닌 내용값을 출력하기 때문에 new 생성자 없이도 literal로만 표현이 가능하다는 특징이 있다.

String 값은 String Literal Pool에 저장된다. 만약 동일한 문자열이 있다면 String 간의 객체 공유가 가능해진다.
그러나 new 연산자를 이용하여 생성된 String 문자열은 객체 공유가 없이 다른 주소값으로 저장된다.



## 3) 배열 타입

배열은 같은 타입의 데이터를 연속된 공간에 저장하는 자료구조로, 같은 타입의 데이터에 번호(Index)를 부여해 접근을 용이하게 할 수 있다.

> 배열의 번호는 0부터 시작한다는 것에 유의한다.

배열 선언은 [ ]를 이용해 두 가지 방식으로 선언할 수 있다.

```java
a.	int[] intArray; // 데이터타입[] 변수명;
b.	int intArray[]; // 데이터타입 변수명[];
```

배열에 선언과 동시에 데이터를 입력하는 방법도 있다.

```java
1.	int []a = new int[] {1, 2}; // a 배열에 1, 2 입력 및 생성 (배열 크기 2)
2.	int []b = {1, 2} 	        // b 배열에 1, 2 입력 및 생성 (배열 크기 2)
```

또는 배열 선언을 하면서 크기만을 정하고, 데이터는 입력하지 않을 수도 있다.

```java
int []c = new int[100];		// a 배열 생성 (배열 크기 100)   
```

배열의 크기는 length 필드로 확인할 수 있으며, 읽기 전용 필드이기 때문에 수정이 불가능하다.

```java
  int[ ]d = {10, 20, 30}  		// d 배열에 10, 20, 30 입력 및 생성 (배열 크기 3) 
  int num = d.length;  // 정수 데이터 변수 num에 d 배열의 크기인 3을 입력
```



### int 배열

int 배열은 정수만을 취급한다. 알파벳이 입력되는 것처럼 보이나 알파벳에 부여된 숫자가 저장되는 것이고, 이는 출력 하면 정확하게 확인할 수 있게 된다.

```java
package test.array;
public class IntTest {
	public static void main(String[] args) {
		int []all=new int[100]; 	// 배열 크기가 100인 정수 배열 all 생성
		System.out.println(all);	// 배열 all의 데이터 저장 위치 주소 출력
        
		all[0]=1;					// 0번째 배열에 정수 1 입력
		all[2]='a';					// 2번째 배열에 문자 'a' 입력
		System.out.println(all[0]);	// 0번째 배열값 출력
		System.out.println(all[1]); // 1번째 배열값 출력 (기본값 0)
		System.out.println(all[2]); // 2번째 배열값 출력 ('a'의 숫자값 97)
		System.out.println(all.length); // 배열 all의 크기(100) 출력
	}		
}
```

```java
package test.array;
public class IntTest {
	public static void main(String[] args) {
		int []all=new int[100]; 		// 배열 크기가 100인 정수 배열 all 생성
		
		for(int i=0;i<all.length;i++) {	// i값이 배열크기 100이 될 때까지 1씩 증가시키면서,
			all[i]=i;					// i번째 배열에 i값 입력하고,
			System.out.println(all[i]); // i번째 배열을 출력하는 반복문 수행
		}
	}
}
```



### String 배열

```java
package test.array;
public class StringTest {
	public static void main(String[] args) {
		String []all=new String[5];	// 크기 5인 String 배열 all 생성
		System.out.println(all);	// 배열이 저장되는 데이터 위치 주소 출력
		System.out.println(all[0]);	// 0번째 배열값 출력 [기본값 null이 출력됨]
		
		String s1=new String("java");//s1에 "java" 입력
		all[0]=s1;				// 0번째 배열에 s1값인 "java" 입력
		
		all[1]=new String("java"); // 1번째 배열에 "java" 직접 입력
		
		all[2]="java";	
		all[3]="java"; // 2번째와 3번째 배열에 더 짧게  "java" 직접 입력
		
		for(int i=0;i<all.length;i++) {	
			System.out.println(all[i]);	
     	}				// 배열 all 차례로 모두 출력 [java java java java null 순으로 출력]
		System.out.println(all[2]==all[3]);	// 2번쨰와 3번째 배열 비교 [같기에 true 출력]
	}
}
```

* 만약 배열 내 같은 문자열로 반복하여 입력한다면, String Literal Pool 내에 있는 c-value에 의하여 같은 주소값을 가지는 문자열로 채워지게 된다. **단, new 생성자를 사용하지 않아야 한다.** 

  > 따라서 같은 java라는 글자임에도 all[2]와 all[3]은 같은 값으로 나타나고, 나머지는 모두 서로 다른 값처럼 인식하게 된다.

  

### public static void main (String[] args) {  }

String[] args는 JVM이 생성하는 args라는 배열로 크기는 0으로 나타난다.

>  정해지지 않은, 제한이 없는 특이한 배열?

args 배열은 실행 시에 외부에서 넘어오는 데이터를 받는다. 그 데이터는 `Run Configurations` 옵션에서 `Argument` 탭을 선택하게 되면, `Program arguments`에 기입할 수 있다. 여기에 띄어쓰기 형식으로 구분되게 작성하면 args 배열의 크기는 입력한 데이터 크기만큼 커지는 것을 알 수 있다.