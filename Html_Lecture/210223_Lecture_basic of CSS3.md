# CSS3

HTMl 페이지에 CSS를 사용해 꾸밀 수 있다. CSS로 작성된 코드를 스타일시트라고 하며, CSS3까지 발전했다. CSS를 사용하면 위치를 지정하고, 색상을 추가하고, 텍스트를 이동하고, 블록 수준 요소에 대한 여백 및 테두리를 설정할 수 있다.

CSS3 작성의 형식은  `선택자 { 속성:속성값; }`으로 구성되어있다.



## 선택자

CSS3에서 특정 HTML 태그를 선택할 때는 선택자를 사용한다. 선택자를 통해 특정 HTML 태그를 선택하면, 선택한 태그에 원하는 스타일이나 스크립트를 적용할 수 있게 된다.  

CSS3 선택자의 종류는 다양하기 때문에 암기하는 것이 아니라 주요 선택자 위주로 계속 해서 사용하면서 차근차근 익숙해지도록 하는 것이 필요하다.

```html
<head>
  <title>CSS3 Selector Basic</title>
  <style>
    h1 {
      color: red;
      background-color: orange;
    }
  </style>
</head>
<body>
  <h1>CSS3 선택자 기본</h1>
</body>
```



### 기본 선택자

#### 전체 선택자

HTMl 페이지 내부의 태그를 모두 선택하는 선택자

```html
<head>
    <style>
   		* { color : red; }
	</style>
</head>    
<body>
    <h1>태그된 모든 것이 빨간색</h1>
    <h2>제목도 빨간색</h2>
    <P>본문도 빨간색</P>    
</body>
```



#### 태그 선택자 

HTML 페이지 내부의 특정 태그를 모두 선택하는 선택자

```html
<head>
    <style>
  		p { color:blue; }
  		h1,h2 { color:red; }
	</style>
</head>
<body>
    <h1>h1 제목은 빨간색</h1>
    <h2>h2 제목도 빨간색</h2>
    <P>본문은 파란색</P>    
</body>
```



#### 아이디 선택자 

특정 id 속성이 있는 태그 선택, 웹 표준에 id 속성은 웹 페이지 내부에서 중복되면 안 된다는 규정이 있으므로 아이디 선택자는 특정 태그 하나를 선택할 때 사용

> 스타일시트에서는 id 속성이 중복되어도 문제는 없지만, 자바 스크립트에 id 중복이 문제가 될 수 있기 때문에, 중복된 id 속성이라면 클래스로 그룹화를 하여 스타일을 지정해야 한다.

```html
<head>
	<style>
    	#header {
    	width:800px; margin: 0 auto;
        background: red;
    	}
	</style>
</head>
<body>
    <div id="header">
        <h1>ID가 header인 부분의 가로폭 800px, 배경 빨간색</h1>
    </div>
</body>
```



#### 클래스 선택자

특정 클래스가 있는 태그 선택

> 웹 페이지 내부에서 id 속성은 중복되지 않아야 하지만 class 속성은 중복될 수 있다.
>
> class 속성을 서로 다른 태그에 적용할 때는 태그 선택자와 클래스 선택자를 함께 사용하여 더 정확하게 태그를 선택할 수 있다.
>
> 또한 하나의 태그에 공백으로 구분하여 클래스를 여러 개 지정할 수도 있다.

```html
<head>
	<style>
    	li.red { color:red; }
        .favorite { background-color: blue; }
	</style>
</head>
<body>
    <h1 class="red">제목은 빨간색으로 나오지 않아</h1>
    <ul>
        <li class="red">사과</li>
        <li class="favorite">바나나</li>
        <li class="red favorite">딸기</li>
        <li>오렌지</li>
    </ul>
</body>
```



### 속성 선택자

```html
<head>
	<style>    
        input [type="text"] { background: red; }
        input [type="password"] { background: blue; }
    </style>    
</head>
<body>
    <h1>텍스트 속성의 배경색, 패스워드 속성의 배경색</h1>
    <form>
        <input type="text">
        <input type="password">
    </form>
</body>
```



### 후손·자손 선택자

#### 후손 선택자

```html
<head>
	<style>
		#header h1, #header h2 {color: red; }
	    #section h1, h2 {color: blue; }
    </style>
</head>
<body>
    <div id="header">
        <h1>빨간 큰 제목</h1>
        <h2>빨간 작은 제목</h2>
        <div id="nav">
            <h1>빨간 큰 제목2</h1>
        </div>
    </div>
    <div id="section">
        <h1>파란 큰 제목</h1>
        <h2>파란 작은 제목</h2>
    </div>
</body>
```



#### 자손 선택자

```html
<head>
	<style>
		#header > h1, #header > h2 {color: red; }
	    #section > h1, h2 {color: blue; }
    </style>
</head>
<body>
    <div id="header">
        <h1>빨간 큰 제목</h1>
        <h2>빨간 작은 제목</h2>
        <div id="nav">
            <h1>일반 큰 제목</h1>
            <h2>파란 작은 제목</h2>
        </div>
    </div>
    <div id="section">
        <h1>파란 큰 제목</h1>
        <h2>파란 작은 제목</h2>
    </div>
</body>
```

> Table 태그에 스타일을 적용할 때에는 자손 선택자를 사용하게 되면, 웹 브라우저가 tbody 태그를 자동으로 추가하게 되므로 스타일 속성이 적용되지 않는 경우가 있다. 따라서 Table 태그에는 자손 선택자를 이용하지 않는 것이 바람직하다.



### 반응·상태·구조 선택자

#### 반응 선택자

반응 선택자는 사용자 반응으로 생성되는 특정한 상태를 선택한다. 사용자가 특정 태그 위에 마우스 커를 올리면 hover 상태이고, 특정 태그를 마우스로 클릭하면 active 상태가 된다.

```html
<head>
	<style>
    	/* 마우스 커서를 올렸을 때 */
	    h1:hover { color : red;}
	    /* 마우스로 클릭했을 때 */
    	h1:active { color : bule;}
	</style>
</head>
<body>
    <h1>지금은 검은색, 마우스를 올리면 빨간색, 클릭하면 파란색</h1>
</body>
```



#### 상태 선택자

상태 선택자는 입력 양식의 상태를 선택할 때 사용한다.

```html
<head>
<style>
    /* input 체크된 상태의 태그에 
    background-color 속성에 black 키워드를 적용 */
    input:checked { background-color: black; }
	/* input 태그가 사용 가능할 경우에
    background-color 속성에 white 키워드를 적용 */
    input:enabled { background-color: white; }

    /* input 태그가 사용 불가능할 경우에
    background-color 속성에 gray 키워드를 적용 */
    input:disabled { background-color: gray; }

    /* input 태그에 초점이 맞추어진 경우에
    background-color 속성에 orange 키워드를 적용 */
    input:focus { background-color: orange; }
</style>
</head>

<body>
    <h2>라디오 버튼을 선택하면, 버튼 배경이 검정색</h2>
    <input type="radio"/>
    <h2>사용 가능한 입력창 배경이 흰색, 선택되면 주황색</h2>
    <input />
    <h2>사용 불가능한 입력창 배경은 회색</h2>
    <input disabled="disabled"/>
</body>
```



#### 구조 선택자

구조 선택자는 특정한 위치에 있는 태그를 선택할 때 사용한다. 구조 선택자를 사용할 때 주의해야할 사항으로는 형제관계에 있는 태그끼리의 순서를 의미한다는 것이다. 따라서 부모 태그가 다른 경우에는 순서에 영향을 받지 않기 때문에 구조 선택자를 효과적으로 사용할 수 없게 된다.

```html
<head>
    <title>CSS3 Selector Basic</title>
    <style>
        ul { overflow: hidden; }
        li {
            list-style: none;
            float:left; padding: 15px;
        }

        /* 첫번째로 등장하는 li 태그의 경계 일부를 둥글게 */
        li:first-child { border-radius: 10px 0 0 10px; }
        /* 마지막으로 등장하는 li 태그의 경계 일부를 둥글게 */        
        li:last-child { border-radius: 0 10px 10px 0; }

        /* 수열 2n에 해당하는 번째의 li 태그마다 배경색 지정 */
        li:nth-child(2n) { background-color: #FF0003; }
        /* 수열 2n+1에 해당하는 번째의 li 태그마다 배경색 지정 */        
        li:nth-child(2n+1) { background-color:#800000; }
    </style>
</head>
<body>
    <ul>
        <li>첫 번째</li>
        <li>두 번째</li>
        <li>세 번째</li>
        <li>네 번째</li>
        <li>다섯 번째</li>
        <li>여섯 번째</li>
        <li>일곱 번째</li>
    </ul>
</body>
```



## 속성 값 (CSS3 단위)

스타일 속성을 적용하려면 먼저 스타일 속성 값으로 입력할 수 있는 CSS3 단위를 알아야 한다. 스타일 값으로 입력할 수 있는 단위에는 키워드, 크기, 색상, URL이 있다. 속성별로 한가지 단위만 사용할 수 있는 것은 아니므로 스타일의 값의 단위 종류부터 알아보자.



### 키워드 단위

키워드는 W3C에서 미리 정의한 단어이다. 키워드를 스타일 값으로 입력하면 키워드에 해당하는 스타일이 자동으로 적용된다. 



### 크기 단위

크기는 CSS3에서 가장 많이 사용하는 단위이다. 종류에는 %, em, cm, mm, inch, px이 있다. 이 중에서 특히 %, em, px를 자주 사용한다.

```html
<head>
    <style>
        p:nth-child(1) { font-size: 50%; }
        p:nth-child(2) { font-size: 100%; }
        p:nth-child(3) { font-size: 150%; }
        p:nth-child(4) { font-size: 200%; }
    </style>
</head>
<body>
    <p>50% 크기</p>
    <p>100% 크기</p>
    <p>150% 크기</p>
    <p>200% 크기</p>
</body>
```

```html
<head>
    <style>
        p:nth-child(1) { font-size: 0.5em; }
        p:nth-child(2) { font-size: 1.0em; }
        p:nth-child(3) { font-size: 1.5em; }
        p:nth-child(4) { font-size: 2.0em; }
    </style>
</head>
<body>
    <p>50% 크기</p>
    <p>100% 크기</p>
    <p>150% 크기</p>
    <p>200% 크기</p>
</body>
```

```html
<head>
    <title>CSS3 Style Property Basic</title>
    <style>
        p:nth-child(1) { font-size: 8px; }
        p:nth-child(2) { font-size: 16px; }
        p:nth-child(3) { font-size: 24px; }
        p:nth-child(4) { font-size: 32px; }
    </style>
</head>
<body>
    <p>50% 크기</p>
    <p>100% 크기</p>
    <p>150% 크기</p>
    <p>200% 크기</p>
</body>
```



### 색상 단위

색상을 입력하는 가장 간단한 방법은 색상에 해당하는 영어 단어를 입력하는 것이다. 하지만 영어 단어로 표현할 수 있는 색상은 제한되어 있기 때문에 CSS3에서는 색상을 더 다양하게 표현할 수 있도록 색상 단위를 제공하고 있다.

색상 단위는 RGB 색상, RGBA 색상, HEX 코드가 있다.

```html
<!-- RGB 색상 -->
    <style>
        h1 { background-color : rgb(1, 128, 255); }
    </style>

<!-- RGBA 색상 [투명도가 추가되었으며, 0~1 값으로 지정] -->
    <style>
        h1 { background-color : rgba(1, 128, 255, 0.5); }
    </style>

<!-- HEX 코드 [# 6자리 16진수 색상조합] -->
    <style>
        h1 { background-color : #0094FF; }
    </style>
```



### URL 단위

이미지나 글꼴 파일을 불러올 때는 URL 단위를 사용한다.

```html
<!-- 이미지 파일과 HTML 파일이 같은 위치에 있는 경우 -->
<style>
    body { background-image: url('img.jpg'); }
</style>

<!-- 이미지 파일과 HTML 파일이 다른 위치에 있는 경우 -->
<style>
    body { background-image: url('FolderName/img.jpg'); }
</style>
```



## CSS3 속성

### 박스 속성

CSS에서는 각 요소가 박스라는 사각 영역을 생성하고, 이 영역이나 이것을 둘러싼 테두리에 크기, 색상, 위치 등과 관련한 속성을 지정함으로써 스타일을 변경한다. 따라서 박스 속성은 웹 페이지의 레이아웃을 구성할 때 가장 중요하다. margin 속성, border 속성, padding 속성, width 속성, height 속성을 모두 합쳐 박스 속성이라고 한다.

#### 박스 크기와 패딩 조정

```html
<head>
    <style>
        /* div 태그로 만든 박스의 너비 100px, 높이 50px */
        div {
            width: 100px; height: 50px;
            background-color: red;
        /* 테두리 20px, 테두리와 박스 사이 여백 30px, 바깥쪽 여백 10px */     
            border: 20px solid black;
            margin: 10px; padding: 30px;
        }
    </style>
</head>
<body>
    <div></div>
</body>
```



#### 박스 여백 조정

margin 속성과 padding 속성은 상하좌우를 각각 지정할 수 있다. 또한 값을 2개 입력하는 것으로 상하와 좌우로 묶어서 지정할 수도 있다.

```html
<head>
    <style>
        div {
            width: 100px; height: 100px;
            background-color: red;

            /* 바깥쪽 상단여백 10, 우측여백 20, 하단여백 30, 좌측여백 40 */
            margin: 10px 20px 30px 40px;
            /* 테두리와 박스 사이 상단여백 10, 우측여백 20, 하단여백 30, 좌측여백 40 */
            padding: 10px 20px 30px 40px;
        }
    </style>
</head>
<body>
    <div></div>
</body>
```

```html
<head>
    <style>
        div {
            width: 100px; height: 100px;
            background-color: red;

            /* 바깥쪽 상하여백 0, 좌우여백 30 */
            /* 테두리와 박스 사이 상하여백 0, 좌우여백 30 */
            margin: 0 30px; padding: 0 30px;
        }
    </style>
</head>
<body>
    <div></div>
</body>
```



#### 박스 테두리

박스에 테두리를 넣을 때는 두께, 형태, 색상에 해당하는 속성을 사용해야 한다. 테두리 두께는 border-width 속성을 사용하고, 테두리 형태는 border-style 속성을 사용하며, 테두리 색상은 border-color 속성을 사용한다. 하지만 속성을 개별적으로 입력하지 않고, border 속성만을 이용해 테두리의 두께, 형태, 색상을 한 번에 입력할 수도 있다. 또한 border 속성도 margin과 padding 처럼 상하좌우 속성을 각각 입력할 수도 있으며, border-radius 속성을 이용해 박스 테두리를 둥글게 만들 수도 있다.

```html
<head>
    <style>
        .box {
            /* 굵은 점선의 검정 테두리 지정 */
            border-width: thick;
            border-style: dashed;
            border-color: black;
            /* 위 세 줄을 이렇게 작성할 수도 있다.
            border thick, dashed, black; */
            
            /* 테두리 왼쪽 위부터 시계방향으로 둥글기 다르게 적용 */
            border-radius: 50px 40px 20px 10px;
        }
    </style>
</head>
<body>
    <div class="box">
        <h1>굵은 점선의 검정 테두리</h1>
    </div>
</body>
```



### 가시 속성

태그가 화면에 보이는 방식을 지정하는 속성으로 대표적으로 display 속성이 있다. CSS의 display 속성을 이용하면 박스를 인라인 형식, 블록 형식 그리고 인라인-블록 형식으로 설정할 수 있다.

```html
<head>
    <style>
        /* 태그가 화면에서 보이지 않게 된다.
        	즉, 대상 객체가 화면에 나타나지 않는다. */
        #box { display: none; }
    </style>
</head>
<body>
    <span>더미 객체</span>
    <div id="box">대상 객체</div>
    <span>더미 객체</span>
</body>
```

```html
<head>
    <title>Display</title>
    <style>
        /* 태그가 화면에 나타나게 되며,
         더미객체 대상객체 더미객체가 각각 한 줄씩, 총 세줄로 나타난다. */
        #box { display: block; }
    </style>
</head>
<body>
    <span>더미 객체</span>
    <div id="box">대상 객체</div>
    <span>더미 객체</span>
</body>
```

```html
<head>
    <title>Display</title>
    <style>
        /* 태그가 화면에 나타나게 되며,
         더미객체 대상객체 더미객체가 한 줄로 나타난다. */
        #box { display: inline; }
    </style>
</head>
<body>
    <span>더미 객체</span>
    <div id="box">대상 객체</div>
    <span>더미 객체</span>
</body>
```

```html
<head>
    <title>Display</title>
    <style>
        /* 태그가 화면에 나타나게 되며,
         더미객체 대상객체 더미객체가 한 줄로 나타난다. */
        #box { display: inline-block; }
    </style>
</head>
<body>
    <span>더미 객체</span>
    <div id="box">대상 객체</div>
    <span>더미 객체</span>
</body>
```

>  inline과 inline-block 키워드의 차이
>
> 두 키워드의 차이는 width, height, margin 속성을 사용했을 때 차이가 나타난다.
> inline 키워드의 경우에는 margin 속성만 좌우로 적용되고, 나머지는 적용이 되지 않는다.
> inline-block 키워드는 block 키워드처럼 width, height, margin 속성을 모두 적용할 수 있게 된다.



### 배경 속성

배경 이미지를 넣을 때는 background-image 속성을 사용한다. background-image 속성은 배경 이미지를 지정하는 속성으로 스타일 값에는 URL 단위나 그레이디언트를 입력한다. 배경 이미지 크기는 background-size 속성으로 조정하고 크기 단위나 키워드를 입력할 수 있다. 크기 단위로는 퍼센트를 많이 사용하는 편이다. 너비와 높이 값 2개를 입력할 수 있다.

CSS3부터는 배경 이미지를 여러 개 적용이 가능해졌다. 먼저 입력한 이미지(왼쪽)가 앞쪽에 위치한다.

```html
<style>
    body {
        background-image: url('Front.png'), url('Back.png');
        /* "전체 이미지"의 너비 100%, 높이 250px */            
        background-size: 100% 250px;
    }
</style>
```

> 너비와 높이에 띄어쓰기를 사용하는 것과 쉼표를 사용하는 것은 엄연히 다르다. 쉼표를 사용하게 되면 각 배경이 서로 다른 크기를 입력하는 것으로 인식하기 때문이다.



background-repeat 속성으로 배경 이미지의 반복 형태를 지정해줄 수 있다. 배경 이미지가 패턴처럼 반복되어 나타나는 것은 background-repeat의 속성의 기본 키워드가 repeat로 되어있기 때문이다. repeat를 입력하면 이미지를 패턴처럼 표시하고, repeat-x 또는 repeat-y를 입력하면 x축 방향 또는 y축 방향으로만 이미지가 반복된다.

background-attachment 속성을 통해 배경 이미지를 화면에 고정시킬 수 있다. background-attachment의 기본 키워드는 scroll으로 화면 스크롤에 따라 배경 이미지가 함께 이동하게 된다.

```html
<head>
    <style>
        body {
            background-color: #E7E7E8;
            background-image: url('BackgroundFront.png'), url('BackgroundBack.png');
            background-size: 100%;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: bottom;
        }
    </style>
</head>
```



### 글자 속성

#### 크기, 글꼴, 스타일 지정

글자 크기를 지정하는 font-size 속성에는 크기 단위나 키워드를 입력할 수 있다. 그리고 글꼴을 지정하는 font-family 속성에는 사용자 컴퓨터에 설치된 글꼴을 입력할 수 있다. 일반적으로 한 단어로 된 글꼴 이름은 따옴표를 사용하지 않지만 두 단어 이상으로 된 글꼴 이름은 따옴표를 사용하는 것을 추천한다. 또한 글꼴이 웹 페이지 사용자 컴퓨터에 없는 경우를 대비하여, font-family 속성을 여러 개 입력하는 것이 좋다. 

글자의 두께와 기울기는 font-style과 font-weight 속성으로 조정한다. font-style 속성은 글자의 스타일(기울기 등)을 지정하며, 키워드를 입력할 수 있다. font-weight 속성은 글자의 두께를 지정하며, 숫자나 키워드를 입력할 수 있다.

```html
<head>
    <style>
        .a { font-size: 32px; }
        .b { font-size: 2em; }
        .c { font-size: large; }
        .d { font-size: small; }
        
        body {
            font-family: '없는 글꼴', 'Times New Roman', Arial;
        	font-style: italic;
            font-weight: bold;
        }   
    </style>
</head>
<body>
    <h1>가장 큰 제목 32px</h1>
    <p class="a">32px의 내용</p>
    <p class="b">2배 크기(32px)의 내용</p>
    <p class="c">large 크기의 내용</p>
    <p class="d">small 크기의 내용</p> 
</body>
```

> HTML 페이지에서 p 태그의 기본 크기는 16px이고, h1 태그의 기본 크기는 32px이다.
>
> font-weight 속성에 400을 입력하는 일반 글자의 두께로 출력되고, 700을 입력하면 두껍게 출력된다.
>
> 모서리가 뾰족한 글자를 Serif 글꼴이라고 하며, 모서리가 네모진 글자를 Sans-serif 글꼴이라고 한다.



#### 정렬 지정

text-align 속성은 글자 정렬을 지정한다.

```html
<head>
    <style>
        .font_big { font-size: 2em; }
        .font_italic { font-style: italic; }
        .font_bold { font-weight: bold; }
        .font_center { text-align: center; }
        .font_right { text-align: right; }
    </style>
</head>
<body>
    <p class="font_big font_italic font_bold font_center">TITLE</p>
    <p class="font_bold font_right">2021.02.23</p>
    <p>TITLE 단락은 굵은, 32px, 이탤릭체로 가운데 정렬을 했다. 날짜 단락은 굵은 글꼴로 오른쪽 정렬을했다. 지금까지 글자 정렬을 지정하는 법을 배웠다. 글자 정렬을 위한 text-align 속성에는 여기서 사용한 center와 right 키워드를 포함해서 end, inherit, initial, justify, left, start, match-parent 등이 있다.</p>
</body>
```

> span 태그에는 text-align 속성이 적용되지 않는다. 왜냐하면 span 태그는 인라인 형태이므로 너비가 없기 때문이다.



#### 수직 중앙 정렬

현대 HTML 페이지는 문서보다 애플리케이션 형태로 많이 사용한다. 그래서 글자 높이를 지정하는 line-height 속성을 사용해 글자를 수직 중앙 정렬한다. CSS에는 block 속성이 있는 태그에 수직 정렬을 지정할 수 있는 스타일 속성이 없기 때문에 글자를 감싸는 박스의 높이와 크기가 같은 크기로 line-height 속성을 지정하면 수직 중앙 정렬이 가능해진다.

```html
<head>
    <style>
        .font_center { text-align: center; }

        .button {
            width: 150px;
            height: 70px;
            background-color: #FF6A00;
            border: 10px solid #FFFFFF;
        }

        .button > a {
            display: block;
            /* 버튼의 높이와 같은 값으로 line-height를 하면 수직중앙정렬 가능 */
            line-height: 70px;
        }
    </style>
</head>
<body>
    <div class="button">
        <a href="#" class="font_center">Click</a>
    </div>
</body>
```



#### 링크 글자의 밑줄 제거

a 태그에 href 속성을 지정하면 글자에 밑줄이 생기면서 파란색으로 변경된다. 하지만 일반 웹 페이지에는 링크에 밑줄이 없다. text-decoration 속성을 통해 밑줄을 제거했기 때문이다.

```html
<head>
	<style>
		a {text-decoration: none;}
    </style>    
</head>
<body>
    <a href="http://www.naver.com">네이버로 가는 밑줄 없는 링크</a>
</body>
```



### 위치 속성

요소 위치를 설정할 때는 X 좌표와 Y 좌표를 지정하는 절대 위치 좌표 방법과 요소를 입력한 순서에 따라 지정하는 상대 위치 좌표 방법이 있다. 

웹 브라우저는 웹 페이지에 나타난 순서대로 요소를 배치한다. 하지만 position 속성을 이용하면 원하는 위치에 요소를 배치할 수 있게 된다.  절대 위치 좌표를 사용하기 위해서는 position 속성의 absolute나 fixed 키워드를 입력하고, 상대 위치 좌표를 사용하기 위해서는 static이나 relative 키워드를 입력한다. static 키워드는 요소가 위에서 아래쪽으로, 왼쪽으로 오른쪽으로 순서에 맞게 배치된다. relative 키워드는 static 키워드로 초기 위치가 지정된 상태에서 상하좌우로 이동할 수 있게 된다.

그런데 position 속성만 사용하게 되면 웹 브라우저마다 출력 형태가 다를 수 있으므로 이를 통일시키기 위해서는 position 속성과 함께 스타일 속성도 같이 사용해주어야 한다. 그리고 요소 순서를 변경하고 싶을 때는 z-index 속성을 사용해야 한다.



#### absolute 키워드

```html
<head>
    <style>
        .box { 
            width: 100px; height: 100px;
			/* 절대위치
            이것만 작성하게 되면 웹 브라우저에 따라 다르게 나타날 수 있다.
            따라서 left 속성과 top 속성의 적용으로 box들의 위치를 정해주어야 한다.*/
            position: absolute;
        }
        .box:nth-child(1) {
            background-color: red;
            /* left 속성과, top 속성 적용 */
            left: 10px; top: 10px;
        }
        .box:nth-child(2) {
            background-color: green;
            /* left 속성과, top 속성 적용 */            
            left: 50px; top: 50px;
        }
        .box:nth-child(3) {
            background-color: blue;
            /* left 속성과, top 속성 적용 */            
            left: 90px; top: 90px;
        }
    </style>
</head>
<body>
    <div class="box"></div>
    <div class="box"></div>
    <div class="box"></div>
</body>
```



#### z-index 속성

겹쳐서 위치한 경우에, z-index 속성에 숫자를 입력하면 숫자가 클수록 앞에 위치하게 된다.



#### 위치 속성 공식

자손의 position 속성에 absolute 키워드를 적용하려면 부모에 height 속성을 입력한다. 이렇게 함으로써 부모 태그가 영역을 차지하게 만들 수 있기 때문이다.

자손의 position 속성에 absolute 키워드를 적용하려면 부모의 position 속성에 relative 키워드를 적용한다. 자손 태그가 부모 위치를 기준으로 절대 위치 좌표를 설정해야하기 때문이다.



#### 내용이 요소 크기를 벗어날 때 처리

overflow 속성은 내용이 요소 크기를 벗어나 모두 보여주기 어려울 때 어떻게 보여 줄지를 지정한다. overflow 속성을 이용하면 키워드를 입력해 벗어난 부분을 자른 것처럼 보이지 않게 하거나 스크롤바를 추가해 스크롤을 가능케 할 수 있다.

```css
/* div 바깥으로 나가게 되는 box들이 잘려 안보인다. */
body > div {
    width: 400px;
    height: 100px;
    border: 3px solid black
    position: relative;
    overflow: hidden;
}

/* div에 스크롤이 생긴다. */
body > div {
    width: 400px;
    height: 100px;
    border: 3px solid black    
    position: relative;
    overflow: scroll;
}
```

> overflow-x와 overflow-y 속성 적용하게 되면 특정한 방향으로만 스크롤을 생성할 수 있게 된다.



### 유동 속성

float 속성은 원래 유동적인 대상을 만들려고 개발했지만, 현대에는 웹 페이지의 레이아웃을 잡을 때 더 많이 사용하게 되었다. 보통 웹 브라우저 크기를 조정하면 텍스트나 그림의 위치가 변하는데, float 속성을 이용하면 태그를 오른쪽이나 왼쪽에 붙일 수 있다. 웹 브라우저 크기에 상관없이 공지 등을 일정한 위치에 고정할 때 적합하다.

```html
<body>
    <img src="img.jpg"/>
    <p>여기 img는 인라인 형식의 태그이고, p는 블록 형식의 태그이므로 이미지와 글자가 분리되어 나타난다. 이를 수정하기 위해서는 float 속성을 이용해 이미지와 글이 어우러진 형태를 만들어줘야한다.</p>
</body>
```

```html
<head>
    <style>
        img { float:left; }
    </style>
</head>
<body>
    <img src="img.jpg"/>
    <p>이렇게 float 속성을 적용하게 되면, 글자와 이미지가 상하로 분리되어 나타나지 않고, 글자 사이에 그림이 어우러지게 자리잡은 배치를 할 수 있게 된다.</p>
</body>
```



#### 수평 정렬

float 속성을 사용하면 태그를 수평으로 정렬할 수 있게 된다. float 속성을 사용해 수평 정렬을 해보자.

```html
<head>
    <style>
        .box {
            width: 100px;
            height: 100px;
            background-color: red;
            margin: 10px;
            padding: 10px;
            /* 태그를 왼쪽으로 붙여서 수평 정렬을 한다.
            1번 박스 2번 박스가 왼쪽 기준으로 나란히 나타난다.
            즉, 1번 박스가 가장 왼쪽에 붙어있다. */
            float: left;
    </style>
</head>
<body>
    <div class="box">1</div>
    <div class="box">2</div>
</body>
```

```html
<head>
    <style>
        .box {
            width: 100px;
            height: 100px;
            background-color: red;
            margin: 10px;
            padding: 10px;
             /* 태그를 오른쪽으로 붙여서 수평 정렬을 한다.
            2번 박스 1번 박스가 오른쪽 기준으로 나란히 나타난다.
            즉, 1번 박스가 가장 오른쪽에 붙어있다. */
            float: right;
        }
    </style>
</head>
<body>
    <div class="box">1</div>
    <div class="box">2</div>
</body>
```



### 그림자와 그레이디언트 속성

#### 그림자

그림자 속성에는 글자에 그림자를 부여하는 text-shadow 속성과 박스에 그림자를 부여하는 box-shadow 속성이 있다.

```html
<head>
    <style>
        div {
            border: 3px solid black;
            /* 가로 5px, 세로 5px, 흐림도 5px의 검은 글자 그림자 */
            text-shadow: 5px 5px 5px black;
            /* 가로 5px, 세로 10px, 흐림도 30px의 검은 상자 그림자 */
            box-shadow: 5px 10px 30px black;
        }
    </style>
</head>
<body>
    <div class="box">
        <h1>Lorem ipsum dolor amet</h1>
    </div>
</body>
```

쉼표를 사용하면 그림자 속성을 여러 개 적용하여 중첩 그림자를 만들 수 있다.

```css
.box {
	border: 3px solid black;
	box-shadow: 10px 10px 10px black, 10px 10px 20px orange, 10px 10px 30px red; 
	text-shadow: 10px 10px 10px black, 10px 10px 20px orange, 10px 10px 30px red; 
}
```



#### 그레이디언트

두 가지 이상의 색상을 혼합하는 채색 기능이다. 코드는 복잡하나 `Ultimate CSS Gradient Generator`를 통해 그레이디언트를 생성한 후 CSS 코드를 복사하여, 해당 코드에 붙여넣기를 통해 간편하게 이용할 수 있다.



## 다양한 레이아웃의 구성과 기능

### 정렬 레이아웃

#### 수평 정렬 레이아웃

자손에게 float 속성을 지정하고, 부모의 overflow 속성에는 hidden 키워드를 적용합니다.

```html
<head>
    <style>
        div.container {
            overflow: hidden;
        }

        div.item {
            float: left;
            margin: 0 3px;
            padding: 10px;
            border: 1px solid black; 
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="item">메뉴 - 1</div>
        <div class="item">메뉴 - 2</div>
        <div class="item">메뉴 - 3</div>
        <div class="item">메뉴 - 4</div>
    </div>
</body>
```



#### 중앙 정렬 레이아웃

중앙 정렬하고 싶은 태그에 width 속성을 부여하고 margin 속성을 '0 auto'로 입력하면, body 태그에 해당하는 제목과 본문이 중앙에 위치하게 된다.

```html
<head>
    <style>
        /* 초기화 */
        * { margin: 0; padding: 0; } 

        /* 주제 */
        body {
            margin: 0 auto;
            width: 700px;
        }
    </style>
</head>
<body>
    <h1>중앙 정렬 레이아웃</h1>
    <h2>레이아웃을 중앙에 정렬하는 방법</h2>
    <p>모든 태그이 margin과 padding을 0으로 초기화 한다. 그리고 본문의 너비를 지정하고, margin에 0 auto로 속성값을 주게 되면, 레이아웃 전체가 중앙으로 정렬된다. margin에 속성 값 0 auto를 기억하자. 마진에 속성 값 0 auto, margin에 속성 값 0 오토, 마진에 속성 값 영 오토, margin에 속성 값 0 auto.</p>
</body>
```



#### One True 레이아웃

One True 레이아웃의 형태는 국내 모든 포털 사이트의 메인 페이지의 구성 방식이다. One True 레이아웃의 기본 원리는 "행을 독립적으로 생각"해서 공간을 나눈다는 원리이다.

```html
<head>
    <style>
        body {
            width: 500px;
            margin: 10px auto;
        }

        #middle { overflow: hidden; }
        #left { float: left; width: 150px; background: red; }
        #right { float: right; width: 350px; background: blue; }

        #top { background: green; }
        #bottom { background: purple; }
    </style>
</head>
<body>
    <div id="top">One true 레이아웃의 top 부분이다. 부모 태그는 body이다. 부모 태그에 고정된 너비를 입력한다.</div>
    <div id="middle">
        <div id="left">One true 레이아웃의 middle이자 left 부분이다. 부모 태그는 middle이다. 수평정렬이 필요하기 때문에 부모 태그에 overflow 속성은 hidden이다. left와 right 너비의 합은 500px가 되어야 한다. float 속성도 </div>
        <div id="right">One true 레이아웃의 middle이자 right 부분이다. 부모 태그는 middle이다. 수평정렬이 필요하기 때문에 부모 태그에 overflow 속성은 hidden이다. left와 right 너비의 합은 500px가 되어야 한다.</div>
    </div>
    <div id="bottom">One true 레이아웃의 bottom 부분이다. 부모 태그는 body이다. 부모 태그에 고정된 너비를 입력한다. </div>
</body>
```



### 요소 배치

절대 위치를 사용한 요소 배치를 다시 정리해보고, 더 깊게 공부해보자.

> 자손의 position 속성에 absolute를 적용하려면 부모의 position 속성에 relative를 적용해야 한다.

> 자손의 position 속성에 absolute 키워드를 적용하려면 부모에 height 속성을 입력해야 한다.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Absolute Position</title>
    <style>
        #container {
            width: 500px; height: 300px;
            border: 3px solid black;
            overflow: hidden;
            position: relative;
        }

        .circle {
            position: absolute;
            width: 100px; height: 100px; 
            border-radius: 50% 50%;
        }

        #red {
            background: red;
            left: 20px; top: 20px;
        }
        #green {
            background: green;
            right: 20px; top: 20px;
        }
        #blue {
            background: blue;
            right: 20px; bottom: 20px;
        }
        #yellow {
            background: yellow;
            left: 20px; bottom: 20px;
        }
    </style>
</head>
<body>
    <h1>Dummy Text</h1>
    <div id="container">
        <div id="red" class="circle"></div>
        <div id="green" class="circle"></div>
        <div id="blue" class="circle"></div>
        <div id="yellow" class="circle"></div>
    </div>
    <h1>Dummy Text</h1>
</body>
</html>
```



#### 요소를 중앙에 배치

1. 요소를 화면 중앙에 배치하기 위해서는 중앙 정렬하려는 div 태그의 position 속성을 absolute로 지정한다.
2. left와 top의 속성을 모두 50%로 지정한다.
3. 중앙에 정렬하려는 div 태그의 margin-left 속성과 margin-top 속성에 음수를 입력하여,
   요소를 왼쪽 위로 끌어당겨 요소의 중심을 페이지 중앙으로 맞춘다.
   (여기서 입력하는 음수값은 div 태그 너비와 높이의 정확히 1/2이어야 한다.)

```html
<head>
    <title>Absolute Position</title>
    <style>
        * { margin: 0; padding: 0; }

        body { background: red; }
        #container {
            
            width: 500px; height: 250px;
            background: orange;
			/* 너비 500, 높이 250인 오렌지색 상자의
				위치를 좌측에서 50%, 상단에서 50% 떨어지게 하면,
            	왼쪽 상단의 꼭지점이 화면 정중앙에 위치하게 된다.
            
            	따라서 상자의 너비와 높이의 반만큼을 좌측상단으로 이동하면,
	 		   	상자가 화면의 정중앙에 위치할 수 있게 되는 것이다.*/
            position: absolute;
            left: 50%; top: 50%;
            margin-left: -250px;
            margin-top: -125px;
        }
    </style>
</head>
<body>
    <div id="container">
        <h1>요소의 중앙 배치</h1>
    </div>
</body>
```



#### 요소를 고정 위치에 배치

```html
<head>
    <style>
		/* 상단에 고정바 생성 */        
        .top_bar {
            background: red;

            position: fixed;
            left: 0; top: 0; right: 0;
            height: 50px;
        }
		/* 좌측에 고정바 생성 */        
        .left_bar {
            background: blue;

            position: fixed;
            left: 0; top: 50px; bottom: 0;
            width: 50px;
        }

		/* 생성된 고정바 크기만큼 이동 */        
        .container {
            margin-top: 50px;
            margin-left: 50px;
        }        
    </style>
</head>
<body>
    <div class="top_bar"></div>
    <div class="left_bar"></div>
    <div class="container">
        <p>상단과 왼쪽에 바를 만들었으니, 가운에 container가 margin-top과 margin-left로 자리를 양보해주는거다.</p>
    </div>
</body>
```



### 글자 생략

```html
<head>
    <style>
        h1, p {
            width: 300px;
        }

        .ellipsis {
            white-space: nowrap; /* 공백문자 있으면 줄바꿈 없이 한줄로 나오게 */
            overflow: hidden; /* 너비 300px 넘으면 내용 보이지 않게 */
            text-overflow: ellipsis; /* 글자가 넘으면 생략부호 ... 표시*/
        }
    </style>
</head>
<body>
    <h1 class="ellipsis">제목 너비 300px인데 여기서부턴 볼 수가 없다.</h1>
    <p class="ellipsis">내용 너비 300px. ellipsis 단어가 낯설지만 여기서부턴 볼 수가 없다.</p>
</body>
```



## 반응형 웹

반응형 웹은 웹 페이지 하나로도 데스크톱, 태블릿PC, 스마트폰에 맞게 디자인이 자동으로 반응해서 변경되는 웹 페이지를 의미한다. 화면 너비에 따라 웹 페이지의 레이아웃이 변경되어 출력되는 것도 반응형 웹의 일종이다.  반응형 웹 페이지는 미디어 쿼리(Media query)를 사용해 개발한다.



### 뷰포트 설정

meta 태그는 웹 페이지의 추가 정보를 제공할 때 사용한다. 다양한 기능이 있지만 대부분 서버와 연동해서 처리하는 경우가 많다. 여기서는 뷰포트(viewport)와 관련한 meta 태그 설정만 알아보자.

페이스북 모바일 페이지, 트위터 모바일 페이지, 네이버 모바일 페이지, 다음 모바일 페이지 등을 보면 title 태그 아래쪽에 meta 태그가 있다. 이것처럼 name 속성에 viewport가 입력된 meta 태그를 viewport meta 태그라고 한다.

```html
<meta name="viewport" content="user-scalabale=no,initial-scale=1,maxium-scale=1"
```

> viewport meta 태그에 입력할 수 있는 값들
>
> ​	width, height [화면의 너비, 높이]
> ​	initial-scale [초기 확대 비율]
> ​	user-scalable [확대 및 축소 가능 여부]
> ​	minimum-scale, maxium-scale [최소 축소, 최대 확대 비율]
> ​	target-densitydpi [DPI 지정]



```HTML
<head>
    <meta name="viewport" content="user-scalable=no,initial-scale=1" />
</head>
<body>
    <h1>Viewport Meta 태그 넣기 </h1>
    <p>스마트폰에서도 이제 정상적인 크기로 볼 수 있게 되었다. user-scalable을 no로 입력했으므로 확대와 축소를 할 수 없고, initial-scale을 1로 지정해서 초기 출력 크기를 기본값으로 설정되게 했다.</p>
</body>
```



### 미디어 쿼리 설정

웹 페이지가 표시되는 장치에 '반응'하도록 하여 반응형 웹을 구현할 수 있는데, 이때 사용하는 것이 미디어 쿼리이다. 미디어 쿼리는 두 가지 방법으로 사용할 수 있다. @media 규칙와 media 속성이다.

@규칙 이란 스타일시트 내부에서 특정한 규칙을 표현하는 데 사용하는 것이다. 보이는 것과 같이 @로 시작한다. 외부 스타일을 가져오는 @import 규칙, 글꼴을 추가로 정의하는 @font-face 규칙 등이 있다.

media 속성은 link 태그에 입력해서 해당 미디어 쿼리 조건에 맞는 장치에서만 CSS 파일을 불러올 때 사용한다.

```CSS
@media (미디어쿼리) {
    CSS 코드
}
```

```html
<link rel="stylesheet" href="파일 이름" media="미디어 쿼리"
```



### 반응형 웹 패턴

```html
<html>
<head>
    <meta name="viewport" content="user-scalable=no,initial-scale=1,maximum-scale=1" />
    <style>
        * { 
            margin:0; 
            padding: 0;
        }

        body {
            width: 960px;
            margin: 0 auto;
            overflow: hidden;
        }
        
        #menu {
            width: 260px;
            float: left;
        }

        #section {
            width: 700px;
            float: right;
        }

        li {
            list-style:none; 
        }

        @media screen and (max-width: 767px) {
            /* 스마트폰 사이즈에서는 전부 해제합니다. */
            body { width: auto }
            #menu { width: auto; float: none; }
            #section { width: auto; float: none; }
        }
    </style>
</head>
    
<body>
    <div id="section">
        <h1>반응형 웹 패턴</h1>
        <p>화면의 너비가 커졌을 때는 왼쪽에 메뉴가 있고, 오른쪽에 섹션이 생긴다. 그러나 모바일 화면처럼 너비가 좁은 상황은 다르다. 메뉴는 아래에 나타나고 섹션은 위에 생길 것이다. 다시 정리하자면, 지금 이 글을 읽고 있는 상황에서 메뉴가 아래에 보인다면 화면이 작은 것이고, 이 글 좌측에 메뉴가 있다면 넉넉한 화면에서 이 글을 읽고 있는 것이다.</p>
    </div>
    <div id="menu">
        <ul>
            <li>메뉴A</li>
            <li>메뉴B</li>
            <li>메뉴C</li>
        </ul>
    </div>
</body>
</html>
```