## React class & function style coding

#### class 방식에서 state 사용 방법

처음에 설정한 숫자 2가 state 값으로 정의되어 화면에 나타나며, random 버튼을 클릭함(setState에 의해) 으로 인해 state 값은 내부적으로 변화하게 된다. 그리고 변화된 state 값이 화면에 나타나게 되는 것이다.

```react
import React from 'react'
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
  return (
    <div className="container">
      <h2>function style component</h2>
      <p>Number : {functionalprops.initNumber}</p>
    </div>
  );
}

class ClassComp extends React.Component{
  state = {
    number : this.props.initNumber // state 값을 정의한다.
  }
  render(){
    return (
      <div className="container">
        <h2>class style component</h2>
        <p>Number : {this.state.number}</p> {/* state 값을 사용한다. */}
        <input type="button" value="random" onClick={
          function(){
            this.setState({number:Math.random()}) {/* state 값을 내부적으로 변경하여, 사용할 수 있게 한다. */}
          }.bind(this)
        }></input>
      </div>
    )
  }
}

export default App;
```
