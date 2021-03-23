# 스프링 부트 사용하기

## Spring boot란?

Servlet에서 프로젝트를 시작하게 되면 맨 땅에서 건물을 짓는 것과 같다. Web-container 설정에서부터 구조를 하나하나 구축해야 한다. 최초 구조 구축 시에는 xml 설정 파일로 하나씩 모두 지정을 해야하는 작업이 필요하다. 초보 개발자가 혼자서 모두 구축해야 하는 것은 상당히 복잡하고 난이도가 높은 작업이다.

Spring 프레임워크는 Java에서 가장 대중적인 프레임워크로 DI, IOC 그리고 AOP라는 특징을 가지고 있다. 이로 인해서 좀 더 결합도를 낮추는 방식으로 개발을 가능케 한다. 하지만 Spring 프레임워크는 기능이 많은만큼 환경설정이 복잡한 편이다. Transaction, Hibernate Datasource, Entity, Session Factory 등 여러 가지 복잡한 프로젝트 세팅이 필요하다. 애너테이션 기능이 강화되면서 Spring boot가 나오게 되었다.

Spring boot는 Spring 프레임워크를 사용하기 위한 설정의 많은 부분을 자동화하여 사용자가 편하게 Spring을 활용할 수 있도록 돕는다. 내장된 Tomcat으로 Web-container 설정이 되어있으며, xml 설정도 되어있어서 마치 점차 웹 애플리케이션을 개발하는 것이 아니라 일반 응용 프로그램을 개발하는 것처럼 보이게 한다.

Spring boot의 특징을 정리하면 아래와 같다.

+ 일반적 응용 프로그램을 단독으로 실행하는 수준으로 스프링 애플리케이션을 구현할 수 있다.
+ 프로젝트 환경을 구축할 때 필요한 톰캣, Jetty, UnderFlow 같은 서버 외적인 툴이 내장되어 있어 따로 설치할 필요가 없다.
+ XML 기반 설정이나 코드 없이 환경 설정을 자동화할 수 있다.
+ 의존성 관리를 쉽게 자동으로 할 수 있다.



## Spring boot 프로젝트 생성하기

+ New Spring Starter Project
  + Name : 프로젝트명
  + Type : Maven
  + Packaging : War
  + Group, Package : 패키지명
+ SQL 항목에서 H2 Database, JDBC API 선택하고, Web 항목에서 Spring Web 선택



## Spring boot 프로젝트 실행하기

+ application.properties에서 프로젝트 전체와 관련된 기능 설정

  ```properties
  #Server 설정 [tomcat 포트번호 설정, 세션 시간 설정]
  server.port=8090
  server.servlet.session.timeout=1800
  ```

+ Controller 클래스 생성하고 `@Controller` 애너테이션 추가

> Application.java가 반드시 있어야 하며, 이는 스프링 부트의 웹 애플리케이션을 일반 자바 애플리케이션처럼 개발하기 위한 목적이다. 따라서 main() 메서드가 있어야 한다.
>
> ServletInitializer.java 파일에 생성된 ServletInitializer 클래스는 web.xml 없이 스프링 부트 애플리케이션을 실행할 수 있게 하는SpringBootServletInitializer 클래스를 상속받는다. 

