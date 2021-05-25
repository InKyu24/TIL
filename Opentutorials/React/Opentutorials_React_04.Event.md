## React

### Event 02

사용자와 상호작용하는 애플리케이션의 핵심인 Event를 React에서 구현하는 방법을 알아보자.



### Component Event 만들기 01

event를 지금까지 사용자로써 event 프로그래밍을 통해 사용만 해왔다. 태그에 event를 직접 만들어서, 해당 태그 또는 그 component를 사용하는 사람들이 event 프로그래밍을 할 수 있도록 event의 생산자가 되어보자.

이를 위해서, 주석 처리해 놓았던 subject component를 다시 이용할 수 있도록 수정을 해놓을 것이다. 그리고 subject component에 event를 만들 것이다. subject component의 제작자, 생산자의 입장에서 subject component를 사용할 때에는 onChangePage라는 이벤트가 있어서, subject component 안에서 링크를 클릭했을 때 event에 설치한 함수를 호출하도록 할 것이다. 

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
        <Subject
          title={this.state.subject.title}
          sub={this.state.subject.sub}
          // onChangePage라고 하는 Event를 정의
          onChangePage={function(){
            alert('Hello');
            this.setState({mode:'welcome'});
          }.bind(this)}
        >
        </Subject>  
        <TOC data={this.state.contents}></TOC>
        <Content title={_title} desc={_desc}></Content>
      </div>
    );
  }
}
```

```react
class Subject extends Component {
  render() {
    return (
      <header>
          {/* a 태그를 클릭했을 때 기본 event를 제거하고, onChagePage event를 호출
          props 형태로 함수를 전달*/}
          <h1><a href="/" onClick={function(e){
            e.preventDefault();
            this.props.onChangePage();
          }.bind(this)}>{this.props.title}</a></h1>
          {this.props.sub}
      </header>           
    );
  }
}
```



### Component Event 만들기 02

이번에는 글 목록을 클릭했을 때, App component의 state 모드를 read로 바꾸기 위해서 TOC component에 onChangePage라는 이름의 Event를 생성할 것이다. 

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
        <Subject
          title={this.state.subject.title}
          sub={this.state.subject.sub}
          onChangePage={function(){
            alert('Hello');
            this.setState({mode:'welcome'});
          }.bind(this)}
        >
        </Subject>  
        <TOC
          data={this.state.contents}
          onChangePage={function(){
            alert('read');
            this.setState({mode:'read'});
          }.bind(this)}
          ></TOC>
        <Content title={_title} desc={_desc}></Content>
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
        lists.push(
          <li key={data[i].id}>
            <a
              href={"/content/"+data[i].id}
              onClick={function(e){
                e.preventDefault();
                this.props.onChangePage();
              }.bind(this)}
            >{data[i].title}</a>
          </li>)
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



### Component Event 만들기 03

이어서 클릭한 글 목록에 해당되는 content가 본문에 나오도록 해보자.

content를 본문에 나오게 하기 위해서, data-tocid를 정의하고 해당 값을 e.target.dataset.tocid로 불러와 onChangePage 함수의 매개변수로 사용하였다. 그리고 매개변수 값이 문자로 인식되기 때문에 Number 함수를 사용하여 숫자 값으로 변화를 주었다.

```react
class App extends Component {
  constructor(props) {
      super(props); // 초기화
      this.state = {
        mode:'read',
        // 기본적으로 2번 contents가 선택되도록 설정
        selected_contents_id:2,
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
      var i = 0;
      while(i < this.state.contents.length) {
        var data = this.state.contents[i];
        if (data.id === this.state.selected_contents_id) {
          _title = data.title;
          _desc = data.desc;
          break;  
        }
        i = i + 1;
      }
    }
    return (
      <div className="App">
        <Subject
          title={this.state.subject.title}
          sub={this.state.subject.sub}
          onChangePage={function(){
            alert('Hello');
            this.setState({mode:'welcome'});
          }.bind(this)}
        >
        </Subject>  
        <TOC
          data={this.state.contents}
          onChangePage={function(id){
            alert('read : '+id);
            this.setState({
              mode:'read',
              selected_contents_id:Number(id)
            }); 
          }.bind(this)}
          ></TOC>
        <Content title={_title} desc={_desc}></Content>
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
        lists.push(
          <li key={data[i].id}>
            <a
              href={"/content/"+data[i].id}
              data-tocid = {data[i].id}
              onClick={function(e){
                e.preventDefault();
                this.props.onChangePage(e.target.dataset.tocid);
              }.bind(this)}
            >{data[i].title}</a>
          </li>)
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

위와 같은 내용을 하는 또 다른 방법이 있다. 속성을 사용하지 않고, bind 함수에 파라미터를 추가하는 방법이다.

```react
class TOC extends Component {
  render() {
      var lists = [];
      var data = this.props.data;
      var i = 0;
      while (i < data.length) {
        lists.push(
          <li key={data[i].id}>
            <a
              href={"/content/"+data[i].id}
              data-tocid = {data[i].id}
              onClick={function(id, e){
                e.preventDefault();
                this.props.onChangePage(id);
              }.bind(this, data[i].id)}
            >{data[i].title}</a>
          </li>)
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

