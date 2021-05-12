# 1. 다차원 배열

int \[ ][ ]all=new int [3][2];

위와 같이 [ ]의 개수를 늘리게 되면, 개수에 따라 N차원 배열이라고 한다.

```java
package test.multi.array;
public class Test {
	public static void main(String[] args) {
        int all[][]=new int[3][2];
		System.out.println(all);	// 전체 배열의 주소값
		System.out.println(all[0]);	//
		System.out.println(all[1]);	//
		System.out.println(all[2]);	// 두 칸의 배열인 N번째 배열 주소값	
		all[0][0]=100;
		all[0][1]=200;
		all[1][0]=300;
		all[1][1]=400;
		all[2][0]=500;
		all[2][1]=600;	// 다차원배열 칸마다 데이터 입력
		
		System.out.println(all.length);	// 전체 다차원 배열의 크기 3
		System.out.println(all[0].length); // 0번째 배열의 크기 2

        // 가변적인 배열 설정도 가능하다.
		int a[][]=new int[3][]; // 일차원 배열의 크기만 정하는 이차원 배열
		System.out.println(a[0]); // 크기가 정해지지 않은 배열이기에 주소값 null
		a[0]=new int[4];	// a[0]에 4칸의 배열 설정
		System.out.println(a[0]); // 크기가 정해진 후 주소값
		a[1]=new int[1];	// a[1]에 1칸의 배열 설정
		char [][]all2= {{'a','b'},{'c','d','e'}};// char[2][] 배열 생성&데이터 입력
		
        System.out.println(all2.length);
		System.out.println(all2[0][0]);
		System.out.println(all2[0][1]);
		System.out.println(all2[1][0]);
		System.out.println(all2[1][1]);
		System.out.println(all2[1][2]);
	}
}
```



# 2. 배열 복사

```java
package test.array.copy;
public class ArrayCopyExample {
	public static void main(String[] args) {
		String[] oldStrArray = {"java", "array","copy"};
		String[] newStrArray = new String[5];
		
		System.arraycopy(oldStrArray, 0, newStrArray, 0, oldStrArray.length);
		// System.arraycopy('복사할 배열', '시작위치', '복사될 배열', '복사할 개수')
	}
}
```



# 3. 향상된 for문

향상된 for문은 반복 실행을 하기 위한 카운터 변수와 증감식을 사용하지 않고 반복한다.

## 기본 for문으로 작성

```java
public class BasicFor {
	public static void main(String[] args) {
		String[] StrArray = {"최", "인","규"};
				
		for(int i=0; i<StrArray.length;i++) {	// for ('초기변수';'조건';'증감') {
			System.out.print(StrArray[i]+", ");	// 실행 명령;
		}										// }
    }
}    
```

## 향상된 for문으로 작성

```java
public class ImprovedFor {
    	public static void main(String[] args) {
		String[] StrArray = {"최", "인","규"};
		
		for(String s:StrArray) {		// for ('데이터 타입' '변수 이름':'배열이름') {
	   		System.out.print(s+",");	// 실행 명령;
		}								// }
	}
}
```