# JavaScript

자바스크립트는 자유롭고 기능과 기술이 다양한 프로그래밍 언어지만, 자바스크립드 기능과 실제 사용하는 기능 사이의 괴리가 매우 크다.



## 자바스크립트 기본 용어

### 표현식과 문장

표현식(Expression)은 값을 만들어 내는 간단한 코드이다. 문장(Statement)은 프로그래밍 언어에 실행할 수 있는 코드의 최소 단위이다. 문장 마지막에 세미콜론(;) 또는 줄 바꿈을 넣어 종결을 나타낸다. 표현식 하나도 세미콜론을 찍으면 문장이 되고, 문장이 모이면 프로그램이 된다.

```javascript
// 표현식의 예시
273;
10 + 20 + 30 * 2;
var name = '최' + '인' + '규';
alert('Hello JavaScript');

// 문장의 예시
273
10 + 20 + 30 * 2
'JavaScript'
```



### 키워드

키워드는 자바스클비트를 처음 만들 때 정해진 특별한 의미가 부여된 단어이다. 현재 대부분의 웹 브라우저에서는 아래와 같은 30가지의 자바스크립트 키워드를 지원하고 있다.

> break	else	instanceof	true	case	false
> new	try	catch	finally	null	typeof
> continue	for	return	var	default	function
> switch	void	delete	if	this	while
> do	in	throw	with	const	class



### 식별자

식별자는 자바스크립트에서 변수나 함수 등에 이름을 붙일 때 사용하는 단어이다. 식별자 생성에는 몇 가지 규칙과 관례가 있다.

> 전 세계 언어를 모두 사용할 수 있지만, 알파벳을 사용하는 것이 개발자들 사이에서의 관례이다.
> 식별자에 키워드를 사용하면 안 된다.
> 특수 문자는 _와 $만 허용한다.
> 숫자로 시작하면 안 된다.
> 공백은 입력하면 안된다.
>
> 생성자 함수 이름은 항상 대문자로 시작한다.
> 변수, 인스턴스, 함수, 메서드의 이름은 항상 소문자로 시작한다.
> 여러 단어로 된 식별자는 각 단어의 첫 글자를 대문자로 한다.

자바스크립트에서 사용하는 주요 식별자로는 변수, 속성, 함수, 메서드가 있다.

변수는 값을 저장할 때 사용하는 식별자이고, 속성은 객체에 소속된 변수이다. 함수는 코드의 집합으로 변수의 일종이다. 메서드는 객체에 소속된 함수이다.

> 변수 : 식별자 뒤에 괄호가 없고, 단독으로 사용 가능하다.
> 속성 : 식별자 뒤에 괄호가 없고, 다른 식별자와 함께 사용한다. (`.`이 있다.)
> 함수 : 식별자 뒤에 괄호가 있고, 단독으로 사용 가능하다.
> 메서드 : 식별자 뒤에 괄호가 있고, 다른 식별자와 함께 사용한다. (`.`이 있다.)

```javascript
input						// 변수
Array.length				// 속성
Math.PI						// 속성
alert('Hello')				// 함수
prompt('Message', 'Defstr')	// 함수
Math.abs(-24)				// 메서드
```



### 주석

주석은 프로그램 진행에 전혀 영향을 주지 않는 코드로 행 주석 `//`과 범위 주석인 `/**/`이 있다.

```javascript
// 행 주석
/* 범위 주석 */
```



## 자바스크립트 출력

자바스크립트의 가장 기본적인 출력 방법은 alert () 함수를 사용해 웹 브라우저에 경고 창을 띄우는 것이다. HTML 문서에서 `<script>` 태그를 이용해 자바스크립트를 사용할 수 있으며, 위치에 대한 제약은 없다. 다만 위에서부터 아래로 실행하기 때문에 하단에 작성된 코드를 실행해보면, 경고창 Hello가 출력되고 확인 버튼을 누르고 나서야 화면에 안녕이 나타나고, 두번째 경고창에 Bye가 뜨는 것을 확인할 수 있다.

```html
<!DOCTYPE html>
<html>
<head>
<title>Insert title here</title>
	<script type="text/javascript">
		alert("Hello");
	</script>
</head>
<body>
	안녕
	<script type="text/javascript">
		alert("Bye");
	</script>
</body>
</html>
```



## 자료형과 변수

### 자료형

자바스크립트에는 숫자, 문자열, 불, 함수, 객체, 정의되지 않은 자료형이 있다.



#### 숫자

가장 기본형인 자료형은 숫자이다. 자바스크립트는 정수와 실수를 구분하지 않으므로 숫자를 쉽게 다룰 수 있다. 숫자는 크롬 웹 브라우저에서 `F12`를 눌러 개발자 도구를 실행한 후 [Console] 탭에 입력하면 자동으로 생성된다. 자바스크립트를 통해서 사칙연산도 수행 가능하다.



#### 문자열

문자열은 문자 집합을 의미한다. 자바스크립트는 두 가지 방법으로 문자열을 생성한다. 첫 번째 방법은 큰따옴표 안에 문자를 넣는 방법이고, 두 번째는 작은따옴표 안에 문자를 넣는 방법이다. 어떤 방법을 사용하든 상관은 없지만 일반적으로 자바스크립트에서는 문자열 내부에 큰따옴표를 자주 넣으므로 작은따옴표를 사용해 문자열을 생성하는 것을 추천한다.

문자열 안에 따옴표를 넣고 싶으면 서로 다른 따옴표로 문자열을 감싸주면 된다. 즉, 작은따옴표를 넣으려면 그 주변을 큰따옴표로 감싸고,  큰따옴표를 넣으려면 그 주변을 작은따옴표로 감싸면 된다.

```javascript
alert("'Hello'") // 출력 내용 : 'Hello'
alert('"Hello"') // 출력 내용 : "Hello"
```

동일한 따옴표를 사용하고 싶을 때는 문자열 내부에 이스케이프 문자(`\`)를 이용하여, `\'`와 `\"`으로 사용한다 . 이스케이프 문자는 다양한 특수한 기능을 수행한다.`\t`는 수평탭 기능, `\n`은 행 바꿈 기능, `\\\`은 역 슬래시 표현 기능 등이 있다.



#### 불

불(bool)은 참과 거짓을 표현할 때 사용하는 자료이다. 불은 true와 false 두 가지만 만든다. 두 대상을 비교할 수 있는 연산자를 비교 연산자라고 한다. 비교 연산자를 통해 숫자는 물론 문자열도 비교할 수 있다. 문자열은 사전의 앞쪽에 위치할수록 값이 작다. 유니코드 문자를 사용해 전 세계 모든 언어를 비교할 수 있다.



### 변수

변수는 값을 저장할 때 사용하는 식별자이다. 이름은 변수이지만 숫자뿐만 아니라 모든 자료형을 저장할 수 있다. 변수는 변수 선언과 변수 초기화를 거쳐 사용할 수 있게 된다. 변수를 만드는 것을 '변수를 선언한다'라고 하고, 변수에 값을 저장하는 것을 '변수에 값을 할당한다'라고 표현한다. 여기서 변수 선언 후 처음으로 값을 할당하는 것을 '변수를 초기화한다'고 표현하는 것이다. 일반적으로 변수 선언과 초기화를 한 번에 처리한다.

```javascript
> var pi;			// 변수 선언
> pi = 3.14159265;  // 값 할당

> var pi = 3.14159265; // 변수 선언과 초기화

> alert(pi); 	// 변수를 이용해 저장된 값 출력
```



## 조건문과 반복문

프로그램은 기본적으로 위쪽에서 아래쪽으로 진행되는데, 제어문을 사용해 이 흐름을 변화시킬 수 있다. 대표적인 제어문으로는 조건문과 반복문이 있다.



### 조건문

#### if 조건문

if 조건문은 가장 기본적인 조건문이다. 조건이 true이면 문장을 실행하고, 조건이 false이면 문장을 무시한다. 조건문을 만족해 실행되는 문장이 한 행이라면 중괄호를 생략 가능하나, 실행되는 문장이 여러 행인 경우에는 중괄호로 감싸주어야 한다.

```html
<script>
    // Date 객체를 선언 [현재 시간 측정]
    var date = new Date();

    // 요소를 추출
    var year = date.getFullYear();
    var month = date.getMonth() + 1; // 0부터 1월
    var day = date.getDay(); // 요일을 숫자로 반환 [일자는 date.getDate]
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var seconds = date.getSeconds();
    
    // 조건문
    if (hours < 12) {
        // 표현식 "hours < 12"가 참일 경우 실행
        alert('오전입니다.');
    }
	
    // 조건문
    if (12 <= hours) {
        // 표현식 "12 <= hours"가 참일 경우 실행
        alert('오후입니다.');
    }    
</script>
```



#### if else 조건문

```html
<script>
    var date = new Date();
    var hours = date.getHours();

    // 조건문
    if (hours < 12) {
        // 표현식 "hours < 12"가 참일 경우 실행
        alert('오전입니다.');
    } else {
        // 표현식 "hours < 12"가 거짓일 경우 실행
        alert('오후입니다.');
    }
</script>

```



#### if else if 조건문

if else if 조건문은 중복되지 않는 조건 세 가지 이상을 구분할 때 사용한다.

```html
<script>
    var date = new Date();
    var hours = date.getHours();

    // 조건문
    if (hours < 5) {
        alert('취침 중이여야 해');
    } else if (hours < 7) {
        alert('일어나서 출근 준비 해');
    } else if (hours < 9) {
        alert('출근 중이겠지');
    } else if (hours < 12) {
        alert('빈둥빈둥');
    } else if (hours < 14) {
        alert('점심시간');
    } else {
        // 여러 가지 업무를 수행합니다.
    }
</script>
```



### 반복문

여러 번 반복하는 일을 간편하게 처리할 수 있게 해주며, 배열과 함께 사용하면 더욱 효과적인 반복문을 작성할 수 있다.

#### 배열

배열은 변수 여러 개를 한꺼번에 다룰 수 있는 자료형이다. 자바스크립트에는 숫자, 문자열, 불, 함수, 객체, 정의되지 않은 자료형까지 총 6개가 있다. 그 중에서 배열은 객체의 일종이며, 대괄호`[]`를 이용해 생성한다. 대괄호 내부의 각 자료는 쉼표`,`로 구분한다.

```html
<script>
    // 변수 선언 및 초기화
    var array = ['가', '나', '다', '라'];

    // 배열요소의 변경
    array[0] = '윤';

    // 각각의 배열 요소 출력
    alert(array[0]);
    alert(array[1]);
    alert(array[2]);
    alert(array[3]);
    
    // 배열 요소의 개수 출력
    alert(array.length);
</script>
```



#### while 반복문

특정한 숫자를 증가시켜 불 표현식을 거짓으로 만들어서 반복문을 벗어난다.

```html
<script>
    var i = 0;
    var array = ['가', '나', '다'];

    while (i < array.length) {
        // 출력
        alert(i + '번째 출력: ' + array[i]);
        // 탈출을 위해 변수를 더한다
        i++;
    }
    /* 0번째 출력 : 가
    1번째 출력 : 나
    2번째 출력 : 다*/
</script>
```



#### for 반복문

while 반복문 외에도 for 반복문이 있다. for 반복문은 원하는 횟수 만큼 반복하고 싶을 때 사용한다. for 반복문은 `for (초기식; 조건식; 종결식) { 실행문 }` 으로 구성되어 있다.

for 반복문을 각 단계별로 설명하면 다음과 같다.

1. 초기식을 비교한다.
2. 조건식을 비교한다. (조건이 거짓이면 반복문을 종료한다.)
3. 실행문을 실행한다.
4. 종결식을 실행한다.
5. 앞의 2단계로 이동한다.

일반적으로 for문은 `for (var i=0; i<반복횟수; i++) { 실행문 }` 형태로 반복할 수 있다.

```html
<script>
    var array = ['가', 273, "문자열", {}, [32,103], function(){}];

    for (var i = 0; i < array.length; i++) {
        alert(i + '번째 출력: ' + array[i]);
    }
    /* 0번째 출력 : 가
    1번째 출력 : 273
    2번째 출력 : 문자열
    3번째 출력 : [object Object]
    4번째 출력 : 32,103
    5번째 출력 : function(){} */
</script>
```

> 정해진 횟수만큼 반복해야 할 때는 for 반복문을 많이 사용하고, 이외에는 while 반복문을 많이 사용한다. 그 예로 외부 요인으로 인한 조건 변경이 있다.

```html
<script>
// 시간(1000밀리초)이라는 외부 요인으로 인한 조건 변경
    var start = new Date().getTime();
    var count = 0;

    while (start + 1000 > new Date().getTime()) {
        count++;
    }

    alert(count + '만큼 반복했습니다.'); 
</script>
```

for 반복문을 통해 0부터 100까지 더하는 코드를 작성해보자.

```html
<script>
    var output = 0;
    for (var i = 0; i <= 100; i++) {
        output += i;
    }
    alert(output);
</script>
```



## 함수

함수는 코드의 집합이다. 함수를 직접 만드는 방법을 알아보자.



### 함수 선언과 호출, 실행 우선순위



#### 선언과 호출

함수는 코드 집합을 나타내는 자료형으로 생성하기 위해서는 함수 이름을 입력하지 않고 만드는 익명 함수 생성과 함수 이름을 입력해서 만드는 선언적 함수 생성이 있다. 익명 함수, 선언적 함수 모두 많이 사용하기 때문에 용어와 생성 방법을 꼭 기억하자. 



##### 익명 함수 선언

```javascript
function () {} 
```

```html
<script>
    // 익명 함수 선언
    var noName = function () {
        alert('함수_01');
        alert('함수_02');
        return "익명 함수";
    };

    alert(noName());
    /* 출력 내용:
        함수_01
        함수_02
        익명 함수 
    */
    
    alert(typeof(noName()));
    /* 출력 내용:
        함수_01
        함수_02
        string 
    */
</script>
```



##### 선언적 함수 선언

```javascript
function 함수 () { }
```

```html
<script>
    // 선언적 함수 선언
    function name() {
        alert('함수_01');
        alert('함수_02');
    };

    alert(name());
    /* 출력 내용:
        함수_01
        함수_02
		undefined
    */   
    
    alert(typeof(name));
    /* 출력 내용: 
    	function
    */    
</script>
```

이렇게 만들어진 함수는 alert() 함수를 사용한 것처럼 함수 이름 뒤에 괄호를 사용해 실행할 수 있다. 이렇게 함수를 실행하는 것을 '함수를 호출한다'라고 표현한다.

함수도 변수이므로, 같은 함수를 선언하고 호출하면 가장 마지막에 선언된 함수를 호출하게 된다. 다만 선언적 함수와 익명 함수를 함께 사용하는 경우에는 실행 순서가 다르다. 자바스크립드는 모든 코드를 읽기 전에 선언적 함수를 먼저 읽기 때문에 선언적 함수가 익명 함수 뒤에 있어도 나중에 있는 익명 함수를 실행하게 되는 것이다.



### 매개변수와 반환 값

매개변수는 alert 함수의 괄호 안에 문자열 또는 숫자 등을 집어넣었던과 같이 함수의 괄호 안에 집어넣어 함수 쪽에 추가적인 정보를 전달하는 것을 말한다.

```javascript
alert('매개변수');
```

시간 정보를 추출했을 때는 다음과 같이 함수 실행 결과를 변수에 입력했는데, 이렇게 함수 실행 결과를 반환 값(리턴 값)이라고 한다.

```javascript
// 반환 값 minutes와 seconds
var minutes = date.getMinutes();
var seconds = date.getSeconds();
```

단, 모든 함수에 매개변수와 반환 값을 사용해야 하는 것이 아니라 필요할 때만 선택적으로 사용한다.

```javascript
function 함수명 (매개변수1, 매개변수2, 매개변수3) {
	// 함수 코드
	// 함수 코드
	// 함수 코드
	return 반환값;
}
```



### 콜백 함수

매개변수로 전달되는 함수를 콜백 함수라고 한다. 다른 프로그래밍 언어에서 잘 사용하지 않는 개념이기에 생소할 수 있다.

```html
<script>
    // callback을 매개변수로 callTenTimes 함수를 선언
    function callTenTimes(callback) {
        // 매개변수로 전달된 callback 함수를 10번 호출
        for (var i = 0; i < 10; i++) {
            callback();
        }
    }

    // 변수 callback 선언 (변수 callback은 alert를 호출하는 익명 함수)
    var callback = function () {
        alert('함수 호출');
    };

    // 함수를 호출합니다.
    callTenTimes(callback);
</script>
```



## 객체

객체는 자료형 여러 개를 한 번에 저장한다. 배열은 객체를 기반으로 만들어졌기 때문에 배열과 유사하다고 느낄 수 있다. 하지만 배열은 인덱스를 기반으로 자료를 저장하지만, 객체는 키(속성)를 기반으로 자료(속성값)를 저장한다. 따라서 배열은 요소에 접근할 때 인덱스를 사용하지만, 객체는 키를 사용한다.

```html
<script>
    // 객체 선언
    var product = {
        제품명: '7D 건조 망고',
        유형: '당절임',
    };
</script>
```

이렇게 객체를 선언하게 되면, `제품명`이라는 키에는 `7D 건조 망고`라는 속성이 생성되고, `유형`키에는 `당절임`이라는 속성이 생성된다.

`product['제품명']` 또는 `product.제품명`과 같은 입력을 통해 `7D 건조 망고`라는 속성에 접근할 수 있다. 만약에 식별자 생성 규칙에 어긋나는 문자를 키로 사용해야 하는 경우에는 `product.제품명`과 같은 형태로 접근이 불가능하고, 오직 `product['제품명']`과 같은 형태로만 접근할 수 있다.



for in 반복문을 사용해 객체 요소를 하나씩 살펴볼 수 있다. `for (var 키 in 객체) { 문장 }` 형식으로 작성해 객체를 순환시킨다.

```html
<script>
    // 객체 선언
    var product = {
        제품명: '7D 건조 망고',
        유형: '당절임',
        원산지: '필리핀'
    };

    // 출력
    for (var i in product) {
        alert(i + ':' + product[i]);
    }
    /* 출력내용
    	제품명:7D 건조 망고
    	유형:당절임
    	원산지:필리핀
    */
</script>
```



### 속성과 메서드

배경에 있는 값 하나하나를 요소라고 하며, 객체에 있는 값 하나하나를 속성이라고 한다. 다른 프로그래밍 언어는 요소와 속성이 다르지만 자바스크립트에서는 요소와 속성이 같아 구분하는 것에는 큰 의미가 없다.

객체 속성에서도 배열 요소처럼 다양한 자료형을 입력할 수 있다.

```html
<script>
    // 객체 선언
    var object = {
        number: 123,
        string: '문자열',
        boolean: true,
        array: [3, 'a', "string"]
        method: function () {}           
    };
</script>
```

객체 속성 중 자료형이 함수인 속성을 특별히 메서드라고 한다. 아래 person 객체에는 name 속성과 eat 속성이 있다. 이 중에 eat 속성의 자료형이 함수이기 때문에 eat() 메서드라고 한다.

```html
<script>
    // 객체 선언
    var person = {
        name: '최인규',
        eat: function (food) {
            alert (food + '을/를 먹는다')
        }           
    };
    
    // 메서드 호출
    person.eat('밥')
    
    // [밥을/를 먹는다]가 출력된다.
</script>
```

객체에 있는 속성을 메서드에서 사용하고 싶을 때는 자신이 가진 속성임을 분명하게 표시해야 한다. 이 표시는 this 키워드를 사용하게 된다.

```html
<script>
    // 객체 선언
    var name = '누군가'
    var person = {
        name: '최인규',
        eat: function (food) {
            alert (name + '가 ' + food + '을/를 먹는다')
            alert (this.name + '가 ' + food + '을/를 먹는다')
        }           
    };
    
    // 메서드 호출
    person.eat('밥')
    
    /* 출력 내용
    	누군가가 밥을/를 먹는다
    	최인규가 밥을/를 먹는다 */
</script>
```



## 문서 객체 모델 (DOM)

HTML 태그를 자바스크립스에서 이용할 수 있게 객체로 만든 것을 문서 객체라고 한다. 따라서 자바스크립트에서 문서 객체를 사용하면 HTML 태그를 생성하고 제거하거나 조작할 수 있다. 또 문서 객체를 사용해 마우스를 클릭하거나 키보드를 누르는 등 이벤트에 반응할 수 있다.



### 문서 객체 모델 기본 용어와 개념

#### 문서 객체 모델 기본 용어

##### 문서 객체

HTML 태그를 자바스크립트에서 사용할 수 있는 객체로 만든 것이 문서 객체(Document object)이다. 즉, HTML에서 요소라고 하던 것을 자바스크립트에서는 문서 객체라고 하는 것이다. 따라서 자바스크립트에서 문서 객체를 조작한다는 말은 결국 태그를 조작한다는 의미이다.

자바스크립트를 사용해 문서 객체를 조작해서 태그를 추가·수정·제거할 수 있다. 즉, HTML 태그의 내용을 바꿀 수도 있고 출력되는 모양이나 색상을 동적으로 변경할 수도 있다.



##### 노드

웹 브라우저는 HTML 페이지를 읽으면서 태그의 포함 관계에 따라 문서 객체를 트리 형태로 만든다. 트리의 각 요소가 노드(Node)이고, 노드는 요소 노드(Element node)와 텍스트 노드(Text node)로 구분한다.

`<h1>`처럼 텍스트 노드를 가진 태그도 있지만, `<br>`, `<hr>`, `<img src="img.png">`처럼 텍스트 노드를 갖지 않은 태그도 있다.



##### 정적 생성과 동적 생성

웹 브라우저는 웹 페이지를 실행할 때 먼저 HTML 파일을 분석한 후 화면에 표시한다. 웹 페이지를 처음 실행할 때 HTML 태그로 적힌 문서 객체를 생성하는 것을 정적 생성이라고 하며, 웹 페이지를 실행 중에 자바스크립트를 사용해 문서 객체를 생성하는 것을 동적 생성이라고 한다. 

그리고 웹 브라우저가 HTML 파일을 분석하고 출력하는 방식을 문서 객체 모델(DOM, Document Object Model)이라고 한다. 문서 객체 모델은 웹 브라우저마다 미세한 차이가 있다.



#### 웹 페이지 실행 순서

문서 객체를 잘 사용하려면 먼저 웹 브라우저가 웹 페이지를 어떤 순서로 실행하는지 반드시 이해해야 한다. 웹 브라우저는 위쪽에서 아래쪽으로 HTML 코드를 실행하기 때문에 아래의 코드를 실행하면 오류가 발생한다. 왜냐하면 script 태그를 읽을 때는 h1 태그와 h2 태그가 생성되어 있지 않기 때문이다.

```html
<head>
    <script>
        // h1 태그의 배경 색상을 변경
        document.querySelector('h1').style.backgroundColor = 'red';

        // h2 태그의 글자 색상을 변경
        document.querySelector('h2').style.color = 'red';
    </script>
</head>
<body>
    <h1>Process - 1</h1>
    <h2>Process - 2</h2>
</body>

<!-- 오류 내용 : Uncaught TypeError: Cannot read property 'style' null -->
```

오류를 해결하기 위한 가장 간단한 방법은 script 태그를 h1 태그와 h2 태그 아래로 삽입하는 것이다. 하지만 이렇게 할 경우에는 HTML 페이지가 방대해져서 유지 보수가 어려워진다.

또 다른 방법은 뒤에서 배우게 될 이벤트 기능을 사용하는 것이다.

```HTML
<head>
    <script>
        function event() {
        	// h1 태그의 배경 색상을 변경
	        document.querySelector('h1').style.backgroundColor = 'red';

    	    // h2 태그의 글자 색상을 변경
        	document.querySelector('h2').style.color = 'red';
        };
    </script>
</head>
<body onload ="event()">
    <h1>Process - 1</h1>
    <h2>Process - 2</h2>
</body>
```

```html
<head>
    <script>
        var event = function () {
        	// h1 태그의 배경 색상을 변경
	        document.querySelector('h1').style.backgroundColor = 'red';

    	    // h2 태그의 글자 색상을 변경
        	document.querySelector('h2').style.color = 'red';
        };
    </script>
</head>
<body onload ="event()">
    <h1>Process - 1</h1>
    <h2>Process - 2</h2>
</body>
```

```html
<head>
    <script>
        window.onload = function () {
        	// h1 태그의 배경 색상을 변경
	        document.querySelector('h1').style.backgroundColor = 'red';

    	    // h2 태그의 글자 색상을 변경
        	document.querySelector('h2').style.color = 'red';
        };
    </script>
</head>
<body>
    <h1>Process - 1</h1>
    <h2>Process - 2</h2>
</body>
```

이벤트 기능을 심화하여 사용하게 되면, 버튼을 통해 적용시킬 수 있는 기능을 만들 수도 있다.

```html
<head>
    <script>
        function event() {
        	// h1 태그의 배경 색상을 변경
	        document.querySelector('h1').style.backgroundColor = 'red';

    	    // h2 태그의 글자 색상을 변경
        	document.querySelector('h2').style.color = 'red';
        };
    </script>
</head>
<body>
    <h1>Process - 1</h1>
    <h2>Process - 2</h2>
    <button onclick="event()">스타일 적용</button>
</body>
```



### 문서 객체 선택

이미 존재하는 HTML 태그를 자바스크립트에서 문서 객체로 변환하는 것을 '문서 객체를 선택한다'고 표현한다. 문서 객체를 조작하기 위해서는 먼저 문서 객체를 선택해야 한다. 문서 객체는 1개 또는 여러 개 선택할 수 있다. 문서 객체를 여러 개 선택하는 메서드를 사용하면 문서 객체가 배열 형태로 반환된다.

> 문서 객체를 선택하는 메서드
>
> document.getElementById('아이디') 						: 아이디로 1개 선택
> document.querySelector('선택자')							: 선택자로 1개 선택
> document.getElementsByName('이름')					: name 속성으로 여러 개 선택
> document.getElementsByClassName('클래스')		: class 속성으로 여러 개 선택
> document.querySelectorAll('선택자')						: 선택자로 여러 개 선택

이전에 CSS3를 공부할 때, id 속성이 중복되어도 문제가 없지만 자바스크립트에서는 문제가 생긴다고 공부한 적이 있다. 자바스크립트에서 id 속성이 중복되었을 경우 문제가 되는 부분이 바로 getElementById() 메서드 이다.



#### getElementById() 메서드

```html
<head>
    <script>
        // 이벤트 연결
        window.onload = function () {
            // 문서 객체 선택 (id로 1개 선택)
            var header = document.getElementById('header');

            // 문서 객체 조작
            header.style.color = 'orange';
            header.style.background = 'red';
            header.innerHTML = 'From JavaScript';
        };
    </script>
</head>
<body>
    <h1 id="header">주황색 글꼴과 빨간색 배경의 제목</h1>
</body>
```



#### querySelector() 메서드

```html
<head>
    <script>
        // 이벤트 연결
        window.onload = function () {
            // 문서 객체 선택 (선택자로 1개 선택).
            var header = document.querySelector('h1');

            // 문서 객체 조작
            header.style.color = 'orange';
            header.style.background = 'red';
            header.innerHTML = 'From JavaScript';
        };
    </script>
</head>
<body>
    <h1>선택자로 딱 하나의 h1 태그를 선택하고 조작했더니 </h1>
    <h1>가장 먼저 등장하는 h1 태그의 글꼴 색은 주황색, 배경색은 빨간색이 되었다.</h1>
</body>
```



#### querySelectorAll() 메서드

```html
<head>
    <script>
        // 이벤트 연결
        window.onload = function () {
            // 문서 객체 선택(선택자로 여러 개를 선택)
            var headers = document.querySelectorAll('h1');

            for (var i = 0; i < headers.length; i++) {
                // 변수 선언
                var header = headers[i];

                // 문서 객체 조작
                header.style.color = 'orange';
                header.style.background = 'red';
                header.innerHTML = 'From JavaScript';
            }
        };
    </script>
</head>
<body>
    <h1>선택자로 모든 h1 태그를 선택하고 조작했더니 </h1>
    <h1>모든 h1 태그의 글꼴 색은 주황색, 배경색은 빨간색이 되었다.</h1>
</body>
```



### 문서 객체 조작

현대적인 방법으로 만든 웹 페이지 소스 코드를 보면, HTML 태그에 어떤 내용도 입력되어 있지 않은 것을 볼 수 있다. Youtube의 소스 코드를 보면 약 700줄인데, 약 350줄 정도가 어떤 내용도 입력되지 않은 틀만 잡는 태그로 구성되어 있고, 대부분의 코드도 내용이 전혀 들어있지 않다. 그것은 Youtube가 SPA 사이트라서 처음에 웹 페이지를 읽어 들일 때만 틀만 읽어 들이고, 이후에 자바스크립트 문서 객체를 조작해서 모든 내용을 집어넣기 때문이다.

> SPA(Single Page Application)는 웹 페이지를 한 번만 읽어 들이고, 사용자가 조작할 때 웹 페이지 내용을 자바스크립트를 사용해 바꾸는 형태의 웹 페이지를 의미한다.

페이지의 일부만 변경하는 경우에 적합하며, SPA 형태의 페이지를 제작하기 위해서는 HTML 페이지 전체가 아닌 일부만 갱신할 수 있도록 하는 Ajax(Asynchronous Javascript And Xml) 기법을 이용한다. 

현대에는 이러한 웹 페이지 개발을 위해 React, Vue 등 다양한 자바스크립트 프레임워크가 등장했다.



#### 글자 조작

문서 객체 내부에 있는 글자를 조작할 때는 textContent나 innerHTML과 같은 속성을 사용한다.

textContent는 문서 객체 내부 글자를 순수 텍스트 형식으로 가져오도록 변경하는 글자 속성이고, innerHTML은 문서 객체 내부 글자의 HTML 태그를 반영해 가져오도록 변경하는 글자 속성이다.

```html
<!-- textContent 형식의 내부 글자 조작 -->
<script>
	// 이벤트 연결
    window.onload = function () {
	    // 변수 선언
    	var output = '';
		for (var i = 0; i < 10; i++) {
			output += '<h1>Header - ' + i + '</h1>';
        }
        // 문서 객체 내의 글자 변경
        document.body.textContent = output;
        };
</script>
<!-- 단순 텍스트의 나열로 출력이 된다. -->
```

```html
<!-- innerHTML 형식의 내부 글자 조작 -->
<script>
	// 이벤트 연결
    window.onload = function () {
	    // 변수 선언
    	var output = '';
		for (var i = 0; i < 10; i++) {
			output += '<h1>Header - ' + i + '</h1>';
        }
        // 문서 객체 내의 글자 변경
        document.body.innerHTML = output;
        };
</script>
<!-- HTML에 작성한 것처럼 0~9까지 10개의 h1 제목이 출력된다. -->
```



#### 스타일 조작

자바스크립트로 CSS 속성 값을 추가·제거·번경할 수 있다. 문서 객체의 style 속성을 변경하면 된다. 스타일시트에서 사용하던 스타일 속성 이름을 그대로 입력하면 된다고 생각할 수 있지만, 자바스크립트에서 특수문자 `-`을 식별자에 사용할 수 없으므로 `-`으로 연결된 속성은 연결된 단어의 첫 글자를 대문자로 변경해야 한다.

스타일시트의 스타일 속성에 `background-image`가 있다면, 자바스크립트의 스타일 식별자에서는 `backgroundImage`로 변환하여야 한다.

문자열을 사용해 스타일 속성에 접근하려는 경우에는 `document.body.style['backgroundColor']='red';`또는 `document.body.style['background-color']='red';` 로 두 가지 방법을 모두 사용할 수 있다.

```html
<script>
	// 이벤트 연결
    window.onload = function () {
	    // 변수 선언
    	var output = '';
		for (var i = 0; i < 10; i++) {
			output += '<h1 id="h'+i+'">Header - ' + i + '</h1>';
        }
        // 문서 객체 내의 글자 변경
    document.body.innerHTML = output;

	var h = document.getElementById('h0');
	h.style.color="red";
    h.style.backgroundColor="blue";	
        };
</script>
```

```html
<script>
	// 이벤트 연결
    window.onload = function () {
		// 문서 객체 추가 [innerHTML 속성으로 div 태그가 256개 추가된다]
        var output = '';
        for (var i = 0; i < 256; i++) {
        	output += '<div></div>';
        }
        document.body.innerHTML = output;

        // 문서 객체 선택
        var divs = document.querySelectorAll('div');
        for (var i = 0; i < divs.length; i++) {
        	// 변수 선언
            var div = divs[i];

            // 스타일 적용 [각각의 div 높이는 2px이며, rgb 색상이 0부터 255까지 순차적으로 증가]
            div.style.height = '2px';
            div.style.background = 'rgb(' + i + ',' + i + ',' + i + ')';
		}
	};
</script>
```



#### 속성 조작

일반적으로 문서 객체의 속성을 조작할 때는 setAttribute(`속성이름`, `속성값`) 메서드와  getAttribute(`속성이름`) 메서드를 사용한다. 웹 표준에서 지정한 속성은 아래와 같은 방법으로 곧바로 접근할 수도 있다. 하지만 웹 표준에서 지원하지만 웹 브라우저 제조사가 구현을 못했다면 접근하지 못할 수도 있습니다.

```javascript
image.src = 'rint.png'
alert(image.src)
```

웹 표준에서 지정하지 않은 속성에 접근할 때는 setAttribute() 메서드와 getAttribute() 메서드를 사용한다. 웹 표준에서 지정하지 않은 속성은 사용자 지정 속성이 있는데, 반드시 속성 조작 메서드를 사용해서 접근해야 한다.



##### img 태그 속성 조작

```html
<head>
    <script>
        // 이벤트 연결
        window.onload = function () {
            // 문서 객체 선택 (id가 image인 객체를 선택하여, 선언된 image 변수값으로 할당)
            var image = document.getElementById('image');
            
            // 선언된 변수에 대한 속성 변경
            image.src = 'http://placehold.it/300x200';
            image.width = 300;
            image.height = 200
            
            var aTag = document.querySelector('a')
            aTag.href="#";
        };
    </script>
</head>
<body>
    <img id="image" />
    <a href>링크</a>
</body>
```



##### body 태그 속성 조작

아래 코드를 실행하고 검사를 사용해서 살펴보면, body 태그 내에 data-custom 속성이 추가되어 있는 것을 볼 수 있다. 다른 속성도 이 방법으로 지정하고 추출하는 것이다.

```html
<head>
    <script>
        // 이벤트 연결
        window.onload = function () {
            // 속성 지정 (body 태그 내에 value 값을 가진 data-custom 속성을 지정)
            document.body.setAttribute('data-custom', 'value');

            // 속성 추출 (dataCustom 변수 선언 및 data-custom 속성을 추출하여, alert 함수를 변수에 할당)
            var dataCustom = document.body.getAttribute('data-custom');
            alert(dataCustom);
        };
    </script>
</head>
<body>
</body>
```



#### 문서 객체를 사용한 시간 표시

```html
<head>
	<script>
	// 이벤트 연결
	window.onload = function () {
		// clock 변수 선언하고 id가 clock인 객체를 선택하여 할당
		var clock = document.getElementById('clock');
		// setInterval 메서드 내에 콜백 함수를 이용해, 1초(1000밀리초)마다 콜백 함수를 수행하도록 한다.
        setInterval(function () {
			// now 변수 선언하고 시스템 날짜를 할당
            var now = new Date();
            // clock에 innerHTML 속성으로 now 변수를 문자열로 조작
			clock.innerHTML = now.toString();
		}, 1000);
	};
	</script>
</head>
<body>
	<h1 id="clock"></h1>
</body>
```



## 이벤트

이벤트는 키보드를 누르거나 마우스를 클릭하는 것처럼 어떤 현상이 프로그램에 영향을 미치는 것을 의미한다. 이벤트는 사용자가 직접 발생시킬 수도 있도 응용 프로그램에서 자체적으로 발생시킬 수도 있다. 자바스크립트에서는 마우스, 키보드, HTML 프레임, HTML 입력 양식, 사용자 인터페이스, 구조 변화, 터치 이벤트를 기본적으로 지원하고 있다.

지금까지 문서 객체를 조작하면서 `window.onload = function () { };` 코드를 계속 사용해온 것을 알 수 있다. 코드에서 `onload`는 이벤트 속성이라고 한다. on을 제외한 `load`를 이벤트 이름 또는 이벤트 타입이라고 한다. 그리고 이벤트 속성에 넣는 함수를 이벤트 리스터 또는 이벤트 핸들러라고 한다.

이벤스 속성은 이름만 보아도 대충 어떤 이벤트인지 알 수 있으나 종류가 매우 다양하다.



### 이벤트 연결

문서 객체에 이벤트를 연결하는 방식을 이벤트 모델이라고 한다. 이벤트 모델은 DOM 레벨에 따라 구분할 수 있다.

+ DOM 레벨 0
  + 인라인 이벤트 모델
  + 고전 이벤트 모델
+ DOM 레벨 2
  + 마이크로소프트 인터넷 익스플로러 이벤트 모델
  + 표준 이벤트 모델

DOM 레벨 0의 이벤트 연결 방식은 쉽기 때문에 널리 사용된다. 하지만 이벤트를 중복해서 연결할 수 없다는 단점이 있다. 반면에 DOM 레벨  2의 이벤트 연결 방식은 이벤트를 중복해서 연결할 수 있지만, 웹 브라우저 종류에 따라 연결하는 방식이 달라 문제가 된다.

DOM 레벨 2의 문제는 jQuery 라이브러리 등을 사용해 극복할 수 있다. 여기서는 DOM 레벨 0에 해당하는 인라인 이벤트 모델과 고전 이벤트 모델만 간단히 살펴 보자.



#### 인라인 이벤트 모델

인라인 이벤트 모델은 HTML 태그 내부에 자바스크립트 코드를 넣어 이벤트를 연결하는 방식이다. 전 세계 추세로 보면 거의 사용하지 않지만, 국내에는 아직 사용하는 웹 사이트가 굉장히 많이 있다.

button 태그 내부에 onclick 속성을 사용해 자바스크립트 코드를 입력하고 실행한다. 그러면 button 태그에 해당하는 버튼을 누를 때 경고창을 출력시킬 수 있다.

```html
<body>
    <button onclick="alert('click')">버튼</button>
</body>
```

인라인 코드 내부에서 세미콜론으로 문장을 구분하여 여러 행을 입력할 수 있지만 지저분해보인다. 그래서 인라인 이벤트 모델을 사용할 때에는 script 태그 내부에 함수를 선언한 후 인라인 이벤트 속성 내부에서 해당 함수를 실행하는 형태를 취하는 것이 일반적이다.

```html
<head>
    <script>
        function buttonClick() {
            alert('click');
            document.write('클릭됨');
        }
    </script>
</head>
<body>
    <button onclick="buttonClick()">버튼</button>
</body>
```



#### 고전 이벤트 모델

고전 이벤트 모델은 과거에 표준으로 정의되어 많이 사용하던 이벤트 모델이다. 이름은 고전이지만 아직도 많이 사용되는 방식이다.

```html
<head>
    <script>
        // 이벤트 연결
        window.onload = function () {
            // 문서 객체 선택
            var button = document.getElementById('button');
            // 이벤트 연결
            button.onclick = function () {
                alert('click');
            };
            // 이벤트 연결
            document.getElementById('button2').onclick = function () {
            	console.log("abc")
            };
        };
    </script>
</head>
<body>
    <button id="button">버튼</button>
    <button id="button2">로그</button>
</body>
```



> 이벤트 리스너 내부에서 this 키워드를 사용하면 이벤트를 발생한 자기 자신을 의미한다. 따라서 이벤트 리스너와 내부에서 this 키워드의 textContent 속성을 사용하면 자기 자신의 글자를 변경시킬 수 있다.



```html
<body>
    <button id="button">버튼 - </button>
    <div></div>
    <div id = "div"></div>
    <script>
        // 이벤트 연결 [변수 선언 없이 한 줄로 작성]
        document.getElementById('button').onclick = function () {
            // 클릭할 때마다 ★이 계속해서 추가된다.
            this.textContent = this.textContent + '★';
            // 클릭하면 노란 별이 들어온다.
            this.style.backgroundColor = "yellow";
            // 클릭하면 첫번째 div 공간에 제목이 생성된다.
            document.querySelector('div').innerHTML="<h1>여기가 div 자리이다.<h2>";
            // 클릭하면 id가 div인 div 공간에 이미지가 생성된다
            document.getElementById('div').innerHTML="<img src='baby.png'>";            
        };   
    </script>
</body>
```



### 이벤트 사용

현실에는 사건(이벤트)이 발생하면 누가, 언제, 어디서, 무엇을, 어떻게, 왜에 해당하는 정보를 알 수 있다. 이벤트가 발생하면 웹 브라우저는 이벤트 정보가 담긴 이벤트 객체를 만들어 이벤트 리스너에 전달한다. 따라서 이벤트 객체를 사용하면 이벤트와 관련한 정보를 알아낼 수 있다.

```html
<script>
    window.onload = function (event) {
        alert(event);
    };
</script>
```

위 코드를 보면 이벤트 리스너의 첫번째 매개변수로 이벤트 객체가 들어와있다. HTML 태그에는 기본적인 몇 가지 이벤트가 있는데, 그 예로 a 태그를 클릭하면 href 속성에 입력한 위치로 이동하고, form 태그로 생성한 <제출> 버튼을 누르면 자동으로 입력 양식을 제출하는 것들이 있다. 이처럼 특정 태그가 가진 기본적인 이벤트를 기본 이벤트라고 한다.

가끔 기본 이벤트를 중단시켜야 할 경우가 있다. 회원가입 페이지에서 <확인> 버튼을 누르면 우선 사용자가 정확한 정보를 입력했는지 확인한 후 이동해야 한다. 즉, 정보를 입력하지 않은 상태에서는 다음 페이지로 넘어가면 안되는 것이다. 이러한 상황에서는 HTML 태그가 가지는 기본 이벤트를 제거해야 한다.



#### 기본 이벤트 제거

고전 이벤트 모델에서 기본 이벤트를 제거하려면 이벤트 리스너의 반환 값을 false로 입력하면 된다.

```html
<head>
    <script>
        // 이벤트 연결
        window.onload = function () {
            // 문서 객체 선택
            var button = document.getElementById('button');
            // 이벤트 연결
            button.onclick = function () {
                // 기본 이벤트 제거
                return false;
            };
        };
    </script>
</head>
<body>
    <a id="button" href="http://google.co.kr">버튼</a>
</body>
<!-- 코드를 실행하고 링크를 클릭하더라도 연결된 웹 페이지로 이동하지 않는다. -->
```

