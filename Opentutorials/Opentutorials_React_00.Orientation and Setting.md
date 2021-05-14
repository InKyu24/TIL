## React

### 수업 소개

React는 Facebook.com의 UI를 더 잘 만들기 위해서 Facebook에서 만든 Javascript UI 라이브러리이다.

웹 사이트는 매우 빠른 속도로 복잡해진다. 정보가 조금만 증가해도 그 정보를 표현하는 HTML 태그는 기하급수적으로 복잡해진다.

가짜 코드를 통해 React의 필요성을 인지해보자. Top, Sidebar와 같은 사용자 정의 태그를 이용해서 Index.html에 아래 코드와 같이 작성될 수 있다. (물론 이해를 돕기 위한 가짜 태그이다.)

```html
<html>
    <body>
        <Top></Top>
        <Sidebar></Sidebar>
    </body>
</html>
```

React는 이러한 기술을 활용한 것이다. React에서는 사용자가 정의해서 태그를 만드는 것을 사용자 정의 태그가 아니라, Component라고 불리운다. 

Component는 세 가지의 특징을 갖는다.

하나, 복잡한 코드들을 줄여, 가독성을 획기적으로 늘릴 수 있다.

둘, 한 번 정의된 Component는 여러 곳에서 재사용을 할 수 있다.

셋, 개선해야 하는 이슈들이 있는 경우, Component의 내용을 수정하게 되면, 사용된 모든 곳에서 동시다발적으로 실시간으로 변경된 내용이 업데이트되기 때문에 유지보수에 용이하다.



### 개발 환경

#### 오리엔테이션

1. 개발 환경을 세팅하고 어디에 코드를 바꿔야하는가를 살펴보는 Coding

2. 그렇게 작성된 코드의 결과를 보는 Run

3. Coding과 Run의 반복을 거쳐 모든 작업이 끝난 후에 최종적으로 소비자에게 전달하는 Deploy

이 세 가지를 살펴보고, 뒤에서 나머지 자세한 개념들을 알아보자.



#### React.js 개발환경의 종류

React 공식 문서에 익숙해지는 것이 중요하다.

개발 환경을 세팅하기 위해서 공식 문서를 살펴보자.

`Get Started`로 들어가게 되면, React를 실행해볼 수 있는 여러가지 방법들이 있다.

1. Online Playground

   온라인 코드 편집기로 온라인 상에서 React application을 구현해볼 수 있다. `CodePen`, `CodeSandbox`, `Stackblitz` 등이 있다.

2. 웹 사이트에 React를 추가하기

   이미 보유한 웹 사이트에 부분적으로 React 기능을 추가하는 방법이다. 뒤로 갈수록 개발환경을 직접 구축해야하는 어려움이 많기 때문에 초급 사용자에게는 상당히 까다로울 수 있는 방법이다.

3. 새 React 앱 만들기

   React로 앱을 개발할 때 필요한 개발환경 및 도구들을 종합적으로 제공하는 편리한 도구들을 toolchain이라 한다.

   Toolchain의 특징은 아래와 같다.

   + 많은 File, Component의 스케일링
   + 서드파티 npm 라이브러리 사용
   + 일반적으로 하는 실수들을 조기에 발견
   + CSS와 JS를 실시간으로 편집
   + 프로덕션 코드 최적화

   React에서 추천하는 Toolchain들은 아래와 같다.

   + React를 배우거나, 새로운 SPA를 제작하기 위해서는 `Create React App`
   + Node.js로 서버 렌더링 웹 사이트를 구축하고 있다면 `Next.js`
   + 정적 콘텐츠 지향 웹 사이트를 구축하고 있다면, `Gatsby`
   + Component 라이브러리 혹은 이미 있는 코드 베이스에 통합을 하고자 한다면,  `More Flexible Toolchains`

   여기서는 `Create React App`을 사용할 것이다.

   ```
   npx create-react-app my-app
   cd my-app
   npm start
   ```

   > npm이란?
   >
   > node.js라는 기술을 이용해서 만든 여러 app들을 명령어 환경에서 손쉽게 설치할 수 있도록 해주는 도구
   >
   > (즉, node.js 계의 App store)
   
   

### npm을 이용해서 create-react-app 설치하기

npm을 사용하기 위해서는 우선 node.js를 설치해야 한다.

> 더 알아보기 위해서는 [npm 생활코딩 강의](https://opentutorials.org/module/4044) 참고

cmd 창에서 아래와 같이 npm 버전을 확인했을 때 결과가 나타나면 성공적으로 node.js가 설치된 것이다.

```
npm -V
```

이후 아래 명령어를 입력하여 `create-react-app`을 설치하면 된다.

```
sudo npm install -g create-react-app
```

> -g는 global

 공식적으로는 npx를 이용하는 것이 정석이다.

> npm이 app을 설치하는 프로그램이라면, npx는 app을 임시로 설치해서 딱 한 번만 실행시키고 지우는 것이다. 그래서 npx는 공간을 차지하지 않고, 항상 최신 상태를 유지할 수 있다는 장점이 있다.



### create-react-app을 이용해서 개발환경  구축

바탕화면에 `react-app` 폴더를 생성하고, cmd 창에서 아래 명령어를 이용해 해당 경로로 이동한다.

```
cd C:\User\user\Desktop\react-app
```

경로가 이동된 것을 확인하고, cmd 창에 아래와 같은 명령어를 작성하면, 해당 경로에 개발환경을 구축하게 된다.  

```
create-react-app .
```



### 샘플 앱 실행하기

Visual Studio Code라는 프로그램으로 샘플 앱을 실행해보자. Visual Studio Code에서는 terminal 명령어 입력[View > Apperance > Show panel] 또는 [Ctrl + J]을 지원한다. 

명령어로 아래와 같이 입력을 하면, 웹 브라우저가 자동으로 열리면서 특정 웹 페이지가 열리게 된다.

```
npm run start
```

특정 웹 페이지는 가장 최소한의 앱을 미리 구현해서 보여주게 되고, 결과창에는 특정 웹 페이지의 주소 경로를 보여주게 된다.

Ctrl + C로 실행을 끌 수 있으며, 다시 명령어를 입력해 켤 수 있다.



### JavaScript 코딩하는 법

index.html 파일 내에는 `<div id="root"></div>` 안쪽에 react를 통해 만든 component가 들어가 있는 것을 볼 수가 있다.

그러면 id가 root인 태그 안쪽에 들어가는 Component는 모두 src라는 디렉토리 내에 위치한 파일들이다.

src 내에 위치한 많은 파일들 중 엔트리 파일은 index.js 파일이다. index.js에서 주목해야 하는 부분은 `ReactDOM.render(<App />, document.getElementById('root'));` 이다. 

왜냐하면 `document.getElementById('root')`로 인해서 index.html 파일 내 id가 root인 태그 안쪽에 component가 들어가는 것이기 때문이다.

이제 `<App />`에 대해서 살펴보자. App은 React를 통해 만든 사용자 정의 태그인 Component를 의미한다.  컴포넌트의 실제 구현은 `import App from './App';`에서 진행된다. `./App`은 현재 폴더 내의 App.js 파일을 의미하며, 확장자명이 생략된 것이다.

따라서 App.js에서 특정 내용을 변경할 수 있다.



### CSS 코딩하는 법

React에서 CSS를 수정하는 방법을 살펴보자. 이건 React에서의 방법이라기 보다는 Create React App의 지배 하에서 CSS를 어떻게 하면 되는가를 살펴보는 것이다.

index.js 파일을 보면, `import './index.css';`를 통해, index.css를 가져오고 있고, index.css를 수정하면 자동으로 반영되는 것을 볼 수 있다.



### 배포하는 법

아래 명령어를 통해, build라는 디렉토리를 생성할 수 있다. 

```
npm run build
```

build 폴더 내부에는 실제 프로덕션 환경에서 사용되는 App을 만들기 위해, 공백과 같이 불필요한 내용들을 정리한 결과들이 나타난다.

따라서 실제로 서비스하기 위해서는 build 내의 존재하는 파일들을 이용하면 된다. 웹 서버가 문서를 찾는 최상위 디렉토리에다가 빌드 디렉토리 안쪽에 있는 파일들을 위치시키면 된다. 그러면 실 서버 환경이 완성된 것이다.

```
npm serve -s build
```

