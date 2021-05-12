# 메이븐과 스프링 STS 사용법

웹 애플리케이션을 구현할 때 이클립스에서 웹 프로젝트를 직접 생성한 후 스프링 기능에 필요한 라이브러리를 직접 다운로드하여 사용했다. 스프링이 나온 초기에는 이런 방식으로 프로그램을 개발했지만 스프링 버전이 자주 업데이트됨에 따라 불편함이 따랐다. 다시 말해 업데이트할 때마다 관련 기능의 라이브러리르 일일이 수정해야 했고, 라이브러리의 기능 사용법이 달라지면 소스도 같이 수정해 주어야 해서 불편했다. 그래서 현재는 메이븐과 같은 도구를 이용해 자동으로 스프링의 라이브러리 기능을 관리하면서 프로그램을 개발한다.



## 메이븐 프로젝트의 구조와 구성 요소

메이븐은 프로젝트 구조와 내용을 기술하는 선언적 접근 방식의 오픈 소스 빌드 툴이다. 메이븐을 사용하면 프로젝트 종속 라이브러리들과 그 라이브러리에 의존하는 Dependency 자원까지 관리할 수 있다. 메이븐은 프로젝트 전반의 리소스 관리와 설정 파일 그리고 이와 관련된 표준 디렉터리 구조를 처음부터 일관된 형태로 구성하여 관리한다.

> 일반적인 애플리케이션은 단지 코드를 컴파일 했다고 해서 동작하는 것이 아니다. 오픈 소스 라이브러리들은 컴파일할 때 합쳐져 하나의 기능을 이루는 것이다. 그리고 컴파일 과정 외에 테스팅, 배포와 같은 과정도 거쳐야 한다.
>
> 즉, 애플리케이션을 만들 때는 컴파일보다 더 많은 과정을 거치게 된다. 이런 과정을 빌드라고 하고 이런 작업을 자동으로 수행해 주는 툴을 빌드 툴이라고 한다. 이런 빌드 툴에는 Ani, Apache Ivy, Maven, Gradle 등이 있다.

메이븐을 사용하면 컴파일과 동시에 빌드를 수행할 수 있을 뿐 아니라 관련된 라이브러리도 일관성있게 관리할 수 있어 편리하다.

스프링 실습을 하면서 라이브러리 관련 jar 파일을 내려 받아 프로젝트에 추가할 경우 이와 연관된 종속 라이브러리까지 다 찾아서 추가해야 했다. 그러나 메이븐을 사용하면 이런 의존 관계를 자동으로 관리할 수 있다.

메이븐의 각 구성 요소들을 정리하면 아래와 같다.

+ pom.xml
  + 프로젝트 정보가 표시되며 스프링에서 사용되는 여러 가지 라이브러리를 설정해 다운로드할 수 있다.
  + pom.xml의 프로젝트 정보 설정 태그 구성 요소는 아래와 같다.
    + groupId
      + 프로젝트 그룹 id를 나타내며 일반적으로 도메인 이름을 사용해 설정
    + artifactId
      + 프로젝트 아티팩트 id를 설정 [대개는 패키지 이름으로 설정]
    + version
      + 프로젝트 버전을 설정
    + packaging
      + 애플리케이션 배포 시 패키징 타입을 설정 [war파일로 패키징]
  + `<dependencies>` 태그를 이용해 프로젝트가 의존하는 여러 가지 라이브러리를 설정한다.  `<dependencies>` 태그 안에서 사용되는 태그들은 아래와 같다.
    + dependency
      + 해당 프로젝트에서 의존하는 다른 라이브러리 정보를 기술
    + groupId
      + 의존하는 프로젝트의 그룹 id
    + artifactId
      + 의존하는 프로젝트의 아티팩트 id
    + version
      + 의존하는 프로젝트 버전 정보
+ src/main/java
  + 자바 소스 파일이 위치한다.
+ src/main/resources
  + 프로퍼티 파일이나 XML 파일 등 리소스 파일이 위치한다.
+ src/main/webapp
  + WEB_INF 등 웹 애플리케이션 리소스가 위치한다.
+ src/test/java
  + JUnit 등 테스트 파일이 위치한다.
+ src/test/resources
  + 테스트 시에 필요한 resource 파일이 위치한다.



### 1. 스프링 프로젝트 만들기

Spring Legacy Project 생성하고, 프로젝트 이름을 입력하고 Spring MVC Project로 템플릿을 선택한다. 마지막으로 패키지 이름을 입력하면 스프링 프로젝트가 생성된다.



### 2. STS 프로젝트 실행하기

#### 2-1. XMl 파일 설정하기

스프링 프로젝트를 만들면 XML 설정 파일이 자동으로 생성된다. 

web.xml은 다른 설정 파일을 읽어 들이는 부분과 DispatcherServlet을 매핑하는 부분이 자동으로 만들어진다.

servlet-context.xml에는 JSP의 위치를 지정하는 뷰리졸버와 JSP에서 사용하는 자바스크립트 파일 또는 이미지 같은 리소스 경로, 애너테이션 설정 등이 프로젝트 생성 시 자동으로 만들어진다.



#### 2-2 자바 클래스와 JSP 파일 만들기

일일이 추가할 필요없이 자동으로 자바 클래스와 JSP 파일이 생성된다.



### 3. STS 환경에서 마이바티스 사용하기

#### 3-1. pom.xml 이용해 마이바티스 라이브러리 설치하기

오라클의 경우에는 오픈 소스가 아니므로 드라이버를 직접 다운로드하여 설치해야 한다. 따라서 lib 폴더를 생성한 후 오라클 드라이버를 복사하여 붙여넣어야 한다. 그리고 pom.xml에는 `<dependency>` 태그를 이용해 라이브러리를 설정하고, 데이터베이스 기능 관련 라이브러리를 설정한다. 또한 mybatis.jar와 mybatis-spring.jar 라이브러리를 설정하고, 오라클 드라이버 경로도 설정해야 한다.

```xml
<dependencies>
    <!-- 데이터 소스 관련 라이브러리 설정-->
    <dependency>
        <groupId>commons-beanutils</groupId>
        <artifactId>commons-beanutils</artifactId>
        <version>1.8.0</version>
    </dependency>
    <dependency>
        <groupId>commons-dbcp</groupId>
        <artifactId>commons-dbcp</artifactId>
        <version>1.2.2</version>
    </dependency>
    <dependency>
        <groupId>cglib</groupId>
        <artifactId>cglib-nodep</artifactId>
        <version>2.2</version>
    </dependency>
    
    <!-- 마이바티스 관련 라이브러리 설정 -->
    <dependency>
        <groupId>org.mybatis</groupId>
        <artifactId>mybatis</artifactId>
        <version>3.1.0</version>
    </dependency>
    <dependency>
        <groupId>org.mybatis</groupId>
        <artifactId>mybatis-spring</artifactId>
        <version>1.1.0</version>
    </dependency>
    
    <!-- 로컬에 설치한 오라클 드라이버 라이브러리를 설정 -->
    <dependency>
        <groupId>jdbc.oracle</groupId>
        <artifactId>OracleDriver</artifactId>
        <version>12.1.0.2.0</version>
        <scope>system</scope>
        <systemPath>${basedir}/src/main/webapp/WEB-INF/lib/ojdbc6.jar</systemPath>
    </dependency>
	</dependencies>
```



#### 3-2. 마이바티스 관련 XML 파일 추가하기

1. WEB-INF/config/jdbc 경로를 구성하고 jdbc.properties 파일을 생성하고, WEB-INF/spring 경로에 action-mybatis.xml을 추가한다.

2. web.xml에서 action-mybatis.xml을 읽을 수 있도록 수정한다.

   ```xml
   <!-- root-context에서 action-mybatis.xml로 수정한다 -->
   <context-param>
       <param-name>contextConfigLocation</param-name>
       <param-value>/WEB-INF/spring/action-mybatis.xml</param-value>
   </context-param>
   ```

3. action-mybatis.xml에서 jdbc.propertis 경로를 수정한다.

   ```xml
   <bean id="propertyPlaceholderConfigurer" class="org.springframework.beans.factory.config.ProperyPlaceholderConfigurer">
   	<property name="Locations">
       	<value>/WEB-INF/config/jdbc/jdbc.properties</value>
       </property>
   </bean>
   ```

4.  src/main/resources 패키지 하위에 mybatis 패키지를 생성하고 그 하위에 mappers와 model 패키지를 생성한다. 그리고 mappers 패키지 내부에는 member.xml을, model 패키지 내에는 modelConfig.xml을 추가한다.

5. modelConfig.xml을 열어 패키지 이름을 수정한다.

   ```xml
   <configuration>
       <!-- MemberVO에 대한 alias를 설정 -->
   	<typeAlisases>
       	<typeAlias type="com.myspring.member.vo.MemberVO" alias="memberVO"></typeAlias>
       </typeAlisases>
   </configuration>
   ```



#### 3-3. 자바 클래스와 JSP 구현하기

브라우저의 URL 요청명에서 뷰리졸버 설정 없이 기능별로 해당 폴더에 쉽게 접근할 수 있도록 MemberControllerImpl 클래스에서 getViewName() 메서드를 수정한다. 



## log4j

정상적으로 실행되었는지 확인하기 위해서는 자바의 println() 메서드를 이욯해 데이터를 콘솔로 출력하곤 했다. 하지만 개발이 끝나고 실제 서비스를 한 후로는 출력 메서드는 필요가 없어진다. 그래서 해당 메서드들을 주석 처리하거나 삭제해야 한다. 하지만 유지관리 시에서 필요한 경우가 생길 수도 있다.

이런 번거로움을 덜기 위해서는 log4j를 이용한다.

실제 애플리케이션에서는 유지관리를 위해 웹 사이트에 접속한 사용자 정보나 각 클래스의 메서드 호출 시각 등 여러 가지 정보를 파일로 저장해서 관리한다. 이런 로그 관련 기능을 제공하는 것이 log4j이다. log4j의 기능은 독립적으로 라이브러리를 설치해서 사용할 수 있으며, 메이븐 같은 빌드 툴에서는 프로젝트 생성 시 자동으로 log4j 라이브러리가 설치된다.

log4j 기능과 관련된 설정은 log4j.xml 파일에서 수행하며, log4j.xml을 이루는 태그들의 특징은 아래와 같다.

+ `<Appender>`

  + 로그의 출력 위치를 결정(파일, 콘솔, DB 등)한다. log4j API 문서의 XXXAppender로 끝나는 클래스들의 이름을 보면 출력 위치를 알 수 있다.

+ `<Layout>`

  + Appender가 어디서 출력할 것인지 결정했다면 어떤 형식으로 출력할지 출력 레이아웃을 결정한다.

+ `<Logger>`

  + 로깅 메시지를 Appender에 전달한다. 개발자가 로그 레벨을 이용해 로그 출력 여부를 조정할 수 있다. logger는 로그 레벨을 가지고 있으며, 로그의 출력 여부는 로그문의 레벨과 로거의 레벨을 가지고 결정된다.

  

## 타일즈

일반적으로 JSP는 모든 화면 기능을 일일이 구현하는 것이 아니라 전체 화면 틀을 일정하게 만들어 놓고 본문(contents) 부분만 변경해서 사용한다. 

웹 애플리케이션 화면 구조는 상단 부분이나 왼쪽 메뉴 그리고 하단 부분을 담당하는 페이지를 따로 만들어 놓고 브라우저에서 웹 페이지를 요청하면 본문 화면만 추가하여 보여주게 된다. 이러한 화면 레이아웃 기능을 제공하는 것이 바로 타일즈 기능이다.

타일즈 기능 역시 pom.xml을 통해 쉽게 라이브러리를 설치하고 사용할 수 있다.

servlet-context.xml에서는 기존 JSP를 표시하기 위해 사용했던 InternalResourceViewResolver를 더 이상 사용하지 않으므로 주석 처리한 다음 타일즈 기능에 관련된 빈들을 설정한다. 그리고 스프링의 TilesConfigurer 클래스 빈을 생성하면서 URL 요청에 대해 브라우저에 나타낼 정보가 저장된 타일즈 설정 파일을 패키지 tiles에서 읽어 들인다.



### JSP에 타일즈 사용하기

1. tile.xml을 작성한다.
2. 레이아웃용 JSP를 작성한다.
3. 레이아웃에 표시할 JSP를 작성한다
4. 컨트롤러에서 tiles.xml에 설정한 뷰이름을 반환한다.