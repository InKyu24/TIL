## Angular.js

#### ECMAScript 와 TypeScript 



#### CDN (Content Delivery Network) 방식

```html
<script src="xxx.jquery.min.js"></script>
```



#### npm(node package manager) 방식



#### 서버와 ajax(asynchronous javascript and Xml) 통신

서버에서는 JSON, XML 형식으로 Data 만 제공

* ajax javascript (cross browser 코딩이 필요하다)
* jquery.ajax()
* axios, rxjs(Angular)

Http Client

*  Angular에서 서버와 http 통신을 하려고 할때 RxJS를 사용한다.



#### Router

Routing, Router는 네비게이션 메뉴를 통한 화면 전환 기능을 제공한다. SPA(Single Page Application)는 단일 페이지 구성으로 index.html이 하나만 있기 때문에 Angular, Reactjs, Vuejs : Router 기능이 필요하다.



#### Augury , postman

VSCode 상에서 Angular code assist를 해주는 PlugIn 설치

Augury - 크롬 개발자 도구상에 angular 컴포넌트 현황 확인

postman - REST API 

ClientAngular CLI 설치 > npm install -g @angular/cli



### Client Project 코드와 설정파일을 자동으로 생성 해주는 라이브러리

#### JavaScript 컴파일러 사용

javascript 컴파일러 역할을 하는 Babel을 사용

reactjs, vue - ECMAScript 6

angular - typescript

ES6 -> ES5 변환, TS -> ES5로 변환



#### 번들링 기능 제공  클라이언트를 위한 Dev server 필요

Webpack

​	번들링(bundling) 기능

​		개발자 작성 코드 .ts 확장자 개발

​		여러개의 ts 파일을 한꺼번에 합쳐서(bundling) 배포

​		node_modules 폴더에 있는 라이브러리 .js 를 합쳐서 배포

​	클라이언트를 위한 Dev Server 가 필요

​		source 수정만 하면 브라우저에 즉시 반영



#### nodejs

package.json 파일은 Node.js에서 의존성(dependency) 설정을 위한 파일

npm i --save rxjs

npm i

현재 폴더에 package.json 파일이 있어야 함

```json
"scripts": {
    "ng": "ng",
    "start": "ng serve",
    "build": "ng build",
    "watch": "ng build --watch --configuration development",
    "test": "ng test"
},
```

\> ng serve: 개발모드 (dev mode) : 컴파일, 번들링, 개발서버 시작
\> ng build: 운영모드 (prod mode): 컴파일, 번들링 후에 생성 파일들을 서버의 static 폴더에 배포하면 됩니다. 



http://localhost:4200
main.ts 웹팩의 설정으로 인해서 가장 먼저 시작됨



src/index.html  ===[src/main.ts (index.html 과 angular 컴포넌트 연결) ]===>  src/app.module.ts ==> src/app.component.ts 

<app-root></app-root>
AppComponent가 Root 컴포넌트 역할을 한다. 
src/app.component.ts  : typescript로 작성한 javascript 코드

selector : ‘app-root’

src/app.component.html : template html 로 작성한 화면

src/app.component.css : Style css 로 작성 스타일



playground

ECMA Script6 Sample Code

```javascript
//var , let
function foo() {
    var a = 'hello'; 
    if (true) {
        var a = 'bye';
        console.log(a);     // bye 
    } console.log(a);		// bye
}
foo();
```

```javascript
//const
const value = 10;
//array
const myArr = [1,2]; 
myArr.push(10);
console.log(myArr);
const myObj1 = {a:10};
const myObj2 = {b:20};

const myObj3 = Object.assign({},myObj1, myObj2);
console.log(myObj3);
```

```javascript
//삼항 연산자
let x = 20;
const answer = x > 10 ? 'greater than 10' : 'less than 10';
console.log(answer);
//For Loop
const myArr = [10,20,30];
for (let i=0; i < myArr.length; i++) {
  console.log(i + " " + myArr[i]);
}
//for-in
for(let val in myArr){
  console.log(val + ' ' + myArr[val]);
}
//for-of
for(let val of myArr) {
  console.log(val);
}
```

```javascript
//Arrow function 화살표 함수, 람다식
function sayHello(msg) {
  return 'Hello ' + msg;
}
console.log(sayHello('Javascript'));

let sayHello2 = msg => 'Hello ' + msg;

sayHello2 = msg => {
  return 'Hello ' + msg;
}

sayHello2 = msg => ('Hello ' + msg);
console.log(sayHello2('람다식'));
```

```javascript
//forEach
const myArr = [10,20,30];
myArr.forEach(function(item){
  console.log(item);
});
myArr.forEach(item => console.log(item));
```

```javascript
//map()
let result = myArr.map(item => item + 10);
console.log(result);

let result2 = myArr.map((item,idx) => item + idx);
console.log(result2);
```

```javascript
//filter() 
//3의 배수인 값만 반환해라
const result3 = myArr.filter(item => item % 3 == 0);
console.log(result3);

//reduce()
const sum = myArr.reduce((prev,curr) => prev + curr);
console.log(sum);
```

```javascript
//일반함수와 Arrow 함수의 this 차이점
//생성자 함수 
function BlackDog() {
  this.name = '흰둥이';
  return {
    name:'검둥이',
    bark: function() {
      console.log(this.name + ' 멍멍!');
    }
  }
}
const blackDog = new BlackDog();
blackDog.bark();

function WhiteDog() {
  this.name = '흰둥이';
  return {
    name:'검둥이',
    bark: () => {
      console.log(this.name + ' 멍멍!');
    }
  }
}
const whiteDog = new WhiteDog();
whiteDog.bark();
```

```javascript
//default parameter value
let volume = (l, w = 3, h = 4 ) => (l * w * h);
console.log(volume(2));

//Template Literals
const host = 'aa.com';
const port = 8090;

const url = 'http://' + host + ':' + port;
console.log(url);
const url2 = `http://${host}:${port}`;
console.log(url2);
```

```javascript
//Array destructuring assignment (비구조화 할당)
let a, b, rest;
[a, b] = [1, 2];
console.log(a);
console.log(b);

let foo = ["one", "two", "three"];

let [foo1, foo2, foo3] = foo;
console.log(foo1);
console.log(foo2);
console.log(foo3);
//swapping
let a = 1;
let b = 3;
[a, b] = [b, a];
console.log(a);
console.log(b);
```

```javascript
//Object destructuring assignment (비구조화 할당)
let obj = {p: 42, q: true}; 
let val1 = obj.p;
console.log(val1);
let val2 = obj.q;
console.log(val2);

let {p, q} = obj;
console.log(p);
console.log(q);
```

```javascript
//Spread Operator (펼침연산자)
// joining arrays
const odd = [1, 3, 5];
const nums = [2 ,4 , 6].concat(odd);
const nums2 = [2, 4, ...odd, 6];
console.log(nums2);
```

```javascript
// cloning arrays
const arr = [1, 2, 3, 4];
const arr2 = arr.slice();
console.log(arr2);
const arr3 = [...arr];
console.log(arr3);

const result1 = arr;  //주소 대입
arr.push(5);
const result2 = [...odd];  //값 대입
odd.push(6);
console.log(result1);
console.log(result2);

const [a, b, ...rest] = [10,20,30,40,50];
console.log(a);
console.log(b);
console.log(rest);
```

```javascript
//객체 Spread Operator (펼침연산자)
//let val = 100;
const {a, b, ...rest} = {a:100, b:true, c:'java', d:100};
console.log(a);
console.log(b);
console.log(rest);
const {c,d} = rest;
console.log(c);
console.log(d);

let x = 100;
let y = 200;
const obj = {x, y} //{x:x, y:y}
console.log(obj);
```



TypeScript 설치

\> npm i -g typescript

tsc 컴파일 명령어

​	tsc 01.basic-type.ts 01.basic-type.js 파일이 생성

js 실행 명령어

node 01.basic-type.js

tsc --target es5 02.class-student.ts



css 모든 컴포넌트에 적용하고 싶은 style을 정의 > src/styles.css
app.component.html에 적용이 되는 style을 정의 > app/app.component.css



index.html -> app.component.ts/html/css -> heroes.component.ts/html/css



index.html

app.component.ts : <app-root> root 컴포넌트

heroes.component.ts : <app-heroes> 하위 컴포넌트



Angular Data Binding

* One Way (단방향)

  * interpolation

    * {{ }} : 컴포넌트(ts)에 정의된 변수나 메서드를 템플릿에서 출력할 때 사용한다.

  * Property Binding

    * 서버 쪽에서 전달 받는 변수(동적인 데이터)를 받아와 템플릿에서 HTML 엘리먼트의 속성 값을 사용

      ```javascript
      var imgUrl = "aa.jpg";
      <img [src] = "ImageUrl">
      ```

  * Event Binding

    * 템플릿에서 event가 발생했을 때 컴포넌트에서 event handler를 작성해야 한다.

      ```javascript
      (click)="myHandler()"
      (keyup)="keyupHeroName($event)"
      ```

* Two Way (양방향)

  * Property Binding and Event Binding

    * ngModel directive를 사용하기 때문에 app.module.ts에서 FormsModule을 import하고 진행

      ```javascript
      <input [(ngModel)]=“name"/>
      ```

      