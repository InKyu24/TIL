## React class & function style coding

#### function 방식에서 state 사용 방법

React 공식 메뉴얼에 의하면 React 16.8 버전에서 hook이라는 기능이 추가되었다. hook은 기존 class 스타일 코딩에서만 가능했던 여러 작업을 functional 스타일 코딩에서도 가능하게 해주는 기능이다. 이 기능을 이용해서 function 방식의 component 내에서 state를 사용하는 방법을 알아보자.

우선, hook의 내장 함수인 useState를 알아보기 위해, 함수를 사용하고, 해당 내용을 console에 출력해 볼 것이다.

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
  // var numberState = React.useState(); 상단 import에 {useState}를 추가하고 아래와 같이 사용 가능하다.
  var numberState = useState();
  console.log("numberState", numberState); // useState를 통해 입력받는 numberState의 값을 확인해볼 것이다.
  return (
    <div className="container">
      <h2>function style component</h2>
      <p>Number : {functionalprops.initNumber}</p>
    </div>
  );
}

class ClassComp extends React.Component{
  state = {
    number : this.props.initNumber
  }
  render(){
    return (
      <div className="container">
        <h2>class style component</h2>
        <p>Number : {this.state.number}</p>
        <input type="button" value="random" onClick={
          function(){
            this.setState({number:Math.random()})
          }.bind(this)
        }></input>
      </div>
    )
  }
}

export default App;
```

console의 내용을 확인해보면 아래와 같다.

```
numberState는 두 개의 값으로 이루어진 배열이다.
    첫 번째 값은 numberState[0]은 undefined으로 정의되어 있다.
```

만약 class component에서 state를 initNumber로 정의했던 것처럼, useState의 첫 번째 파라미터로 initNumber를 지정하게 되면 어떻게 될까? 예상한대로 똑같이 state가 정의되는 것을 알 수 있다.

즉, numberState는 배열로 값을 반환하고, 첫 번째 자리의 값으로 state를 정의할 수 있다는 것이다.

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
  var numberState = useState(functionalprops.initNumber);
  console.log("numberState", numberState);
  var number = numberState[0];
  return (
    <div className="container">
      <h2>function style component</h2>
      <p>Number : {number}</p>
    </div>
  );
}

class ClassComp extends React.Component{
  state = {
    number : this.props.initNumber
  }
  render(){
    return (
      <div className="container">
        <h2>class style component</h2>
        <p>Number : {this.state.number}</p>
        <input type="button" value="random" onClick={
          function(){
            this.setState({number:Math.random()})
          }.bind(this)
        }></input>
      </div>
    )
  }
}

export default App;
```

class component에서 random 버튼을 클릭할 때마다 state값이 갱신되듯이 하기 위해서는 useState 함수로 정의된 numberState 배열의 두 번째 값에 해답이 있다.

두 번째의 값 안에는 함수가 담겨있다. 그리고 그 함수를 통해서 state를 변경할 수 있게 되는 것이다. 

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
  var numberState = useState(functionalprops.initNumber);
  console.log("numberState", numberState);
  var number = numberState[0];
  var setNumber = numberState[1];
  return (
    <div className="container">
      <h2>function style component</h2>
      <p>Number : {number}</p>
      <input type="button" value="random" onClick={
          function(){
            setNumber(Math.random());
          }
        }></input>
    </div>
  );
}

class ClassComp extends React.Component{
  state = {
    number : this.props.initNumber
  }
  render(){
    return (
      <div className="container">
        <h2>class style component</h2>
        <p>Number : {this.state.number}</p>
        <input type="button" value="random" onClick={
          function(){
            this.setState({number:Math.random()})
          }.bind(this)
        }></input>
      </div>
    )
  }
}

export default App;
```

함수 방식에서 state를 만들 때는 React의 useState를 호출한다. 그리고 useState의 인자로 해당 state의 초기값이 온다.  그러면 useState는 두 개의 값으로 구성된 배열을 반환하게 되고, 배열의 첫 번째 값은 그 state 값이며, 두 번째 값은 그 state를 변경할 수 있는 함수가 오게 되는 것이다.



이번에는 날짜를 출력하는 예제를 직접 만들어보자. 

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
  // var numberState = useState(functionalprops.initNumber);
  // console.log("numberState", numberState);
  // var number = numberState[0];
  // var setNumber = numberState[1];
  var [number, setNumber] = useState(functionalprops.initNumber);

  // var dateState = useState(new Date().toString());
  // console.log("dateState", dateState);
  // var date = dateState[0];
  // var setDate = dateState[1];
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
