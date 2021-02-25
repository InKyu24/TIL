# jQuery 라이브러리

jQuery 라이브러리는 모든 웹 브라우저에서 동작하는 클라이언트용 자바스크립트 라이브러리이다. jQuery는 무료로 사용 가능한 오픈 소스 라이브러리로, 쉬운 문서 객체 모델과 관련한 처리 구현, 쉽고 일관된 이벤트 연결 구현, 쉬운 시각적 효과 구현, 쉬운 Ajax 응용 프로그램 개발을 목적으로 사용하게 된다.



## jQuery 라이브러리 설정

jQuery는 자바스크립트 라이브러리로 자바스크립트를 더욱 손쉽게 활용할 수 있게 한다. 일부 미세하게 처리해야 하는 부분을 제외하면 jQuery 라이브러리를 사용해 모든 웹 브라우저에서 같은 형태로 웹 페이지를 표시할 수 있다.

jQuery 라이브러리를 사용하려면 먼저 사용한 jQuery 라이브러리를 구해야 한다. jQuery 라이브러리는 두 가지 방법으로 사용할 수 있다.

첫 번째는 파일을 다운로드해서 외부 자바스크립트 파일로 추가하는 방법이다. http://jquery.com에 접속해 메인 페이지에서 `Downlad jQuery` 버튼을 누르면 다운로드할 수 있다.

두 번째 방법은 CDN 호스트를 사용하는 것이다. http://code.jquery.com/에 접속하면 jQuery 파일들이 있다. 원하는 파일에 해당하는 링크의 주소를 복사해서 사용할 수 있다. CDN는 jQuery를 비롯해 구글, MS 등에서도 제공한다. 원하는 회사의 링크를 복사해서 HTML 페이지를 작성한다.

>  CDN(Content Delivery Network)은 파일을 여러 서버에 분산시키고 사용자가 접속하는 지역과 가장 가까운 곳의 서버에서 파일을 전송하는 기술이다.  CDN을 사용하면 트래픽이 특정 서버에 집중되지 않고 각각의 지역 서버에 분산된다. 

두 번째 방법을 이용하여 jQuery 라이브러리를 설정하였다.

```html
<script src="http://code.jquery.com/jquery-3.1.0.js"></script>

<script>
    $(document).ready(function () {
    });
</script>
```

위의 코드 중에서 두 번째로 `<script>` 태그를 변형하면 아래와 같이 표현할 수 있다.

```html
<script src="http://code.jquery.com/jquery-3.1.0.js"></script>

<script>
    var a=$(document);
    function b() {
    }
    a.ready(b);
</script>
```

```html
<script src="http://code.jquery.com/jquery-3.1.0.js"></script>

<script>
    var a=$(document);
    a.ready(function () {
    });
</script>
```

그럼 계속해서 똑같이 표현되는 첫 번째 `<script>` 태그는 무엇인지 알아보자. 첫 번째 `<script>` 태그에서 작성된 링크는 `$` 표시와 연결하여, 선언된 변수 `var a` 에는 호출한 jQuery 객체가 할당되는 것이다.



## 문서 객체 선택

jQuery 라이브러리는 다음 형태로 사용된다.

`$(선택자).메서드(매개변수, 매개변수)`

자바스크립트는 식별자로 $와 _를 사용할 수 있었다. 따라서 $() 함수는 별도의 특별한 기능이 있는 것이 아니라 jQuery 라이브러리의 기본 함수인 jQuery()를 쉽게 사용할 수 있도록 대치하는 것이다.

```javascript
Window.jquery = window.$ = jQuery;
```

jQuery 라이브러리를 사용하면 훨씬 쉽게 문서 객체를 선택할 수 있다.  querySelector() 메서드와 달리 문서 객체 여러개를 한 번에 선택한다. 또 document.querySelectorAll() 메서드와 달리 반복문을 사용하지 않아도 된다.

```html
<head>
    <script src="http://code.jquery.com/jquery-3.4.1.js"> </script>
    <script>
		$(document).ready(function() {
            // 모든 h1 객체에 css 함수로 배경을 검정색으로 한다.
            $('h1').css('background','black') ;
            // 모든 h1 객체에 css 함수로 색상을 빨간색으로 한다.
            $('h1').css('color', 'red');
        });
    </script>
</head>
<body>
     <h1>header</h1>
     <h1>header</h1>
     <h1>header</h1>
</body>
```



```html
<head>
    <script src="http://code.jquery.com/jquery-3.4.1.js"> </script>
    <script>
		$(document).ready(function(){
            // id가 here인 객체에 css 함수로 배경을 검정색으로 한다.
            $('#here').css('background','black') ;
            // id가 here인 객체에 css 함수로 색상을 빨간색으로 한다.
            $('#here').css('color', 'red');
        });
    </script>
</head>
<body>
     <h1 id="here">header</h1>
</body>
```



## 문서 객체 조작

jQuery 라이브러리를 사용하면 문서 객체도 쉽게 조작할 수 있다. 문서 객체 조작하는 메서드의 사용 방법은 비슷하기 때문에 속성 조작 메서드 위주로 살펴보자.



### 속성 조작

jQuery 라이브러리를 사용해서 문서 객체 속성을 조작할 때는 attr() 메서드를 사용한다. attr() 메서드는 매개변수를 넣는 방법에 따라 속성을 지정하거나 추출할 수 있다.



#### 속성 추출

아래 코드와 같은 attr() 메서드에 매개변수를 하나 입력하면 해당 속성을 추출한다. jQuery 라이브러리는 문서 객체 여러 개를 한 번에 선택한다. 문서 객체 여러 개를 선택하고 속성을 추출하면, 가장 첫 번째 문서 객체 속성을 추출한다.

```javascript
// img 태그의 경로가 선언된 변수 src에 할당된다.
var src = $('img').attr('src');
```



```html
<head>
    <script src="http://code.jquery.com/jquery-3.1.0.js"></script>
    <script>
        $(document).ready(function () {
            // id가 here인 객체의 배경을 검은색으로 한다.
			$('#here').css('background', 'black');
            // 모든 h1 객체의 글꼴 색상을 빨간색으로 한다.
            $('h1').css('color', 'red');
            // 모든 img 객체의 이미지의 경로를 "funny.jpg"로 변경한다.
            $('img').attr('src', "funny.jpg");
            // 가장 첫 번째 img 객체의 속성을 추출하여, console log에 출력한다.
            var s = $('img').attr('src');
            console.log(s);
        });
    </script>
</head>
<body>
    <h1 id="here">header</h1>       
	<img src="baby.png">
</body>
```



#### 속성 지정

문서 객체 속성은 세 가지 방법으로 지정할 수 있다. 속성 값을 입력해 지정하는 방법과 객체를 입력해 속성을 지정하는 방법, 그리고 함수를 이용해 속성을 지정하는 방법이 있다. 

##### 속성 값을 입력해 속성 지정

attr() 메서드의 첫 번째 매개변수에 속성 이름을 입력하고, 두 번째 매개변수에 속성 값을 입력한다.

```javascript
$('img').attr('src', 'http://placehold.it/300x200');
```

```html
<head>
    <script src="http://code.jquery.com/jquery-3.1.0.js"></script>
    <script>
        // 이벤트 연결
        $(document).ready(function () {
            // 속성 지정
            // 모든 이미지 객체에 alt 속성을 지정 [이미지가 안나올 때 '속성 지정' 문구 출력]
            $('img').attr('alt', '속성 지정');
            // 모든 이미지 객체에 경로를 지정
            $('img').attr('src', 'http://placehold.it/100x100');
            // 모든 이미지 객체에 너비를 100으로 지정
            $('img').attr('width', '100');
        });
    </script>
</head>
<body>
    <img />
    <img />
    <img />
</body>
```



##### 객체를 입력해 속성 지정

attr() 메서드의 매개변수에 객체를 넣는다.

```javascript
$('img').attr({
	src: 'http://placehold.it/300x200',
	width: 300,
	height: 200
});
```

```html
<head>
    <script src="http://code.jquery.com/jquery-3.1.0.js"></script>
    <script>
        // 이벤트 연결
        $(document).ready(function () {
            // 속성 지정
            // 모든 img 객체에 객체를 입력해 속성을 지정
            // 객체는 { }로 선언!
            $('img').attr({
                alt: 'jQuery 라이브러리를 사용한 속성 지정',
                src: 'http://placehold.it/100x100',
                width: 100
            });
        });
    </script>
</head>
<body>
    <img />
    <img />
    <img />
</body>
```



##### 함수를 이용해 속성 지정

attr() 메서드의 첫 번째 매개변수에 속성 이름을 입력하고, 두 번째 매개변수에는 함수를 입력한다. 두 번째 매개변수에 함수를 입력하면 해당 콜백 함수의 매개변수로 문서 객체의 인덱스를 차례대로 전달한다.

아래 두 코드를 보자. src 속성에 함수를 지정하면 콜백 함수에 index 객체가 순서대로 지정되고, 반환 값을 속성에 적용한다. 콜백 함수가 호출될수록 가로가 길어지는 형태가 된다.

```javascript
$('img').attr('src', function (index) {
	var size = (index+1)*100;
    return 'http://placehold.it/' +size+ 'x100'; 
});
```

```html
<head>
    <script src="http://code.jquery.com/jquery-3.1.0.js"></script>
    <script>
        // 이벤트 연결
        $(document).ready(function () {
            // 속성 지정
            // 객체를 이용하여 alt 속성 및 속성 값 지정
            // 객체를 이용하여 src 속성 지정 및 함수를 이용한 속성 값 지정
            $('img').attr({
                alt: 'jQuery 라이브러리를 사용한 속성 지정',
                src: function (index) {
                    // 변수 선언
                    var size = (index + 1) * 100;

                    // 리턴
                    return 'http://placehold.it/' + size + 'x100';

                    // 첫 번째 img는 index가 0, 
                    // 두 번째 img는 index가 1, 
                    // 세 번째 img는 index가 2
                    
                }
            });
        });
    </script>
</head>
<body>
    <img />
    <img />
    <img />
</body>
```



>메서드 체이닝(Method Chaining)
>
>jQuery 라이브러리에서 문서 객체를 조작하는 메서드는 호출 이후에 자기 자신을 다시 반환한다. 따라서 $() 함수를 여러 번 사용할 필요 없이 메서드를 연속해서 사용할 수 있다.
>아래와 같이 메서드를 사용하는 것을 메서드 체이닝이라고 한다. 메서드가 사슬처럼 연결되어 작성되는 것처럼 보인다. 메서드 체이닝은 jQuery 라이브러리뿐만 아니라 다양한 곳에서 활용되므로 기억하자.
>
>```html
><head>
><script src="http://code.jquery.com/jquery-3.1.0.js"></script>
><script>
>   // 이벤트 연결
>   $(document).ready(function () {
>       // 메서드 체이닝을 통한 속성 지정
>       $('img').attr('alt', 'jQuery 라이브러리를 사용한 속성 지정').attr('src', 'http://placehold.it/100x100').attr('width', '100');
>   });
></script>
></head>
><body>
><img />
><img />
><img />
></body>
>```



### 스타일 조작

jQuery 라이브러리를 사용해 스타일을 조작할 때는 css() 메서드를 사용한다. css() 메서드는 attr() 메서드와 같은 방법으로 사용한다. 하지만 속성과 달리 하이픈(-)이 들어가는 스타일 속성은 아래 두 가지 방법으로 입력해야 한다.

```javascript
$('body').css('backgroundColor');
```

```javascript
$('body').css('background-color');
```



##### 속성 값을 입력해 스타일 속성 지정

css() 메서드의 두 번째 매개변수에 속성 값을 입력해서 태그의 스타일 속성을 조작한다.

```html
<head>
    <script src="http://code.jquery.com/jquery-3.1.0.js"></script>
    <script>
        $(document).ready(function () {
            // 모든 box 클래스에 float 적용
            $('.box').css('float', 'left');
            // 모든 box 클래스에 margin 적용            
            $('.box').css('margin', 10);
            // 모든 box 클래스에 width 적용            
            $('.box').css('width', 100);
            // 모든 box 클래스에 height 적용            
            $('.box').css('height', 100);
            // 모든 box 클래스에 float 적용            
            $('.box').css('backgroundColor', 'red');
        });
    </script>
</head>
<body>
    <div class="box"></div>
    <div class="box"></div>
    <div class="box"></div>
</body>
```



##### 객체를 입력해 스타일 속성 지정

css() 메서드의 매개변수에 객체를 넣은 후 코드 형태로도 스타일을 조작할 수 있다.

```html
<head>
    <script src="http://code.jquery.com/jquery-3.1.0.js"></script>
    <script>
        $(document).ready(function () {
            // 모든 box 클래스에 객체를 입력해 스타일 적용
            $('.box').css({
                float: 'left',
                margin: 10,
                width: 100,
                height: 100,
                backgroundColor: 'red'
            });
        });
    </script>
</head>
<body>
    <div class="box"></div>
    <div class="box"></div>
    <div class="box"></div>
</body>
```



##### 함수를 이용해 스타일 속성 지정

스타일 속성에 함수를 지정하면 콜백 함수에 객체가 지정되고, 반환 값을 속성에 적용하게 된다.

```html
<head>
    <script src="http://code.jquery.com/jquery-3.1.0.js"></script>
    <script>
        $(document).ready(function () {
            // 문서 객체 추가 [innerHTML 속성으로 div 태그가 256개 추가된다]
            var output = '';
            for (var i = 0; i < 256; i++) {
                output += '<div></div>';
            }
            document.body.innerHTML = output;

            // 모든 div 객체에 스타일 height 적용, 함수를 이용해 배경색 적용
            // [각 rgb 색상이 0부터 255까지 순차적으로 증가]
            $('div').css({
                height: 2,
                backgroundColor: function (i) {
                    return 'rgb(' + i + ',' + i + ',' + i + ')';
                }
            });
        });
    </script>
</head>
<body>
</body>
```



### 글자 조작

jQuery 라이브러리로 문서 객체 내부의 글자를 조작할 때는 html() 이나 text() 와 같은 메서드를 사용한다.

+ html() 메서드 : 문서 객체 내부의 HTML 태그 조작
+ text() 메서드 : 문서 객체 내부의 글자 조작

> 이전에 배운 innerHTML 속성과 textContent 속성을 기억한다면 메서드가 왜 2개인지 이해할 수 있을 것이다.



#### 문서 객체 글자 조작

##### text() 메서드로 내부 글자 조작

```html
<head>
    <script src="http://code.jquery.com/jquery-3.1.0.js"></script>
    <script>
        $(document).ready(function () {
            // 내부 글자 변경
            // h1의 첫번째 객체의 텍스트를 <a href="#">text()</a>으로 변경 [일반 글자처럼 출력]
            $('h1:nth-child(1)').text('<a href="#">text()</a>');
            // h1의 두번째 객체의 텍스트를 <a href="#">html()</a>으로 변경 [글자에 태그를 적용]
            $('h1:nth-child(2)').html('<a href="#">html()</a>');
        });
    </script>
</head>
<body>
    <h1>Header - 0</h1>
    <h1>Header - 1</h1>
</body>
```



##### html() 메서드로 내부 글자 조작

```html
<head>
    <script src="http://code.jquery.com/jquery-3.1.0.js"></script>
    <script>
        $(document).ready(function () {
            // 변수 선언
            // 모든 h1 객체의 글자를 추출 [Header - 0Header - 1]
            var text = $('h1').text();
            // 첫 번째 h1 객체의 글자를 추출 [Header - 1]
            var html = $('h1').html();

            // 출력
            // [text: Header - 0Header - 1]
            alert("text: " + text);
            // [html: Header - 1]
            alert("html: " + html);
        });
    </script>
</head>
<body>
    <h1>Header - 0</h1>
    <h1>Header - 1</h1>
</body>
```



### 클래스 조작

문서 객체의 class 속성 값을 다음 코드와 같이 띄어쓰기로 구분해 여러 개  입력할 수 있다.

```html
<p class="bold big italic">굵고 큰 이탤릭체</p>
```

클래스를 하나 추가하고 제거하는데 attr() 메서드를 사용한다면 문자열 연산을 수행해야 하기 때문에 번거롭다. 그래서 jQuery 라이브러리에서는 이런 귀찮은 일들을 줄이고자 클래스 조작 메서드를 별도로 제공하고 있다. 클래스를 조작할 때는 addClass(), removeClass(), toggleClass()와 같은 메서드를 사용한다.

> toggleClass() : 클래스 전환

클래스 조작에 사용되는 메서드는 간단한 메서드이다. 아래 코드에서 사용되는 hover() 메서드는 첫 번째 매개변수에 마우스 커서를 올렸을 때 실행할 것을 입력하고, 두 번째 매개변수에 마우스 커서를 내렸을 때 실행할 것을 입력한다. 코드를 실행하고 마우스 커서를 div 태그로 만든 도형 위에 올리거나 내리면 class 속성이 바뀌어 모양이 변하는 것을 알 수 있다.

```html
<head>
    <style>
        /* id가 박스인 객체에 스타일 적용 [빨간 정사각형] */
        #box {
            width: 100px; height: 100px;
            background-color: red;
        }
        /* id가 박스인 객체의 hover 클래스에 스타일 적용 [파란 동그라미] */        
        #box.hover {
            background-color: blue;
            border-radius: 50px;
        }
    </style>
    <script src="http://code.jquery.com/jquery-3.1.0.js"></script>
    <script>
        $(document).ready(function () {
            $('#box').hover(function () {
                // [마우스 커서를 올렸을 때의 실행] id가 박스인 객체에 hover 클래스 추가
                $('#box').addClass('hover');
            }, function () {
                // [마우스 커서를 내렸을 때의 실행] id가 박스인 객체에 hover 클래스 제거
                $('#box').removeClass('hover');
            });
        });
    </script>
</head>
<body>
    <div id="box"></div>
</body>
```



## 이벤트

순수하게 자바스크립트만 사용해 이벤트를 연결하는 방법을 배웠다면 이번에는 jQuery 라이브러리를 사용해 손쉽게 이벤트를 생성해보려 한다. jQuery 라이브러리를 통한 이벤트는 모든 웹 브라우저에서 동작한다.



### 이벤트 연결

jQuery 라이브러리로 웹 페이지를 작성할 때는 항상 아래와 같은 코드를 작성했다.

```javascript
// 이벤트 연결
$(document).ready(function (){ 
});
```

여기서 ready()는 간단한 이벤트 연결 메서드이다. ready() 메서드를 사용하면 ready 이벤트(문서 객체 준비 완료)가 연결된다. ready 이벤트 이외에도 jQuery 라이브러리는 다양하고 간단한 이벤트 연결 메서드를 제공하고 있다.

> 간단한 이벤트 연결 메서드
>
> blur	focus	focusin	focusout	load
> resize	scroll	unload	click	dbclick
> mousedown	mouseup	mousemove	mouseover	mouseout
> mouseenter	mouseleave	change	select	submit
> keydown	keypress	keyup	error	ready

간단한 방식으로 이벤트를 연결할 때는 다음 코드를 사용한다.

```javascript
$(selector).method(function (event) { });
```



#### click 이벤트 연결

```html
<head>
    <script src="http://code.jquery.com/jquery-3.1.0.js"></script>
    <script>
        // 이벤트 연결
        $(document).ready(function () {
            // 이벤트 연결 [모든 h1 객체를 클릭하면 경고 창이 출력되도록]
            $('h1').click(function () {
                alert('클릭!');
            });
        });
    </script>
</head>
<body>
    <h1>Click</h1>
</body>
```



#### 복합 이벤트 연결 메서드

```html
<head>
    <script src="http://code.jquery.com/jquery-3.1.0.js"></script>
    <script>
        // 이벤트 연결
        $(document).ready(function () {
            // 이벤트 연결
            $('h1').hover(function () {
                // 색상 변경
                $(this).css({
                    background: 'red',
                    color: 'white'
                });
            }, function () {
                // 색상 제거
                $(this).css({
                    background: '',
                    color: ''
                });
            });
        });
    </script>
</head>
<body>
    <h1>Click</h1>
</body>
```



### 이벤트 사용

jQuery 라이브러리로 일반 이벤트를 연결할 때는 on() 메서드를 사용하고, 이벤트를 제거할 때는 off() 메서드를 사용한다.

사용자 정의 이벤트 또는 새로 나왔지만 아직 업데이트를 못한 이벤트는 반드시 on() 메서드를 사용해서 아래 형식으로 연결해야 한다.



#### 일반 이벤트 연결

```javascript
$(selector).on(eventName, eventHandler);
```

```html
<head>
    <script src="http://code.jquery.com/jquery-3.1.0.js"></script>
    <script>
        $(document).ready(function (){
	        $('#box').css({
    	        width: 100,
        	    height: 100,
            	background: 'orange'
	        }).on('click',function() {
    	        $(this).css('background','red');
        	}).on('mouseenter',function(){
                $(this).css('background','blue');
        	}).on('mouseleave',function(){
                $(this).css('background','orange');
            });
		});
    </script> 
</head>
<body>
    <div id="box"></div>
</body>
```





```javascript
$(selector).on({
    eventName_0: eventHandler_0,
    eventName_1: eventHandler_1,
    eventName_2: eventHandler_2
});
```

```html
<head>
    <title>jQuery Basic</title>
    <script src="http://code.jquery.com/jquery-3.1.0.js"></script>
    <script>
        $(document).ready(function () {
            // 스타일 변경 및 이벤트를 연결
            $('#box').css({
                width: 100,
                height: 100,
                background: 'orange'
            }).on({
                click: function () {
                    $(this).css('background', 'red');
                },
                mouseenter: function () {
                    $(this).css('background', 'blue');
                },
                mouseleave: function () {
                    $(this).css('background', 'orange');
                }
            });
        });
    </script>
</head>
<body>
    <div id="box"></div>
</body>
```



jQuery 라이브러리를 이용하면 모든 웹 브라우저에서 같은 방법으로 이벤트 객체를 사용할 수 있다. jQuery 라이브러리는 다음 코드와 같이 이벤트 리스너의 매개변수를 사용해 이벤트 객체를 전달한다.

```javascript
$('h1').click(function (event) {
    
});
```



#### 기본 이벤트 제거

이벤트 객체의 preventDefalut() 메서드를 사용하면 문서 객체의 기본 이벤트를 제거한다.

```html
<head>
    <title>Event Basic</title>
    <script src="http://code.jquery.com/jquery-3.1.0.js"></script>
    <script>
        // 이벤트 연결
        $(document).ready(function () {
            // 이벤트 연결
            $('a').click(function (event) {
                // 출력
                alert('click');

                // 기본 이벤트 제거
                event.preventDefault();
            });
        });
    </script>
</head>
<body>
    <a href="http://google.co.kr">본 링크는 구글로 가는 이벤트 제거됨. 경고 창 출력함.</a>
</body>
```



> 기본 이벤트 제거를 활용한 유효성 검사
>
> ```html
> <head>
>     <script src="http://code.jquery.com/jquery-3.1.0.js"></script>
>     <script>
>         // 이벤트 연결
>         $(document).ready(function () {
>             // 이벤트 연결
>             $('form').submit(function (event) {
>                 // input 태그 값을 추출
>                 var value = $('input').val();
> 
>                 // 유효성 검사
>                 if (value.replace(/[가-힣]/g, '').length == 0) {
>                     // 유효성 검사 통과 시
>                     alert('과정을 진행합니다.');
>                 } else {
>                     // 유효성 검사 실패 시
>                     alert('한글 이름을 입력해주세요.');
>                     event.preventDefault();
>                 }
>             });
>         });
>     </script>
> </head>
> <body>
>     <form>
>         <label>이름</label>
>         <input type="text" />
>         <input type="submit" />
>     </form>
> </body>
> ```



# 자바스크립트와 jQuery 라이브러리 응용

## 입력 양식 포커스

인터넷 웹 사이트의 회원가입 양식에서 주민등록번호 또는 전화번호를 입력할 때 앞자리를 입력하자마자 자동으로 뒷자리를 입력하는 칸으로 이동하는 것은 첫 번째 입력 양식에 여섯 번째 글자를 입력하는 자동으로 두 번째 입력 양식에 포커스가 맞추어지도록 자바스크립트를 사용했기 때문이다.

```html
<head>
    <title>Event</title>
    <script>
        // 이벤트 연결
        window.onload = function () {
            // 문서 객체 선택
            var input_1 = document.querySelectorAll('input')[0];
            var input_2 = document.querySelectorAll('input')[1];
            
            // input_1
            input_1.onkeydown = function () {
                // 글자 개수가 여섯 개 이상일 경우
                if (6 <= input_1.value.length) {
                    // input_2 문서 객체로 초점을 이동
                    input_2.focus();
                }
            };
            // input_2
            input_2.onkeydown = function (event) {
                // 이벤트 객체 추출
                var event = event || window.event;
                // 사용자의 입력이 '백 스페이스'이고 입력된 글자가 없는 경우
                if (event.keyCode == 8 && input_2.value.length == 0) {
                    input_1.focus();
                }
            };
        };
    </script>
</head>
<body>
    <input type="text" maxlength="6" />
    <span>-</span>
    <input type="text" maxlength="7" />
</body>
```

> KeyCode 확인
>
> ```html
> window.onload = function () {
> 	window.onkeydown = function (event) {
> 		alert(event.keyCode);
> 	};
> };
> ```



## 문서 객체 생성과 추가

순수하게 자바스크립트만 사용해 문서 객체를 생성하면 매우 복잡하다. 하지만 jQuery 라이브러리를 사용하면 문서 객체를 쉽게 생성할 수 있다. 그리고 생성한 문서 객체는 `jQuery 문서 객체 추가 메서드`를 사용해 화면에 추가한다. prependTo() 메서드와 appendTo() 메서드는 대상의 내부에 추가되며, beforeTo() 메서드와 afterTo() 메서드는 대상의 외부에 추가된다는 것에 유의하자.

> $(객체).pretendTo(대상) : 객체를 대상의 앞부분에 추가
> $(대상).pretend(객체)
>
> $(객체).appendTo(대상) : 객체를 대상의 뒷부분에 추가
> $(대상).append(객체)
>
> $(객체).beforeTo(대상) : 객체를 대상의 앞쪽에 추가
> $(대상).before(객체)
>
> $(객체).afterTo(대상): 객체를 대상의 뒤쪽에 추가
> $(대상).after(객체)



#### 문서 객체 생성

```html
<head>
    <script src="http://code.jquery.com/jquery-3.1.0.js"> </script>
    <script>
        // 이벤트 연결.
        $(document).ready(function () {
            // 문서 객체 생성
            $('<h1>Create Document Object By jQuery</h1>')
        });
    </script>
</head>
<body>
</body>
```



#### appendTo() 메서드를 사용한 문서 객체 추가

```html
<head>
    <script src="http://code.jquery.com/jquery-3.1.0.js"></script>
    <script>
        // 이벤트 연결
        $(document).ready(function () {
            // 10회 반복
            for (var i = 0; i < 10; i++) {
                // 문서 객체 생성 및 스타일 지정
                $('<h1>Create Document Object + ' + i + '</h1>').css({
                    backgroundColor: 'black',
                    color: 'red'  
                }).appendTo('body');
            }
        });
    </script>
</head>
<body>

</body>
```

```html
<head>
    <script src="http://code.jquery.com/jquery-3.1.0.js"></script>
    <script>
        // 이벤트 연결
        $(document).ready(function () {
            // 10회 반복
            for (var i = 0; i < 10; i++) {
                // 문서 객체 생성
                var $dynamic = $('<h1>Create Document Object + ' + i + '</h1>').css({
                        backgroundColor: 'black',
                        color: 'red'
                    });
                
                // 문서 객체 추가
                $('body').append($dynamic);
            }
        });
    </script>
</head>
<body>

</body>
```