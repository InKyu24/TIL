#### Redux를 사용하는 이유

서로 강하게 연결되어 있는 부품들이 있다고 가정하자. 그 부품들이 많아지면 많아질수록 코드는 복잡하고, 유지보수는 더욱 어렵게 된다. Redux는 부품의 변경에 따른 변화를 자동적으로 진행할 수 있도록 하여, 강한 연결을 그대로 유지하면서 코드는 단순하고, 유지보수를 쉽게 할 수 있게 된다. 

또한 Redux를 사용하면 시간 여행이 가능해진다. Redux는 애플리케이션의 state의 변화를 이력을 보관하고 있으며, 시간 여행 도구를 사용하여 언제든지 과거로 돌아갈 수 있도록 해준다.

##### Redux가 없다면?

Redux 없이 red, green, blue 박스를 생성하고, 각각의 박스 내의 버튼을 클릭한 경우에 해당 되는 색상으로 모든 박스의 배경색이 바뀌는 코드를 작성해보았다. 코드는 복잡하고, 만약 yellow 박스를 추가로 생성하게 되거나, blue 박스를 제거하게 되는 경우에는 모든 코드를 수정해야하는 번거로움이 생길 것이다.

```html
<html>
    <body>
        <style>
            .container {
                border:5px solid black;
                padding: 10px;
            }
        </style>
        <div id="red"></div>
        <div id="green"></div>
        <div id="blue"></div>
        <script>
            function red() {
                document.querySelector('#red').innerHTML = `
					<div class="container" id="component_red">
						<h1>red</h1>
						<input type="button" value="fire" onclick="
						document.querySelector('#component_red').style.backgroundColor ='red';
						document.querySelector('#component_green').style.backgroundColor ='red';
						document.querySelector('#component_blue').style.backgroundColor ='red';
						">
            		</div>
				`;
            }
            red();
            
            function green() {
                document.querySelector('#green').innerHTML = `
					<div class="container" id="component_green">
						<h1>green</h1>
						<input type="button" value="fire" onclick="
						document.querySelector('#component_red').style.backgroundColor ='green';
						document.querySelector('#component_green').style.backgroundColor ='green';
						document.querySelector('#component_blue').style.backgroundColor ='green';
						">
            		</div>
				`;
            }
            green();
            
            function blue() {
                document.querySelector('#blue').innerHTML = `
					<div class="container" id="component_blue">
						<h1>blue</h1>
						<input type="button" value="fire" onclick="
						document.querySelector('#component_red').style.backgroundColor ='blue';
						document.querySelector('#component_green').style.backgroundColor ='blue';
						document.querySelector('#component_blue').style.backgroundColor ='blue';
						">
            		</div>
				`;
            }
            blue();
        </script>
    </body>
</html>
```



#### Redux가 있다면?

Redux가 없이 작성했던 내용들을 Redux를 활용하여 작성해보자.

##### 1. Store 생성

```html
<!DOCTYPE html>
<html>
    <head>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/redux/4.0.1/redux.js"></script>
    </head>
    <body>
        <style>
            .container {
                border:5px solid black;
                padding: 10px;
            }
        </style>
        <div id="red"></div>
        <script>
            // store를 생성하기 위해서는 createStore 함수를 사용한다.
            // createStore 함수의 인자는 반드시 reducer 함수를 갖는다.
            // reducer 함수는 state와 action을 인자로 갖는다.
            function reducer(state, action) {
                // redux의 store에 존재하는 초기값을 설정한다.
                if (state === undefined) {
                    return {color:'yellow'}
                }
            }
            var store = Redux.createStore(reducer);
			console.log(store.getState()); // console에는 {color:'yellow'}가 출력된다.
            
            function red() {
                // red 함수에 state 값을 받아서 style로 지정한다.
                var state = store.getState();
                document.querySelector('#red').innerHTML = `
					<div class="container" id="component_red" style="background-color:${state.color}">
						<h1>red</h1>
						<input type="button" value="fire" onclick="
						document.querySelector('#component_red').style.backgroundColor ='red';
						">
            		</div>
				`;
            }
            red();
        </script>
    </body>
</html>
```



##### 2. reducer와 action을 이용해서 새로운 state 값 만들기

state를 바꾸기 위해서는 action을 만들어주어야 한다. 그리고 해당 action이 dispatch에 전달되면 dispatch가 reducer 함수를 호출한다. 

```html
<!DOCTYPE html>
<html>
    <head>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/redux/4.0.1/redux.js"></script>
    </head>
    <body>
        <style>
            .container {
                border:5px solid black;
                padding: 10px;
            }
        </style>
        <div id="red"></div>
        <script>
            function reducer(state, action) {
                console.log(state, action);
                if (state === undefined) {
                    return {color:'yellow'}
                }
                // state 값을 변경하지 않고, 새로운 state를 생성하여 진행한다.
                // newState는 Object.assign()이라는 명령을 이용해 복제한다.
                var newState;
                if(action.type === 'CHANGE_COLOR') {
                    newState = Object.assign({}, state, {color:'red'});
                }
                return newState;
            }
            var store = Redux.createStore(reducer);
            
            function red() {
                var state = store.getState();
                document.querySelector('#red').innerHTML = `
					<div class="container" id="component_red" style="background-color:${state.color}">
						<h1>red</h1>
						<input type="button" value="fire" onclick="
							store.dispatch({type:'CHANGE_COLOR', color:'red'});
						">
            		</div>
				`;
            }
            red();
        </script>
    </body>
</html>
```



##### 3. state의 변화를 UI에 반영하기

이제는 state 값의 변화에 따라 UI의 모습도 변경될 필요가 있다. 

```javascript
<!DOCTYPE html>
<html>
    <head>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/redux/4.0.1/redux.js"></script>
    </head>
    <body>
        <style>
            .container {
                border:5px solid black;
                padding: 10px;
            }
        </style>
        <div id="red"></div>
        <script>
            function reducer(state, action) {
                console.log(state, action);
                if (state === undefined) {
                    return {color:'yellow'}
                }
                var newState;
                if(action.type === 'CHANGE_COLOR') {
                    newState = Object.assign({}, state, {color:action.color});
                }
                return newState;
            }
            var store = Redux.createStore(reducer);

            function red() {
                var state = store.getState();
                document.querySelector('#red').innerHTML = `
					<div class="container" id="component_red" style="background-color:${state.color}">
						<h1>red</h1>
						<input type="button" value="fire" onclick="
							store.dispatch({type:'CHANGE_COLOR', color:'red'});
						">
            		</div>
				`;
            }
			// 최초로 한 번 red 함수를 직접 호출하고 있다.
            red();
			// state 값이 변화할 때마다 자동적으로 red 함수가 호출되도록 하고 싶기 때문에 subscribe 함수를 사용한다.
			store.subscribe(red);
        </script>
    </body>
</html>
```



##### 4. 더 많은 부품 추가하기

Redux가 존재하기 때문에 각각의 부품 간의 의존성을 낮출 수 있다.  

```javascript
<!DOCTYPE html>
<html>
    <head>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/redux/4.0.1/redux.js"></script>
    </head>
    <body>
        <style>
            .container {
                border:5px solid black;
                padding: 10px;
            }
        </style>
        <div id="red"></div>
		<!-- div 태그 추가 -->
        <div id="green"></div>
		<div id="blue"></div>
        <script>
            function reducer(state, action) {
                console.log(state, action);
                if (state === undefined) {
                    return {color:'yellow'}
                }
                var newState;
                if(action.type === 'CHANGE_COLOR') {
                    newState = Object.assign({}, state, {color:action.color});
                }
                return newState;
            }
            var store = Redux.createStore(reducer);

            function red() {
                var state = store.getState();
                document.querySelector('#red').innerHTML = `
					<div class="container" id="component_red" style="background-color:${state.color}">
						<h1>red</h1>
						<input type="button" value="fire" onclick="
							store.dispatch({type:'CHANGE_COLOR', color:'red'});
						">
            		</div>
				`;
            }
            red();
			store.subscribe(red);

			// green 함수 추가
			function green() {
                var state = store.getState();
                document.querySelector('#green').innerHTML = `
					<div class="container" id="component_green" style="background-color:${state.color}">
						<h1>green</h1>
						<input type="button" value="fire" onclick="
							store.dispatch({type:'CHANGE_COLOR', color:'green'});
						">
            		</div>
				`;
            }
			green();
			store.subscribe(green);

			// blue 함수 추가
			function blue() {
                var state = store.getState();
                document.querySelector('#blue').innerHTML = `
					<div class="container" id="component_blue" style="background-color:${state.color}">
						<h1>blue</h1>
						<input type="button" value="fire" onclick="
							store.dispatch({type:'CHANGE_COLOR', color:'blue'});
						">
            		</div>
				`;
            }
			blue();
			store.subscribe(blue);
        </script>
    </body>
</html>
```



#### Redux를 이용해서 할 수 있는 일 - 시간 여행 디버깅, 로깅

Redux의 본질적인 존재는 단일 store를 통해 애플리케이션의 데이터 흐름을 일관되고, 단순하게 유지할 수 있다는 점이다. 하지만 이와 유사한 여러 해결책들이 있기 때문이 이것을 Redux만의 장점이라고 할 수는 없다.

따라서 Redux만의 혁신적인 장점은 시간여행이라고 할 수 있다.

 ```javascript
var store = Redux.createStore(reducer,
	window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
);
 ```

```javascript
console.log(action.type, action, state, newState);
```

