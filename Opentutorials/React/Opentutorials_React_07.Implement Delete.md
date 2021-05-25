## React

### Delete 기능 구현

CRUD에서 마지막 기능 Delete가 남아있다. Delete를 구현해보자. 

TOC 목록 중 하나를 선택하고, Delete 버튼을 클릭하게 되면 해당 목록이 삭제되도록 구현할 것이다.

```react
class App extends Component {
  constructor(props) {
      super(props);
      this.max_content_id=3;
      this.state = {
        mode:'welcome',
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
      _article = <UpdateContent data={this.getReadContent()} onSubmit={function(_id, _title, _desc){
        var _contents = Array.from(this.state.contents);
        var i = 0;
        while(i < _contents.length) {
          if(_contents[i].id === _id) {
            _contents[i] = {id:_id, title:_title, desc:_desc};
            break;
          }
          i = i+1;
        }
        this.setState({
          contents:_contents,
          mode:'read'
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
          <!-- 만약 mode가 delete라면, -->
          if(_mode === 'delete') {
            <!-- 사용자에게 확인을 받고, (예를 누르게 되면) -->            
            if(window.confirm("really?")){
              <!-- _contents는 contents들의 배열이다. -->              
              var _contents = Array.from(this.state.contents);
              var i = 0;
              <!-- 반복문을 실행할 것이다.-->              
              while (i < this.state.contents.length) {
                <!-- _contents의 아이디 값과 selected_contents의 id 값과 일치하는 경우에 -->   
                if(_contents[i].id === this.state.selected_contents_id) {
                  <!-- 어디서 부터 몇 개를 지울 것인지를 파라미터로 하는 splice 함수 이용 -->   
                  _contents.splice(i,1);
                  break;                  
                }
                i = i + 1;
              }
			  <!-- 반복문이 수행되면, mode를 welcome으로 변경하고,
 			  contents의 값을 _contents로 변경-->
              this.setState({
                mode:'welcome',
                contents:_contents
              });
              alert("deleted")
            }
          } else {
            this.setState({
              mode:_mode
            });
          }
          
        }.bind(this)}></Control>
        {this.getContent()}
      </div>
    );
  }
}
```

