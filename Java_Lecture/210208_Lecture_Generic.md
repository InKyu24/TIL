# Generic

Java 5부터 성능 개선을 위해 제네릭 타입이 새로 추가가 되었다. 제네릭은 타입 매개변수(타입 파라미터)를 가지는 클래스와 인터페이스를 말한다. 제네릭을 이용함으로써 잘못된 타입이 사용될 수 있는 문제를 컴파일 과정에서 제거할 수 있게 되었다. 컴파일 시 강한 타입 체크를 가능하게 하기 때문이다. 또한 불필요한 타입 변환도 줄일 수 있다.

제네릭의 특징은 강제적으로 형변환을 할 필요가 없다는 것이고, 따라서 컴파일 시에 타입이 제한된다는 것이다. 그래서 `ClassCastException`이 나타나지 않는다.



```java
public class 클래스명<T> {
}

public interface 인터페이스명<T> {
}

// 제네릭 타입은 클래스나 인터페이스 뒤에 <>이 붙고, 사이에 타입 파라미터가 위치한다. 타입 파라미터는 일반적으로 대문자 알파벳 한 글자로 표현된다.

List<String> list=new ArrayList<String>();
// 타입 파라미터를 명시적으로 String으로 지정
List<Integer> list=new ArrayList<Integer>();
// 타입 파라미터를 명시적으로 Integer로 지정

List<String> list=new ArrayList();
// 타입 파라미터를 String으로 추정
List<Integer> list=new ArrayList();
// 타입 파라미터를 Integer로 추정
```



```java
import java.util.*;

public class test {
	public static void main(String[] args) {
        // ArrayList를 가져와, List 형태로 쓰겠다. [String 타입만 객체로 받는다.]
     	// 즉, ArrayList만이 가진 특성들은 Shadow effect 하겠다.
		List<String> list=new ArrayList<String>(); 

		list.add("Hi");
		
		String []array=new String[10]; // 10칸의 String 배열 첫번째에 "Hi" 저장
		array[0] ="Hi";
				
		int [] all = new int[10];	// 10칸이 정수 배열 첫번째에 1 저장
		all[0] = 1;       
	}
}
```

```java
import java.util.*;

public class test {
	public static void main(String[] args) {
        // ArrayList를 가져와, List 형태로 쓰겠다. [Int 타입만 객체로 받는다.]    
		List<Integer> list=new ArrayList<Integer>();
		Integer o1 = new Integer(1);	// 정수 1을 o1 객체에 저장
		Integer o2 = new Integer(2);	// 정수 2을 o2 객체에 저장
		list.add(o1); // list에 o1 객체 추가 (정수 1) 
		list.add(o2); // list에 o2 객체 추가 (정수 2)

        list.add(1); // list에 정수 1 추가
//        java1.5 이후부터 auto-boxing 을 통해 가능해짐
//		 현재 list = [1, 2, 1]

		int i = list.get(2); 
//			int i에 list의 두번째 값 저장
// 		  java1.5 이후부터 unboxing 을 통해 가능해짐        
	}
}
```



## 와일드카드 타입 <?>, <? extends ..>, <? super ...>

코드에서 ?를 일반적으로 와일드카드(Wildcard)라고 부른다. 제네릭 타입을 매개값이나 리턴 타입으로 사용할 때 구체적인 타입 대신에 와일드카드를 다음과 같이 세 가지 형태로 사용할 수 있다.

+ `제네릭타입 <?>` : 제한 없음 [모든 클래스나 인터페이스 타입이 올 수 있다]
+ `제네릭타입 <? extends 상위타입>` : 상위 클래스 제한
+ `제네릭타입 <? super 하위타입>` : 하위 클래스 제한



```java
import java.util.*;

class LandAnimal {
	public void crying() {
    	System.out.println("육지동물");
    }
}
	
class Cat extends LandAnimal {
    public void crying() {
        System.out.println("냐옹냐옹");
    }
}

class Dog extends LandAnimal {
    public void crying() {
        System.out.println("멍멍"); 
    }
}

class Sparrow {
    public void crying() {
        System.out.println("짹짹");
    }
}

class AnimalList<T> {
    ArrayList<T> al = new ArrayList<T>();
    public static void cryingAnimalList(AnimalList<? extends LandAnimal> al) {
        LandAnimal la = al.get(0);
        la.crying();
    }
    void add(T animal) {
        al.add(animal);
    }
    T get(int index) { 
        return al.get(index);
    }
    boolean remove(T animal) {
        return al.remove(animal);
    }
    int size() {
        return al.size(); 
    }
} 
```







