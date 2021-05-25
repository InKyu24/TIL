## React

### Create 기능 구현

모든 정보 기술은 CRUD(Create, Read, Update, Delete) 안에 갇혀있다. 지금까지 Read에 대해서 살펴보았다면, 이제 Create에 대해 알아보려 한다. 



### Create 구현 : 소개

글 목록과 본문 사이에 생성, 수정, 삭제 버튼을 둘 것이다. component 상에서는 TOC와 Contents 사이에 새로운 component가 생기는 것이다. 그래서 생성 버튼을 누르면 App component의 모드가 read에서 create로 변경될 것이다. 그에 따라서 Read mode에서 나타나는 Contents component가 글을 추가할 때 사용하는 component로 바꿀 것이다.   



### Create 구현 : mode 변경

먼저 세 가지 모드(create, update, delete)로 진입할 수 있도록 버튼을 생성한다. 세 가지 버튼들을 control component로 만들어준다. 그리고 control component에 onChangeMode라는 Event를 정의한다. 

```react
import React, { Component } from 'react';
import TOC from './components/TOC';
import Content from './components/Content';
import Subject from './components/Subject';
import Control from './components/Control';

import './App.css';

class App extends Component {
  constructor(props) {
      super(props);
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
        {/* Control component 생성 및 mode 변경 event 정의 */}
        <Control onChangeMode={function(_mode){
          this.setState({
            mode:_mode
          });
        }.bind(this)}></Control>
        <Content title={_title} desc={_desc}></Content>
      </div>
    );
  }
}

export default App;
```

```react
import React, { Component } from 'react';

class Control extends Component {
  render() {
    return (
      <ul>
        <li>
          <a href="/create" onClick={function(e){
            e.preventDefault();
            this.props.onChangeMode('create');
          }.bind(this)}>Create</a>
        </li>
        <li>
          <a href="/update" onClick={function(e){
            e.preventDefault();
            this.props.onChangeMode('update');
          }.bind(this)}>Update</a>
        </li>
        <li>
          <input type="button" value="delete" onClick={function(e){
            e.preventDefault();
            this.props.onChangeMode('delete');
          }.bind(this)}></input>
        </li>
      </ul>         
    );
  }
}

export default Control;
```



### Create 구현 : mode 전환 기능

create 버튼을 누르면 읽기 기능을 가지고 있던 Content component가 쓰기에서 사용될 component로 대체될 수 있도록 할 것이다.  따라서 기존의 읽기 기능을 가지고 있는 Content component의 이름도 ReadContent로 이름을 바꾸고, 새롭게 CreateContent를 생성할 것이다. 그리고 모드가 변경됨에 따라 해당되는 component로 변경될 수 있도록 할 것이다.

 ```react
 import React, { Component } from 'react';
 import TOC from './components/TOC';
 import ReadContent from './components/ReadContent';
 import CreateContent from './components/CreateContent';
 import Subject from './components/Subject';
 import Control from './components/Control';
 
 import './App.css';
 
 class App extends Component {
   constructor(props) {
       super(props);
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
       // _article 내용 정의 [ReadContent]
       _article = <ReadContent title={_title} desc={_desc}></ReadContent>
          
     } else if (this.state.mode === 'read'){
       var i = 0;
       while(i < this.state.contents.length) {
         var data = this.state.contents[i];
         if (data.id === this.state.selected_contents_id) {
           _title = data.title;
           _desc = data.desc;
           // _article 내용 정의 [ReadContent]
           _article = <ReadContent title={_title} desc={_desc}></ReadContent>
           break;  
         }
         i = i + 1;
       }
     } else if(this.state.mode === 'create') {
         // _article 내용 정의 [CreateContent]
       _article = <CreateContent></CreateContent>
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
         {/* _article 내용 화면 호출 */}
         {_article}
       </div>
     );
   }
 }
 
 export default App;
 ```



### Create 구현 : form

CreateContent로 나타날 form을 추가한다.

 ```react
 import React, { Component } from 'react';
 
 class CreateContent extends Component {
     render() {
 		return (
         <article>
           <h2>Create</h2>
           <form action="/create_process" method="post"
             onSubmit={function(e){
               e.preventDefault();
               alert("submit!!!");
             }}>
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
 
 export default CreateContent;
 ```



### Create 구현 : onSubmit Event

Create component에서 onSubmit event를 기본 event를 제거하고, 입력된 title과 desc를 props로 전달하도록 정의한다.

그리고 App component에서 해당 값을 가져왔는지 확인하기 위해 console.log로 찍어본다.

```react
import React, { Component } from 'react';

class CreateContent extends Component {
    render() {
      return (
        <article>
          <h2>Create</h2>
          <form action="/create_process" method="post"
            // onSubmit event를 정의
            onSubmit={function(e){
              e.preventDefault();
              // this.props.onsubmit 파라미터는 title과 desc의 입력값        
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

export default CreateContent;
```

```react
import React, { Component } from 'react';
import TOC from './components/TOC';
import ReadContent from './components/ReadContent';
import CreateContent from './components/CreateContent';
import Subject from './components/Subject';
import Control from './components/Control';

import './App.css';

class App extends Component {
  constructor(props) {
      super(props);
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
          _article = <ReadContent title={_title} desc={_desc}></ReadContent>
          break;  
        }
        i = i + 1;
      }
    } else if(this.state.mode === 'create') {
      // 입력값을 가져온다.
      _article = <CreateContent onSubmit={function(_title, _desc){
        // 입력된 값을 가져왔는지 확인
        console.log(_title, _desc);
      }}></CreateContent>
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

export default App;
```



### Create 구현 : contents 변경

이제 App component 내 contents의 끝에 새롭게 입력된 데이터를 추가할 수 있도록 할 것이다. 추가하기 위해서는 기존의 추가된 데이터의 id 값을 읽어서, 최대 id 값보다 1이 더 큰 새로운 id 값을 만들어주어야 한다. 

```react
import React, { Component } from 'react';
import TOC from './components/TOC';
import ReadContent from './components/ReadContent';
import CreateContent from './components/CreateContent';
import Subject from './components/Subject';
import Control from './components/Control';

import './App.css';

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
          _article = <ReadContent title={_title} desc={_desc}></ReadContent>
          break;  
        }
        i = i + 1;
      }
    } else if(this.state.mode === 'create') {
      _article = <CreateContent onSubmit={function(_title, _desc){
        this.max_content_id = this.max_content_id+1;
        var _contents = this.state.contents.concat(
          {id:this.max_content_id, title:_title, decs:_desc}
        );
        this.setState({
          contents:_contents 
        });
        console.log(_title, _desc);
      }.bind(this)}></CreateContent>
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

export default App;
```



배열에 데이터를 추가하는 방법은 push와 concat 두 가지가 있다.

```javascript
var arr = [1,2];
arr.push(3);
// arr = [1,2,3]

var arr2 = [1,2];
var result = arr2.concat(3);
// arr = [1,2] \
// result = [1,2,3]
```

state에 값을 추가할 때에는 push와 같이 원본 데이터를 변경하는 것을 쓰지 않고, concat처럼 원본 데이터를 변경하지 않고 새로운 데이터를 추가하는 것을 사용해야 한다. 추후 성능 개선에 큰 차이가 있기 때문이다.



### Create 구현 : shouldComponentUpdate

push가 아닌 concat을 사용하는 당위성에 대해 알아보자.

아래와 같이 TOC가 render 될 때마다 'TOC render'라는 콘솔이 찍히도록 설정을 하게 되면, 처음 화면이 로드될 때는 물론이고 글 목록이 변화되지 않는 경우의 동작에도 콘솔에 'TOC render'가 나타나, 계속 TOC가 render되는 것을 알 수 있다.

```react
class TOC extends Component {
  render() {
    console.log('TOC render');
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

이렇게 효율적이지 못한 부분을 수정해주기 위해서는 우선 shouldComponentUpdate라는 함수를 이해할 필요가 있다.

먼저 shouldComponentUpdate의 return 값을 true로 설정해보자. 처음 페이지 로드 시에는 'TOC render'만 출력되며 shouldComponentUpdate'가 콘솔에 출력되지는 않는 것을 알 수 있고, 모든 행동을 할 때마다 'shouldComponentUpdate'와  'TOC render'가 함께 출력되는 것을 알 수 있다.

```react
class TOC extends Component {
  shouldComponentUpdate() {
    console.log('shouldComponentUpdate');
    return true;
  }
  render() {    
    console.log('TOC render');
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

그렇다면 이제 shouldComponentUpdate의 return 값을 false로 놓아보자.

첫 화면에서는 똑같이 'TOC render'가 출력되고, 이후 모든 동작에 대해서 'shouldComponentUpdate'만이 출력될 뿐, TOC render'가 출력되지 않는 것을 알 수 있다.

```react
class TOC extends Component {
  shouldComponentUpdate() {
    console.log('shouldComponentUpdate');
    return false;
  }
  render() {    
    console.log('TOC render');
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

지금까지 확인해 본 결과, shouldComponentUpdate의 역할을 추론해보자.

> 최초 실행 시에는 shouldComponentUpdate 함수는 호출되지 않는다. 이후 return 값이 true인 경우에는 render 함수가 호출되며, false인 경우에는 render 함수가 호출되지 않는다.
>
> 즉, render 함수의 호출 여부를 제어할 수 있다.

즉, shouldComponentUpdate로 TOC component로 들어가는 내용의 변경 유무를 인지할 수 있다면 render 함수가 비효율적인 부분을 수정할 수 있다는 사실을 알 수 있다.

shouldComponentUpdate는 파라미터 값을 가질 수 있는데, 그 파라미터는 새롭게 바뀐 값(newProps와 newState)이다. 이전 값과 새로운 값 비교가 가능해짐으로써 비효율적인 부분의 수정이 가능해진다는 것이다. 아래의 코드를 통해 shouldComponentUpdate의 파라미터가 어떻게 사용되는지 알아보자.

```react
class TOC extends Component {
  shouldComponentUpdate(newProps, newState) {
    console.log('shouldComponentUpdate', newProps.data, this.props.data);
    return false;
  }
  render() {    
    console.log('TOC render');
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

위와 같이 작성하게 되면, 콘솔에 shouldComponentUpdate와 TOC에서 설정한 array가 두 개 출력된다. 두 개의 array는 서로 같지만, 만약 Create 버튼을 통해 목록을 추가하게 되면 두 개의 array가 서로 달라지는 것을 볼 수 있다.

따라서 아래처럼 코드를 변경하여 효율적을 제고할 수 있게 된다.

```react
class TOC extends Component {
  shouldComponentUpdate(newProps, newState) {
    console.log('shouldComponentUpdate', newProps.data, this.props.data);
    if(newProps.data === this.props.data) {
      return false;
    }
    return true;
  }
  render() {    
    console.log('TOC render');
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

그럼 다시 본론으로 돌아와서 생각해 볼 것이 있다. 만약 concat을 사용하지 않고, push를 사용하게 된다면 이 둘의 비교가 가능할까? 아닐 것이다. 기존의 데이터가 바뀌기 때문에 이전의 값과 새로운 값이 같은 값을 가지게 되는 것이다.

따라서 이제 concat을 사용해야 하는 당위성을 갖게 된 것이다. 



### Create 구현 : Immutable (불변)

이렇게 원본을 바꾸지 않는 것을 불변성이라고 한다.

```javascript
var a = [1,2];
var b = Array.from(a);
console.log(a, b, a===b); // a와 b는 서로 같은 array를 갖지만 서로 다른 값임을 알 수 있다. 즉, 서로 내용이 같을 뿐
```

따라서 아래 두 가지 코드는 서로 같은 내용이라는 것을 알 수 있다.

```javascript
var a = [1,2];
var b = Array.from(a);
b.push(3);
```

```javascript
var a = [1,2];
var b = a.concat(3);
```

이는 배열의 경우에만 사용 가능하다는 것에 유의하자.

그럼 객체가 있다고 가정해보자. 객체는 Object.assign()을 통해서 객체를 복제할 수 있다.  

```javascript
var a = {name : 'Inkyu'};
var b = Object.assign({},a);
console.log(a, b, a===b); // a와 b는 서로 같은 내용을 갖지만 서로 다른 값임을 알 수 있다. 즉, 서로 내용이 같을 뿐

b.name = 'Choi';
console.log(a, b, a===b); // {name : "Inkyu"}, {name : "Choi"}, false
```

만약 Object.assign()의 첫 번째 파라미터 {}가 값을 갖게 된다면 어떻게 될 지 확인해보자.

```javascript
var a = {name : 'Inkyu'};
var b = Object.assign({adverb : 'always', adjective : 'nice'}, a);
console.log(b); // {adverb: "always", adjective: "nice", name: "Inkyu"}
```

