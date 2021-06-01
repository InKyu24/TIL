## React class & function style coding

#### class 방식에서 LifeCycle 이용 방법

class 방식으로 component를 생성할 때, 그 component의 여러 메소드들은 어떤 순서로 호출되는지 알아보자.

1. getDefaultProps()

2. getInitialState()

3.  `componentWillMount()`

   component의 생성 전에 처리해야 하는 일이 있다면  componentWillMount() 메서드를 구현하는 것을 통해 작업할 수 있다.

4. render()

5. `componentDidMount()`

   만약 render() 다음에 해야할 일이 있다면 `componentDidMount()`를 구현하여 작업할 수 있게 된다.

* 화면 변경사항이 생기게 되는 경우

1. componentWillReceiveProps(nextProps)

2. shouldComponentUpdate(nextProps, nextState)

3. componentWillUpdate(nextProps, nextState)

4. render()

5. componentDidUpdate(nextProps, nextState)



```react
import React, {useState} from 'react'
import './App.css';

function App() {
  return (
    <div className="container">
      <h1>Hello World</h1>
      <FuncComp initNumber={2}></FuncComp>
      <ClassComp initNumber={2}></ClassComp>
    </div> 
  );
}

function FuncComp(functionalprops){
  var [number, setNumber] = useState(functionalprops.initNumber);
    
  var [date, setDate] = useState(new Date().toString());

  return (
    <div className="container">
      <h2>function style component</h2>
      <p>Number : {number}</p>
      <p>Date : {date}</p>
      <input type="button" value="random" onClick={
        function(){
          setNumber(Math.random());
        }
      }></input>
      <input type="button" value="date" onClick={
        function(){
          setDate(new Date().toString());
        }
      }></input>
    </div>
  );
}

class ClassComp extends React.Component{
  state = {
    number : this.props.initNumber,
    date : new Date().toString()
  }
  render(){
    return (
      <div className="container">
        <h2>class style component</h2>
        <p>Number : {this.state.number}</p>
        <p>Date : {this.state.date}</p>
        <input type="button" value="random" onClick={
          function(){
            this.setState({number:Math.random()})
          }.bind(this)
        }></input>

        <input type="button" value="date" onClick={
          function(){
            this.setState({date:new Date().toString()})
          }.bind(this)
        }></input>
      </div>
    )
  }
}

export default App;
```

