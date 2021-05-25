## React

### Update 기능 구현

Read 기능와 Create 기능이 결합되었다고 볼 수 있는 Update 기능을 구현해보자. Update를 한다는 것은 기존의 컨텐츠를 수정하는 것이기 때문에 Read처럼 기존의 컨텐츠를 불러와서 form에 내용을 추가해주는 작업이 필요하다.

UpdateContent component를 생성하고 App.js에 추가한다.

```react
class App extends Component {
  constructor(props) {
      super(props);
      this.max_content_id=3;
      this.state = {
        mode:'read',
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
    var _title, _desc, _article = null;
      
    if(this.state.mode === 'welcome') {
      _title = this.state.welcome.title;
      _desc = this.state.welcome.desc;
      _article = <ReadContent title={_title} desc={_desc}></ReadContent>
          
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
      _article = <ReadContent title={_title} desc={_desc}></ReadContent>
          
    } else if(this.state.mode === 'create') {
      _article = <CreateContent onSubmit={function(_title, _desc){
        this.max_content_id = this.max_content_id+1;
        var _contents = this.state.contents.concat(
          {id:this.max_content_id, title:_title, desc:_desc}
        );
        this.setState({
          contents:_contents 
        });
        console.log(_title, _desc);
      }.bind(this)}></CreateContent>
          
    } else if(this.state.mode === 'update') {
      _article = <UpdateContent onSubmit={function(_title, _desc){
        this.max_content_id = this.max_content_id+1;
        var _contents = this.state.contents.concat(
          {id:this.max_content_id, title:_title, desc:_desc}
        );
        this.setState({
          contents:_contents 
        });
        console.log(_title, _desc);
      }.bind(this)}></UpdateContent>
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
        <Control onChangeMode={function(_mode){
          this.setState({
            mode:_mode
          });
        }.bind(this)}></Control>
        {_article}
      </div>
    );
  }
}
```

```react
class UpdateContent extends Component {
    render() {
      return (
        <article>
          <h2>Update</h2>
          <form action="/update_process" method="post"
            onSubmit={function(e){
              e.preventDefault();
              this.props.onSubmit( 
                e.target.title.value,
                e.target.desc.value
              );
              alert("submit!!!");
            }.bind(this)}>
            <p>
              <input type="text" name="title" placeholder="title"></input>
            </p>
            <p>
              <textarea name="desc" placeholder="description"></textarea>
            </p>
            <p>
              <input type="submit"></input>
            </p>
          </form>
        </article>            
      );
    }
}
```

위와 같이 코드를 추가하게 되면 render 함수가 상당히 길어져서 가독성이 떨어지고 있다. 그래서 render 함수 내에서 _article의 표시를 담당하는 부분들을 getContent() 함수로 새롭게 정의하고, 이를 호출하는 방식으로 변경할 것이다.

```react
class App extends Component {
  constructor(props) {
      super(props);
      this.max_content_id=3;
      this.state = {
        mode:'read',
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
  // getContent 함수 정의
  getContent() {
    var _title, _desc, _article = null;
      
    if(this.state.mode === 'welcome') {
      _title = this.state.welcome.title;
      _desc = this.state.welcome.desc;
      _article = <ReadContent title={_title} desc={_desc}></ReadContent>
          
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
      _article = <ReadContent title={_title} desc={_desc}></ReadContent>
          
    } else if(this.state.mode === 'create') {
      _article = <CreateContent onSubmit={function(_title, _desc){
        this.max_content_id = this.max_content_id+1;
        var _contents = this.state.contents.concat(
          {id:this.max_content_id, title:_title, desc:_desc}
        );
        this.setState({
          contents:_contents 
        });
        console.log(_title, _desc);
      }.bind(this)}></CreateContent>
          
    } else if(this.state.mode === 'update') {
      _article = <UpdateContent onSubmit={function(_title, _desc){
        this.max_content_id = this.max_content_id+1;
        var _contents = this.state.contents.concat(
          {id:this.max_content_id, title:_title, desc:_desc}
        );
        this.setState({
          contents:_contents 
        });
        console.log(_title, _desc);
      }.bind(this)}></UpdateContent>
    }  
      return _article;
  }

  render() {    
    
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
        <Control onChangeMode={function(_mode){
          this.setState({
            mode:_mode
          });
        }.bind(this)}></Control>
        <!-- getContent 함수 호출 -->
        {this.getContent()}
      </div>
    );
  }
}
```

이제 update 버튼을 클릭하게 되면, 선택된 콘텐츠의 title과 desc가 나타나도록 해볼 것이다. 이는 Read 기능을 이용할 것이고 코드의 가독성을 높이기 위해 GetReadContent라는 함수를 정의하는 것까지 동시에 진행해볼 것이다.

```react
class App extends Component {
  constructor(props) {
      super(props);
      this.max_content_id=3;
      this.state = {
        mode:'read',
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
  // getReadContent 함수 정의
  getReadContent() {
    var i = 0;
    while(i < this.state.contents.length) {
      var _content = this.state.contents[i];
      if (_content.id === this.state.selected_contents_id) {
        //_title = data.title;
        //_desc = data.desc;
        return _content;
        break;  
      }
      i = i + 1;
    }
  }

  getContent() {
    var _title, _desc, _article = null;
      
    if(this.state.mode === 'welcome') {
      _title = this.state.welcome.title;
      _desc = this.state.welcome.desc;
      _article = <ReadContent title={_title} desc={_desc}></ReadContent>
          
    } else if (this.state.mode === 'read'){
      // getReadContent 함수 호출
      _article = <ReadContent title={this.getReadContent().title} desc={this.getReadContent().desc}></ReadContent>
          
    } else if(this.state.mode === 'create') {
      _article = <CreateContent onSubmit={function(_title, _desc){
        this.max_content_id = this.max_content_id+1;
        var _contents = this.state.contents.concat(
          {id:this.max_content_id, title:_title, desc:_desc}
        );
        this.setState({
          contents:_contents 
        });
        console.log(_title, _desc);
      }.bind(this)}></CreateContent>
          
    } else if(this.state.mode === 'update') {
      _article = <UpdateContent onSubmit={function(_title, _desc){
        this.max_content_id = this.max_content_id+1;
        var _contents = this.state.contents.concat(
          {id:this.max_content_id, title:_title, desc:_desc}
        );
        this.setState({
          contents:_contents 
        });
        console.log(_title, _desc);
      }.bind(this)}></UpdateContent>
    }  
      return _article;
  }

  render() {    
    
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
        <Control onChangeMode={function(_mode){
          this.setState({
            mode:_mode
          });
        }.bind(this)}></Control>
        {this.getContent()}
      </div>
    );
  }
}
```



update 부분에서 getReadContent 함수의 결과값을 사용할 수 있도록 해볼 것이다.

```react
class App extends Component {
  constructor(props) {
      super(props);
      this.max_content_id=3;
      this.state = {
        mode:'read',
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
  getReadContent() {
    var i = 0;
    while(i < this.state.contents.length) {
      var _content = this.state.contents[i];
      if (_content.id === this.state.selected_contents_id) {
        //_title = data.title;
        //_desc = data.desc;
        return _content;
        break;  
      }
      i = i + 1;
    }
  }

  getContent() {
    var _title, _desc, _article = null;
      
    if(this.state.mode === 'welcome') {
      _title = this.state.welcome.title;
      _desc = this.state.welcome.desc;
      _article = <ReadContent title={_title} desc={_desc}></ReadContent>
          
    } else if (this.state.mode === 'read'){      
      _article = <ReadContent title={this.getReadContent().title} desc={this.getReadContent().desc}></ReadContent>
          
    } else if(this.state.mode === 'create') {
      _article = <CreateContent onSubmit={function(_title, _desc){
        this.max_content_id = this.max_content_id+1;
        var _contents = this.state.contents.concat(
          {id:this.max_content_id, title:_title, desc:_desc}
        );
        this.setState({
          contents:_contents 
        });
        console.log(_title, _desc);
      }.bind(this)}></CreateContent>
          
    } else if(this.state.mode === 'update') {
      // getReadContent에서 얻은 data를 update component에서 사용할 수 있도록 주입
      _article = <UpdateContent data={this.getReadContent()} onSubmit={function(_title, _desc){
        this.max_content_id = this.max_content_id+1;
        var _contents = this.state.contents.concat(
          {id:this.max_content_id, title:_title, desc:_desc}
        );
        this.setState({
          contents:_contents 
        });
        console.log(_title, _desc);
      }.bind(this)}></UpdateContent>
    }  
      return _article;
  }

  render() {    
    
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
        <Control onChangeMode={function(_mode){
          this.setState({
            mode:_mode
          });
        }.bind(this)}></Control>
        {this.getContent()}
      </div>
    );
  }
}
```



### Update 기능 구현 : form 작업

Update component에서 title의 value값에 getReadContent 함수의 결과값을 나타나게 하기 위해 아래와 같이 만들었다.

```react
class UpdateContent extends Component {
    render() {
      return (
        <article>
          <h2>Update</h2>
          <form action="/update_process" method="post"
            onSubmit={function(e){
              e.preventDefault();
              this.props.onSubmit( 
                e.target.title.value,
                e.target.desc.value
              );
              alert("submit!!!");
            }.bind(this)}>
            <p>
              <input 
                  type="text" 
                  name="title" 
                  placeholder="title" 
                  value={this.props.data.title}
              >
              </input>
            </p>
            <p>
              <textarea name="desc" placeholder="description"></textarea>
            </p>
            <p>
              <input type="submit"></input>
            </p>
          </form>
        </article>            
      );
    }
}

export default UpdateContent;
```

물론 값이 input 태그 내에 나타나는 것을 확인할 수 있지만, 수정이 불가능하다. 그 원인은 개발자 도구에서 확인 가능하다. 

> `Warning: You provided a 'value' prop to a form field without an 'onChange' handler. This will render a read-only field. If the field should be mutable use 'defaultValue'. Otherwise, set either 'onChange' or 'readOnly'.` 
>
> (onChange라는 handler 없이 Props를 직접 value에 넣어버리게 되면,  읽기 전용이 되어버린다.)

props의 데이터는 읽기 전용이기에 React가 중간에 개입하여, 편집 기능을 막는 것이다. 

따라서 value 값으로 가변적인 데이터가 들어갈 수 있도록 state화를 시켜주고,  onChange Handler를 달아주어야 한다.

```react
class UpdateContent extends Component {
    // render 함수보다 먼저 실행되면서 Component를 초기화
    constructor(props){
      super(props);
      // state에 props 값 대입
      this.state = {title: this.props.data.title}
    }
    render() {
      return (
        <article>
          <h2>Update</h2>
          <form action="/update_process" method="post"
            onSubmit={function(e){
              e.preventDefault();
              this.props.onSubmit( 
                e.target.title.value,
                e.target.desc.value
              );
              alert("submit!!!");
            }.bind(this)}>
            <p>
              <input
                type="text"
                name="title"
                placeholder="title"
                value={this.state.title} // value 값에 state 대입  
                onChange={function(e){
                  // value 값이 변할 때마다 state.title 값으로 계속해서 동기화
                  this.setState({title:e.target.value});
                }.bind(this)}
              >
              </input>
            </p>
            <p>
              <textarea name="desc" placeholder="description"></textarea>
            </p>
            <p>
              <input type="submit"></input>
            </p>
          </form>
        </article>            
      );
    }
}
```

Description 부분도 이처럼 진행하게 되면, 아래와 같은 코드를 완성할 수 있게 된다.

```react
class UpdateContent extends Component {
    constructor(props){
      super(props);
      this.state = {
        title:this.props.data.title,
        desc:this.props.data.desc
      }
    }
    render() {
      return (
        <article>
          <h2>Update</h2>
          <form action="/update_process" method="post"
            onSubmit={function(e){
              e.preventDefault();
              this.props.onSubmit( 
                e.target.title.value,
                e.target.desc.value
              );
              alert("submit!!!");
            }.bind(this)}>
            <p>
              <input
                type="text"
                name="title"
                placeholder="title"
                value={this.state.title}
                onChange={function(e){
                  console.log(e.target.value);
                  this.setState({title:e.target.value});
                }.bind(this)}
              >
              </input>
            </p>
            <p>
              <textarea name="desc"
                placeholder="description"
                value={this.state.desc}
                onChange={function(e){
                  this.setState({desc:e.target.value})
                }.bind(this)}
              >
              </textarea>
            </p>
            <p>
              <input type="submit"></input>
            </p>
          </form>
        </article>            
      );
    }
}
```

이런 방식으로 하나하나 onChange를 만드는 것은 불편한 일이기 때문에 inputFormHandler라는 함수를 정의하여, 중복을 제거해줄 것이다.

```react
class UpdateContent extends Component {
    constructor(props){
      super(props);
      this.state = {
        title:this.props.data.title,
        desc:this.props.data.desc
      }
      // 계속 사용되는 .bind(this)를 정의하여 중복 제거  
      this.inputFormHandler = this.inputFormHandler.bind(this);  
    }
    // inputFormHandler 함수 정의
    // [e.target.name]으로 사용되는 것!!!
    inputFormHandler(e){
      this.setState({[e.target.name]:e.target.value});
    }
    render() {
      return (
        <article>
          <h2>Update</h2>
          <form action="/update_process" method="post"
            onSubmit={function(e){
              e.preventDefault();
              this.props.onSubmit( 
                e.target.title.value,
                e.target.desc.value
              );
              alert("submit!!!");
            }.bind(this)}>
            <p>
              <input
                type="text"
                name="title"
                placeholder="title"
                value={this.state.title}
                // inputFormHandler 함수 호출
                onChange={this.inputFormHandler}
              >
              </input>
            </p>
            <p>
              <textarea name="desc"
                placeholder="description"
                value={this.state.desc}
                // inputFormHandler 함수 호출  
                onChange={this.inputFormHandler}
              >
              </textarea>
            </p>
            <p>
              <input type="submit"></input>
            </p>
          </form>
        </article>            
      );
    }
}
```



### Update 기능 구현 : state 변경

props로 들어온 데이터를 state로 만들고, 각각의 form과 동기화시켜서 state의 값을 계속해서 변화될 수 있도록 만들어보았다.

```react
class UpdateContent extends Component {
    constructor(props){
      super(props);
      this.state = {
        id:this.props.data.id,
        title:this.props.data.title,
        desc:this.props.data.desc
      }
      this.inputFormHandler = this.inputFormHandler.bind(this);  
    }
    inputFormHandler(e){
      this.setState({[e.target.name]:e.target.value});
    }
    render() {
      return (
        <article>
          <h2>Update</h2>
          <form action="/update_process" method="post"
            onSubmit={function(e){
              e.preventDefault();
              // onSubmit 함수에 파라미터 this.state.id를 추가
              this.props.onSubmit( 
                this.state.id,
                this.state.title,
                this.state.desc
              );
              alert("update!!!");
            }.bind(this)}>
            <!-- hidden 태그를 통해 this.state.id 값을 추가 -->  
            <input type="hidden" name="id" value={this.state.id}></input>
            <p>
              <input
                type="text"
                name="title"
                placeholder="title"
                value={this.state.title}
                onChange={this.inputFormHandler}
              >
              </input>
            </p>
            <p>
              <textarea name="desc"
                placeholder="description"
                value={this.state.desc}
                onChange={this.inputFormHandler}
              >
              </textarea>
            </p>
            <p>
              <input type="submit"></input>
            </p>
          </form>
        </article>            
      );
    }
  }
```

```react
class App extends Component {
  constructor(props) {
      super(props);
      this.max_content_id=3;
      this.state = {
        mode:'read',
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
  getReadContent() {
    var i = 0;
    while(i < this.state.contents.length) {
      var _content = this.state.contents[i];
      if (_content.id === this.state.selected_contents_id) {
        //_title = data.title;
        //_desc = data.desc;
        return _content;
        break;  
      }
      i = i + 1;
    }
  }

  getContent() {
    var _title, _desc, _article = null;
      
    if(this.state.mode === 'welcome') {
      _title = this.state.welcome.title;
      _desc = this.state.welcome.desc;
      _article = <ReadContent title={_title} desc={_desc}></ReadContent>
          
    } else if (this.state.mode === 'read'){      
      _article = <ReadContent title={this.getReadContent().title} desc={this.getReadContent().desc}></ReadContent>
          
    } else if(this.state.mode === 'create') {
      _article = <CreateContent onSubmit={function(_title, _desc){
        this.max_content_id = this.max_content_id+1;
        var _contents = this.state.contents.concat(
          {id:this.max_content_id, title:_title, desc:_desc}
        );
        this.setState({
          contents:_contents,
          mode:'read',
          selected_content_id:this.max_content_id
        });
      }.bind(this)}></CreateContent>
          
    } else if(this.state.mode === 'update') {
      // onSubmit 함수에 _id 파라미터 추가  
      _article = <UpdateContent data={this.getReadContent()} onSubmit={function(_id, _title, _desc){
        // 현재 입력한 값을 복제하여 _contents 배열로 정의
        var _contents = Array.from(this.state.contents);
        var i = 0;
        // _contents 배열의 id 값과 _id 값이 일치하는 경우, 업데이트
        while(i < _contents.length) {
          if(_contents[i].id === _id) {
            _contents[i] = {id:_id, title:_title, desc:_desc};
            break;
          }
          i = i+1;
        }
        this.setState({
          contents:_contents,
          // 업데이트 후, 자동 모드 변경
          mode:'read',
        });
        console.log(_title, _desc);
      }.bind(this)}></UpdateContent>
    }  
      return _article;
  }

  render() {    
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
        <Control onChangeMode={function(_mode){
          this.setState({
            mode:_mode
          });
        }.bind(this)}></Control>
        {this.getContent()}
      </div>
    );
  }
}
```

 
