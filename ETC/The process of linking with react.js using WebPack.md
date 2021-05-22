## WebPack을 이용한 react.js 연동 과정

1. Node.js 설치

2. WebPack 설치 [npm(Node Package Manager)을 이용] 

   * npm install -g webpack : 전역에서 WebPack을 사용한다.
   * npm install --save dev webpack : 특정 의존성으로 설치한다.
   * Webpack : 브라우저 상에서 import 및 require로 호출, JS 파일 하나로 병합한다.
   * Webpack-dev-server : 별도 서버 구축없이 static 파일을 다루는 웹 서버를 열고, hot-loader를 통해 코드 수정마다 자동으로 reload 되게 해준다.

3. 모듈 파일 디렉토리 생성

   * WebPack을 이용한 Front-end 개발 시에는 모듈들을 모아두는 디렉토리가 필요하다. 빌드 시 포함될 필요가 없기 때문에 빌드 시에 포함되지 않아도 될 위치에 디렉토리를 생성하면 된다.
   * 가장 적절한 위치는 npm root 디렉토리인 src/main 밑에 생성하는 것이다

4. WebPack 설정 [npm install --save-dev webpack]

   * 앞서 global로 설치한 WebPack을 project level에서 한번 더 설치해야한다.
   * 추가로 --save 옵션을 주어 package.json 파일에 자동으로 dependency를 추가해준다.

5. webpack.config.js 파일 생성

   * 일일이 웹 서비스를 개발할 때마다 webpack 명령어를 쳐서 번들화 작업을 할 수 없기에 webpack.config.js 파일을 이용해 자동 번들화를 할 수 있도록 한다.

   ```javascript
   const path = require('path');
   
   module.exports = {
     context: path.resolve(__dirname, 'app.js'),
     entry: {
       home: './home.js',
     },
     output: {
       path: path.resolve(__dirname, 'webapp/resources'),
       filename: 'filename.js',
       publicPath: '/project_name/resources',
     }
   };
   ```

   * entry : 번들링할 파일의 정보
   * output : 번들 후에 나올 파일의 정보
   * 여기서 중요한 설정은 context, path, publicPath이다.
     * context : 앞에서 생성한 모듈 파일의 디렉토리
     * path는 엔트리 파일(번들 파일)이 저장될 위치를 설정한다. 이 디렉토리는 빌드 시 포함되는 디렉토리이며, WAS를 통해 접근 가능해야 한다.
     * publicPath 설정은 각종 리소스를 URL로 통해 접근할 때 URL 앞에 붙는 공통 경로로, WAS의 root context와 resource가 저장되는 디렉토리를 합쳐서 결정한다.

6. Spring context 설정

   * 엔트리 파일(번들 파일)이 저장되는 디렉토리는 WAS를 통해 접근이 가능해야 한다. 따라서 Spring context 파일에 아래와 같이 설정한다.

     ```xml
     <resources mapping="/resources/**" location="/resources/" />
     ```

7. package.json 설정

   * package.json 파일에 script 항목을 추가한다.

     ```json
     "scripts": {
       "develop": "webpack -w --mode development --devtool inline-source-map",
       "build": "webpack --mode production"
     }
     ```

   * 해당 스크립트들은 npm run ★스크립트명★으로 실행 가능하다.
   * develop 스크립트는 WebPack을 개발 모드로 실행한다.
     * inline-source-map 개발 도구를 사용한다. 
     * w(watch) 옵션을 주어서 모듈 파일이 변경 시 바로 번들링 되게 한다.
   * build 스크립트는 WebPack을 배포 모드로 실행한다.
     * 배포 모드로 실행 시에는 난독화 및 압축이 자동으로 설정되어, 엔트리 파일의 용량을 줄여준다.

8. Spring 프로젝트에 WebPack 적용

   * 개발 후 배포 시 war 파일로 배포된다.
   * WebPack을 이용해 Front-End 개발을 하면 두 종류(모듈 파일과 번들 파일)의 파일이 생성된다.
     * 번들링하게 되면 모듈이 모두 포함되기 때문이다. 모듈 파일은 개발 시에만 필요하다. 따라서 배포 시 모듈 파일을 war 파일에 포함시켜 war 파일의 용량을 키울 필요가 없다.