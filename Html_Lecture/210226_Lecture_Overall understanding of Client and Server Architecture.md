# 클라이언트/서버 아키텍처

클라이언트/서버 아키텍처는 크게 클라이언트 프로세스와 서버 프로세스로 구성된다. 서버 프로세스는 주어진 타입의 리소스를 모아 관리하는 리소스 관리자의 역할을 수행하는 쪽이며, 클라이언트 프로세스는 공유된 하드웨어와 소프트웨어 리소스에 대한 액세스가 필요한 작업을 수행하는 쪽이다. 즉, 클라이언트/서버 아키텍쳐에서는 모든 공유 리소스가 서버 프로세스에 의해 관리된다.

클라이언트/서버 아키텍쳐에서 행해지는 분산 컴퓨팅은 하나의 프로그램(클라이언트 프로세스)이 다른 프로그램(서버 프로세스)과의 통신을 통해 데이터를 교환하는 형태로 이루어진다. 클라이언트와 서버가 통신할 때는 대개 동일한 언어(클라이언트와 서버가 모두 이해할 수 있는 프로토콜)를 사용한다.

TCP/IP는 가장 일반적으로 많이 사용되고 있는 프로토콜 중 하나이며, WWW(World Wide Web)은 데이터 전송 프로토콜로 HTTP(Hypertext Transfer Protocol)을 사용하고 있다.



## HTTP(Hypertext Transfer Protocol)

Hypertext Transfer Protocol(HTTP)은 클라이언트와 서버가 파일을 주고받기 위해 사용하는 FTP와 유사한 것으로, 웹 브라우저와 웹 서버가 커뮤니케이션하기 위해 사용되는 프로토콜이다.

HTTP를 이용할 경우 커넥션(connection)당 단 한 번의 요청만 할 수 있다. 클라이언트와 서버에 연결해서 원하는 파일 하나를 수신한 후 클라이언트와 서버와의 연결이 끊어짐을 의미한다. 이와 같은 메커니즘을 사용함으로써 서버가 처리할 수 있는 처리량보다 더 많은 사용자가 서버에 연결해서 작업할 수 있다. 

Hypertext Transfer Protocol(HTTP)은 request-response 기반의 프로토콜이다. 즉, request-response가 하나의 작업 단위(트랜잭션)로 이루어져 있고, 하나의 작업단위가 끝났을 때 클라이언트와 서버와의 연결은 끊어지게 된다. 

웹 브라우저가 요청(request)을 서버에 전송하면, 웹 서버는 클라이언트가 요청한 파일이 어떤 것인지를 결정한 후, 이 파일을 클라이언트에게 응답(response)으로 보낸다. 서버의 응답을 받은 클라이언트는 이 응답정보를 해석한 후 화면에 디스플레이한다. 이때 서버가 보내는 응답 정보는 일반적으로 HTML 문서가 된다.



## URL(Uniform Resource Locate)

웹 브라우저가 다양한 서비스를 제공하고 있는 수많은 서버들로부터 필요한 정보를 얻기 위해서는 이들의 위치를 표시하기 위한 방법이 필요한데, 이를 위해 URL이 사용되고 있다. URL은 웹상에서 서비스를 제공하는 각 서버들에 있는 파일들의 위치를 명시하기 위한 것으로 접속해야 할 서비스의 종류, 서버의 위치(도메인 네임), 파일의 위치를 포함하고 있다.



## CGI(Common Gateway Interface)

서버는 URL을 이용해 어떤 CGI 프로그램을 실행시킬지를 결정하게 된다. CGI 프로그램은 HTTP request를 통해 전송되어온 CGI 데이터를 파싱해서, 이 데이터를 이용해 프로세싱을 수행한 후, 응답(response)을 생성하게 된다. 이때 생성되는 응답(reponse)은 보통 HTML 페이지가 된다. CGI 응답(response)은 HTTP 응답(response)을 이용해 서버에서 클라이언트로 전송된다.

CGI 프로그램은 사용자의 요청 시 사용자 요청을 처리하기 위해 웹 서버에 의해 별도의 프로세스 단위로 실행된다. CGI 프로그램은 새로운 CGI 요청이 들어올 때마다 이 요청은 독립된 별도의 프로세스가 생성되어 처리되게 된다. 

CGI 프로그램은 새로운 CGI 요청이 들어올 때마다 이 요청은 독립된 별도의 프로세스가 생성되어 처리되게 된다. 여러 개의 CGI 요청을 처리해야 할 경우 시스템의 오버헤드는 높아지게 된다.



## Java Servlet

간단히 말해서 자바 서블릿은 자바를 사용해 웹을 만들기 위해서 꼭 필요한 기술이다. 클라이언트가 어떤 요청을 하면, 그에 대한 결과를 다시 전송해주어야 하는데 이러한 역할을 하는 프로그램인 것이다. 따라서 자바 서블릿은  자바로 구현된 CGI라고 볼 수 있다. 서블릿을 이용해 할수 있는 작업들은 CGI를 이용해 수행했던 작업들과 거의 유사하지만, 실행 구조측면에서 서로 다른 구조를 가지고 있다.

서블릿은 CGI 프로그램과 달리, 컴포넌트 컨테이너 아키텍처(component container architecture) 환경에서 실행된다. 여기에서 컨테이너는 일반적으로 웹 컨테이너(Web container)라고 하는데, 웹 컨테이너는 서블릿 API을 구현하고 있는 JVM이고, 서블릿 인스턴스는 웹 컨테이너에 의해 관리되고 HTTP 요청을 처리한다.

CGI는 HTTP 요청을 독립된 프로세스 단위로 처리하는 반면, 서블릿은 스레드 단위로 처리한다. 하나 이상의 HTTP 요청이 발생할 경우, 서블릿 인스턴스가 추가적으로 생성되거나 오퍼레이션 시스템 프로세스가 추가적으로 생성되지 않는다. 대신 각각의 요청은 스레드를 이용해 처리된다. 따라서 CGI 아키텍쳐 보다 서버 시스템의 오버헤드를 줄일 수 있다. 



## Servlet Container

서버에 Servlet를 만들었다고 해서 스스로 작동하는 것이 아니다. Servlet을 관리해주는 것이 필요하기 때문이다. 이를 Servlet Container라고 부른다. 대표적으로는 Apache Tomcat이 있다.

Servlet이 어떠한 역할을 수행하는 정의서라고 보면, Servlet Container는 그 정의서를 수행한다고 볼 수 있다. Servlet Container는 클라이언트의 요청을 받아들이고, 응답할 수 있도록 웹 서버와 소켓으로 통신한다.

Servlet Container는 Servlet과 Web server가 손쉽게 통신할 수 있게 해준다. Socket을 만들고, Listen, accept 등의 복잡한 과정들을 생략할 수 있도록, 이러한 기능들을 API로 제공하고 있다. 그래서 개발자가 Servlet에 구현해야 할 비즈니스 로직에 대해서만 초점을 둘 수 있게 해준다.

또한 Servlet Life Cycle을 관리해준다. Servlet 클래스를 로딩하여 객체화하고, 메소드를 호출해준다. 그리고 Servlet이 생명을 다하게 되면 적절하게 Garbage Collection을 진행하는 편의도 제공한다. Servlet Life Cycle에 대한 자세한 내용은 후술하도록 한다.

Servlet Container는 요청이 올 때마다 새로운 Java Thread를 하나 생성하는데, HTTP 서비스 메소드를 실행하고 나면, Thread는 자동으로 죽게 된다. 원래는 Thread를 관리해야 하지만 Server가 다중 Thread를 생성 및 운영해주니 Thread의 안정성에 대해 걱정할 필요가 없어진다.

Servlet Container를 사용하면 개발자는 보안에 관련된 내용들을 Servlet 또는 Java 클래스에 구현해둘 필요가 없어진다. 일반적인 보안관리는 XML 배포 서술자에 기록하기 때문에, 보안에 대해 수정할 일이 생겨도 source 코드를 수정하여 다시 컴파일 하지 않아도 보안관리 가능합니다.



## Servlet Life Cycle

클라이언트가 Servlet에 요청을 하면, Servlet이 바로 호출되는 것이 아니다. Servlet은 객체를 생성하고 초기화 작업을 거친 후, 요청을 처리하는 생명주기를 가지고 있다.

1. HTTP Request가 오면, Servlet Contatiner로 전송되고, 클래스가 로딩되어 요청에 대한 Servlet 객체(HttpServletRequest, HttpServletResponse)가 생성된다.
2. 서버는 init() 메소드를 호출해서 Servlet를 초기화한다.
3. web.xml을 기반으로 사용자가 요청한 URL이 어느 Servlet에 대한 요청인지 확인하여, 해당 Servlet에서 Service() 메소드를 호출한다.
4. Service() 메소드는 브라우저의 Request를 처리하도록 doGet() 또는 doPost() 메소드 등을 호출한다.
5. doGet() 또는 doPost() 메소드에서 동적 페이지를 생성한 후 HttpServletResponse객체에 응답을 보낸다.
6. Container를 종료하거나 source가 변경되었을 때, destroy() 호출하여 HttpServletRequest, HttpServletResponse 두 객체를 소멸시킨다.

> 한 번 Servlet 객체가 생성된다면, Servlet 객체는 메모리에 저장되어 있다. 그래서 init() 메소드는 호출되지 않고, 곧바로 Service() 메소드를 호출한다.



## HTTP servlet

![](https://1.bp.blogspot.com/-45Enya5j6Vc/YDtV5CVLfsI/AAAAAAAAGYI/cLkVw8Ao4qQWt0OJJK-LO71uVSVYa2CoACLcBGAsYHQ/w597-h640/aa.jpg)



## HTTP get 방식과 post 방식

HTTP Get 방식은 가장 일반적으로 많이 사용되는 HTTP 방식이기에 기본값으로  설정되어 나타난다. 단순히 서버에게 자원을 요청하는 일을 한다. Get 방식으로 보낼 수 있는 글자수(데이터의 양)는 제한되어 있다. Get 방식은 URL 주소 뒤에 데이터를 붙이는데, 이 데이터(파라미터)가 URL 주소창에 표시되기 때문에 주요 Data는 Get 방식으로 보내면 안된다. 하지만 Get 방식은 URL 자체가 Data가 되기 때문에 해당 페이지를 북마크할 수 있다는 장점도 있다.

Get 방식은 URL 주소 뒤에 파라미터가 붙기 때문에 URL주소와 파라미터 사이의 구분이 필요하다. 그 구분자는 `?`표시로 나타난다. 

Post 방식은 서버에게 요청 시 필요한 정보를 URL 주소가 아닌 요청 헤더에 포함시켜 전송하는 방식이다. 따라서 Get 방식과는 달리 길이에 제한이 없으며, 보안을 지킬 수 있다는 장점이 있다.

> Get 방식이 단순한 페이지 연결이 목적이라면, Post 방식은 데이터 전달을 주목적으로 한다.

![img](https://1.bp.blogspot.com/-vkKQHCF5jvo/YDtV5JHt5jI/AAAAAAAAGYE/LvPduZZ2iYMkLqegYKiKBC6-ZZPXSaUwwCLcBGAsYHQ/s16000/Http%2Brequest%2B%2526%2Bresponse.png)



## JSP (Java Server Pages)

JSP는 자바를 이용해 동적 HTML 페이지를 생성하기 위해 제공되는 기술로 서블릿과 거의 같은 구조(멀티 스레딩)로 실행된다. PHP, ASP, JSP는 같은 목적으로 사용될 수 있는 기술들이다.









개별 프로젝트 일환의 과제

Web10 project

blog2.html 의 

좌측 상단 me를 누르면 login 창

우측 상단 who를 누르면 회원가입이 될 수 있도록

