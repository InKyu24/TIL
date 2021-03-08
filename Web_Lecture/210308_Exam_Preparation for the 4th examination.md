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

   1) http://localhost:8080/greeting으로 호출할 수 있다.

   ***<u>2) http://localhost:8080/SayHello/greeting으로 호출할 수 있다.</u>***

   3) http://localhost:8080/Hello/greeting으로 호출할 수 있다.

   4) http://localhost:8080/servlet/greeting으로 호출할 수 있다.

> `http://IP주소:포트번호/프로젝트이름(컨텍스트이름)/서블릿매핑이름`



9. servlet  파일을 접근하려고 할 때 다음처럼 web browser에서 request를 한다면 무슨 문제점이 있는가?          http://localhost:8080/SayHello/servlet/web.controller.FormProcessingServlet

   1) 경로가 복잡하기 때문에 속도의 저하를 가져온다.

   2) 많은 양의 data를 전송할수 없다.

   ***<u>3) web container의 경로명이 노출되기 때문에 보안에 문제가 생긴다.</u>***

   4) servlet에 대한 접근을 web browser에서만 해야한다.

> 클래스  이름이 길어지면 입력하기 불편해진다. 그리고 일반적으로 클래스 이름을 보면 그 클래스가 어떤 기능을 하는지 짐작할 수 있는데, 브라우저에서  버젓이 클래스 이름으로 입력하는 것은 보안에도 좋지 않다. 따라서 서블릿 클래스 이름에 대응되는 서블릿 매핑 이름으로 실제 서블릿을  요청한다.



1. 다음 중 틀린 설명은?

   1) 웹컨테이너에 의해 Web Application당 한 개의 ServletContext객체가 생성된다.

   2) 웹컨테이너에 의해 HTTP request에 대응되는 HttpServletRequest 객체가 생성된다.

   3) 웹컨테이너에 의해 HTTP response에 대응되는 HttpServletResponse 객체가 생성된다.

   ***<u>4) 웹컨테이너에 의해 Web Application당 한 개의 서비스 Thread가 생성된다.</u>***

> 요청에 의해  계속 Thread 생성
