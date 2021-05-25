## React

### Event 01

사용자와 상호작용하는 애플리케이션의 핵심인 Event를 React에서 구현하는 방법을 알아보자.



### Event, State, Props 그리고 render 함수

Event는 애플리케이션을 역동적으로 만들어주는 기술이다. Prop, State, Event는 세 가지가 모두 상호작용을 하면서 애플리케이션의 역동성을 만들어내기 때문에 함께 고민해 볼 필요가 있다.

목표는 해당 링크에 Event를 설치하여, App Component에 State가 변경되고, 그 변경된 State가 Content Component에 Props의 값으로 전달됨으로써 동적으로 애플리케이션이 바뀌는 것을 구현하는 것이다.

우선 최상단 타이틀에 링크를 넣는다.

```react
class Subject extends Component {
  render() {
    return (
      <header>
          <h1><a href="/">{this.props.title}</a></h1>
          {this.props.sub}
      </header>           
    );
  }
}
```

페이지를 구분하기 위해서 App Component 내 state에 mode라는 값을 'welcome'으로 부여할 것이다.

그리고 mode가 'welcome'인 경우에는 contents 영역에 표시할 텍스트도 지정을 하겠다.

```react
class App extends Component {
  constructor(props) {
      super(props); // 초기화
      mode:'welcome',
      this.state = {
          subject:{title:'WEB', sub:'World wide web!'},
          welcome:{title:'Welcome', desc:'Hello, React!'},
          contents:[
            {id:1, title:'HTML', desc:'HTML is HyperText Markup Language.'},
            {id:2, title:'CSS', desc:'CSS is for design.'},
            {id:3, title:'JavaScript', desc:'JavaScript is for interactive.'}
          ]
      }
  }
  render() {
    return (
      <div className="App">
        <Subject title={this.state.subject.title} sub={this.state.subject.sub}></Subject> 
        <TOC data={this.state.contents}></TOC>
        <Content title="HTML" desc="HTML is HyperText Markup Language."></Content>
      </div>
    );
  }
}
```

여기서 또 하나의 중요한 사실을 알게 된 것이다. React에서는 Props나 State 값이 바뀌게 되면, Component의 render 함수가 다시 호출된다는 것이다. 그리고 그 render 함수가 다시 호출됨에 따라서 그 render 함수 하위에 있는 Component들도 각자 보유하고 있는 render 함수들도 다시 호출된다. 그렇게 화면이 다시 그려지게 된다.

render라는 함수가 하는 일은 어떤 HTML을 그릴 것인가를 결정하는 역할을 하기 때문이다.

그러면, mode의 값에 따라 만들어지는 render 결과가 달라질 수 있도록 조건문을 넣겠다.

```react
class App extends Component {
   constructor(props) {
      super(props); // 초기화
      this.state = {
        mode:'welcome',
        subject:{title:'WEB', sub:'World wide web!'},
        welcome:{title:'Welcome', desc:'Hello, React!'},
        contents:[
          {id:1, title:'HTML', desc:'HTML is HyperText Markup Language.'},
          {id:2, title:'CSS', desc:'CSS is for design.'},
          {id:3, title:'JavaScript', desc:'JavaScript is for interactive.'}
        ]
      }
  }
  render() {
    var _title, _desc = null;  
    if(this.state.mode === 'welcome') {
        _title = this.state.welcome.title;
        _desc = this.state.welcome.desc;
         
    } else if (this.state.mode === 'read'){
        _title = this.state.contents[0].title;
        _desc = this.state.contents[0].desc;
    }
    return (
      <div className="App">
        <Subject title={this.state.subject.title} sub={this.state.subject.sub}></Subject>
        <TOC data={this.state.contents}></TOC>
        <Content title={_title} desc={_desc}></Content>
      </div>
    );
  }
}
```



### Event 설치

React에서 Event 프로그래밍을 어떻게 하는가를 살펴보자. 최종적으로는 생성한 링크를 클릭했을 때 Subject 바깥쪽에 있는 App에 State를 바꿔주는 것을 할 것이다.

일단은 Subject Component를 풀어서 안에 있는 내용을 그대로 App에 도입할 것이고, Event를 구현해볼 것이다. 따라서 현재 Subject Component는 존재하지만 사용하지 않는 상태가 된다.

```react
class App extends Component {
  constructor(props) {
      super(props); // 초기화
      this.state = {
        mode:'welcome',
        subject:{title:'WEB', sub:'World wide web!'},
        welcome:{title:'Welcome', desc:'Hello, React!'},
        contents:[
          {id:1, title:'HTML', desc:'HTML is HyperText Markup Language.'},
          {id:2, title:'CSS', desc:'CSS is for design.'},
          {id:3, title:'JavaScript', desc:'JavaScript is for interactive.'}
        ]
      }
  }
  render() {
    var _title, _desc = null;  
    if(this.state.mode === 'welcome') {
        _title = this.state.welcome.title;
        _desc = this.state.welcome.desc;
         
    } else if (this.state.mode === 'read'){
        _title = this.state.contents[0].title;
        _desc = this.state.contents[0].desc;
    }
    return (
      <div className="App">
        {/* <Subject title={this.state.subject.title} sub={this.state.subject.sub}></Subject> */}
        <header>
            <h1>
                <a href="/" onClick={function() {
                        alert("HI");
                    }}>{this.state.subject.title}</a></h1>
            {this.state.subject.sub}
        </header>   
        <TOC data={this.state.contents}></TOC>
        <Content title={_title} desc={_desc}></Content>
      </div>
    );
  }
}
```

위와 같이 코드를 작성하면, 제목을 클릭했을 때 HI가 경고창으로 나타난다. 하지만 경고창에 확인 버튼을 클릭하게 되면 페이지가 reload된다. React 사용의 이점은 reload를 하지 않고도 역동적인 사이트를 제작할 수 있다는 것인데, 이렇게 제작하게 되면 React의 이점을 이용하지 않으면서 React를 사용하는 꼴이 되어버린다.

따라서 a라는 태그는 href의 속성이 가리키는 페이지로 이동하는 기본적인 동작을 못하도록 기본 Event를 제거해주어야 한다. 

React는 Event에 설치한 함수의 매개변수 값으로 Event 객체를 주입하는 것이 약속되어 있다. 따라서 onClick이라는 Event에 설치한 함수의 매개변수의 값을 넣어주어야 한다. 매개변수를 e라고 부여한 후에, e라는 객체에 내장된 함수(`preventDefault`)를 사용할 것이다. 이렇게 기본 Event를 제거할 수 있다.

```react
class App extends Component {
  constructor(props) {
      super(props); // 초기화
      this.state = {
        mode:'welcome',
        subject:{title:'WEB', sub:'World wide web!'},
        welcome:{title:'Welcome', desc:'Hello, React!'},
        contents:[
          {id:1, title:'HTML', desc:'HTML is HyperText Markup Language.'},
          {id:2, title:'CSS', desc:'CSS is for design.'},
          {id:3, title:'JavaScript', desc:'JavaScript is for interactive.'}
        ]
      }
  }
  render() {
    var _title, _desc = null;  
    if(this.state.mode === 'welcome') {
        _title = this.state.welcome.title;
        _desc = this.state.welcome.desc;
         
    } else if (this.state.mode === 'read'){
        _title = this.state.contents[0].title;
        _desc = this.state.contents[0].desc;
    }
    return (
      <div className="App">
        {/* <Subject title={this.state.subject.title} sub={this.state.subject.sub}></Subject> */}
        <header>
          <h1>
            <a href="/" onClick={function(e) {
              alert("HI");
              e.preventDefault();
            }}>
            {this.state.subject.title}</a>
          </h1>
          {this.state.subject.sub}
        </header>   
        <TOC data={this.state.contents}></TOC>
        <Content title={_title} desc={_desc}></Content>
      </div>
    );
  }
}
```



### Event에서 State 변경하기

지금까지 State를 세팅해놓은 작업과 Event를 설치한 작업을 연결시키기만 하면 된다.

그렇게 해서, WEB이라고 쓰여있는 제목을 클릭했을 때, App Component의 mode 값을 welcome으로 바꿔줄 것이다. 변화를 확인하기 위해서 현재 mode를 read로 변경해두었다.

Event에서 mode를 welcome으로 바꿔주는 코드를 아래와 같이 작성하였다.

```react
class App extends Component {
  constructor(props) {
      super(props); // 초기화
      this.state = {
        mode:'read',
        subject:{title:'WEB', sub:'World wide web!'},
        welcome:{title:'Welcome', desc:'Hello, React!'},
        contents:[
          {id:1, title:'HTML', desc:'HTML is HyperText Markup Language.'},
          {id:2, title:'CSS', desc:'CSS is for design.'},
          {id:3, title:'JavaScript', desc:'JavaScript is for interactive.'}
        ]
      }
  }
  render() {
    var _title, _desc = null;  
    if(this.state.mode === 'welcome') {
        _title = this.state.welcome.title;
        _desc = this.state.welcome.desc;
         
    } else if (this.state.mode === 'read'){
        _title = this.state.contents[0].title;
        _desc = this.state.contents[0].desc;
    }
    return (
      <div className="App">
        {/* <Subject title={this.state.subject.title} sub={this.state.subject.sub}></Subject> */}
        <header>
          <h1>
            <a href="/" onClick={function(e) {
              alert("HI");
              e.preventDefault();
              this.state.mode = 'welcome';
            }}>
            {this.state.subject.title}</a>
          </h1>
          {this.state.subject.sub}
        </header>   
        <TOC data={this.state.contents}></TOC>
        <Content title={_title} desc={_desc}></Content>
      </div>
    );
  }
}
```

하지만 해당 코드를 실행하게 되면 `Cannot read property 'state' of undefined` 에러가 나타나게 된다. 그 이유는 `this.state.mode = 'welcome';`라고 작성한 코드에는 두 가지의 문제를 가지고 있기 때문이다. 

첫 번째 문제는 이 이벤트가 호출되었을 때, 실행되는 함수인 `function(e)` 내에서는 this의 값이 component 자기 자신을 가리키지 않고, 아무런 값도 세팅되어 있지 않다. 그렇기 때문에 에러가 나타나는 것이다. 이벤트를 설치할 때, this를 찾을 수 없어서 에러가 발생하면 해당 함수가 끝난 직후에 `.bind(this)`를 추가해주면 된다. 그러면 해당 함수 내에서 this는 component를 가리킬 수 있게 된다.

```react
class App extends Component {
  constructor(props) {
      super(props); // 초기화
      this.state = {
        mode:'read',
        subject:{title:'WEB', sub:'World wide web!'},
        welcome:{title:'Welcome', desc:'Hello, React!'},
        contents:[
          {id:1, title:'HTML', desc:'HTML is HyperText Markup Language.'},
          {id:2, title:'CSS', desc:'CSS is for design.'},
          {id:3, title:'JavaScript', desc:'JavaScript is for interactive.'}
        ]
      }
  }
  render() {
    var _title, _desc = null;  
    if(this.state.mode === 'welcome') {
        _title = this.state.welcome.title;
        _desc = this.state.welcome.desc;
         
    } else if (this.state.mode === 'read'){
        _title = this.state.contents[0].title;
        _desc = this.state.contents[0].desc;
    }
    return (
      <div className="App">
        {/* <Subject title={this.state.subject.title} sub={this.state.subject.sub}></Subject> */}
        <header>
          <h1>
            <a href="/" onClick={function(e) {
              alert("HI");
              e.preventDefault();
              this.state.mode = 'welcome';
            }.bind(this)}>
            {this.state.subject.title}</a>
          </h1>
          {this.state.subject.sub}
        </header>   
        <TOC data={this.state.contents}></TOC>
        <Content title={_title} desc={_desc}></Content>
      </div>
    );
  }
}
```

하지만 이러한 조치를 취하더라도 아무 것도 바뀌지 않는다. 왜냐하면 두 번째 문제가 남아있기 때문이다. 

두 번째 문제는 React는 state 값이 바뀌었다는 사실을 모른다는 것이다. React에서는 `this.setState({mode:'welcome'})`와 같이 setState라는 함수를 호출하고, 바꾸고 싶은 값을 파라미터로 적용시켜주면 된다. 

```react
class App extends Component {
  constructor(props) {
      super(props); // 초기화
      this.state = {
        mode:'read',
        subject:{title:'WEB', sub:'World wide web!'},
        welcome:{title:'Welcome', desc:'Hello, React!'},
        contents:[
          {id:1, title:'HTML', desc:'HTML is HyperText Markup Language.'},
          {id:2, title:'CSS', desc:'CSS is for design.'},
          {id:3, title:'JavaScript', desc:'JavaScript is for interactive.'}
        ]
      }
  }
  render() {
    var _title, _desc = null;  
    if(this.state.mode === 'welcome') {
        _title = this.state.welcome.title;
        _desc = this.state.welcome.desc;
         
    } else if (this.state.mode === 'read'){
        _title = this.state.contents[0].title;
        _desc = this.state.contents[0].desc;
    }
    return (
      <div className="App">
        {/* <Subject title={this.state.subject.title} sub={this.state.subject.sub}></Subject> */}
        <header>
          <h1>
            <a href="/" onClick={function(e) {
              alert("HI");
              e.preventDefault();
              this.setState({mode:'welcome'});
            }.bind(this)}>
            {this.state.subject.title}</a>
          </h1>
          {this.state.subject.sub}
        </header>   
        <TOC data={this.state.contents}></TOC>
        <Content title={_title} desc={_desc}></Content>
      </div>
    );
  }
}
```



### Event에서 bind 함수 이해하기

bind라는 것은 무언가를 엮는 역할을 한다. 기본적으로 render라는 함수가 호출될 때, render 함수 안에서 this는 component 자신을 가리킨다. 하지만 설치된 event 내의 함수에서는 this 값을 component 자신은 물론 아무것도 가리키지 않는다. 그럴 때 bind 함수를 이용해 강제로 this 값을 주입시켜주는 것이다. 

```javascript
var obj = {name:'inkyu'}

function bindTest(){
    console.log(this.name);    
}
bindTest();			// 결과값 : 'undefined'

var bindTest2 = bindTest.bind(obj)
bindTest2();		// 결과값 : 'inkyu'
```

 

### Event에서 setState 함수 이해하기

state 값을 직접 변경하면 안되고, setState 함수 형태로 state 값을 변경해야하는 이유에 대해서 알아보자.

React 입장에서 Component가 생성된 후에 state 값을 직접 변경하게 되면, 사용자가 몰래 바꾼 셈이 된다. 따라서 React를 변경된 state 값을 받아들이지 못한다. state 값은 변경되는 것이지만, render를 할 수 없는 상태가 도니다. 

Component가 생성될 때 최초로 가장 먼저 실행되는 constructor라는 함수에서는 state 값을 직접 변경할 수 있다. 하지만 이미 Component의 생성이 끝난 후에 동적으로 state 값을 바꿀 때에는  setState 함수를 사용해야 하는 것이다.