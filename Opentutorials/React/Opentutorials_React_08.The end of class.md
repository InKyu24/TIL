## React

#### immutable

* 구현을 단순하게 유지하여 더 높은 복잡성에 도전하기 위한 노력
* 배열, 객체의 대체재로 사용하는 immutable.js 
* 모든 연산이 원본을 변경하지 않고, 복제된 원본을 변경한 결과를 반환

```html
<script src="immutable.min.js"></script>
<script>
	var map1 = Immutable.Map({ a:1, b:2, c:3 });
    var map2 = map1.set('b', 50);
    map1.get('b'); // 2
    map2.get('b'); // 50
</script>
```



#### router

+ React 웹 어플리케이션은 하나의 URL로 모든 페이지를 다루고 있다. 페이지 전환마다 네트워크 로딩을 하지 않는다는 장점이 있지만, URL만을 이용해 페이지를 찾지 못한다는 단점도 있다.
+ 이런 상황에서 우리를 도와줄 도구가 React Router이다. 
+ React Router를 사용하면 URL에 따라 적당한 Component가 실행되게 할 수 있다.
+ URL로 접근하는 사용자에게는 그 URL에 해당하는 UI를 서비스할 수 있는 퍼머링크 기능도 제공할 수 있다.



#### Create-react-app

+ Create-react-app은 매우 편리하지만 독선적이다. 제작자가 정해준 대로 사용할 수 밖에 없다.
+ 하지만 더 복잡한 작업을 하다보면 기본 도구만으로는 부족함을 느낄 수 있다.
+ 이런 경우에는 npm run eject를  실행하면, create-react-app에서 감춰진 여러 설정을 수정할 수 있게 된다.
+ 이 때부터는 마음대로 개발 환경 수정이 가능하지만 한 번 eject을 하게 되면 되돌아갈 수 없다는 것에 유의해야 한다.



#### redux

+ react의 component가 많아지면 component 간의 교류가 굉장히 까다로워진다.
+ 부모가 자식으로 데이터를 전달할 때는 Props을 활요해야 하고, 자식이 부모를 찾아갈 때는 event를 bubbling 시켜야 한다.
+ 이런 상황에서 redux가 필요하게 된다. redux는 중앙에 데이터 저장소를 하나 만들고, 모든 component는 중앙 저장소와 직접 연결된다. 그래서 중앙 저장소의 값이 변경되면 모든 component가 그 값 변경에 영향을 받게 된다.



#### react server side rendering

* 서버 쪽에서 웹 페이지를 완성한 후에 클라이언트로 완성된 HTML을 전송하는 것으로 어플리케이션의 구동을 시작할 수 있다. 덕분에 초기 구동시간을 단축할 수 있으며, 동시에 JavaScript 특유의 로딩이 필요없는 어플리케이션의 특성을 유지할 수 있다. 그러면서도 검색 엔진과 같은 로봇들이 HTML 태그를 직접 읽을 수 있기 때문에 웹 페이지 분석에 친화적인 기술이라고 할 수 있다.



#### react native

+ react native를 이용하면 react와 같은 방법으로 ios, android와 같은 native app을 만들 수 있다. 

