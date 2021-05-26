## How to use Props

Component를 사용하는 쪽에서는 해당 Component가 제공하는 props를 통해서, 그 component를 이용할 수 있다.

```react
import MyName from './MyName';

class App extends Component {
    render() {
        return {
          <MyName name="최인규"></MyName>  // Component를 사용
        };
    }
}
export default App;
```

```react
class MyName extends Component {
    render() {
        return {
            <div>
                안녕하세요. 제 이름은 <b>{this.props.name}</b> 입니다.
            </div>
        }
    }
}
export default Myname;
```

Component를 만드는 쪽에서는 state라고 하는 data를 통해, 내부에서 여러 가지 작업을 할 수 있게 된다.

```react
class Counter extends Component {
    state = {
        number : 0
    }
	
	handleIncrease = () => {
        this.setState({
            number: this.state.number + 1
        });
    }
    handleDecrease = () => {
        this.setState({
            number: this.state.number - 1
        });
    }
    
    render() {
        return (
        	<div>
            	<div> 값 : {this.state.number} </div>
                <button onClick={this.handleIncrease}>더하기</button>
                <button onClick={this.handleDecrease}>빼기</button>
            
            </div>
        );
    }
}
export default Counter;
```



다시 본 예제로 돌아오자. props는 class 방식과 function 방식 모두 사용 가능하다. state는 class 방식에서만 사용 가능했고, function 방식에서 사용이 제한되었다. 하지만 현재는 사용이 가능해졌다.



#### class 방식과 function 방식에서 props 사용 방법

```react
import React from 'react'
import './App.css';

function App() {
  return (
    <div className="container">
      <h1>Hello World</h1>
      <FuncComp initNumber={2}></FuncComp> {/* Function 방식의 Component를 사용 */}
      <ClassComp initNumber={2}></ClassComp> {/* class 방식의 Component를 사용 */}
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
  render(){
    return (
      <div className="container">
        <h2>class style component</h2>
        <p>Number : {this.props.initNumber}</p>
      </div>
    )
  }
}

export default App;
```
