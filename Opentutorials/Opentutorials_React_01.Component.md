## React

### Component 제작

App이라는 클래스를 만든다.
App이라는 클래스는 React의 Component를 상속받는다.
그리고 App이라는 클래스는 render라는 메서드를 가지고 있다.

```react
class App extends Component {
	render() {
		return (
			<div className="App">Hello, React</div>
		);
	}
}

export defalut App;
```

웹 브라우저는 React의 개념을 알지 못한다. 따라서 React.js는 유사 JavaScript(JSX)이다. 따라서 JavaScript(JS)와 유사해보일 뿐 JavaScript가 아니다.



이제 Component를 만들어보자.

```react
class Content extends Component {
  render() {
    return (
      <article>
        <h2>HTML</h2>
        HTML is HyperText Markup Language.
      </article>         
    );
  }
}

class TOC extends Component {
  render() {
    return (
      <nav>
        <ul>
          <li><a href="1.html">HTML</a></li>
          <li><a href="2.html">CSS</a></li>
          <li><a href="3.html">JavaScript</a></li>
        </ul>
      </nav>           
    );
  }
}

class Subject extends Component {
  render() {
    return (
      <header>
        <h1>WEB</h1>
        World Wide Web!
      </header>
    );
  }
}

class App extends Component {
  render() {
    return (
      <div className="App">
        <Subject></Subject>
        <TOC></TOC>
        <Content></Content>
      </div>
    );
  }
}
```

React의 Component를 바라보는 첫 번째 시각은 정리정돈의 도구로 보자. 마치 집에 널부러진 물건을 정리정돈하여 자리에 이름을 붙여놓는 것처럼 말이다. 



### Props

언제나 똑같은 값을 보여주게 되는 Component의 속성 값 부분만을 개별적으로 넣을 수 있도록 Props를 이용할 수 있다. 이로써 재사용성을 현저하게 높일 수 있다.

```react
class Content extends Component {
  render() {
    return (
      <article>
        <h2>{this.props.title}</h2>
		{this.props.desc}
      </article>         
    );
  }
}

class TOC extends Component {
  render() {
    return (
      <nav>
        <ul>
          <li><a href="1.html">HTML</a></li>
          <li><a href="2.html">CSS</a></li>
          <li><a href="3.html">JavaScript</a></li>
        </ul>
      </nav>           
    );
  }
}

class Subject extends Component {
  render() {
    return (
      <header>
        <h1>{this.props.title}</h1>
        {this.props.sub}
      </header>
    );
  }
}

class App extends Component {
  render() {
    return (
      <div className="App">
        <Subject title="WEB" sub="World wide web!"></Subject>
        <Subject title="React" sub="For UI"></Subject>    
        <TOC></TOC>
        <Content title="HTML" desc="HTML is HyperText Markup Language."></Content>
      </div>
    );
  }
}
```



### [React Developer Tools](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi)

크롬 확장 프로그램을 설치하면, JavaScript가 아닌 React.js의 소스 코드들을 확인할 수 있다.



### Component 파일로 분리하기

1. src 경로 내에 component 폴더를 생성한다.

2. App.js 에 있는 클래스 이름으로 component 폴더 내에 .js 파일을 생성한다.

3. App.js에 해당 클래스가 선언되는 부분을 component 폴더 내 .js 파일에 옮겨 적는다.

4. 맨 윗 라인에 `import React, { Component } from 'react';`를 적는다.

5. 마지막 라인에 `export default TOC;`를 적는다.

6. App.js 파일에서 작성한 js 파일을 import 한다.

   `import Subject from './components/~';`

