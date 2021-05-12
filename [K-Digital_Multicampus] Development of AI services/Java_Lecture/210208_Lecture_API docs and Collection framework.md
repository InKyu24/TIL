# API documents

자바에서 제공하는 API(Application Programming Interface)는 라이브러리라고 불리기도 하는데, 프로그램 개발에 자주 사용되는 클래스 및 인터페이스를 모음이라고 보면 된다. API documents는 쉽게 API를 찾아 이용할 수 있도록 문서화한 것을 말한다. 오라클에서 제공한 페이지에 [방문](http://docs.oracle.com/javase/8/docs/api)하면 볼 수 있다.



API를 통해 Object 클래스를 확인하면, toString 메소드와 equals 메소드를 볼 수 있다. 이는 주소값을 리턴해주는 기능과 주소값을 비교하는 기능을 할 수 있게 만들어주는 메소드이다. 하지만 String 클래스에서의 toString 메소드와 equals 메소드는 새롭게 재정의(override)되어 내용값을 리턴하고 내용값을 비교하는 기능을 하고 있다는 것을 알 수 있다.



## 저장된 String 문자열의 변경

```java
public class Test {
	public static void main(String[] args) {
		String s1 = new String("java");
		String s2 = "java";
		 
		s1.concat("1"); 
		s2.concat("1"); 
 
		System.out.println(s1);
		System.out.println(s2);
        
// 이어붙이기 메소드 concat을 사용하더라도, "java"가 출력된다.
// 왜냐하면 String은 문자열의 배열이기에 resize가 불가하다. [원본 변경 불가 (immutable)]

// 현재 concat 메소드로 생성된 "java1"은 새로운 주소값으로 저장되고 있다.
// 따라서 새로운 주소값을 지정해주어야 한다.
        
		s1 = s1.concat("1"); 
		s2 = s2.concat("1"); 
		
		System.out.println(s1);
		System.out.println(s2);
	}
}
```

concat 메소드는 String 문자열의 변경이 있을 때마다 계속해서 String이 생성된다. String의 누적된 생성으로 인해 메모리 효율성의 저해를 야기시킨다. 이런 사정으로 인해 `StringBuffer`와 `StringBuilder`가 생겨났다. 

이 둘은 java.lang 패키지의 클래스로서 내부 버퍼에 문자열을 저장해두고, 그 안에서 추가, 수정, 삭제 작업을 할 수 있도록 설계되어 있다. 다만 `StringBuffer`의 경우에는 멀티 스레드 환경에서 사용할 수 있도록 동기화가 되어있고, `StringBuilder`의 경우에는 단일 스레드 환경에서만 사용할 수 있도록 설계가 되어 있다.

```java
public class Test1 {
	public static void main(String[] args) {
		StringBuffer sb1 = new StringBuffer("java");
		StringBuffer sb2 = sb1.append("1"); // 추가하다.
		
		System.out.println(sb1);
		System.out.println(sb2);
		System.out.println(sb1==sb2);
	}
}
```

concat 메소드와 달리, 만약 문자열의 변경이 많다면 `StringBuffer`를 이용하고, 문자열이 변경이 적거나, 고정되어 있다면 `String`을 이용하는 것이 좋다. `StringBuffer`와 대동소이한`StringBuilder`가 있다.  `StringBuilder`는 thread, unsafe

```java
public class Test1 {
	public static void main(String[] args) {		
		StringBuilder sb1 = new StringBuilder("java");
		StringBuilder sb2 = sb1.append("1"); // 추가하다.
		
		System.out.println(sb1);
		System.out.println(sb2);
		System.out.println(sb1==sb2);
    }
}
```

+ StringBuffer : Thread Safe(멀티 Thread) - 문자열 변경이 잦은 경우
+ StringBuilder : Thread Unsafe (단일 Thread) - 문자열 변경이 적거나 고정되어 있는 경우





# Collection Framework

배열은 쉽게 생성하고 사용할 수 있지만 단점이 있다. 저장할 수 있는 객체 수가 처음에 결정되기 때문에 배열의 길이를 확정짓지 못하는 경우가 생길 수 있다는 점과 객체를 삭제했을 때 배열의 해당 인덱스가 비게 되어, 비어있는 부분을 일일이 확인해야 한다는 점이다.

자바는 배열의 이러한 문제점을 해결하고자 java.util 패키지에 Collection과 관련된 인터페이스과 클래스들을 포함시켜 놓았다. 이들을 총칭해서 Collection Framework라고 부른다.

자바 컬렉션을 객체를 수집해서 저장하는 역할을 하며, 프레임워크란 사용 방법을 미리 정해 놓은 라이브러리를 의미한다. 컬렉션 프레임워크의 주요 인터페이스로는 List, Set, Map이 있다.

![img](https://lh3.googleusercontent.com/-QsBEP6B4jBQ/YCCzf2FKR2I/AAAAAAAAGWM/0GKE_uSFa8APbNbjYzrpm0_VfPPLYJvjQCLcBGAsYHQ/w640-h414/image.png)



## List 컬렉션

List 컬렉션은 객체를 일렬로 늘어놓은 구조를 가지고 있다. 객체를 인덱스로 관리하기 때문에 객체를 저장하면 자동으로 인덱스가 부여되고 인덱스로 객체를 검색하고 삭제할 수 있는 기능을 제공한다. List 컬렉션은 객체를 자체를 저장하는 것이 아니라 객체의 번지를 참조한다. 동일한 객체를 중복 저장할 수 있는데, 이 경우에는 동일한 번지가 참조된다. null 값도 저장이 가능한데, 이 경우에는 해당 인덱스는 객체 참조를 하지 않는다.

### ArrayList

ArrayList는 List 인터페이스의 구현 클래스로, ArrayList에 추가된 객체는 인덱스로 관리된다. 이러한 점은 일반 배열과 유사하지만 ArrayList는 저장 용량을 초과한 객체들이 들어오면 자동적으로 저장 용량을 늘릴 수 있다는 것이다.

```java
import java.util.ArrayList; // ArrayList 가져오기
public class ListTest {
	public static void main(String[] args) {
		ArrayList list = new ArrayList(); // ArrayList 컬렉션 생성
		list.add("첫번째");		// 컬렉션에 String 객체 추가
		list.add("두번째");
		list.add("첫번째");		// 중복 가능
		list.add(new ListTest()); // 컬렉션에 class 객체 추가
		System.out.println(list);	// ArrayList 출력 [첫번째 두번째 첫번째 @106d69c]
		System.out.println(list.size()); // list 내 원소 개수 출력 [4]
		System.out.println(list.get(0)); // 첫번째 원소 출력 [첫번째]
	}
}
```

타입 파라미터를 이용하여, 저장할 객체의 타입을 지정하여 불필요한 타입 변환을 하지 않도록 할 수도 있다. 타입 파라미터를 이용하면 향상된 for문까지 사용 가능해진다.

```java
import java.util.ArrayList; // ArrayList 가져오기
public class ListTest {
	public static void main(String[] args) {
		ArrayList<String> list = new ArrayList<String>(); // String만 객체로 들어오도록.
		list.add("첫번째");
		list.add("두번째");
		list.add("첫번째");
//		list.add(new ListTest()); 	String이 아닌 객체 추가 불가
        		
		for(String s:list) {			// 향상된 for문을 사용할 수 있어짐
			System.out.println(s);		
		}
	}
}
```



## Set 컬렉션

List 컬렉션을 저장 순서를 유지하지만, Set 컬렉션은 저장 순서가 유지되지 않는다. 또한 객체를 중복해서 저장할 수 없고, 하나의 null만 저장할 수 있다. Set은 인덱스로 관리하지 않기 때문에 인덱스를 매개값으로 갖는 메소드는 없다.



### HashSet

```java
import java.util.HashSet;
import java.util.Iterator;

public class SetTest {
	public static void main(String[] args) {
		HashSet<String> set = new HashSet<String>();
		set.add("a");
		set.add("b");
		set.add("c");
		set.add("a");
		set.add("b");
		set.remove("c");
	//	set.add(new SetTest()); String이 아닌 객체 추가 불가 [타입 파라미터로 지정했기 때문.]
		
		System.out.println(set.size()); // 중복된 개체 제외 [3 출력]
        
        Iterator<String> ite=set.iterator(); 
        // 전체 객체 대상을 한번씩 반복해서 가져오는 반복자 리턴 (next 메소드 사용으로 하나의 객체를 가져온다.)
        
		while(ite.hasNext()) { // hasNext() 가져올 객체가 있으면 true, 없으면 false
			Object o=ite.next();
			System.out.println(o);
		} 
	}
}
```



## Map 컬렉션

Map 컬렉션은 Key와 Value로 구성된 객체를 저장하는 구조를 가지고 있다. 여기서 Key와 Value 모두 객체이며, Key는 중복 저장될 수 없지만 Value는 중복 저장될 수 있다. 만약 기존의 Key와 동일한 Key로 Value를 저장하면 기존의 Value는 없어지고 새로운 값으로 대치된다.

### HashTable

```java
import java.util.Enumeration;
import java.util.Hashtable;

public class MapTest {
	public static void main(String[] args) {
		Hashtable map = new Hashtable();
		map.put("a", "1");
		map.put("b", "2");
		map.put("c", "1");
		map.put("d", new MapTest());
		map.put("a", "2");		// Key의 중복으로 value값이 2로 대체
	
		System.out.println(map); // {b=2, a=2, d=test.Map.MapTest@106d69c, c=1} 출력
		System.out.println(map.size()); //  4 출력
		Object o1=map.get("a");	// a Key의 value를 Object o1에 저장
		Object o2=map.get("b"); // b Key의 value를 Object o2에 저장
		System.out.println(o1==o2); // true 출력
		
		Enumeration enu = map.keys(); // 열거형 인터페이스 enu=["a", "b", "c", "d"] 
		while(enu.hasMoreElements()) {	// enu에서 하나의 Key를 꺼낸 뒤,
			Object o = enu.nextElement(); // 해당 Key를 Object o에 저장
			System.out.println(o+": "+map.get(o)); // map.get(o) Key에 해당하는 Value를 가져온다.
// Enumeration 인터페이스를 통해 가져온 key의 개수가 3개면 hasMoreElements 메소드도 3번 사용 가능하다.
		}
	}
}
```



