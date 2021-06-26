## 실전 리액트 프로그래밍

### ES6+를 품은 자바스크립트, 매력적인 언어가 되다.

 ES6는 ECMA에서 2015년에 채택한 자바스크립트 표준이다. ES6 이후로 자바 스크립트에는 많은 변화가 있었다.

#### 1. 변수를 정의하는 새로운 방법: const, let

ES5까지의 자바스크립트에서는 var를 이용해 변수를 정의했고, 그것이 유일한 방법이었다. 하지만 ES6에서 const와 let을 이용하는 새로운 변수 정의 방법이 생겼다. 새로운 방법이 나온 이유는 기존 방식으로는 해결되지 않는 문제가 있었기 때문이다.

##### 1-1. var가 가진 문제

###### var의 첫 번째 문제: 함수 스코프

var의 첫 번째 문제는 정의된 변수가 함수 스코프를 가진다는 것이다. 스코프는 변수가 사용될 수 있는 영역을 말한다. 스코프는 변수가 정의된 위치에 의해 결정된다. var로 정의된 변수는 함수 스코프이기 때문에 함수를 벗어난 영역에서 사용하면 에러가 발생한다.

```javascript
function example() {
    var i = 1;
}
console.log(i); // 참조 에러
```

var 변수가 함수가 아닌 프로그램의 가장 바깥에 정의하면 전역 변수가 되는데, 이는 프로그램 전체를 감싸는 하나의 함수가 있다고 생각하면 이해가 쉽다. 특이한 점은 함수 안에서 var 키워드를 사용하지 않고 변수에 값을 할당하면 그 변수는 전역 변수가 된다는 점이다.

```javascript
function example1() {
    i = 1;
}
function example2() {
    console.log(i);
}
example1();
example2(); // 1이 출력됨
```

이런 상황에 대처하기 위해 use strict를 사용할 수 있다. 파일 상단에 use strict;를 선언하면 에러가 발생한다.

var는 함수 스코프이기 때문에 for 반복문에서 정의된 변수가 반복문이 끝난 이후에도 계속 남게 되는 문제점이 있다. 이는 for문 뿐만 아니라 while문, switch문, if문 등 함수 내부에서 작성되는 모든 코드는 같은 문제를 안고 있다.

```javascript
for (var i = 0; i < 10; i++) {
    console.log(i);
}
console.log(i); // 10
```

var 변수의 스코프를 제한하기 위해 즉시 실행 함수를 사용하기도 한다. 즉시 실행 함수는 함수를 정의하는 시점에 바로 실행되고 사라지는 함수이다. var 변수는 함수 스코프이므로 즉시 실행 함수로 묶으면 변수의 스코프를 제한할 수 있다. 즉시 실행 함수는 작성하기도 번거롭고 가독성도 떨어진다는 점에서 var 변수의 스코프 문제를 해결하려고 노력을 많이 하게 되는 것이다.

###### var의 두 번째 문제: 호이스팅

var로 정의된 변수는 그 변수가 속한 스코프의 최상단으로 끌어올려진다. 이를 호이스팅이라고 부른다. 끌어올려진다는 말의 의미가 무엇인지 조금씩 살펴보자.

```javascript
console.log(myVar); // 참조 에러
```

```javascript
console.log(myVar); // undefined
var myVar = 1;
```

변수를 정의하기 전에 사용했음에도 이 코드를 실행하면 에러가 발생하지 않는다. 특이한 점은 1이 출력되는 게 아니라 undefined가 출력된다는 점이다. 이것은 해당 변수의 정의가 위쪽으로 끌어올려졌기 때문인데, 코드가 다음처럼 변경됐다고 생각하면 이해하기 쉽다.

```javascript
var myVar = undefined;
console.log(myVar); // undefined
var myVar = 1;
```

변수의 정의만 끌어올려지고 값은 원래 정의했던 위치에서 할당된다. 특이하게도 다음처럼 변수가 정의된 곳 위에서 값을 할당할 수도 있다.

```javascript
console.log(myVar); // undefined
myVar = 2;
console.log(myVar); // 2
var myVar = 1;
```

버그처럼 보이는 코드가 에러 없이 사용될 수 있다는 것은 단점이라고 할 수 있따. 이처럼 호이스팅은 직관적이지 않으며, 보통의 프로그래밍 언어에서는 찾아보기 힘든 성질이다.

###### var의 기타 문제들

var의 또 다른 문제를 살펴보자. var를 이용하면 한 번 정의된 변수를 재정의할 수 있다.

```javascript
var myVar = 1;
var myVar = 2;
```

변수를 정의한다는 것은 이전에 없던 변수를 생성한다는 의미로 통용된다. 따라서 앞의 코드가 에러 없이 사용될 수 있다는 것은 직관적이지 않으며 버그로 이어질 수 있다.

또 다른 문제는 var가 재할당 가능한 변수로밖에 만들 수 없다는 점이다. 상수처럼 쓸 값도 무조건 재할당 가능한 변수로 만들어야 한다. 이런 상황에서 재할당 불가능한 변수를 사용한다면 코드의 복잡도가 낮아지고 가독성은 높아진다.

##### 1-2. var가 가진 문제

###### const, let은 블록 스코프다

var는 함수 스코프였지만 const, let은 블록 스코프다. 함수 스코프의 단점 대부분이 블록 스코프에는 없다. 많은 언어에서 블록 스코프를 사용하기 때문에 다른 언어를 사용해 봤다면 블록 스코프가 익숙할 것이다.

```javascript
if (true) {
    const i = 0;
}
console.log(i); // 참조 에러
```

블록 스코프에서 if 문의 블록 안에서 정의된 변수는 if문을 벗어나면 참조할 수 없다. 따라서 if문에서 생성된 변수를 블록 바깥에서 사용하려고 하면 에러가 발생한다. 이러한 상황에서 에러가 발생하는 것이 직관적이며 오히려 이해하기 쉽다. var를 사용하는 경우에는 if문 안에서 생성된 변수가 if문을 벗어나도 계속 살아 있기 때문에, 함수 스코프를 벗어나기 전까지 계속해서 신경써서 관리해야 했다.

이번에는 블록 스코프에서 같은 이름의 변수를 정의하는 경우를 살펴보자.

```javascript
let foo = 'bar1';
console.log(foo); // bar1
if (true) {
    let foo = 'bar2';
    console.log(foo); // bar2
}
console.log(foo); // bar1
```

###### const, let에서의 호이스팅

const 또는 let으로 정의된 변수도 호이스팅한다. 하지만 const 또는 let으로 변수를 정의하기 전에 그 변수를 사용하려고 하면 참조 에러가 발생한다.

```javascript
console.log(foo); // 참조 에러
const foo = 1;
```

똑같은 경우에 var는 에러가 발생하지 않았다. 따라서 const 또는 let으로 정의된 변수는 호이스팅이 되지 않는다고 생각하기 쉽다. 하지만 const 또는 let으로 정이된 변수도 호이스팅된다. 다만 변수가 정의된 위치와 호이스팅된 위치 사이에서 변수를 사용하려고 하면 에러가 발생한다. 이 구간을 임시적 사각지대라고 부른다.

임시적 사각지대에서 변수를 사용하지 못한다면 호이스팅의 역할은 무엇인지 생각해보자. 다음 코드에서는 같은 이름의 변수가 서로 다른 스코프에 정의되어 있다.

```javascript
const foo = 1;
{
    console.log(foo); // 참조 에러
    const foo = 2;
}
```

만약 `const foo=2;`가 호이스팅되지 않았다면 참조 에러는 발생하지 않고, `const foo=1;` 값이 출력될 것이다. 이 예제를 통해 호이스팅의 역할을 짐작할 수 있다. `const foo=2;`가 호이스팅 되었기 때문에 `console.log(foo);`는 `const foo=1;`를 참조하게 된다. 그리고 `const foo=1;`를 참조했지만 임시적 사각지대여서 에러가 발생한다.

var로 정의된 변수에는 임시적 사각지대가 없기 때문에 다음 코드에서는 참조 에러가 발생하지 않는다.

```javascript
var foo = 1;
(function() {
    console.log(foo); // undefined
    var foo=2;
})
```

###### const는 변수를 재할당 불가능하게 만든다

const로 정의도니 변수는 재할당이 불가능하다. 반대로 let, var로 정의된 변수는 재할당할 수 있다. 재할당 불가능한 변수는 프로그램의 복잡도를 상당히 낮춰주기 때문에 되도록이면 재할당 불가능한 변수를 사용하는 게 좋다.

```javascript
const bar = 'a';
bar = 'b'; // 에러 발생

var foo = 'a';
foo = 'b';

let value = 'a';
value = 'b';
```

이처럼 const로 정의된 변수에 값을 재할당하면 에러가 발생한다. 다만 const로 정의된 객체의 내부 속성값은 수정 가능하다는 점을 주의해야 한다.

```javascript
const bar = {prop1: 'a'};
bar.prop1 = 'b';
bar.prop2 = 123;
console.log(bar); // {prop1: 'b', prop2: 123}

const arr = [10, 20];
arr[0] = 100;
arr.push(300);
console.log(arr); // [100, 20, 300]
```

이미 존재하는 속성값을 수정하거나 새로운 속성값을 추가하는 것 모두 가능하다. 객체의 내부 속성값도 수정 불가능하게 만들고 싶다면 immer, immutable, js 등의 외부 패키지를 활용하는 게 좋다. 이러한 외부 패키지는 객체를 수정하려고 할 때 기존 객체는 변경하지 않고 새로운 객체를 생성한다. 새로운 객체를 생성하는 편의 기능은 필요 없고 단지 수정만 할 수 없도록 차단하고 싶다면, 다음과 같은 자바스크립트 내장 함수를 이용하면 된다.

* Object.preventExtensions
* Object.seal
* Object.freeze

당연한 이야기지만 const로 정의했다면 객체를 참조하는 변수 자체를 변경하는 것은 불가능하다.

```javascript
const bar = {prop1: 'a'};
bar = {prop2: 'b'}; // 에러 발생
```



#### 2. 객체와 배열의 사용성 개선

ES6+에서 객체와 배열에 추가된 문법을 알아보자. 단축 속성명과 계산된 속성명을 이용하면 객체와 배열을 생성하고 수정하는 코드를 쉽게 작성할 수 있다. 또한, 전개 연산자와 비구조화 할당 덕분에 객체와 배열의 속성값을 밖으로 꺼내는 방법이 한결 쉬워졌다.

##### 2-1. 객체와 배열을 간편하게 생성하고 수정하기

###### 단축 속성명

단축 속성명은 객체 리터럴 코드를 간편하게 작성할 목적으로 만들어진 문법이다. 단축 속성명을 사용하면 간편하게 새로운 객체를 만들 수 있다.

```javascript
const name = 'mike';
const obj = {
    age: 21;
    name,
    getName() {return this.name}
};
```

새로 만들려는 객체(name)의 속성값 일부가 이미 변수로 존재하면 간단하게 변수 이름만 적어주면 된다. 이때 속성명은 변수 이름과 같아진다. 속성값이 함수이면 function 키워드 없이 함수명(getName)만 적어도 된다. 이때 속성명은 함수명과 같아진다.

이번에는 단축 속성명을 사용한 경우와 사용하지 않은 경우를 비교해 보자.

```javascript
function makePerson1 (age, name) {
    return { age: age, name: name};
}

function makePerson2 (age, name) {
    return {age, name};
}
```

makePerson1이 단축 속성명을 사용하지 않은 경우이고, makePerson2가 사용한 경우이다. 보다시피 단축 속성명을 사용한 경우가 코드를 작성하기도 편하고 가독성도 좋다.

또한, 단축 속성명은 디버깅을 위해 콘솔 로그를 출력할 때 유용하다.

```javascript
const name = 'mike';
const age = 21;
console.log('name=', name, ', age = ' age); // name=mike, age=21
console.log({name, age}); // {name: 'mike', age: 21}
```

단축 속성명이 있기 때문에 `console.log({name, age});`와 같이 작성하여 코드를 훨씬 간결하게 작성할 수 있다는 것을 확인할 수 있다.

###### 계산된 속성명

계산된 속성명은 객체의 속성명을 동적으로 결정하기 위해 나온 문법이다. 계산된 속성명을 사용하면 같은 함수를 간결하게 작성할 수 있다.

```javascript
function makeObject1 (key, value) {
    const obj = {};
    obj[key] = value;
    return obj;
}

function makeObject2 (key, value) {
    return { [key] : value };
}
```

계산된 속성명은 다음과 같이 컴포넌트의 상태값을 변경할 때 유용하게 쓸 수 있다.

```react
class MyComponent extends React.Component {
    state = {
        count1:0,
        count2:0,
        count3:0,
    };
	// ...
	onClick = index => {
        const key = 'count${index}';
        const value = this.state[key];
        this.setState({ [key]: value + 1});
    };
}
```

setState 호출 시 계산된 속성명을 사용할 수 있다. 만약 계산된 속성명을 사용하지 않았따면 앞의 코드는 좀 더 복잡했을 것이다.

##### 2-2. 객체와 배열의 속성값을 간편하게 가져오기

###### 전개 연산자

전개 연산자는 배열이나 객체의 모든 속성을 풀어놓을 때 사용하는 문법이다. 다음과 같이 매개변수가 많은 함수를 호출할 때 유용하다.

```javascript
Math.max(1, 3, 7, 9);
const numbers = [1, 3, 7, 9];
Math.max(...numbers);
```

`Math.max(1, 3, 7, 9);`과 같은 방식으로는 동적으로 매개변수를 전달할 수 없다. 만약 네 개의 변수를 사용하면 값은 동적으로 전달할 수 있지만 매개변수 개수는 항상 네 개로 고정이다. 전개 연산자를 사용하면 `Math.max(...numbers);`와 같이 동적으로 함수의 매개변수를 전달할 수 있다.

> ###### 동적으로 함수의 매개변수를 전달하는 다른 방법
>
> 전개 연산자를 사용하지 않고도 다음과 같이 동적으로 함수의 매개변수를 전달할 수 있다.
>
> ```javascript
> const numbers = [-1, 5, 11, 3];
> Math.max.apply(null, numbers);
> ```
>
> 이 코드는 this 바인딩이 필요하지 않기 때문에 첫 번째 매개변수로 null을 입력하고 있다. 전개 연산자 방식보다 작성하기 번거롭고 가독성도 떨어진다.

전개 연산자는 배열이나 객체를 복사할 때도 유용하다.

```javascript
const arr1 = [1, 2, 3];
const obj1 = { age: 23, name:'mike' };

const arr2 = [...arr1];
const obj2 = {...obj2};

arr2.push(4);
obj2.age = 80;
```

전개 연산자를 사용해서 새로운 객체(obj2)와 배열(arr2)을 생성했다. 전개 연산자를 사용해서 새로운 객체가 생성되었기 때문에 속성을 추가하거나 변경해도 원래의 객체와 배열에는 영향을 주지 않는다.

배열의 경우 전개 연산자를 사용하면 그 순서가 유지된다.

```javascript
[1, ...[2, 3], 4]; // [1, 2, 3, 4]
new Date(...[2018, 11, 24]) // 2018년 11월 24일
```

배열 리터럴에서 중간에 전개 연산자를 사용하면 전개 연산자 전후의 순서가 유지된다. 함수의 인수는 정의된 매개변수의 순서대로 입력해야 하므로, 순서가 유지되는 전개 연산자의 성질을 이용하기 좋다. 예를 들어, Data 생성자의 매개변수 순서대로 날짜 데이터를 관리하면 Date 객체를 쉽게 생성할 수 있다.

전개 연산자를 사용하면 서로 다른 두 배열이나 객체를 쉽게 합칠 수 있다.

```javascript
const obj1 = { age: 21, name: 'mike' };
const obj2 = { hobby: 'soccer' };
const obj3 = { ...obj1, ...obj2 };
console.log(obj3); // { age: 21, name:'mike', hobby: 'soccer' };
```

그런데 이 코드에서 obj1과 obj2가 같은 이름의 속성을 가지고 있었다면 어떻게 될까? ES5까지는 중복된 속성명을 사용하면 에러가 발생했지만, ES6부터는 중복된 속성명이 허용된다.

```javascript
const obj1 = { x: 1, x: 2, y: 'a' }; // {x: 2, y: 'a' }
const obj2 = { ...obj1, y: 'b' }; // {x: 2, y: 'b' }
```

중복된 속성명 사용 시 최종 결과는 마지막 속성명의 값이 된다. 중복된 속성명과 전개 연산자를 이용하면 객체의 특정 속성값을 변경할 때 이전 객체에 영향을 주지 않고 새로운 객체를 만들어 낼 수 있다. 이는 변수를 수정 불가능하도록 관리할 때 유용하게 사용될 수 있다.

###### 배열 비구조화

배열 비구조화는 배열의 여러 속성값을 변수로 쉽게 할당할 수 있는 문법이다. 다음은 배열 비구조화를 사용한 코드이다.

```javascript
const arr = [1, 2];
const [a, b] = arr;
console.log(a); // 1
console.log(b); // 2
```

배열의 속성값이 왼쪽의 변수에 순서대로 들어간다.

이렇게 새로운 변수로 할당할 수도 있고 다음 코드처럼 이미 존재하는 변수에 할당할 수도 있다.

```javascript
let a, b;
[a, b] = [1, 2];
```

배열 비구조화 시 기본값을 정의할 수 있다. 배열의 속성값이 undefined라면 정의된 기본값이 할당되고, 그렇지 않다면 원래의 속성값이 할당된다.

```javascript
const arr = [1];
const [a = 10, b = 20] = arr;
console.log(a); // 1
console.log(b); // 20
```

첫 번째 변수의 속성값은 존재하기 때문에 기본값 10은 사용되지 않고 속성값이 그대로 할당된다. 두 번째 변수의 속성값은 undefined이므로 기본값 20이 할당된다. 배열 비구조화를 사용하면 두 변수의 값을 쉽게 교환할 수 있다.

```javascript
let a = 1;
let b = 2;
[a, b] = [b, a];
console.log(a); // 2
console.log(b); // 1
```

두 변수가 값을 교환하기 위해서는 제3의 변수를 이용하는 게 일반적이다. 하지만 배열 비구조화를 사용하면 제3의 변수가 필요하지 않은 뿐만 아니라 단 한 줄의 짧은 코드로 구현할 수 있다.

배열에서 일부 속성값을 무시하고 진행하고 싶다면 건너뛰는 개수만큼 쉼표를 입력하면 된다.

```javascript
const arr = [1, 2, 3];
const [a, , c] = arr;
console.log(a); // 1
console.log(c); // 3
```

첫 번째 속성값은 변수 a에 할당된다. 두 번째 속성값은 건너뛰고 세 번째 속성값이 변수 c에 할당된다.

쉼표 개수만큼을 제외한 나머지를 새로운 배열로 만들 수도 있다.

```javascript
const arr = [1, 2, 3];
const [first, ...rest1] = arr;
console.log(rest1); // [2, 3]
const [a, b, c, ...rest2] = arr;
console.log(rest2); // []
```

배열 비구조화 시 마지막에 ...과 함께 변수명을 입력하면 나머지 모든 속성값이 새로운 배열로 만들어진다. 나머지 속성값이 존재하지 않으면 빈 배열이 만들어진다.

###### 객체 비구조화

객체 비구조화는 객체의 여러 속성값을 변수로 쉽게 할당할 수 있는 문법이다. 다음은 객체 비구조화를 사용한 코드이다.

```javascript
const obj = { age: 21, name: 'mike' };
const { age, name } = obj;
console.log(age); // 21
console.log(name); // mike
```

객체 비구조화에서는 중괄호를 사용한다. 배열 비구조화에서는 배열의 순서가 중요했지만 객체 비구조화에서 순서는 무의미하다. 따라서 name과 age의 순서를 바꿔도 결과는 같다. 단, 배열 비구조화에서 왼쪽 변수의 이름은 임의로 결정할 수 있지만, 객체 비구조화에서는 기존 속성명을 그대로 사용해야 한다.

```javascript
const obj = { age: 21, name: 'mike' };
const { age, name } = obj;
const { name, age } = obj;
const { a, b } = obj;
```

객체 비구조화에서 순서는 무의미하므로 `const { age, name } = obj;`과 `const { name, age } = obj;`의 결과는 같다. 하지만 존재하지 않는 속성명을 사용한 `const { a, b } = obj;`에는 undefined가 할당된다.

객체 비구조화에서는 속성명과 다른 이름으로 변수를 생성할 수 있따. 이는 중복된 변수명을 피하거나 좀 더 구체적인 변수명을 만들 때 좋다.

```javascript
const obj = { age: 21, name: 'mike' };
const { age: theAge, name } = obj;
console.log(theAge); // 21
console.log(age); // 참조 에러
```

속성명이 age인 값을 theAge변수에 할당한다. theAge라는 이름의 변수만 할당되고 age 변수는 할당되지 않는다. 객체 비구조화에서도 기본값을 정의할 수 있다. 배열 비구조화처럼 속성값이 undefined인 경우에는 기본값이 들어간다.

```javascript
const obj = { age: undefined, name: null, grade: 'A' };
const { age = 0, name = 'noName', grade = 'F' } = obj;
console.log(age); // 0
console.log(name); // null
console.log(grade); // A
```

age는 undefined이므로 기본값이 들어간다. 따라서 age는 0이 된다. 속성값이 null이면 기본값은 들어가지 않는다. 따라서 name은 null이 된다.

기본값을 정의하면서 별칭을 함께 사용할 수 있다.

```javascript
const obj = { age: undefined, name: 'mike' };
const { age: theAge = 0, name } = obj;
console.log(theAge); // 0
```

기본값으로 함수의 반환값을 넣을 수 있다.

```javascript
function getDefaultAge() {
    console.log('hello');
    return 0;
}
const obj = { age: 21, grade: 'A' };
const { age = getDefaultAge(), grade } = obj; // hello 출력되지 않음
console.log(age); // 21
```

한 가지 재밌는 점은 기본값이 사용될 때만 함수가 호출된다는 점이다. age의 속성값은 undefined가 아니므로 기본값이 사용되지 않고, getDefaultAge 함수도 호출되지 않는다.

객체 비구조화에서도 사용되지 않은 나머지 속성들은 별도의 개체로 생성할 수 있다.

```javascript
const obj = { age: 21, name: 'mike', grade: 'A' };
cosnt { age, ...rest } = obj;
console.log(rest); // { name: 'mike', grade: 'A' }
```

배열 비구조화와 비슷한 방식으로 나머지 속성들을 별도의 객체로 분리하고 있다.

for문에서 객체를 원소로 갖는 배열을 순회할 때 객체 비구조화를 사용하면 편리하다.

```javascript
const people = [{ age: 21, name: 'mike' }, { age: 51, name: 'sara' }];
for (const { age, name }) of people) {
    // ...
}
```

###### 비구조화 심화 학습

비구조화는 객체와 배열이 중첩되어 있을 때도 사용할 수 있다.

```javascript
const obj = { name: 'mike', mother: { name: 'sara' } };
const = {
    name,
    mother: { name: motherName },
} = obj;
console.log(name); // mike
console.log(motherName); // sara
console.log(mother); // 참조 에러
```

세 개의 단어가 등장하지만, 비구조화의 결과로 motherName이라는 이름의 변수만 생성된다.

비구조화에서 기본값의 정의는 변수로 한정되지 않는다.

```javascript
const [{ prop: x } = { prop: 123 }] = [];
console.log(x); // 123

const [{ prop: x } = { prop: 123 }] = [{}];
console.log(x); // undefined

const [{ prop: x } = { prop: 123 }] = [{ prop:456 }];
console.log(x); // 456
```

두 코드의 차이는 배열의 첫 번째 원소가 존재의 유무이다. []의 내부에 원소가 존재하지 않아서 기본값이 할당되고, 두 번째 코드는 []의 내부에 {}라는 원소가 존재하기 때문에 기본값이 할당되지 않는다. 그리고 {} 원소에는 prop라는 이름의 속성명이 존재하지 않으므로 x에는 undefined가 할당된다.

객체 비구조화에서도 계산된 속성명을 활용할 수 있다.

```javascript
const index = 1;
const { [`key${index}`]: valueOfTheIndex } = { key1: 123 };
console.log(valueOfTheIndex); // 123
```

객체 비구조화에서 계산된 속성명을 사용할 때에는 반드시 별칭을 입력해야 한다.

별칭은 단순히 변수명만 입력할 수 있는 것은 아니다.

```javascript
const obj = {};
const arr = [];
({ foo: obj.prop, bar: arr[0] } = { foo: 123, bar: true });
console.log(obj); // { prop:123 }
console.log(arr); // [true]
```

객체 비구조화를 이용해서 obj 객체의 prop이라는 속성과 배열의 첫 번째 원소에 값을 할당하고 있다.

#### 3. 강화된 함수의 기능

ES6에서는 함수의 기능이 많이 보강되었다. 사실 이전의 함수가 뼈대만 구성해놓은 상태였다면, ES6에서는 살을 붙여서 함수의 기능을 온전하게 완성했다고 볼 수 있다. 매개변수에 기본값을 줄 수 있게 되었고, 나머지 매개변수를 통해 가변 길이 매개변수를 좀 더 명시적으로 표현할 수 있게 되었다. 명명된 매개변수를 통해서 함수를 호출하는 코드의 가독성이 월등히 좋아졌다. 그리고 화살표 함수가 추가되면서 함수 코드가 간결해졌고, this 바인딩에 대한 고민을 덜 수 있게 되었다.

##### 3-1. 매개변수에 추가된 기능

###### 매개변수 기본값

ES6부터 함수 매개변수에 기본값을 줄 수 있다.

```javascript
function printLog (a = 1) {
    console.log({ a });
}
printLog(); // { a: 1 }
```

인수 없이 함수를 호출하므로 a에는 undefined가 입력된다. 기본값이 정의된 매개변수에 undefined를 입력하면 정의된 기본값 1이 사용된다.

객체 비구조화처럼 기본값으로 함수 호출을 넣을 수 있고 기본값이 필요한 경우에만 함수가 호출된다.

```javascript
function getDefault() {
    return 1;
}
function printLog(a = getDefault()){
    console.log({ a });
}
printLog(); // { a: 1 }
```

입력값이 undefined인 경우에만 호출된다는 특징을 이용하면 매개변수에서 필수값을 표현할 수 있다.

```javascript
function required() {
    throw new Error('no parameter');
}
function printLog(a = required()) {
    console.log({ a });
}
printLog(10); // { a: 10 }
printLog(); // 에러 발생: no parameter
```

매개변수의 값이 존재하면 required 함수는 호출되지 않는다. 매개변수의 값이 없으면 required 함수에서 예외가 발생하기 때문에 매개변수 a는 필수값이 된다.

###### 나머지 매개변수

나머지 매개변수는 입력된 인수 중에서 정의된 매개변수 개수만큼을 제외한 나머지를 배열로 만들어 준다. 나머지 매개변수는 매개변수 개수가 가변적일 때 유용하다.

```javascript
function printLog(a, ...rest) {
    console.log({ a, rest });
}
printLog(1, 2, 3); // { a: 1, rest: [2, 3] }
```

하나의 인자를 제외한 나머지를 rest 매개변수에 할당한다.

ES5에서는 arguments 키워드가 비슷한 역할을 한다. 위의 코드를 arguments 키워드로 작성하면 다음과 같다.

```javascript
function printLog(a) {
    const rest = Array.from(arguments).splice(1);
    console.log({ a, rest });
}
printLog(1, 2, 3); // { a: 1, rest: [2, 3] }
```

매개변수 정의에서 arguments의 존재가 명시적으로 드러나지 않기 때문에 가독성이 좋지 않다. arguments는 배열이 아니기 때문에 배열처럼 사용하기 위해서는 배열로 변환하는 과정이 필요하다는 단점이 있다. 따라서 나머지 매개변수를 사용한 방식이 더 낫다.

###### 명명된 매개변수

자바스크립트에서 명명된 매개변수는 객체 비구조화를 이용해서 구현할 수 있다. 명명된 매개변수를 사용하면 함수 호출 시 매개변수의 이름과 값을 동시에 적을 수 있으므로 가독성이 높다.

```javascript
const numbers = [10, 20, 30, 40];
const result1 = getValues(numbers, 5, 25);
const result2 = getValues({ numbers, greaterThan: 5, lessThan: 25 });
```

함수 호출 시 매개변수의 이름이 보이지 않아 인수가 의미하는 바를 알기 어렵다. 반대로 명명된 매개변수를 이용하면 매개변수의 이름이 노출된다.

명명된 매개변수를 이용하면 선택적 매개변수의 활용도가 올라간다. 필수값과 반대되는 의미로, 있어도 되고 없어도 되는 매개변수를 선택적 매개변수라고 부른다.

```javascript
const result1 = getValues(numbers, undefined, 25);
const result2 = getValues({ numbers, greaterThan: 5 });
const result3 = getValues({ numbers, lessThan: 25 });
```

result1은 명명된 매개변수 없이 선택적 매개변수를 사용한 예로, 필요없는 매개변수 자리에 undefined를 넣으면 된다. 그러나 이 방식은 매개변수 개수가 많아지면 관리하기 힘들어진다. result2와 result3은 명명된 매개변수를 사용했다. 필요한 인수만 넣어주면 되기 때문에 선택적 매개변수가 늘어나도 문제 없이 사용할 수 있다.

명명된 매개변수를 사용하면 함수를 호출할 때마다 객체가 생성되기 때문에 비효율적일 것이라 생각할 수 있다. 하지만 자바스크립트 엔진이 최적화를 통해 새로운 객체를 생성하지 않으므로 안심하고 사용하자.

##### 3-2. 함수를 정의하는 새로운 방법: 화살표 함수

ES6에서는 화살표 함수를 이용해 함수를 정의하는 방법이 추가되었다. 화살표 함수를 이용하면 함수를 간결하게 작성할 수 있다.

```javascript
const add = (a, b) => a + b;
console.log(add(1, 2)); // 3

const add5 = a => a + 5;
console.log(add5(1)); // 6

const addAndReturnObject = (a, b) => ({ result: a + b });
console.log(addAndReturnObject(1, 2).result); // 3
```

화살표 함수를 중괄호로 감싸지 않으면 오른쪽의 계산 결과가 반환된다. 명시적으로 return 키워드를 작성하지 않아도 되기 때문에 코드가 간결해진다. 매개변수가 하나라면 매개변수를 감싸는 소괄호도 생략할 수 있다. 객체를 반환해야 한다면 소괄호로 감싸야 한다.

###### 화살표 함수의 코드가 여러 줄인 경우

화살표 함수에 여러 줄의 코드가 필요하다면 다음과 같이 전체를 중괄호로 묶고, 반환값에는 return 키워드를 사용한다.

```javascript
const add = (a, b) => {
  if (a <= 0 || b <= 0) {
      throw new Error('must be positive number');
  }
  return a + b;
};
```

###### this와 arguments가 바인딩되지 않는 화살표 함수

화살표 함수가 일반 함수와 다른 점은 this와 arguments가 바인딩되지 않는다는 점이다. 따라서 화살표 함수에서 arguments가 필요하다면 나머지 매개변수를 이용한다.

```javascript
const printLog = (...rest) => console.log(rest);
print(1, 2); // [1, 2]
```

###### 일반 함수에서 this 바인딩 때문에 버그가 발생하는 경우

이번에는 일반 함수의 this 바인딩을 알아보자. 일반 함수에서 this는 호출 시점에 사용된 객체로 바인딩된다. 따라서 객체에 정의된 일반 함수를 다른 변수에 할당해서 호출하면 버그가 발생할 수 있다.

```javascript
const obj = {
    value = 1,
    increase: function() {
        this.value++;
    },
};
obj.increase();
console.log(obj.vaule); // 2
const increase = obj.increase;
increase();
console.log(obj.value); // 2
```

increase 함수는 일반 함수이므로 호출 시 사용된 객체가 this로 바인딩된다. obj 객체가 this에 바인딩되므로 obj.value가 증가한다. 객체 없이 호출되는 경우에는 전역 객체가 바인딩되는데, 브라우저 환경에서는 window 객체가 바인딩된다. 따라서 obj.value는 증가하지 않는다. 화살표 함수 안에서 사용된 this와 arguments는 자신을 감싸고 있는 가장 가까운 일반 함수의 것을 참조한다. 따라서 increase 함수를 화살표 함수로 작성했다면 this는 window 객체를 가리키기 때문에 함수를 호출해도 obj.value는 항상 변하지 않는다.

###### 생성자 함수 내부에서 정의된 화살표 함수의 this

이번에는 생성자 함수 내부에서 정의된 화살표 함수를 살펴보자. 생성자 함수 내부에서 정의된 화살표 함수의 this는 생성된 객체를 참조한다.

```javascript
function Something() {
    this.value = 1;
    this.increase = () => this.value++;
}
const obj = new Something();
obj.increase();
console.log(obj.value); // 2
const increase = obj.increase;
increase();
console.log(obj.value); // 3
```

화살표 함수 increase의 this는 가장 가까운 일반 함수인 Something의 this를 참조한다. Something 함수는 생성자이고, obj 객체가 생성될 때 호출된다. 주의할 점은 new 키워드를 이용해서 생성자 함수를 호출하면 this는 생성되는 객체를 참조한다는 점이다. 따라서 increase 함수의 this는 생성된 객체를 가리킨다. 그러므로 호출 시점의 객체와는 무관하게 increase 함수의 this는 항상 생성된 객체를 참조하고 obj.value는 계속 증가한다.

###### setInterval 함수 사용 시 this 바인딩 문제

다음은 1초마다 obj.value를 증가시키는 코드다. 아래 코드에서 this가 어떤 객체를 참조할지 생각해보자.

```javascript
function Something() {
    this.value = 1;
    setInterval(function increase() {
        this.value++;
    }, 1000);
}
conse obj = new Something();
```

실행해보면 알겠지만 의도와 달리 obj.value는 증가하지 않는다. setInterval 함수의 인수로 들어간 increase 함수는 전역 환경에서 실행되기 때문에 this는 window 객체를 참조한다.

ES5에서는 앞에서의 문제를 해결하기 위해 다음과 같은 편법을 사용했다.

```javascript
function Something() {
    this.value = 1;
    var that = this;
    setInterval(function increase() {
        that.value++
    }, 1000);
}
const obj = new Something();
```

increase 함수에서는 클로저를 이용해서 미리 저장해둔 that 변수를 통해 this 객체에 접근한다.

> 클로저 개념 이해하기
>
> 클로저는 함수가 생성되는 시점에 접근 가능했던 변수들을 생성 이후에도 계속해서 접근할 수 있게 해주는 기능이다. 접근할 수 있는 변수는 그 함수를 감싸고 있는 상위 함수들의 매개변수와 내부 변수들이다.
>
> ```javascript
> function makeAddFunc(x) {
>     return function add(y) {
>         return x + y;
>     };
> }
> const add5 = makeAddFunc(5);
> console.log(add5(1)); // 6
> const add7 = makeAddFunc(7);
> console.log(add7(1)); // 8
> console.log(add5(1)); // 6
> ```
>
> add 함수는 상위 함수인 makeAddFunc의 매개변수 x에 접근할 수 있다. add5 함수가 생성된 이후에도 상위 함수를 호출할 때 사용했던 인수에 접근할 수 있다. 중간에 makeAddFunc(7)가 호출되지만 add5에 영향을 주지는 않는다. 즉, 생성된 add 함수별로 클로저 환경이 생성된다.

화살표 함수를 사용하면 편법을 사용하지 않고도 원하는 기능을 구현할 수 있다.

```javascript
fucntion Something() {
    this.value = 1;
    setInterval(() => {
        this.value++;
    }, 100)
}
const obj = new Something();
```

화살표 함수를 사용했기 때문에 this는 setInterval의 동작과는 상관없이 obj를 참조한다.



#### 4. 향상된 비동기 프로그래밍 1:프로미스

프로미스는 비동기 상태를 값으로 다룰 수 있는 개체다. 프로미스를 사용하면 비동기 프로그래밍을 할 때 동기 프로그래밍 방식으로 코드를 작성할 수 있다. 프로미스가 널리 보급되기 전에는 비동기 프로그래밍 코드인 콜백 패턴이 많이 쓰였다. 그러다가 몇 가지 프로미스 라이브러리가 등장하면서 프로미스를 사용하는 개발자가 많아졌고, 이제는 여러 라이브러리의 비동기 함수가 프로미스를 반환할 만큼 널리 사용되고 있다.

그리고 마침내 ES6에서는 프로미스가 자바스크립트 언어에 포함됐다. 자바스크립트 언어에서 지원하는 프로미스의 기능을 알아보자.

##### 4-1. 프로미스 이해하기

###### 콜백 패턴의 문제

자바스크립트에서는 비동기 프로그래밍의 한 가지 방식으로 콜백 패턴을 많이 사용했었다. 하지만 콜백 패턴은 콜백이 조금만 중첩돼도 코드가 상당히 복잡해지는 단점이 있다.

```javascript
function requestData1(callback) {
    // ...
    callback(data);
}
function requestData2(callback) {
    // ...
    callback(data);
}
function onSuccess1(data) {
    console.log(data);
    requestData2(onSuccess2);
}
function onSuccess2(data) {
    console.log(data);
    // ...
}
requestData1(onSuccess1);
```

콜백 패턴은 코드의 흐름이 순차적이지 않기 때문에 코드를 읽기가 상당히 힘들다. 하지만 프로미스를 사용하면 코드가 순차적으로 실행되게 작성할 수 있다.

```javascript
requestData1()
	.then(data => {
    	console.log(data);
    	return requestData2();
	})
	.then(data => {
    	console.log(data);
    	// ...
	});
```

지금은 이 코드를 이해하지 못해도 괜찮다. 프로미스를 사용하면 비동기 프로그래밍을 할 때 코드를 순차적으로 작성할 수 있다는 사실만 기억해두자.

