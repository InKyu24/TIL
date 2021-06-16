## React.js

### Front-End Library

리액트는 프론트엔드 라이브러리이다. 요즘의 웹 사이트는 단순한 웹 페이지가 아니라 웹 애플리케이션이다. 브라우저 상으로도 매우 많은 것들을 할 수 있다는 것이다. 어떠한 유저 인터페이스를 동적으로 나타내기 위해서는 수많은 상태들을 관리해주어야 한다.

```html
<div>
    <h1>Counter</h1>
    <h2 id='number'>0</h2>
    <button id='increase'>+</button>
</div>
```

위의 코드에서 버튼을 클릭해서 숫자 0 값을 바꿔주기 위해서는 각 DOM element에 대한 reference를 찾고 해당 DOM에 접근해서 원하는 작업을 해야 한다.

```javascript
var number = 0;
var elNumber = document.getElementById('number');
var btnIncrease = document.getElementById('increase');

btnIncrease.onclick = function() {
    number++;
    elNumber.innerText = number;
}
```



프로젝트의 규모가 커지고 다양한 유저 인터페이스와 인터렉션을 제공하게 된다면 많은 DOM 요소들을 직접 관리하고 정리하는 것은 번거롭다.

웹 개발을 하게 될 때, 귀찮은 DOM 관리와 상태 값 업데이트 관리를 최소한으로 하고, 오직 기능 개발과 사용자 인터페이스 구현에만 집중할 수 있도록 하기 위해 프론트엔드 라이브러리와 프레임워크들(Angular, Ember, Backbone, Vue, React 등)이 만들어졌다.



### Front-End Library 종류

#### Angular

Angular는 다양한 기능들이 내장되어 있어서, Angular만으로도 엄청나게 많은 것들을 만들어 낼 수 있다. Http Client, Router, 다국어 지원까지 내장되어 있다.

TypeScript의 사용이 기본이 된다는 점을 기억하자.

#### React

컴포넌트라는 개념에 집중이 되어 있는 라이브러리이다. 컴포넌트는 데이터를 넣으면 지정한 인터페이스를 조립해서 보여주는 역할을 한다.

Angular와 달리 사용자에게 보여주는 view만 신경쓰고, 나머지 기능들은 third-party 라이브러리(Redux, React-Router)를 활용하게 된다.

#### Vue

Vue는 입문자가 사용하기에 매우 쉽다. WebPack과 같은 모듈 번들러가 없어도 CDN으로 불러오는 형태로도 자주 이용된다. HTML을 템플릿처럼 그대로 사용할 수 있어서 마크업을 만들어주는 디자이너나 퍼블리셔가 있는 경우에는 작업 흐름이 매우 매끄럽고 React와 달리 공식 Router와 공식 상태 관리 라이브러리가 존재한다.

Angular처럼 디렉티브라는 기능도 있으며, React처럼 Virtual DOM 기반 컴포넌트도 존재한다. 또한 React에서 사용하는 JSX도 사용 가능하다.



### React의 Virtual DOM

React가 생기기 전에도 Angular, Backbone, Ember 등 수 많은 프레임워크들이 존재했고, 해당 프레임워크들은 MVC 패턴, MVVM 패턴, MVW 패턴들로 이루어져 있다. 

> MVC 패턴 : 데이터 단을 담당하는 Model, 화면을 보여주게 되는 View, 사용자가 발생시키게 되는 이벤트를 관리하는 Controller로 구성

여기서 이 모든 패턴의 공통점은 Model에 있다. 여기서 언급된 프레임워크들의 Model은 대부분 양방향 바인딩을 통해 작동한다.

> 양방향 바인딩 : Model의 값이 변하면 View에서도 해당 값을 변화시켜주고, View에서 값이 변하게 되면 Model에서도 해당 값을 변화시켜주는 것

변화(Mutation)라는 키워드에 집중해보자. React를 만들기 전 페이스북에서는 이러한 발상을 했었다. 

`Mutation을 하지 말자. 그 대신에 데이터가 바뀌면 그냥 뷰를 날려버리고 새로 만들어버리면 어떨까?`

그런데 브라우저는 DOM 기반으로 작동하기 때문에 페이지가 그때그때 새로운 View를 만들어 내려고 한다면 성능적으로 엄청난 문제가 있을 것이다.

그래서 존재하는 것이 Virtual DOM이다. Virtual DOM은 가상의 DOM이다. 변화가 일어나면 실제로 브라우저의 DOM에 새로운 것을 넣는 것이 아니라 JavaScript로 이루어진 가상의 DOM에 한 번 렌더링을 하고, 기존의 DOM과 비교를 한 다음에 변화가 필요한 곳에만 업데이트를 해주는 것이다. 쉽게 말하면 `바뀐 부분만 바꿔주도록 하는 것`이라 할 수 있다.



### WebPack 과 Babel

WebPack을 한 마디로 정의하자면 `웹 프로젝트를 만들 때 전체적으로 파일들을 관리해주는 도구`라고 할 수 있다. WebPack은 코드들을 의존하는 순서대로 잘 합쳐서 하나의 파일로 만들어준다. 기본적으로 하나의 파일로 만들어주고, 원한다면 규칙에 따라 분리도 가능하다.

JavaScript는 계속해서 발전하고 있기에, Node.js나 브라우저의 엔진에서 그 모든 문법을 지원할 수 없다. 따라서 Babel은 `JavaScript 변환 도구`로 모든 문법을 지원하는 기능을 한다.



### React 문법 이해하기

```react
// 설치된 react 모듈에서 React와 내부의 컴포넌트를 불러와 사용하겠다.
import React, { Component} from 'react';
```

```react
// 클래스를 통한 컴포넌트 생성
Class App extends Component {
    // 클래스 형태로 생성된 컴포넌트에는 꼭 render 함수가 있어야 한다.
    render() {
        // render 함수 내에서는 JSX를 return 해주어야 한다.
        return(
        	<div>
                <h1>리액트, 안녕?</h1>
            </div>
        );
    }
}
// 작성된 컴포넌트를 다른 곳에서 불러와서 사용할 수 있도록 내보내기를 해준다.
export default App;
```

#### JSX

HTML처럼 보이지만 `jsx`는 JavaScript로, React 컴포넌트를 작성할 때 사용하는 문법이다. 따라서 HTML과 다른 규칙이 몇 가지 있다. 

* 꼭 닫혀야 하는 태그

  * 태그는 꼭 닫혀있어야 한다. HTML의 경우에는 input이나 br 태그를 작성할 때 태그를 안 닫는 경우가 있는데, JSX에서는 꼭 태그를 닫아주어야 한다.  

* 감싸져 있는 엘리먼트

  * 2개 이상의 엘리먼트는 무조건 1개의 엘리먼트로 감싸져 있어야 한다. 따라서 `<div id = 1>한 개</div> <div id =2>두 개</div>` 와 같은 형태는 불가능하다. 이를 가장 간단하게 해결하는 방법은 이를 div 태그로 감싸주는 것이다.

    ```react
    <div id=mother>
    	<div id=1>한 개</div>
    	<div id=2>두 개</div>
    </div>
    ```

  * 가끔 어떤 상황에서는 단순히 div 태그로 감싸는 것이 스타일 설정에 불편함을 야기하는 경우가 있다. 그러한 상황에서는 Fragment 태그(`<Fragment>`)를 사용하면 된다.

* JSX 내부에서 JavaScript 값 사용하기

  * JSX 내부에서 JavaScript 값을 사용할 때에는 아래와 같이 사용할 수 있다.

    ```react
    class App extends Component {
      render() {
        const name = 'react';
        return (
          <div>hello {name}!</div>
        );
      }
    }
    ```

    > const : ES6에서 도입된 키워드로, 상수 값을 설정할 때 사용 (scope가 블록 단위)
    >
    > let : 변수 값을 설정할 때 사용 (scope가 블록 단위)
    >
    > var : (scope가 함수 단위)

* 조건부 렌더링

  * JSX 내부에서 조건부 렌더링을 할 때에는 보통 삼항 연산자를 사용하거나, AND 연산자를 사용한다.

    ```react
    // 삼항 연산자 사용 예시 [true 또는 false]
    class App extends Component {
      render() {
        return (
          <div>
            { 
              1 + 1 === 2 
                ? (<div>맞아요!</div>)
                : (<div>틀려요!</div>)
            }
          </div>
        );
      }
    }
    ```

    ```react
    // AND 연산자 사용 예시 [true]
    class App extends Component {
      render() {
        return (
          <div>
            { 1 + 1 === 2 && (<div>맞아요!</div>) }
          </div>
        );
      }
    }
    ```

  * if 문을 사용할 수는 없으며, 사용하기 위해서는 IIFE라는 즉시 실행 함수 표현을 사용해야 한다.

    ```react
    // IIFE 사용 예시
    class App extends Component {
      render() {
        const value = 1;
        return (
          <div>
            {
              (function() {
                if (value === 1) return (<div>하나</div>);
                if (value === 2) return (<div>둘</div>);
                if (value === 3) return (<div>셋</div>);
              })()
            }
          </div>
        );
      }
    }
    ```

    ```react
    // Switch 사용 예시
    class App extends Component {
      render() {
        const value = 1;
        return (
          <div>
            (() => {
              if (value === 1) return (<div>하나</div>);
              if (value === 2) return (<div>둘</div>);
              if (value === 3) return (<div>셋</div>);
            })()
          </div>
        );
      }
    }
    ```

* ClassName

  * HTML에서 클래스를 설정할 때에는 `<div class='Hello'>`와 같이 사용했으나, react 컴포넌트에서는 class 대신에 className을 사용한다.

* Style, CSS

  * JSX에서 style과 CSS 클래스를 설정할 때에도 HTML과는 다르다. 그냥 텍스트 형태로 작성했던 HTML과는 달리 React에서는 객체 형태로 작성해주어야 한다.

    ```react
    // Style
    class App extends Component {
      render() {
        const style = {
          backgroundColor: 'black',
          padding: '16px',
          color: 'white',
          fontSize: '36px'
        };
        return <div style={style}>안녕하세요!</div>;
      }
    }
    ```

    ```react
    import React, { Component } from 'react';
    import './App.css'
    
    class App extends Component {
      render() {
        return (
          <div className="App"> 리액트 </div>
        );
      }
    }
    ```

* 주석

  * 마지막으로 주석은 아래와 같은 방법으로 작성된다.

    ```react
    class App extends Component {
      render() {
        return (
          <div>
            {/* 주석은 이렇게 작성되고 */}
            <h1
              // 태그 사이에 작성할 때는 이렇게 작성한다.
            >리액트</h1>
          </div>
        );
      }
    }
    ```



### props와 state

react 컴포넌트에서 다루는 데이터는 두 가지(props, state)로 구분할 수 있다.

props는 `부모 컴포넌트가 자식 컴포넌트에게 물려주는 값`이다. 따라서 자식 컴포넌트에서는 props를 받아오기만 하고, 받아온 props를 직접 수정할 수 없다.

반면, state는 `컴포넌트 내부에서 선언하며 내부에서 값을 변경`할 수 있다.

#### props

자신이 받아온 props 값은 `this.` 키워드를 통해 조회할 수 있다. 그리고 가끔씩 실수로 props를 빠뜨리는 경우가 있다. 또는 특정 상황에 props를 일부러 비워야 하는 경우도 있다. 그러한 경우에는 props의 기본값을 설정해줄 수도 있다. 이 때 사용하는 것이 바로 `defalutProps`이다.

```react
class MyName extends Component {
  static defaultProps = {
    name: '기본이름'
  }
  render() {
    return (
      <div>
        안녕하세요! 제 이름은 <b>{this.props.name}</b> 입니다.
      </div>
    );
  }
}
```

#### state

동적인 데이터를 다룰 때에는 state를 사용한다.

https://react-anyone.vlpt.us/04.html