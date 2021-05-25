## React class & function style coding

앞으로 실습하게 될 예제의 구조부터 파악해보자. Component는 크게 세 가지로 나눌 수 있다.

### Class VS Function [Component]

#### 	Functional Style [Component]

#### 	Class Style [Component]



```react
import React from 'react'
import './App.css';

function App() {
  return (
    <div className="container">
      <h1>Hello World</h1>
      <FuncComp></FuncComp>
      <ClassComp></ClassComp>
    </div> 
  );
}

// 함수를 이용해 Component를 만들 때에는 return을 이용하면 된다.
// function 방식은 자기 자신이 render 역할을 한다는 것을 알 수 있다.
function FuncComp(){
  return (
    <div className="container">
      <h2>function style component</h2>
    </div>
  );
}

// 함수를 이용해 Component를 만들 때에는 render라는 이름의 함수를 정의하고, 그 return값이 UI가 되는 것이다.
class ClassComp extends React.Component{
  render(){
    return (
      <div className="container">
        <h2>class style component</h2>
      </div>
    )
  }
}

export default App;
```

 

Component 구별을 위해  App.css 파일을 열어서 container라는 이름의 태그에 디자인을 추가하고 마무리하겠다.

```react
.container{
    border : 5px solid red;
    margin : 5px;
    padding : 5px;
}
```
