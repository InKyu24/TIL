## React Router DOM

React를 이용해서 여러 개의 페이지로 이뤄져있는 애플리케이션을 쉽게 구축할 수 있는 React Router DOM에 대해 알아보자.

React Router DOM을 이용하기 위해서는 `npm install react-router-dom` 명령어를 이용해 설치를 해주어야 한다.



### Router

사용자가 어떤 주소로 들어왔을 때, 그 주소에 해당하는 적당한 페이지를 보여주는 것을 Router, Routing이라 한다.

#### BrowserRouter

```react
import {BrowserRouter} from 'react-router-dom';
```

react-router-dom에서 가져온 BrowserRouter는 react-router-dom을 적용하고 싶은 component의 최상위 component에서 감싸주는 wrapper component이다. 따라서 최상위 component인 App을 BrowserRouter로 감싸주면 된다.

```react
ReactDOM.render(
    <BrowserRouter><App /></BrowserRouter>,
  document.getElementById('root')
);
```

그렇게 한다면, 이제 App component에서는 BrowserRouter를 사용할 수 있는 상태가 된 것이다.



이제 Routing의 가장 본질적인 작업을 위해서는 Route라는 component가 필요하다.

#### Route

```react
import {BrowserRouter, Route} from 'react-router-dom';
```

url에 따라서 달라져야 하는 component들을 Route component로 감싸주고, Route의 속성인 path를 지정해줄 것이다.

```react
function App() {
  return (
    <div>
      <h1>React Router DOM example</h1>
          <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/topics">Topics</a></li>
            <li><a href="/contact">Contact</a></li>
          </ul>
        <Route path="/"><Home></Home></Route>
        <Route path="/topics"><Topics></Topics></Route>
        <Route path="/contact"><Contact></Contact></Route>
    </div>
  )
}
```

위와 같이 작성하게 되면, Home을 클릭하게 되었을 때, Home component가 routing 된다.

하지만 Topics를 클릭하게 되면, Home component가 함께 보여지면서 Topics component가 routing되는 것을 볼 수 있다. Contact를 클릭하더라도 Home component가 함께 보여지면서 Contact component가 routing되는 것을 볼 수 있다.

이 원인은 이렇게 생각할 수 있다. `localhost:3000/topics`과 같은 경로는 `localhost:3000/`에도 영향을 받으면서 동시에 url이 완전히 일치하는 `localhost:3000/topics`에도 영향을 받는다는 것이다. 

따라서 지정한 path 속성을 조금 수정할 필요가 있다. Route component가 가진 속성 중에서는 exact라는 속성이 있다. 이는 정확하게 path가 일치하는 경우에만 match를 시켜주는 역할을 한다. 이를 활용하여 아래와 같이 수정하였다.

```react
function App() {
  return (
    <div>
      <h1>React Router DOM example</h1>
          <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/topics">Topics</a></li>
            <li><a href="/contact">Contact</a></li>
          </ul>
        <Route exact path="/"><Home></Home></Route>
        <Route path="/topics"><Topics></Topics></Route>
        <Route path="/contact"><Contact></Contact></Route>
    </div>
  )
}
```

위와 같이 수정하게 되면, 이제 동시에 component가 나타나지 않는 것을 확인할 수 있다. 좀 더 깊게 생각을 해보면 더 많은 차원을 가진 애플리케이션을 구축할 때 상당히 유용할 것으로 예상할 수 있다.



#### Switch

```react
import {BrowserRouter, Route, Switch} from 'react-router-dom';
```

Router를 이용한 코드들을 보면, Router를 Switch로 감싸고 있는 것을 확인할 수가 있다. Switch는 exact를 사용하지 않고도 exact를 사용한 것과 같은 효과를 얻어낼 수 있는 component이다. 

```react
function App() {
  return (
    <div>
    	<h1>React Router DOM example</h1>
        	<ul>
            	<li><a href="/">Home</a></li>
	            <li><a href="/topics">Topics</a></li>
    	        <li><a href="/contact">Contact</a></li>
          	</ul>
		<Switch>
	        <Route path="/"><Home></Home></Route>
    	    <Route path="/topics"><Topics></Topics></Route>
        	<Route path="/contact"><Contact></Contact></Route>
        </Switch>
	</div>
  )
}
```

위와 같이 Switch component로 감싸게 되면, Topics나 Contact를 클릭하더라도 Home component만 나타나는 것을 알 수 있다.

왜 그런 것일까? Switch라는 component로 Router를 감싸게 되면, React-Router-DOM은 path와 일치하는 첫 번째 component가 발견되면, 나머지 component들은 버린다. 그렇기 때문에 모든 component가 `/`에 걸리게 되고, Home component만이 채택되는 것이다.

그렇다면 Home component가 호출되는 부분을 맨 뒤로 보내게 되면, 어떨까?

```react
function App() {
  return (
    <div>
    	<h1>React Router DOM example</h1>
        	<ul>
            	<li><a href="/">Home</a></li>
	            <li><a href="/topics">Topics</a></li>
    	        <li><a href="/contact">Contact</a></li>
          	</ul>
		<Switch>
    	    <Route path="/topics"><Topics></Topics></Route>
        	<Route path="/contact"><Contact></Contact></Route>
	        <Route path="/"><Home></Home></Route>            
        </Switch>
	</div>
  )
}
```

Home component가 뒤로 가게 되면, 모든 component가 정상적으로 작동하게 된다. 이를 응용하면 아래와 같은 사용도 가능해진다.

```react
function App() {
  return (
    <div>
    	<h1>React Router DOM example</h1>
        	<ul>
            	<li><a href="/">Home</a></li>
	            <li><a href="/topics">Topics</a></li>
    	        <li><a href="/contact">Contact</a></li>
          	</ul>
		<Switch>
		    <Route exact path="/"><Home></Home></Route>
    	    <Route path="/topics"><Topics></Topics></Route>
        	<Route path="/contact"><Contact></Contact></Route>
        	<Route path="/">올바르지 않은 경로</Route>
        </Switch>
	</div>
  )
}
```

이렇게 작성한다면 기존의 경로는 계속 유지하면서, 사용자가 무언가 잘못된 경로로 진입을 시도하는 경우에 `올바르지 않은 경로`임을 나타낼 수 있다.



Single Page Application을 제작하는 것에서 중요한 것은 페이지가 re-load되지 않는다는 것이다. 이는 동적으로 가져오는 데이터는 코딩으로 만들거나, ajax와 같은 것들을 통해 비동기적으로 데이터를 끌고 와서 코딩으로 페이지를 동적으로 꾸며주는 것이 굉장히 중요한 요소이다.

하지만 현재 작성한 페이지는 클릭할 때마다 페이지가 완전히 새로 loading되고 있다. 이를 자동으로 해주는 기능인 Link를 알아보자.



#### Link

```react
import {BrowserRouter, Route, Switch, Link} from 'react-router-dom';
```

a 태그를 Link로 교체하고, href 속성을 to로 교체하는 것만으로 아주 간단하게 SPA를 구현할 수 있게 된다.

```react
function App() {
  return (
    <div>
    	<h1>React Router DOM example</h1>
        	<ul>
            	<li><Link to="/">Home</Link></li>
	            <li><Link to="/topics">Topics</Link></li>
    	        <li><Link to="/contact">Contact</Link></li>
          	</ul>
		<Switch>
		    <Route exact path="/"><Home></Home></Route>
    	    <Route path="/topics"><Topics></Topics></Route>
        	<Route path="/contact"><Contact></Contact></Route>
        	<Route path="/">올바르지 않은 경로</Route>
        </Switch>
	</div>
  )
}
```



#### HashRouter

BrowserRouter를 HashRouter로 바꾸게 되면, 주소가 바뀌게 된다. 기존의 홈 화면의 주소였던 `http://localhost:3000/`는 `http://localhost:3000/#/`로 바뀌게 되고, Topics나 Contact도 `http://localhost:3000/#/Topics`와 `http://localhost:3000/#/Contact`로 바뀌어 있음을 알 수있다. 여기서 #는 북마크라는 것인데, 웹 서버는 북마크를 무시한다.



#### NavLink

Link를 NavLink로 바꾸더라도 표면적으로 보여지는 부분에서는 변경된 사항이 없다. 하지만 개발자 도구의 Elements에서 확인하게 되면, 선택된 content 목록의 a 태그의 속성(aria-current와 class)이 추가되는 것을 볼 수 있다. 그리고 Route 경로가 루트인 부분에서는 속성이 추가된 채로 계속 유지가 되고 있다. 그 이유는 Route와 같기 때문에 NavLink에도 exact를 넣어줄 필요가 있다.

이렇게 만들게 되면, 선택되는 목록마다 class가 부여된다. 이를 이용하면 선택되는 목록을 지정하여 꾸며주거나 어떤 기능을 추가할 수 있게 되는 것이다.



#### Nested Routing, Parameter

이번엔 parameter를 살펴볼 것이고, Nested Routing을 통해 Route를 중첩해서 사용해보려 한다.

```react
<Route path = '/contact/:id'>
    <Contact/>
</Route>
```

위의 태그를 이해하기 위해서 Topics 하위에 또 다른 페이지를 구현했다. Topics component는 아래와 같다.

```react
function Topics() {
  return (
    <div>
      <h2>Topics</h2>
          <ul>
	          <li>	<NavLink to="/topics/1">HTML</NavLink>	</li>
	          <li>	<NavLink to="/topics/2">JS</NavLink>	</li>
	          <li>	<NavLink to="/topics/3">React</NavLink>	</li>
          </ul>
		  <Switch>
              <Route path="/topics/1">
              	HTML is ...
              </Route>
              <Route path="/topics/2">
              	JS is ...
              </Route>
              <Route path="/topics/3">
              	React is ...
              </Route>
          </Switch>
    </div>
  )
}
```

이렇게 하면 Route 내에 Route가 중첩해서 작동할 수 있게 되는 것이다.

이제 배열을 하나 만들어서 자동으로 List가 만들어지고, 그에 따라 자동으로 Route가 만들어지도록 할 것이다. 우선 component 바깥 쪽에 배열을 하나 생성한다.

```react
var contents = [
  {id:1, title:'HTML', description: 'HTML is ...'},
  {id:2, title:'JS', description: 'JS is ...'},
  {id:3, title:'React', description: 'React is ...'}
]
```

이렇게 전역변수에 배열을 담았다. 실무에서는 이를 ajax 같은 것들을 통해서 데이터를 가져오는 경우가 많을 것이다. 그러면 이를 Topics component에 담아보겠다.

```react
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import reportWebVitals from './reportWebVitals';
import {BrowserRouter, Route, Switch, NavLink, useParams} from 'react-router-dom';

function Home() {
  return (
    <div>
      <h2>Home</h2>
      Home...
    </div>
  )
}

var contents = [
  {id:1, title:'HTML', description: 'HTML is ...'},
  {id:2, title:'JS', description: 'JS is ...'},
  {id:3, title:'React', description: 'React is ...'}
]
function Topic() {
  var params = useParams();
  console.log('params', params, params.topic_id);
  var topic_id = params.topic_id;
  var selected_topic = {
    title:'Sorry',
    description:'Not found'
  }
  for (var i =0; i<contents.length; i++) {
    if (contents[i].id === Number(topic_id)) {
      selected_topic = contents[i];
      break;
    }
  }
  return (
    <div>
      <h3>{selected_topic.title}</h3>
      {selected_topic.description}
    </div>
  )
}
function Topics() {
  var list = [];
  for (var i=0; i<contents.length; i++) {
    list.push(<li key={contents[i].id}><NavLink to={'/topics/'+contents[i].id}>{contents[i].title}</NavLink></li>)
  }
  return (
    <div>
      <h2>Topics</h2>
          <ul>
	          {list}
          </ul>
          <Route path="/topics/:topic_id">
             <Topic></Topic>
          </Route>
    </div>
  )
}
function Contact() {
  return (
    <div>
      <h2>Contact</h2>
      Contact...
    </div>
  )
}
function App() {
  return (
    <div>
    	<h1>React Router DOM example</h1>
        	<ul>
            	<li><NavLink exact to="/">Home</NavLink></li>
	            <li><NavLink to="/topics">Topics</NavLink></li>
    	        <li><NavLink to="/contact">Contact</NavLink></li>
          	</ul>
		<Switch>
		    <Route exact path="/"><Home></Home></Route>
    	    <Route path="/topics"><Topics></Topics></Route>
        	<Route path="/contact"><Contact></Contact></Route>
        	<Route path="/">올바르지 않은 경로</Route>
        </Switch>
	</div>
  )
}

ReactDOM.render(
    <BrowserRouter><App /></BrowserRouter>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
```

조금 복잡하지만 요약하면 다음과 같다. 이전에는 수동으로 Swtich와 Route들을 만들었던 것과 달리 하나의 Route로 `:topic_id`에 들어오는 값들이 Topic component로 전달되는데, 이는 useParams()를 이용해 그 값을 가져올 수 있다. 



