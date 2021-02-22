# 웹 프로그래밍

서버 프로그램은 자바, C#, 루비, 파이썬, 자바스크립트 같은 언어로 개발한다. 웹 서버를 쉽게 개발할 수 있도록 이 프로그래밍 언어를 기반으로 만든 기본 웹 프레임워크(ASP.NET, JSP, PHP 등), MVC 프레임워크(ASP.NET MVC, Spring MVC, Ruby on Rails 등), 비동기 프레임워크(Node.js Express, Jetty)를 활용한다. 프레임워크는 IoC(Inversion of Control) 속성을 가진 모듈을 의미한다. 간단하게 특적 목적의 개발을 쉽게 할 수 있게 여러 기능을 모아 둔 것이라고 이해하고 추후에 확장하여 이해해보자.

웹 브라우저에서 작동하는 클라이언트 프로그램은 서버 프로그램과 달리 클라이언트 프로그램은 반드시 HTML, CSS, 자바스크립트로 개발해야 한다. HTML로 요소를 생성하고 CSS로 디자인해서 자바스크립트로 프로그래밍 요소를 부여한다.

현대 웹 페이지에 사용되는 표준 기술은 HTML5 표준, CSS3 표준, ECMAScript 표준으로 정리할 수 있다. ECMAScript 표준은 자바스크립트 표준의 공식 명칭이다.

HTML5는 큰 의미로는 웹 표준 기술을 총칭하고, 작은 의미로는 웹 페이지를 구성하는 HTML 마크업 언어 그 자체를 뜻한다. 

> 마크업(Markup) : 웹 페이지의 서식이나 구조를 표현하는 정보

CSS는 HTML 페이지에 스타일을 지정하는 스타일시트를 작성할 때 사용하는 언어이다.

자바스크립트는 HTML 페이지에서 사용자 반응 등을 처리하는 스크립트를 작성하는 언어이다. 



```html
<html>
	<head>
    
    </head>   
    <body>
        <h1>
            hello html~!
        </h1>
    </body>
</html>
```



# HTML5 기본 용어

## 요소와 태그

HTML5를 공부하려면 기본적으로 태그, 요소, 속성 용어를 알아야 한다. 요소는 HTML 페이지를 구성하는 각 부품이고, 태그는 요소를 만들 때 사용하는 작성 방법을 의미한다. 흔히 요소와 태그를 구분하지 않고 사용한다. 요소는 내용을 가질 수 있는 요소와 내용을 가질 수 없는 요소로 구분되며, 내용을 가질 수 있는 요소는 `<요소 이름>내용</요소 이름>` 형태로 생성하고, 내용을 가질 수 없는 요소는 `<요소 이름>` 형태로 생성한다. 내용에는 텍스트가 들어갈 수도 있으며, 다른 요소가 들어갈 수도 있다. 또한 내용은 가질 수 있는 선택 옵션으로 내용을 입력하지 않아도 상관없다.

> 내용을 가질 수 있는 요소 : `<h1>Hello HTML5</h1>`
>
> 내용을 가질 수 없는 요소 : `<br>`

내용을 가질 수 없는 요소는 HTML 표기법으로 생성할 수 있고, XHTML 표기법으로도 생성할 수 있다. HTML 표기법으로는 태그만 보고는 내용을 가질 수 있는 태그의 시작 태그인지, 내용을 가질 수 없는 태그인지 구분하기 어렵다. 따라서 XML 작성 방식을 적용해 XHTML 표기법을 만들게 되었다. XHTML 표기법에서는 `<요소 이름 />` 형태로 생성한다.

## 속성

속성은 태그에 추가 정보를 부여할 때 사용하는 것으로, `<h1 title="header">Hello HTML5</h1>`와 같은 형태를 갖는다. 여기서 `title`은 속성 이름이고, `=`은 속성 블록을 나타내며, `"header"`는 속성 값을 의미한다. 

## 주석

프로그램이 커지면 자기가 작성한 코드도 무슨 목적으로 작성했는지 알아보기가 힘든 경우가 있다. 다라서 어떤 기능을 하는 코드인지 설명을 기록할 수 있는 방법이 필요하다. 그래서 프로그램 실행에 영향을 미치지 않고 설명을 할 수 있는 코드가 필요하고, 이를 주석이라 한다. HTML에서 주석의 형태는 `<!-- 주석-->` 으로 표기한다.



# HTML5 페이지의 구조와 작성법

## HTML5 페이지의 구조

```html
<!DOCTYPE html>		 <!-- 웹 브라우저에 HTML5 문서라는 것을 알리기 위해 반드시 첫 행에 기입 -->
<html>			<!-- 모든 HTML 페이지의 기본 요소로, 모든 태그가 이 html 태그 내부에 작성됨 -->
<head>						   	   <!-- Body 태그에 필요한 스타일시트와 자바스크립트를 제공-->
<meta charset="UTF-8">
<title>Insert title here</title>				   <!-- 웹 브라우저에 표시하는 제목 지정 -->
</head>
<body>
	hello 인규~! <br>안녕?						 <!-- 사용자에게 실제로 보이는 부분을 작성 -->
</body>
</html>
```

> HTML5 페이지의 작성과 실행 : 
> HTML 페이지를 만들고 실행하기 위해서는 코드를 작성하고, 확장자명을 .html 또는 .htm으로 저장해야 웹 브라우저에서 HTML 파일로 인식한다.



## 스타일시트 작성과 실행

웹 페이지는 두 가지 방법의 스타일시트를 사용해 스타일을 적용한다. 이를 내부 스타일 방법과 외부 스타일 방법이라 할 수 있다. 먼저 내부 스타일 방법은 HTML 페이지 내부에서 style 태그를 사용해 스타일시트를 직접 입력하는 방법이고, 외부 스타일 방법은 스타일시트를 별도의 파일로 만든 후, HTML 페이지 내부에서 link 태그의 href 속성을 사용해 스타일시트를 불러오는 방법이다.

스타일시트가 짧은 경우에는 내부 스타일 방법도 괜찮지만, 여러 사람이 함께 협업하고 프로젝트의 규모가 큰 경우에는 외부 스타일이 더 효율적이다.



### 내부 스타일시트 작성과 실행

html 문서 내부에 style 태그를 사용하여, 제목 글자의 스타일을 변경해보자.

```html
<!DOCTYPE html>		 			
<html lang="ko">							
<head>
    <meta charset="UTF-8">
	<title>Insert title here</title>
    <!-- 내부 스타일 시트-->
	<style type="text/css">		  
		h1{
			color:white;
			background:black;
		}
	</style>
</head>
<body>
	<h1> hello~! </h1>
</body>
</html>
```



### 외부 스타일시트 작성과 실행

html 문서 외부에 link 태그를 사용하여, 외부 파일인 Style.css에서 스타일을 가져와 제목 글자의 스타일을 변경해보자.

```html
<!DOCTYPE html>		 			
<html lang="ko">							
<head>
    <meta charset="UTF-8">
	<title>Insert title here</title>
    <!-- 외부 스타일 시트-->
	<link rel="stylesheet" href="Style.css"> 
</head>
<body>
	<h1> hello~! </h1>
</body>
</html>
```

```css
/* Style.css */
h1{
			color:white;
			background:black;
}
```



## 자바스크립트 작성과 실행

자바스크립트도 스타일시트처럼 script 태그를 사용해 내부에서 작성하거나 script 태그의 scr 속성을 사용해 외부에서 불러오도록 작성할 수 있다. 일반적으로 자바스크립트 코드는 입력하다 보면 1000행이 넘는 경우가 많아 주로 외부 자바스크립트로 작성한다.



### 내부 자바스크립트 작성과 실행

내부에 경고 창을 출력하는 자바스크립트를 작성하기 위해서, script 태그를 사용해보자.

```html
<!DOCTYPE html>		 			
<html lang="ko">							
<head>
    <meta charset="UTF-8">
	<title>Insert title here</title>
	<link rel="stylesheet" href="Style.css">
    <!-- 내부 자바스크립트-->
	<script type="text/javascript">
		alert('hello javascript');
	</script>
	
</head>
<body>
	<h1> hello~! </h1>
</body>
</html>
```



### 외부 자바스크립트 작성과 실행

외부 자바스크립트를 통해 경고 창을 출력하기 위해, script 태그의 src 속성을 사용해 보자.

```html
<!DOCTYPE html>		 			
<html lang="ko">							
<head>
    <meta charset="UTF-8">
	<title>Insert title here</title>
	<link rel="stylesheet" href="Style.css">
    <!-- 외부 자바스크립트 -->
	<script src="OuterJavaScript.js">
	</script>
	
</head>
<body>
	<h1> hello~! </h1>
</body>
</html>
```

```javascript
/* OuterJavaScript.js */
alert('hello javascript');
```



# 오류와 검증

프로그램이 원하지 않는 방향으로 동작하는 것을 버그라고 하며, 버그를 잡는 행위를 디버그라고 한다. 디버그는 웹 브라우저의 검사 기능을 쉽게 수행할 수 있게 한다. 크롬을 실행한 후 `F12`키 또는 `Ctrl`+`Shift`+`I` 를 누르거나 마우스 오른쪽  버튼을 누르고 [검사] 메뉴를 선택하면 검사가 실행된다.

검사 기능은 다양하지만 일반적으로는 [Element] 탭과 [Console] 탭만을 사용한다. 



# 기본 태그

## 글자 태그

웹 페이지는 글자 태그의 비중이 가장 크다. 글자 태그의 다양한 종류를 알아보자.



### 제목 글자 태그

제목 글자 태그에서 h는 heading(제목)을 의미한다. 첫번째로 큰 제목 글자는 h1 태그를 사용하며, h6까지 사용 가능하다.

```html
<body>
    <h1> 제일 큰 제목 </h1>
	<h2> 두번째로 큰 제목 </h2>
	<h3> 세번째로 큰 제목 </h3>
	<h4> 네번째로 큰 제목 </h4>
	<h5> 다섯번째로 큰 제목 </h5>
	<h6> 제일 작은 제목 </h6>	
</body>
```



### 본문 글자 태그

본문의 단락을 구문하는 태그 p는 paragraph(단락)를 의미한다.  각각의 p 태그가 문단을 하나씩 만들게 된다.

```html
<body>
	<h1>제목 글자</h1>
	<p> 어쩌구 저쩌구 </p>
	<p> 동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라 만세 </p>
	<p> p 태그를 이용하면 단락이 끝날 때마다 자동으로 행 바꿈이 일어난다. </p>
	<p> 이것이 네 번째 단락이겠지 </p>
</body>
```

줄 바꿈이 필요한 경우에는 br 태그를 사용하며, break(줄 바꿈)를 의미한다.

```html
<body>
	<h1>제목 글자</h1>
	<p> 어쩌구 저쩌구 </p>
	<p> 동해물과 백두산이 마르고 닳도록<br>하느님이 보우하사 우리나라 만세<br>무궁화 삼천리 화려강산<br>대한사람 대한으로 길이 보전하세</p>
	<p> br 태그를 이용하면 줄 바꿈이 일어난다. p태그와 달리 단락의 변경은 없다.</p>
	<p> 이것이 네 번째 단락이겠지 </p>
</body>
```

수평줄을 삽입하고자 하면 horizontal rule을 의미하는 hr 태그를 사용할 수 있다. 

```html
<body>
	<h1>제목 글자</h1>
	<p> 어쩌구 저쩌구 </p>
	<p> 동해물과 백두산이 마르고 닳도록<br>하느님이 보우하사 우리나라 만세<hr>무궁화 삼천리 화려강산<br>대한사람 대한으로 길이 보전하세</p>
	<p> hr 태그를 이용해 애국가 후렴를 구분해보았다. </p>
	<p> 이것이 네 번째 단락이겠지 </p>
</body>
```



### 특수 문자 표기

HTML 태그 내부에 공백 3개를 연속으로 입력한 후 패일을 실행해도 연속된 공백을 하나의 공백으로 인식하며, 공백이 제대로 표시되지 않는다. 이때 non-breaking space를 의미하는 `&nbsp;`를 사용하여 개수만큼의 공백을 표현할 수 있다.



<, >는 HTML에서 중요한 문구로 사용된다. 텍스트 자체로 <, >를 사용하기 위해서는 `&lt;`와 `&gt;`를 통해 입력해야 한다.

```html
<body>
	<h1>제목 글자</h1>
	<p> h1하고 h2를 비교해보자 </p>
	<P> h1 태그가 h2 태그보다 더 큰 제목이다. </P>
	<!-- <h1>이 <h2>보다 더 큰 제목이다. -->
    <P> &lt;h1&gt;이 &lt;h2&gt;보다 더 큰 제목이다. </P>
</body>
```



### 앵커 태그

HTML(HyperText Markup Language)에서 가장 중요한 글자는 H인 하이퍼텍스트이다. 하이퍼텍스트는 사용자의 선택에 따라 관련한 특정 정보로 이동할 수 있도록 조직된 문서를 의미한다. HTML 페이지가 조직화된 문서 형태가 될 수 있는 이유는 하이퍼링크를 생성하는 a 태그 덕분이다. a 태그는 anchor를 의미하며, 다른 웹 페이지나 웹 페이지 내부의 특정 위치로 이동할 때 사용하게 된다. 

a 태그만으로는 어떤 웹 페이지로 이동할지 웹 브라우저에 알려줄 수 없기에 href 속성을 사용한다. href는 hyper reference를 의미하고, 웹 페이지나 파일의 위치를 나타내는 경로가 들어가는 위치이다.

#### 특정 웹 페이지에 연결하기

```html
<a href="http://google.co.kr">구글 접속</a> <br>
<a href="http://naver.com">네이버 접속</a>
```

#### 웹 페이지 내부에 연결하기

```html
<a href="#alpha">Alpha 부분</a> <br>
<a href="#beta">Beta 부분</a>
<!-- 수많은 글-->
<h1 id="alpha">Alpha</h1>
<!-- 수많은 글-->
<h1 id="beta">Beta</h1>
<!-- 수많은 글-->
```



### 글자 모양 태그

글자 모양 태그는 단독으로 사용하거나, 2개 이상의 글자 모양 태그를 겹쳐서 사용할 수도 있다. 다만 제목 글자와 본문 글자 태그 내부에 글자 모양 태그를 넣을 수 있으나 글자 모양 태그 내부에는 제목 글자와 본문 글자 태그를 넣을 수 없다는 것에 유의하자.

```html
<body>
    <h1><b>굵은 제목</b></h1>
    <h1><i>기울어진 제목</i></h1>
    <h1><small>작은 제목</small></h1>
    <h1>제목에<sub>아래 첨자</sub></h1>
    <h1>제목에<sup>위 첨자</sup></h1>
    <h1><ins>밑줄 그어진 제목</ins></h1>
    <h1><del>취소선 그어진 제목</del></h1>
    <hr />
    <b>굵은 내용</b><br />
    <i>기울어진 내용</i><br />
    <small>작은 내용</small><br />
    내용에 <sub> 아래 첨자</sub><br />
    내용에 <sup> 위 첨자</sup><br />
    <ins>밑줄 그어진 내용</ins><br />
    <del>취소선 그어진 내용</del><br />
</body>
</html>
```



## 목록 태그

웹 페이지에서 빠지지 않고 등장하는 요소는 바로 네비게이션 메뉴이고, 네비게이션 메뉴를 제작할 때는 주로 목록 태그를 사용한다. 순서가 없는 목록을 생성하기 위해서는 ul 태그를 사용하고, 순서가 있는 목록을 생성하기 위해서는 ol 태그를 사용한다. 그리고 li 태그를 통해 목록 요소를 생성하게 된다.

```html
<!-- 순서 없는 목록 -->
<ul>
    <li>서울</li>
    <li>대전</li>        
    <li>대구</li>
    <li>부산</li>
</ul>

<!-- 순서 있는 목록 -->
<ol>
    <li>금메달</li>
    <li>은메달</li>        
    <li>동메달</li>
</ol>

<!-- 중첩된 목록 -->
<ul>
    <li> <b> 내가 좋아하는 과일 순위 </b></li>
    <ol>
        <li> 딸기 </li>
        <li> 바나나 </li>
        <li> 키위 </li>
    </ol>
    
    <li> <b> 내가 좋아하는 가족 순위 </b></li>
    <ol>
	    <li> 엄마 </li>
	    <li> 할머니 </li>
    	<li> 누나 </li>
    </ol>
</ul>
```





## 테이블 태그

표를 삽입하는 태그는 table이다.  표의 테두리 두께를 지정하는 border 속성을 가지고 있고 tr, th, td 태그 없이는 독립적으로 사용하지 않는 특징이 있다. 

tr은 표의 행을 삽입하는 태그이다. 행을 우선적으로 삽입하고 제목 셀이나 일반 셀을 생성하는 것이 기본 순서이다. 여기서 제목 셀을 삽입하기 위해서는 th 태그를, 일반 셀을 삽입하기 위해서는 td 태그을 이용한다. th와 td 태그는 colspan 속성과 rowspan 속성을 통해 셀의 너비와 높이를 지정할 수 있다.

<table border="3">
    <tr>
        <th colspan="5">5월</th>
    </tr>
    <tr>
        <td>월</td><td>화</td><td>수</td><td>목</td><td>금</td>
    </tr>
    <tr>
    <td>21</td><td>22</td><td>23</td><td>24</td><td>25</td>
	</tr>
    <tr>
    <td>28</td><td>29</td><td>30</td><td>31</td><td></td>
	</tr>
</table>

```html
<table border="3">
    <tr>
        <th colspan="5">5월</th>
    </tr>
    
    <tr>
        <td>월</td>
        <td>화</td>
        <td>수</td>
        <td>목</td>
        <td>금</td>
    </tr>
    
    <tr>
   		<td>21</td>
        <td>22</td>
        <td>23</td>
        <td>24</td>
        <td>25</td>
	</tr>
    
    <tr>
    	<td>28</td>
        <td>29</td>
        <td>30</td>
        <td>31</td>
        <td></td>
	</tr>
</table>
```



## 미디어 태그

지금까지는 배운 태그는 텍스트를 이용한 태그였다. 여기서는 이미지, 오디오, 비디오와 같은 멀티미디어를 넣는 태그를 알아보자.

+ img 태그
  + scr 속성 : 이미지의 경로 지정
  + alt 속성 : 이미지가 없을 때 나오는 글자 지정
  + width 속성 : 이미지의 너비 지정
  + height 속성 : 이미지의 높이 지정

+ audio, video 태그
  + src 속성 : 음악, 비디오의 경로 지정
  + preload 속성 : 음악, 비디오를 준비 중일 때 데이터를 모두 불러올지 여부를 지정
  + autoplay 속성 : 음악, 비디오의 자동 재생 여부 지정
  + loop 속성 : 음악, 비디오의 반복 여부 지정
  + controls 속성 : 음악, 비디오 재생 도구 출력 여부 지정

+ video 태그
  + width 속성 : 비디오의 너비 지정
  + height 속성 : 비디오의 높이 지정



멀티 미디어는 웹 브라우저의 버전에 따라 실행되지 않는 경우가 있다. 이는 웹 브라우저마다 지원하는 확장자의 형식이 다르기 때문에 나타나는 현상이다. 이는 source 태그를 audio 태그나 video 태그의 내부에 작성하는 것을 통해 해결할 수 있다. 또한 video 태그의 poster 속성을 이용하면 동영상을 불러오는 동안 사용자에게 보여 줄 이미지를 지정할 수 있다.

```html
<!-- 이미지 삽입 -->
<body>
    <img src="Penguins.jpg" alt="펭귄" width="300" />
    <img src="Nothing" alt="그림이 존재하지 않습니다." width="300" />
</body>

<!-- 오디오 삽입 -->
<body>
   <audio src="Kalimba.mp3" controls="controls"></audio>
</body>

<!-- 오디오 삽입[웹 브라우저 제약 없이] (type 입력으로 다운로드없이 재생 가능한지 확인 가능)-->
<body>
	<audio controls="controls">
        <source src="Kalimba.mp3" type="audio/mp3" />
        <source src="Kalimba.ogg" type="audio/ogg" />
	</audio>
</body>

<!-- 동영상 삽입[웹 브라우저 제약 없이] -->
<body>
    <video width="640" controls="controls">
        <source src="Wildlife.mp4" type="video/mp4" />
        <source src="Wildlife.webm" type="video/webm" />
    </video>
</body>

<!-- 동영상 삽입[poster] -->
<body>
    <video width="640" controls="controls" poster="이미지 경로">
        <source src="Wildlife.mp4" type="video/mp4" />
        <source src="Wildlife.webm" type="video/webm" />
    </video>
</body>
```



# 입력 양식 태그와 구조화 태그

## 입력 양식 태그

입력 양식은 사용자에게 정보를 입력받는 요소로 입력 양식 태그를 사용해 만든다. 회원가입 양식이 가장 대표적인 입력 양식이다. 입력 양식은 form 태그로 영역을 생성하고, 내부에 input 태그를 넣어 만든다.

form 태그는 method 속성으로 전송 방식을 지정하고, action 속성으로 해당 위치에 데이터를 전달한다.  method 속성에 입력해서 데이터를 전송할 때 가장 많이 사용하는 전송 방식은 get 방식과 post 방식이 있다. get 방식으로 데이터를 전달하면 주소에 데이터를 입력해서 전달하기 때문에 데이터 크기가 한정되어 있는 반면, post 방식은 주소가 변경되지 않고 비밀스럽게 데이터를 전달하기 때문에 데이터 용량에 대한 제한이 없다. 이 둘의 차이는 웹 브라우저의 주소창을 통해 URL을 보면 알 수 있다.

```html
<body>
    <form action="전송 위치" method="전송 방식">
        <input type="text" name="search">
        <input type="submit">
    </form>
</body>
```



HTML5에서는 input 태그에 type 속성을 지정해서 다양한 종류의 기본 입력 양식을 생성할 수 있다. input 태그는 form 태그 내부에 들어간다는 것을 기억하자. 또한 value 속성을 통해 보여지는 내용을 넣을 수도 있으며, name 속성을 통해 보여지는 파라미터의 이름을 설정할 수 있다. 라디오 버튼의 경우에는 여러 버튼을 같은 name속성으로 생성하게 되면, 여러 버튼 중 하나만을 선택하는 형태를 구현할 수 있다.

```html
<body>
    <form>
        <!-- 글자 입력 양식 -->
        <input type="text" name="text" value="text" /><br />
		<!-- 비밀번호 입력 양식 -->
        <input type="password" name="password" value="password" /><br />
		<!-- 파일 입력 양식 -->        
        <input type="file" name="file" value="file" /><br />
		<!-- 체크 박스 생성 -->        
        <input type="checkbox" name="checkbox" value="checkbox" /><br />
		<!-- 라디오 버튼 생성 -->        
        <input type="radio" name="radio" value="radio" /><br />
        <!-- 해당 내용 표시 안 함 -->
        <input type="hidden" name="hidden" value="hidden" /><br />
        <!-- 버튼 생성 -->
        <input type="button" value="button" /><br />
        <input type="reset" value="reset" /><br />
        <input type="submit" value="submit" /><br />
        <!-- 이미지 형태 생성 -->
        <input type="image" src="http://placehold.it/100x100" />
    </form>
</body>
```



Select 태그는 선택 가능한 입력 양식을  생성할 때 사용한다. 만약 2개 이상의 선택을 가능케 하고자 한다면 multiple 속성을 이용해야 한다. 또한 선택 가능한 옵션들을 labe 속성을 통해 그룹으로 묶을 수 있다. 

```html
<!-- 단일 선택 -->
<body>
    이 중 하나만 고르세요 <br />
    <select>
        <option>김밥</option>
        <option>떡볶이</option>
        <option>순대</option>
        <option>어묵</option>
    </select>
</body>

<!-- 다중 선택 -->
<body>
    먹고 싶은 건 다 고르세요 <br />
    <select multiple="multiple">
        <option>김밥</option>
        <option>떡볶이</option>
        <option>순대</option>
        <option>어묵</option>
    </select>
</body>

<!-- 선택옵션 그룹화 -->
<body>
    <select>
        <optgroup label="유럽">
            <option>영국</option>
            <option>프랑스</option>
            <option>이탈리아</option>
        </optgroup>
        <optgroup label="아시아">
            <option>대한민국</option>
            <option>호주</option>
        </optgroup>
    </select>
</body>
```



연관있는 입력 양식 그룹으로 묶기 위해서는 fieldset 태그를 사용하고, 그 내부에 legend 태그를 작성하여 만들어 낼 수 있다. 또한 여러 행의 글자를 입력하기 위한 양식은 textarea 태그로 생성 가능하다.

```html
<body>
    <form>
        <fieldset>
            <legend>입력 양식</legend>
            <table>
                <tr>
                    <td><label for="name">이름</label></td>
                    <td><input id="name" type="text" /></td>
                </tr>
                <tr>
                    <td><label for="mail">이메일</label></td>
                    <td><input id="mail" type="email" /></td>
                </tr>
            </table>
            <input type="submit" />
        </fieldset>
    </form>
    
	<!-- 여러 행의 글자 입력 양식 생성 [5줄 높이 30글자 너비]-->
        <textarea rows=5 cols=30></textarea>
</body>
```



## 구조화 태그

### 공간 분할 태그

웹 페이지는 레이아웃 구성을 위해 공간을 구분한다. HTML5의 대표적인 공간 분할 태그는 div 태그와 span 태그이다. dic 태그는 공간을 블록 형식으로 분할하고, span 태그는 인라인 형식으로 분할한다. div 태그와 span 태그를 적절하게 사용하는 것이 레이아웃 구성에 가장 중요한 요소이다.

div 태그를 사용해 공간을 분할하면 각 태그가 한 행 전체를 블록 형태로 모두 차지하게 된다.

span 태그를 사용해 공간은 분할하면 한 행 내에서도 span 태그 내 글자 크기만큼 영역으로 구분된다.



### 시맨틱 태그

HTML5의 가장 큰 변화는 시맨틱 태그이다. 시맨틱 태그를 사용해 각 태그에 의미를 부여하여 웹 페이지를 만드는 것이다.
