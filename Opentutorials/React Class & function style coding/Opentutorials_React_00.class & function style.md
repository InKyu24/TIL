## React class & function style coding

React의 component를 만드는 방법에는 두 가지 방법이 있다. 그 두 가지 방법은 class 방식과 function 방식이다. 

#### class 문법을 이용한 component 생성

```react
class ClassComp extends React.Component{render(){
    return (
    	<div className = "container">
            <h2>class style component</h2>
            <p>Number : {this.state.number}</p>
            <p>Date : {this.state.date}</p>
            <input type="button" value="random" onClick={
                    function(){
                        setNumber(Math.randon());
                    }
            }></input>
        </div>
    )
}}
```

#### function 문법을 이용한 component 생성

```react
function FuncComp(props){
    return (
    	<div className = "container">
            <h2>class style component</h2>
            <p>Number : {this.state.number}</p>
            <p>Date : {this.state.date}</p>
            <input type="button" value="random" onClick={
                    function(){
                        setNumber(Math.randon());
                    }
            }></input>
        </div>
    )
}
```



class 문법을 이용하게 되면 React의 기능을 온전히 사용할 수 있으나, class라는 문법을 알아야 하고 코드가 장황하다는 단점이 있다.

반면에 function 문법을 이용하게 되면, 비교적 간단한 function 문법만 이해하면 된다. 하지만 기능이 부족하다. 대표적으로 component 내부에 state를 만들어 사용할 수도 없었으며, component의 생성, 변경, 소멸에 대한 event인 life cycle API를 사용할 수도 없었다. 그래서 function 방식은 상위 component가 시키는 일만 처리하는 단순한 component에서만 사용되었다.

최신 React에는 hook이라는 개념이 도입되면서, function 방식에서도 내부적으로 state를 다룰 수 있게 되었고, component의 life cycle에 따라 해야할 작업을 정리할 수 있게 된 것이다.



지금부터 class 방식과 function 방식으로 동일한 작업을 하는 component를 생성해보면서,  두 방식을 알아보도록 할 것이다.
