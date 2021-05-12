1. 다음 코드의 실행 결과 total값은? 

   ```java
   int total=0, x=0,y;
   while(x++<5){
       y=x*x;
       System.out.println(y);
       total +=y;
   }
   System.out.println("총합은 "+total);
   ```

   ​	1) `0` 	2) `5` 	3) `30`	4) `55`

   

2. 다음 접근 제한자를 제한이 낮은 순에서 높은 순으로 정렬한 것은?

   ```java
   a. (default)     b. private     c. protected     d. public
   ```

   ​	1) `dcab`	2) `dacb`	3) `bacd`	4) `bcda`

   

3. Radio, Speaker, Earphone클래스와 Playable, Portable 인터페이스가 있다. 다음 중 잘못된 것은?

   ```java
   1) public class Radio extends Speaker implements Playable
   2) public class Radio extends Speaker implements Playable, Portable
   3) public class Radio extends Speaker, Earphone
   4) public class Speaker implements Playable, Portable
   ```



4. 다음  코드의 설명으로 옳은 것은? 

   ```java
   public class Test{
       public static void  main(){
           System.out.println("test");         
       }
   }
   ```

   ​	1) 컴파일 에러가 발생한다.
   ​	2) 컴파일 OK, 실행하면 test가 출력된다.
   ​	3) 컴파일 OK, 실행시 에러가 발생한다.
   ​	4) 컴파일 OK, 실행하면 아무것도 출력되지 않는다.  



5. 다음  중에서 생성자(Constructor)가 가질 수 없는 접근자(modifier)를 고르시오. 

   ​	1) `private`	2) `public`	3) `static`	4) `protected`



6. 다음  소스에 대한 설명중 옳은 것은?

   ```java
   public class Test{
       public static void  main(String args[]){             
           TestA a = new  TestA();
           a.i = 200;  
           a.go();  
       }
   }
   
   class TestA{
       public int i = 100;          
       public TestA( int i ){ 
           this.i = i;   
       }   
       public void go(){  
           System.out.println("i = " + i);         
       }   
   }     
   ```

   ​	1) 정상적으로  컴파일되지만, 실행시 Exception이 발생한다.

   ​	2) 정상적으로  컴파일되고, 실행결과는 i = 100 이라고 출력된다.

   ​	3) 정상적으로  컴파일되고, 실행결과는 i = 200 이라고 출력된다.

   ​	4) 컴파일시 오류가  발생한다. 

   

7. 다음  중에서 변수, 클래스, 메소드등의 이름(Identifier)으로서 가능하지 않은 것은?

   ​	1) `3num`	2) `c35`	3) `_class`	4) `$AB`

   

8. 다음과  같이 길이가 0 인 배열을 선언 했을 때 옳은 설명을 고르시오.

   ```java
   public class TestM{
       public static void  main(String args[]){ 
           int x[] = new  int[0];        //(1)
           String y[] =  new String[0];  //(2)   
       } 
   }        
   ```

   ​	1) 어떠한  타입이라도 길이가 0 인 배열을 선언할 수 있으므로 컴파일/실행시에 문제가 없다.

   ​	2) 기본형인  경우에만 길이가 0 인 배열을 선언할 수 있으므로 (2)에서 컴파일 에러가 난다.

   ​	3) 참조형인  경우에만 길이가 0 인 배열을 선언할 수 있으므로 (1)에서 컴파일 에러가 난다.

   ​	4) 길이가 0 인  배열을 선언할 수 없다. 

   

9. 다음을  컴파일하고 실행할 경우 옳은 결과를 고르시오.

   ```java
   public class TestQ{
       public static void  main(String args[]){  
           char[] y = {h, e, l,  l, o};       
           for(int i=0; i <  y.length ; i++){       
               System.out.print(y[i]);      
           }       
       }     
   }  
   ```

   ​    1) 컴파일 후 실행하면 hello 가 출력된다. 

   ​	2) 컴파일 후 실행하면 helo 가 출력된다.  

   ​	3) 컴파일 후 실행하면 Exception이 일어난다.  

   ​	4) 컴파일 에러가 난다. 



10. 다음  코드가 컴파일 되기 위해서 삭제해야 되는 method를 고르시오.

    ```java
    public class Test{   
        public String getDetails(){  
            return "String"
        }        
        public void getDetails(char  c){
        }       
        public void getDetails(){			// 1) 
        }							    
        void getDetails(String  s){			// 2)  
        }							    
        public void getDetails(int  i){		// 3) 
        } 
        void getDetails(double  d){			// 4) 
        }							       
    }
    ```

    ​                    

11. 다음과 같은 클래스가 있다. 정상적으로 컴파일 되는 코드는?

    ```java
    class Person{
    }       
    
    class Student extends Person{
    }  
    
    class Teacher extends Person{
    }         
    
    class Staff extends Person{
    }    
    ```

    ​	1) Staff st  = (Staff)new Student(); 

    ​	2) Student  s = (Student)new Person(); 

    ​	3) Teacher t = (Teacher)new Student(); 

    ​	4) Staff f  = (Staff)new Teacher(); 

    ​                 

12. **제네릭을 설명한 내용 중 틀린 것은?**

    ​	1) 제네릭 타입은  타입 매개변수를 가지는 클래스와 인터페이스를 의미한다

    ​	2) 컴파일 할 때  타입을 결정하므로 안전하다

    ​	3) 강제 타입 변환을  제거한다.

    ​	4) 제네릭 메서드는  동적 다형성을 이용하는 메서드이다.

    

13. **다음 설명 중 틀린 것은?**

    ​	1) 자바  애플리케이션은 최소한 하나의 쓰레드를 가진다.

    ​	2) Thread  클래스는 run() 메서드를 가진다.

    ​	3) 쓰레드는  Thread의 자식 클래스로서만 만들 수 있다

    ​	4) 쓰레드를  실행하려면 쓰레드 객체의 start() 메서드를 호출해야 한다.

    ​	

14. **다음은 Company 클래스를 Singleton으로 만드는 간단한 예이다. 밑줄에 들어갈 단어를 순서대로 나열한것을 고르시오.**              

    ```java
    public class Company{
        private _____ Company  instance = new Company();   
        public _____ Company  getCompany(){    
            return instance;       
        }           
        ______  Company(){     
        }        
    }          
    ```

    ​	1) static,  static, public 

    ​	2) static,  final, private 	

    ​	3) final,  static, public 

    ​	4) static,  static, private 

    ​	

15. DataInputStream과 DataOutputStream을 사용해서 클라이언트와 서버 사이의 데이터를 주고 받을 수 있는 메소드가 아닌  것은 어느것인지 고르시오.

    ​	1) readUTF(), writeUTF() 

    ​	2) readString(),  wirteString() 

    ​	3) readLong(), writeLong() 

    ​	4) readBoolean(), writeBoolean() 



16. **다음  아래의 코드를 보고 틀리게 설명한 것을 고르시오.**  

    ```java
    public class MyStack {     
        //...            
        public void push(char c)  {           
            synchronized(this)  {            
                data[idx]=c;      
                idx++;           
            }         
        }       
        //...     
    }  
    ```

    ​	1) 모든 객체는  "lock flag"라고 생각할 수 있는 flag를 가지고 있다. 

    ​	2) synchronized라는 키워드는 flag를 가지고 Thread객체간  상호작용을 할 수 있게 해준다. 

    ​	3) 이 프로그램의  Thread객체간 공유데이터는 MyStack객체이다. 

    ​	4) synchronized라는  키워드는 Thread객체가 공유데이터에 동시에 접근할 수 있게 해준다. 

    ​	

17. 다음  코드를 수행할때의 결과는?     

    ```java
    public class Test{  
        public static void  main(String [] args){   
            int out = 10;              
      		class Inner{              
                public int  count(){        
                    int  cnt = 0;          
                    for (  int i = 0 ; i < out ; i++){ 
                        cnt += i;                   
                    }                   
                    return cnt;          
                }          
            }              
            Inner in = new  Inner();   
            System.out.println(  in.count() );  
        }     
    }       
    ```

    ​	1) 컴파일 오류가  발생한다. 

    ​	2) 45가 출력된다. 

    ​	3) 55가  출력된다. 

    ​	4) 10이  출력된다. 



18. **다음  코드를 람다식으로 바꾼 것으로 옳은 것은?**    

    ```java
    new Thread(new Runnable() {
        @Override  
        public void run() {  
            System.out.println("Welcome  Heejin blog");    
        }   
    }).start();
    ```

    ```java
    1) new Thread(->{
          System.out.println("Welcome Heejin blog");
    	}).start();
    
    2) new Thread(()->{
          System.out.println("Welcome Heejin blog");
    	}).start();
    
    3) new (()->{
          System.out.println("Welcome Heejin blog");
    	}).start();
    
    4) new Runnable(()->{
          System.out.println("Welcome Heejin blog");
    	}).start();
    ```

    

19. **다음  코드에서 (1)에 들어갈 옳은 구문은?**    

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
        public static void  cryingAnimalList(AnimalList< /*(1)*/  > al) { 
            LandAnimal la =  al.get(0);  
            la.crying();    
        }     
        void add(T animal) {
            al.add(animal); 
        }    
        T get(int index) {
            return  al.get(index); 
        }     
        boolean remove(T animal) { 
            return  al.remove(animal); 
        }      
        int size() { return al.size(); 
                   }
    }
    
    ```

    ```java
    1) ? super LandAnimal
    2) ? implements LandAnimal
    3) ? super T
    4) ? extends LandAnimal
    ```

    

20. **다음  코드를 컴파일 한 후의 타입 변환이 가장 올바른 것은?**  

    ```java
    public static void main(String... args) { 
        List<String> list = new  ArrayList<>(); 
        list.add("Hi");           
        Object[] array = new  Long[10];     
        array[0] = 1L;   
    }
    ```

     ```java
    1)	public static void main(String... var0) {
      		ArrayList var1 = new ArrayList();
     	 	var1.add("Hi");
     		Long[] var2 = new Long[10];
      		var2[0] = Long.valueOf(1L);
    	}
    
    2)	public static void main(String... var0) {
    	 	List var1 = new ArrayList();
     	 	var1.add("Hi");
     	 	Long[] var2 = new Long[10];
     	 	var2[0] = Long.valueOf(1L);
    	}
    
    3)	public static void main(String... var0) {
      		ArrayList var1 = new ArrayList();
      		var1.add("Hi");
    		Object[] var2 = new Long[10];
     		var2[0] = Long.valueOf(1L);
    	}
    
    4)	public static void main(String... var0) {
    	  	List var1 = new ArrayList();
    	 	 var1.add("Hi");
         	 Object[] var2 = new Long[10];
         	 var2[0] = Long.valueOf(1L);
    	}
     ```

    

21. 클래스의  구성요소와 가장 거리가 먼 것은?

    ​	1) `필드`	2) `지역변수`	3) `메서드`	4) `생성자`

    

22. 다음  중에서 static에 대한 설명으로 틀린 것을 고르시오. 

    ​	1) static은  변수, 메소드, 내부클래스 등의 지정자(modifier)로 사용된다. 

    ​	2) static으로  선언된 것은 객체를 생성하여 클래스를 통해 참조할 수 있다. 

    ​	3) static  변수는 선언할 때 또는 정적 초기화블록에서 초기화 해주어야 한다. 

    ​	4) static으로  선언된 멤버는 클래스 멤버라고도 한다. 

    

23. **다음  코드를 보고 밑줄에 알맞는 코드를 고르시오.** 

    ```java
    //...       
    ServerSocket s = null;     
    s = new ServerSocket(5432);  
    while (true) {   
        try {     
            Socket s1 =  s.accept();   
            OutputStream s1out =  ____________________ ;    
            DataOutputStream dos  = new DataOutputStream(s1out);  
    //...    
    ```

    ```java
    1) new  OutputStream() 
    2) new Stream(s1); 
    3) s1.getOutputStream() 
    4) s1.getStream() 
    ```

    ​     

24. 다음 중 Exception에 해당하지 않는 것은?

    ​	1) null값이 할당된  클래스 변수의 메소드 호출을 하였을 때

    ​	2) 0으로 나누었을  때 

    ​	3) JVM  에러  

    ​	4) 배열의 크기를  벗어난 사용 

    

25. 다음 코드의 (1) 부분에 올 수 있는 가장 적당한 것은?        

    ```java
    	/*(1)*/
    public interface Math {   
        public int Calc(int first, int second);  
    }
    ```

    ​	1) @FunctionalInterface

    ​	2) @StaticInterface

    ​	3) @DefaultInterface

    ​	4) @FunctionalClass