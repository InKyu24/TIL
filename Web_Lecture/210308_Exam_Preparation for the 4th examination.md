1. 다음 중 CGI  Scripts 의 장점이 아닌 것은?

   1) CGI  Scripts는 웹 서버에 의해 제공되는 어떠한 프로그래밍 또는 스크립팅 언어로 작성될 수 있다. 

   2) CGI  Scripts는 웹서버의 기능을 확장한다. 

   3) CGI  Scripts는 서버에 있는 프로그램 코드를 수행 한다. 

   ***<u>4) CGI  Scripts는 동시 사용자가 많을 때 성능에 유리하다.</u>*** 
   
   > CGI  Script 장점은 심플한 규격으로 확장이 용이한 것이고, 단점은 요청이 올 때 마다 신규 process를 생성하기 때문에 부하가 심할 수  있다는 것이다.



2. 웹 컨테이너에  대한 설명으로 틀린 것은?

   ***<u>1) 웹컨테이너는 반드시 웹서버와 독립적으로 존재해야 한다.</u>***

   2) 웹컨테이너는 static page에 대한 요청도 처리할 수 있다. 

   3) 웹컨테이너는 HTTP request, HTTP response에 해당되는 객체를 생성한다. 

   4) 웹컨테이너는 요청URL에 대응되는 Servlet객체의 service 메서드를 호출함으로써 Servlet을 활성화시킨다.
   
   > 반드시  독립적이여야 한다?



3. 웹  컨테이너가 사용자의 요청에 응답하는 순서를 바르게 나열한 것은? 

   ```JAVA
   1. 웹컨테이너는 HttpServletRequest객체를 생성한다.
   2. 웹컨테이너는 HttpServletResponse객체를 생성한다.
   3. HTTP service는 요청 데이터를 웹컨테이너에게 전송한다.
   4. 웹컨테이너는 요청된 Servlet의 service메소드를 실행한다.
   5. 웹컨테이너는 Servlet에 의해 생성된 응답 데이터를 HTTP service에게 보낸다.
   6. 클라이언트가 HTTP request를 HTTP service에게 보낸다.
   7. HTTP Service는 HTTP response를 클라이언트에게 보낸다.
   ```

   1)  6-3-1-4-2-5-7 

   2)  6-3-4-1-2-5-7

   ***<u>3)  6-3-1-2-4-5-7</u>***

   4)  6-3-2-4-1-5-7 



4. 다음 코드를  브라우저의 주소창에서 http://localhost:8080/servlet/Test1으로 실행했을 때의 결과는?

   ```java
   import java.io.*;
   import javax.servlet.*;
   import javax.servlet.http.*;
   
   public class Test1 extends HttpServlet{
       public void  doPost(HttpServletRequest req,HttpServletResponse res) throws  ServletException,IOException{
           res.setContentType("text/html");
           PrintWriter out=res.getWriter();
           out.println("Hello");    
           out.close();    
       } 
   }
   ```

   1) Hello

   2) text/html

   3) 아무 것도 출력되지 않는다.

   ***<u>4) 실행 시 에러가 난다</u>***.
   
   > 직접 해봄  (init method 없어서?)



5. web container에 저장되어 있는 개별 servlet을 최초로 실행되는 메소드부터 web container가 shutdown시에 실행되는 메소드를 차례대로 나열한 것은?

   1) service  -> start -> init 

   ***<u>2) init  -> service -> destroy</u>***

   3) start  -> init -> destroy

   4) init -> start -> service
   
   > init  -> service -> destroy



6. 다음 중  HTTP 1.1프로토콜에 의해 제공되는 GET 메서드에 대한 설명으로 옳은 것은?

   ***<u>1) 전송할 데이터를  헤더의 URL의 뒤에 붙여서 전송한다.</u>***

   2) 전송할 데이터를 바디부분에 스트림의 형태로 전송한다.

   3) URL과  전송메시지의 구분자는 & 이다.

   4) 전송 메시지에서 각 데이터를 분리해주는 구분자는 ? 이다.
   
   > 전송할 데이터를  헤더의 URL의 뒤에 붙여서 전송한다.
   >
   > 2번은 POST 메서드
   >
   > 3번과 4번 구분자 바뀜



7. 다음 코드를  브라우저의 주소창에서 http://localhost:8080/servlet/Test1으로 실행했을 때의 결과는?

   ```JAVA
   import java.io.*;    
   import javax.servlet.*;   
   import javax.servlet.http.*;   
   
   public class Test1 extends HttpServlet{     
       public void  doGet(HttpServletRequest req,HttpServletResponse res) throws  ServletException,IOException{     
           res.setContentType("text/html");   
           PrintWriter  out=res.getWriter();    
           String  name=req.getParameter("name");
           out.println("name="+name.trim()  );  
           out.close();  
       }   
   }
   ```

   1) "name=null"이  출력된다. 

   2) "name="이  출력된다. 

   3) 아무 것도  출력되지 않는다. 

   ***<u>4) 실행 시 NullPointerException이 발생한다.</u>*** 
   
   > 직접 해봄  (NullPointerException)



8. SayHello라는  웹컨텍스트의 web.xml에서 다음 부분을 보고 맞게 설명한 것은? 

   ```xml
   <servlet-mapping>
       <servlet-name>Hello</servlet-name>      
       <url-pattern>/greeting</url-pattern>   
   </servlet-mapping>     
   ```

   1) `http://localhost:8080/greeting`으로 호출할 수 있다.

   ***<u>2) `http://localhost:8080/SayHello/greeting`으로 호출할 수 있다.</u>***

   3) `http://localhost:8080/Hello/greeting`으로 호출할 수 있다.

   4) `http://localhost:8080/servlet/greeting`으로 호출할 수 있다.
   
   > `http://IP주소:포트번호/프로젝트이름(컨텍스트이름)/서블릿매핑이름`



9. servlet  파일을 접근하려고 할 때 다음처럼 web browser에서 request를 한다면 무슨 문제점이 있는가?          

   ```html
http://localhost:8080/SayHello/servlet/web.controller.FormProcessingServlet
   ```

   1) 경로가 복잡하기 때문에 속도의 저하를 가져온다.

   2) 많은 양의 data를 전송할수 없다.
   
   ***<u>3) web container의 경로명이 노출되기 때문에 보안에 문제가 생긴다.</u>***
   
   4) servlet에 대한 접근을 web browser에서만 해야한다.
   
   > 클래스  이름이 길어지면 입력하기 불편해진다. 그리고 일반적으로 클래스 이름을 보면 그 클래스가 어떤 기능을 하는지 짐작할 수 있는데, 브라우저에서  버젓이 클래스 이름으로 입력하는 것은 보안에도 좋지 않다. 따라서 서블릿 클래스 이름에 대응되는 서블릿 매핑 이름으로 실제 서블릿을  요청한다.



10. 다음 중 틀린 설명은?

    1) 웹컨테이너에 의해 Web Application당 한 개의 ServletContext객체가 생성된다.

    2) 웹컨테이너에 의해 HTTP request에 대응되는 HttpServletRequest 객체가 생성된다.

    3) 웹컨테이너에 의해 HTTP response에 대응되는 HttpServletResponse 객체가 생성된다.

    ***<u>4) 웹컨테이너에 의해 Web Application당 한 개의 서비스 Thread가 생성된다.</u>***

    > 요청에 의해  계속 Thread 생성



11. MVC pattern에 대한 설명으로 틀린 것은?

    ***<u>1) HTTP request로부터 들어온 데이터를 Business Service를 이용하여 검수한다.</u>***

    2) Controller가 Model에 있는 데이터를 갱신시켜 준다.

    3) View는 HTML 문서를 만들어내기 위해 Model로부터 데이터를 가져간다.

    4) Controller는 Model의 상태를 변경할 수 있다.

    > MVC란 Model View Controller의 약자로 웹 애플리케이션을 화면 부분, 요청 처리 부분, 로직 처리 부분으로 나누어 개발하는 방법이다.
    >
    > + Model은 데이터베이스 연동과 같은 비즈니스 로직을 수행. [DAO 클래스와 VO 클래스]
    >   Model은 자신의 상태 변화에 대해서 View, Controller에게 알려주긴 하지만, View와 Controller에 대한 의존성이 없다.
    >
    > + View는 사용자에게 보여줄 화면을 담당. Model에서 처리한 결과를 화면에 표시.[JSP]
    >   화면에 표시하기 위해 필요한 상태 및 데이터를 Model에서 직접 가져온다.
    >
    > + Controller에서는 사용자의 요청 및 흐름 제어를 담당. 클라이언트 요청 분석, 요청에 대해 필요한 Modle 호출, Model에서 처리한 결과를 보여주기 위한 JSP 선택 [서블릿]
    >   Model로 요청을 전달하는 역할만 하는것이 아니라, 사용자의 요청을 해석하여 Model을 조작하는 역할을 맡고있다.

    

12. 다음은 MVC pattern 중에서 View에 대한 설명이다. 틀린 것은?

    1) View는 HTML response를 만든다.

    ***<u>2) Model의 상태를 변경시킬 수 있다.</u>***

    3) Application의 “window” 역할을 한다.

    4) Model로부터 변경된 자료를 가져올 수 있다.

    > 상태가 변경되면 Model은 View에게 변경 사실을 알린다.
    >
    > 사용자의 요청 때문이든 다른 내부적인 변화 때문이든, Model에서 무언가가 변경되면 View에게 상태가 변경되었음을 알린다.

    

13. MVC 패턴을  사용하는 이유로 적절하지 않은 것은?

    ***<u>1) 응용프로그램의  응답속도가 빨라진다.</u>***

    2) 응용프로그램의  유지보수가 쉬워진다.

    3) 응용프로그램의  확장성이 좋아진다.

    4) 응용프로그램의  이식성이 좋아진다.

    > + MVC의 장점
    >   + 개발 및 유지보수가 편리
    >   + 높은 재사용성
    >   + 분업화
    >
    > + MVC의 단점
    >   + 기본기능 설계를 위해 클래스들이 많이 필요하기 때문에 복잡할 수 있다.
    >   + 설계시간이 오래 걸리고 숙련된 개발자가 필요하다.
    >   + Model과 View의 완벽한 분리가 어렵다.

    

14. 다음 중 Session에 대한 설명으로 틀린 것은?

    1) 서버에 사용자의 정보를 유지 관리한다.

    2) 사용자 인증 후 여러 페이지에 걸쳐 정보를 공유하여 사용 할 수 있게 해준다.

    ***<u>3) 사용자가 정해준 옵션에 의해서 사용가능 여부가 결정된다.</u>***

    4) 객체형을 포함한 어떠한 형태의 데이터도 저장 가능 하다.

    > 세션 : 웹 사이트의 여러 페이지에 걸쳐 사용되는 사용자 정보를 저장하는 방법
    >
    > + 일정 시간동안 같은 사용자(브라우저)로부터 들어오는 일련의 요구를 하나의 상태로 보고, 그 상태를 일정하게 유지시키는 기술로 웹 서버에 웹 컨테이너의 상태를 유지하기 위한 정보를 저장한다.
    >
    > + 브라우저를 닫거나, 서버에서 세션을 삭제했을때만 삭제가 되므로, 쿠키보다 비교적 보안이 좋다.
    >
    > + 저장 데이터에 제한이 없다.(서버 용량이 허용하는 한...)
    >
    > + 각 클라이언트 고유 Session ID를 부여한다.
    > + Session ID로 클라이언트를 구분하여 각 클라이언트 요구에 맞는 서비스 제공

    

15. 다음 중 옳은 설명은?

    1) Cookie는 Server에서 원할 경우 언제든지 Client에 Setting할 수 있다.

    2) Cookie에도 사용자가 만든 객체를 저장할 수 있다.

    3) Cookie를 저장할 때 Server에서 원한다면 제한 없이 저장할 수 있다.

    ***<u>4) Cookie는 사용자가 거부할 수 있다.</u>*** 

    > 쿠키
    >
    > + 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각
    >
    > + 한개에 4KB 까지 저장 가능하며, 최대 300개 까지 저장할 수 있는 텍스트 파일
    >
    > + 클라이언트에 저장
    >
    > + 이름, 값, 만료날짜, 경로 정보가 들어있다

    

16. 같은 Servlet class에 대한 요청을 처리하는 모든 thread는 같은 Servlet 객체를 공유한다. 그래서  동시성문제(Concurrency Issue)가 발생할 수 있는데, 다음 중에서 동시성 문제를 발생시키지 않는 것은?

    1) Local Variable

    2) Instance Variable

    3) Class Variable

    4) Session Attribute

    

17. 다음 중  Spring framework에 대한 올바른 주장은?

    1) Spring은 개발자가 POJO를 사용하여 엔터프라이즈급 애플리케이션을 개발할 수 있도록 한다.

    2) Spring은 모듈 방식으로 구성된다.

    3) DispatcherServlet은 모든 HTTP 요청과 응답을 처리한다.

    ***<u>4) 위의 모든 것.</u>***

    > 스프링
    >
    > + POJO 프레임워크 중 하나
    > + 자바 애플리케이션 개발을 위한 포괄적인 인트라 스트럭처를 제공하는 자바 플랫폼이다.
    >
    > DispatcherServlet
    >
    > + 유일한 서블릿 클래스로서 모든 클라이언트의 요청을 가장 먼저 처리하는 Front Controller

    

18. 다음 중  Spring framework과 관계 없는 것은?

    1) 의존성  주입(DI)

    ***<u>2) 성능향상(Performance  effect)</u>***

    3) 제어  반전(IoC)

    4) 관점지향프로그래밍(AOP)

    

19. 다음  Spring framework 설정 파일(person.xml)을 보고 유추할 수 있는 내용으로 맞지 않는 것은?

    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE beans PUBLIC "-//SPRING//DTD BEAN//EN"  "http://www.springframework.org.dtd/spring-beans-2.0.dtd"  >  
    <beans> 
        <bean id="personService"  class="com.spring.ex01.PersonServiceImpl">     
            <property  name="name"> 
                <value>홍길동</value>  
            </property> 
        </bean> 
    </beans>
    ```

    1) `BeanFactory factory=new XmlBeanFactory(new FileSystemResource("person.xml"));` 로  설정 파일을 적용할 수 있다.

    2) BeanFactory 객체의 메소드를 다음과 같이 사용하여 PersonServiceImpl객체를 주입 받을 수  있다. `getBean("personService");`

    ***<u>3) PersonServiceImpl  클래스에 setName 메소드가 없이도 name 값이 할당된다.</u>***

    4) 주입 받은  PersonServiceImpl 객체는 name 값이 홍길동으로 할당되어 있다.

    

20. 다음 중 스프링부트에 관한 설명으로 틀린 것은?

    1) 스프링 부트 애플리케이션은 내장된 톰캣을 통해 실행된다.

    2) 스프링 부트 애플리케이션은 main 메소드를 가진 클래스의 선언부에 @SpringBootApplication을 지정해야 한다.

    3) SpringBootServletInitializer는 web.xml없이 톰캣에서 실행하게 해주는 역할을 한다.

    ***<u>4) 웹  프로그램이므로 main 메소드는 필요하지 않다.</u>***

    > 해당 클래스 명이 아니더라도 @SpringBootApplication 어노테이션이 있는 클래스의 main 메소드가 실행된다. 
    >
    > web.xml이 없는 SpringBoot 웹 애플리케이션을 외부 Tomcat에서 동작하도록 하기 위해서는 WebApplicationInitializer 인터페이스를 구현한 SpringBootServletInitializer를 상속을 받는 것이 필요하다.

21. 다음 중  Servlet의 장점이 아닌 것은?

    1) 신뢰성  (Reliability) 

    ***<u>2) Java에서 제공되는 다른 기술을 같이 사용 할 수 없다.</u>*** 

    3) 확장성  (Scalability) 

    4) 플랫폼과 서버에 독립적이다. 

    > Servlet : 모든 자바 API 사용 가능

    

22. HttpServlet class의 service method에서 request 방식에 따라서 재호출되는 method가 아닌 것은?

    1) doPost()

    2) doPut()

    ***<u>3) doAdd()</u>***

    4) doDelete()

    > Servlet 객체 생성 이후 GET, POST, PUT, DELETE 메소드에 대한 메소드가 실행된다.

    

23. 기존의 HttpSession을 얻기 위한 방법으로 맞는 것은? (보기의 request는 HttpServletRequest 객체임)

    1) HttpSession  session=new HttpSession();

    ***<u>2) HttpSession  session=request.getSession(false);</u>***

    3) HttpSession  session=HttpSession.getInstance();

    4) HttpSession  session=request.getSession();

    > getSession(), getSession(true) : HttpSession이 존재하면 현재 HttpSession을 반환하고 존재하지 않으면 새로이 세션을 생성
    >
    > getSession(false) : HttpSession이 존재하면 현재 HttpSession을 반환하고 존재하지 않으면 새로이 생성하지 않고 그냥 null을 반환
    >
    > 
    >
    > [참고] getSession(), getSession(true)는 null 체크없이 바로 getAttribute()를 사용해도 무방하지만, getSession(false)는 null을 리턴할수 있기 때문에 null체크를 해야 한다.

    

24. 세션 무효화에  관한 설명 중 틀린 것은?

    ***<u>1) 한번 연결된 session은 무효화 시킬 수 없다.</u>***

    2) invalidate 메소드를 사용해서 바로 무효화 시킬 수 있다.

    3) web.xml에  session-timeout 설정을 사용해서 시간을 지정 할 수 있다.

    4) setMaxInactiveInterval()메소드를 사용해서 시간을 지정 할 수 있다.

    

25. 다음 코드를  보고 웹브라우저에서 `Hello Boot!!` 가 출력되기 위한 요청 URL로 맞는 것은?  

    ```java
    package com.myboot01;  
    import org.springframework.stereotype.Controller;   
    import org.springframework.web.bind.annotation.*;      
    
    @Controller 
    public class DemoController{    
        @ResponseBody      
        @RequestMapping("/")    
        public String home(){      
            System.out.println("Hello  Boot!!");   
            return "Hello  Boot!!";    
        }   
    }
    ```

    ***<u>1) `http://localhost:8080`</u>***

    2) `http://localhost:8080/home`

    3) `http://localhost:8080/DemoController`

    4) `http://localhost:8080/DemoController/home`
    
    > @Controller 애너테이션은 해당 클래스가 Controller임을 나타낸다.
    >
    > @RequestMapping은 url과 함께 애너테이션을 하고, 어떤 Controller 또는 어떤 Method가 request를 처리할 지를 맵핑한다.
    >
    > 메서드 내에서 viewName을 별도로 설정하지 않고 @RequestMapping을 하게 되면, path로 설정한 URL이 그대로 viewName으로 설정된다.
    >
    >  @ResponseBody가 메서드에서 부여되면 메서드가 리턴하는 오브젝트는 메시지 컨버터를 통해 바로 HTTP Response Body에 직접 쓰여진다. 