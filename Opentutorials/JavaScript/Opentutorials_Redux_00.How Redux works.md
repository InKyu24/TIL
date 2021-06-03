## Redux

Redux는 Javascript로 만든 애플리케이션들 위한 예측 가능한 상태 저장소이다.

소프트웨어를 개발할 때 가장 큰 위협은 복잡성이다. 복잡성이 위협적인 이유는 눈에 보이지 않기 때문이다. 따라서 코드의 복잡성을 낮추어, 더욱 복잡한 애플리케이션 개발에 도전할 수 있도록 해야한다. 

Redux는 애플리케이션의 복잡성을 획기적으로 낮추어, 코드가 어떤 결과를 가져올 지 예측 가능하게 해주는 도구이다.

가장 중요한 Redux의 특징은 `Single Source of Truth`이다. 하나의 상태를 갖는다라는 것이다. 상태는 하나의 객체이고, 하나의 객체 안에 애플리케이션에서 필요한 모든 데이터를 욱여넣는 것을 통해서 Redux는 애플리케이션의 복잡성을 낮춘다. 한 곳에 데이터를 중앙집중적으로 관리하면, 훨씬 더 관리하기 쉬워질 것이다.

상태는 중요 데이터를 가지고 있기 때문에, 외부로부터 철저히 데이터를 수정하고 읽는 것을 차단을 시킨다. 따라서 데이터를 읽고 쓸 때에는 인가된 함수만을 통해서 가능하다. 이처럼 데이터를 외부에서 직접적으로 제어할 수 없도록 하여, 의도치 않게 상태가 조작되는 것을 사전에 차단하여 애플리케이션을 예측 가능하도록 하는 것이다.



#### Redux의 동작 방법

Redux의 핵심은 store에 있다.

store는 정보가 저장되는 곳이고, store 내에는 state라고 하는 실제 정보가 저장된다. 한 가지 중요한 것은 절대 state에 직접 접근할 수 없다는 것이다.

store를 만들 때 제일 먼저 해야하는 것은 reducer라는 함수를 만들어서 공급해줘야 한다. reducer라는 함수를 작성하는 것이 redux를 만드는 일이라고 해도 과언이 아닐 정도로 중요한 역할을 한다. 

```javascript
// Redux에 createStore를 하게 되면 store가 생성이 된다. (store를 생성할 때는 reducer를 반드시 줘야하는 인자)
function reducer (oldState, action) {
    // ....
}
var store = Redux.createStore(reducer);
```

또 하나 중요한 것은 render라는 것이다. render는 store 바깥에 위치하여, UI를 만들어주는 redux와 관계없는 코드이다.

은행에 있는 돈을 함부로 건드리지 못하는 것처럼, store 내의 state로 직접 접근할 수 없기 때문에 store에는 마치 은행 창구 직원과 같은 역할을 하는 세 가지의 중요한 함수(dispatch, subscribe, getState)가 있다. 이 함수들과 render가 서로 어떻게 협력해서 애플리케이션을 만드는가를 살펴보자.

```javascript
// getState 함수(store에 있는 state 값을 가져오기)를 이용해 render에 state 값을 전달
function render() {
    var state = store.getState();
    // ....
    document.querySelector('#app').innerHTML = `<h1>WEB</h1> ...`
}
```

```javascript
// subscribe 함수(store에 있는 state 값이 변경될 때마다 render 함수를 호출하기)
store.subscribe(render);
```

```javascript
// dispatch 함수 (reducer를 호출해서 state 값을 변경하고 subscribe를 호출해서 render 함수 호출)
<form onsubmit = "
	// ...
	store.dispatch({type:'create', payload:{title:title, desc:desc}});
">
```

