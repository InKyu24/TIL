# 스프링 MVC 기능

## 스프링 프레임워크 MVC의 특징

스프링 프레임워크는 웹 애플리케이션 개발에 필요한 여러 가지 기능을 미리 만들어서 제공한다. MVC 기능도 그 중 하나이다. 스프링에서 제공하는 기능 사용법을 익히고 나면 MVC 기능을 일일이 만들 필요 없이 편리하게 MVC 기능을 사용할 수 있다.

스프링에서 지원하는 MVC 기능의 특징은 아래와 같다.

+ 모델2 아키텍처를 지원한다.
+ 스프링과 다른 모듈과의 연계가 쉽다.
+ 타일즈(tiles)나 사이트메시(sitemesh) 같은 View 기술과의 연계가 쉽다.
+ 태그 라이브러리를 통해 message 출력, theme 적용 그리고 입력 폼을 보다 쉽게 구현할 수 있다.

스프링에서는 애플리케이션 개발 시 많이 사용되는 모델2 기반의 MVC 기능을 제공하므로 편리하게 애플리케이션을 개발할 수 있다. 그리고 타일즈나 사이트메시처럼 화면 관련 프레임워크와도 쉽게 연동할 수 있다.

스프링 프레임워크 MVC 기능 수행 과정은 아래와 같다.

1. 브라우저가 DispatcherServlet에 URL로 접근하여 해당 정보를 요청한다.
2. 핸들러 매핑에서 해당 요청에 대해 매핑된 컨트롤러가 있는지 요청한다.
3. 매핑된 컨트롤러에 대해 처리를 요청한다.
4. 컨트롤러가 클라이언트의 요청을 처리한 결과와 view 이름을 ModelAndView에 저장해서 DispatcherServlet으로 반환한다.
5. DispatcherServlet에서는 컨트롤러에서 보내온 View 이름을 ViewResolver로 보내 해당 View를 요청한다.
6. ViewResolver는 요청한 View를 보낸다.
7. View의 처리 결과를 DispatcherServlet으로 보낸다.
8. DispatcherServlet은 최종 결과를 브라우저로 전송한다.



# SimpleUrlController 이용한 스프링 MVC 실습 [SpringTest02_MVC.ex01]

브라우저의 요청 URL에 대해 미리 매핑해 놓은 컨트롤러를 호출하여 컨트롤러에서 지정한 JSP를 브라우저로 전송하는 과정을 실습해보자.

1. 브라우저에서 URL주소로 요청한다.
2. DispatcherServlet은 요청에 대해 미리 action-sevlet.xml에 매핑된 SimpleUrlController를 요청한다.
3. 컨드롤러는 요청에 대해 해당 장소에 있는 JSP를 브라우저로 전송한다.

서블릿에서는 브라우저 요청 처리 시 서블릿에서 제공하는 메서드를 이용해 요청명을 일일이 가져왔지만, 스프링에서는 브라우저의 요청을 쉽게 가져올 수 있는 여러 기능들을 제공한다.



# MultiActionController 이용한 스프링 MVC 실습 [SpringTest02_MVC.ex02]

SimpleUrlController를 이용해 요청을 처리하려면 각 요청명에 대해 다시 스프링의 Controller 인터페이스를 구현한 각각의 컨트롤러 클래스를 만들어야만 한다. 하지만 MultiActionController를 이용하려면 여러 요청명에 대해 한 개의 컨트롤러에 구현된 각 메서드로 처리할 수 있어 편리하다.



# 요청명과 동일한 JSP 표시하는 실습 [SpringTest02_MVC]