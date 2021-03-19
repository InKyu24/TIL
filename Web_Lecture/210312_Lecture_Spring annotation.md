# 스프링 애너테이션 기능

## 스프링 애너테이션이란?

스프링 2.5까지는 DI나 AOP 같은 기능은 따로 XML 파일로 설정한 후 애플리케이션에서 사용했다. 그러나 애플리케이션의 기능이 복잡해짐에 따라 XML 설정 파일의 내용도 복잡해졌고 관리에도 문제가 생기기 시작했다.

따라서 3.0부터는 DI 같은 자바 코드와 관련된 설정은 직접 코드에서 할 수 있게 애너테이션(Annotation)이라는 기능을 제공한다. 현재 스프링 기반 애플리케이션에서는 XML에서 설정하는 방법과 애너테이션 기능을 사용하는 방법 두 가지를 혼합해서 사용하고 있다.



### 스프링 애너테이션 제공 클래스

스프링에서 애너테이션을 사용하려면 먼저 스프링에서 제공하는 애너테이션 관련 클래스를 XML 설정 파일에서 빈으로 설정해야 한다.

+ DefaultAnnotationHandlerMapping
  + 클래스 레벨에서 @RequestMapping을 처리한다.
+ AnnotationMethodHandlerAdapter
  + 메서드 레벨에서 @RequestMapping을 처리한다.



### `<context:component-scan>` 태그 기능

`<context: component-scan>` 태그를 사용해 패키지 이름을 지정하면 애플리케이션 실행 시 해당 패키지에서 애너테이션으로 지정된 클래스를 빈으로 만들어 준다.

`<context: component-scan base-package="패키지 이름" />`로 지정한 패키지에 위치하는 클래스에 지정할 수 있는 애너테이션들을 아래와 같다.

+ @Controller
  + 스프링 컨테이너가 component-scan에 의해 지정한 클래스를 컨트롤러 빈으로 자동 변환
+ @Service
  + 스프링 컨테이너가 component-scan에 의해 지정한 클래스를 서비스 빈으로 자동 변환
+ @Repository
  + 스프링 컨테이너가 component-scan에 의해 지정한 클래스를 DAO 빈으로 자동 변환
+ @Component
  + 스프링 컨테이너가 component-scan에 의해 지정한 클래스를 빈으로 자동 변환



## 스프링 애너테이션 이용해 URL 요청 실습하기 [Spring_Annotation]



## 스프링 애너테이션 이용해 로그인 기능 구현하기

#### 메서드에 @RequestParam 적용하기

```java
Public ModelAndView login (HttpServletRequest request, HttpServlet response) throws Exception {
	String ID = request.getParameter("userID")
}

위의 코드를 아래와 같이 작성할 수 있다.

Public ModelAndView login (@RequestParam("userID") String userID, HttpServletRequest request, HttpServlet response) throws Exception {
}
```

#### @requestPara의 required 속성 사용하기

required 속성을 이용하면 반드시 전달해야 하는 필수 매개변수인 경우와 그렇지 않은 경우를 설정할 수 있다. 속성을 생략하면 기본값은 true이며, 메서드 호출 시 반드시 지정한 이름의 매개변수를 전달해야 하고, 매개변수가 없으면 예외가 발생하게 된다. false로 설정한 경우에는 메서드 호출 시 지정한 이름의 매개변수가 없으면 null을 자동 할당하게 된다.

```java
Public ModelAndView login (@RequestParam(value="userName", required=false) String userName, HttpServletRequest request, HttpServlet response) throws Exception {
}
```

#### @RequestParam 이용해 Map에 매개변수 값 설정하기

```java
Public ModelAndView login (@RequestParam Map<String,String> info, HttpServletRequest request, HttpServlet response) throws Exception {
    String id = info.get("id");
    String pw = info.get("pw");
}
```



#### @ModelAttribute 이용해 VO에 매개변수 값 설정하기

```java
Public ModelAndView login (@ModelAttribute("info") MemberVO memVO, HttpServletRequest request, HttpServlet response) throws Exception {
    System.out.println("ID: "+memVO.getUserID());
}
```



#### Model 클래스 이용해 값 전달하기

Model 클래스를 이용하면 메서드 호출 시 JSP로 값을 바로 바인딩하여 전달할 수 있다.

Model 클래스의 addAttribut() 메서드는 ModelAndView의 addObject() 메서드와 같은 기능을 한다.

Model 클래스는 따로 뷰 정보를 전달할 필요가 없을 때 사용하면 편리하다.

``` java
Public ModelAndView login (@ModelAttribute("info") MemberVO memVO, HttpServletRequest request, HttpServlet response) throws Exception {
    ModelAndView mav = new ModelAndView();
    System.out.println("ID: "+memVO.getUserID());
    mav.setViewname("result");
}

위의 코드를 아래와 같이 작성할 수 있다.
    
Public ModelAndView login (Model model, HttpServletRequest request, HttpServlet response) throws Exception {
    model.addAttribute("userID", "choi");
	return "result";
}
```



## @Autowired 이용해 빈 주입하기

XML에서 빈을 설정한 후 애플리케이션이 실행될 때 빈을 주입해서 사용하면 XML 파일이 복잡해지면서 사용 및 관리가 불편하다는 단점이 있다. 현재 스프링에서는 @Autowired를 이용해서 개발자가 만든 클래스의 빈을 직접 자바 코드에서 생성하여 사용한다.

@Autowired의 특징은 아래와 같다.

+ 기존 XMl 파일에서 각각의 빈을 DI로 주입했던 기능을 코드에서 애너테이션으로 자동으로 수행한다.
+ @Autowired를 사용하면 별도의 setter나 생성자 없이 속성에 빈을 주입할 수 있다.



1. web.xml 내에 ContextLoaderListener를 이용해 애플리케이션이 실행될 때 action-mybatis.xml을 읽어 들이도록 설정한다.

   ```xml
   <listener>
   	<listener-class> org.springframework.web.context.ContextLoaderListener</listener-class>
   </listener>
   
   <context-param>
       <param-name>contextConfigLocation</param-name>
       <param-value>
       	/WEB-INF/config/action-mybatis.xml
       </param-value>
   </context-param>
   ```

2. action-servlet.xml의 JSP 경로를 변경한다.

   ```xml
   <beans>
   <bean class="org.springframework.web.servlet.view.InternalResourceViewResolver">
   	<property name="prefix" value="WEB-INF/views/member/"></property>
       <property name="suffix" value=".jsp"></property>
   </bean>
   <bean class="org.springframework.web.servlet.mvc.annotation.
                DefaultAnnotationHandlerMapping"></bean>
   <bean class="org.springframework.web.servlet.mvc.annotation.
                AnnotationMethodHandlerAdapter"></bean>
       <context:component-scan base-package="com.spring"></context:component-scan>
   </beans>    
   ```

3. action-mybatis.xml에서 스프링에서 제공하는 클래스의 빈을 사용하기 위해 설정한다.

   ```xml
   <bean id="dataSource" class="org.apache.ibatis.datasource.pooled.PooledDataSource">
   	<property name="driver" value="${jdbc.driverClassName}" />
   	<property name="url" value="${jdbc.url}" />
   	<property name="username" value="${jdbc.username}" />
   	<property name="password" value="${jdbc.password}" />
   </bean>
    
   <bean id="sqlSessionFactory" class="org.mybatis.spring.SqlSessionFactoryBean">
       <property name="dataSource" ref="dataSource" />
       <property name="configLocation" value="classpath:mybatis/model/modelConfig.xml" />
       <property name="mapperLocations" value="classpath:mybatis/mappers/*.xml" />
   </bean>
   
   <bean id="sqlSession" class="org.mybatis.spring.SqlSessionTemplate">
   	<constructor-arg index="0" ref="sqlSessionFactory"></constructor-arg>
   </bean>
   ```

4. 매퍼 파일을 설정한다. [member.xml 과 modelConfig.xml]

5. 클래스들에 @Autowired 애너테이션을 이용한다.

   ```java
   @Controller
   public class HomeController {
       @Autowired
       MemberService memService;
   }
   
   @Service
   public class MemberService {
       @Autowired
       MemberDAO memDAO;
   }
   
   @Repository
   public class MemberDAO {
       @Autowired
   	SqlSession session;
   }
   ```

   