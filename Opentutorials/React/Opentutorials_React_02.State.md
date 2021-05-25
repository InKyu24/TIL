## React

### State 소개

State라고 하는 개념을 살펴보자.

State라는 개념은 Props와 함께 서로 간의 차이점을 생각하면서 이해하려 한다면, 더 잘 이해할 수 있다.

우선 비유를 이용해 파악해보자. 어떤 제품이 있고, 그 제품에 대한 사용자의 입장과 구현자의 입장이 있다.

일반적인 사용자는 버튼을 통해 제품을 조작한다. 그리고 이를 UI라고 부르기도 하는데, 이것이 react에서 말하는 props가 되는 것이다. 그렇다면 제품을 만드는 구현자는 내부적인 구현을 위해서 내부적 조작장치 매커니즘들을 가지고 있는데 그러한 것들을 State라고 말할 수 있다.

즉, Props는 사용자가 Component를 사용하는 입장에서 중요한 것이고, State는 Props의 값에 따라 내부 구현에 필요한 데이터들이라 할수 있다.

> Component를 외부에서 조작할 때는 props를 사용한다.
>
> Component를 내부적으로 상태를 관리할 때는 state를 사용한다.

### State 사용

Props값을 State로 만들고, 그 State의 값을 Subject의 Props로? 전달하는 것을 통해서 코드를 개선한다.

1. Subject Component는 아래와 같이 작성되어 있다.

```react
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
```

2. App.js에서는 Subject Component를 아래와 같이 사용하고 있다.

```react
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

3. App.js에 존재하는 App Component를 아래와 같이 바꿔보자

```react
class App extends Component {
// 어떠한 Component가 실행될 때, render라고 하는 메서드보다 먼저 실행이 되면서 해당 Component를 초기화시켜주고 싶은 코드는 생성자 내부에 코드를 작성한다.
  constructor(props) {
      super(props); // 초기화
      this.state = {
          subject:{title:"WEB", sub:"World wide web!"}
      }
  }
  render() {
    return (
      <div className="App">
        <Subject title={this.state.subject.title} sub={this.state.subject.sub}></Subject>
        <Subject title="React" sub="For UI"></Subject>    
        <TOC></TOC>
        <Content title="HTML" desc="HTML is HyperText Markup Language."></Content>
      </div>
    );
  }
}
```

> 상위 Component의 App의 상태를 하위 Component로 전달하는 것은 가능하다. 
>
> [상위 Component의 state 값을 하위 Component의 props의 값으로 전달]



### Key

익숙해질 수 있도록 State를 조금 더 사용해보자. 지금까지 배웠던 State는 단일 엘리먼트만을 생성하고 전달했다. 이제는 복수의 엘리먼트를 다루는 것은 약간의 사용법이 다르다.

```react
class App extends Component {
  // 어떠한 Component가 실행될 때, render라고 하는 메서드보다 먼저 실행이 되면서 해당 Component를 초기화시켜주고 싶은 코드는 생성자 내부에 코드를 작성한다.
  constructor(props) {
      super(props); // 초기화
      this.state = {
          subject:{title:'WEB', sub:'World wide web!'},
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
        <Subject title="React" sub="For UI"></Subject>    
        <TOC data={this.state.contents}></TOC>
        <Content title="HTML" desc="HTML is HyperText Markup Language."></Content>
      </div>
    );
  }
}
```

```react
class TOC extends Component {
  render() {
      var lists = [];
      var data = this.props.data;
      var i = 0;
      while (i < data.length) {
          lists.push(<li><a href={"/content/"+data[i].id}>{data[i].title}</a></li>)
          i = i + 1;
      }
      
    return (
      <nav>
        <ul>
          {lists}
        </ul>
      </nav>           
    );
  }
}
```

위와 같이 복수의 엘리먼트를 생성할 때, 한 가지 주의할 점이 있다. 여러 개의 엘리먼트를 자동으로 생성하는 경우에는 브라우저 개발자 도구를 열어보면, 에러가 발생한다. `Each Child in a list should have a unique "key" prop.`

각각의 List 항목들은 고유의 prop를 가지고 있어야 하고, 이를 key라고 부른다. 다시 말해서 key라는 특수한 props를 부여해야 한다는 것이다. 이제 key의 사용법을 알아보자.

```react
class TOC extends Component {
  render() {
      var lists = [];
      var data = this.props.data;
      var i = 0;
      while (i < data.length) {
          lists.push(<li key={data[i].id}><a href={"/content/"+data[i].id}>{data[i].title}</a></li>)
          i = i + 1;
      }
      
    return (
      <nav>
        <ul>
          {lists}
        </ul>
      </nav>           
    );
  }
}
```

이렇게 부여된 key 값은 만들고 있는 애플리케이션에서 사용되는 것은 아니고, React의 내부적인 필요의 의해서 요청하는 것이다. key 값을 부여하면 더 이상 에러는 나타나지 않게 된다.