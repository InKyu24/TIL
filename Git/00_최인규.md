# 마크다운(Markdown)

> 일반 텍스트 형식 구문을 사용하는 마크업 언어의 일종으로 사용법이 쉽고 간결하며 빠르게 문서 정리를 할 수 있습니다. 단, 모든 HTML 마크업을 대체하지는 않습니다.
>
> 마크다운: Farmating에서 자유로운 간단한 문서 양식
>
> (HTML 용어) Markup <-> Markdown
>
> * 마크업: 문서에서 특정 내용이 어떤 역할을 하는지 표시(Mark) -> HTML(태그)
> * 마크다운: 마크업의 태그가 번거롭기 때문에 더 간단한 기호로 표시



## 1. 문법

### 1.1 Header

> 헤더는 제목을 표현할 때 사용합니다. 단순히 글자의 크기를 표현하는 것이 아닌 의미론적인 중요도를 나타냅니다.

* `<h1>` 부터 `<h6>` 까지 표현 가능합니다.
* `#`의 개수로 표현하거나 `<h1></h1>`의 형태로 표현 가능합니다.



# h1 태그입니다.

## h2 태그입니다.

### h3 태그입니다.

#### h4 태그입니다.

##### h5태그입니다.

###### h6 태그입니다.



### 1.2 List

> 목록을 나열할 때 사용합니다. 순서가 필요한 항목과 그렇지 않은 항목으로 구분할 수 있습니다. 순서가 있는 항목 아래 순서가 없는 항모긍ㄹ 지정할 수 있으며 그 반대도 가능합니다.

* 순서가 없는 목록
  * `1.`을 누르고 스페이스바를 누르면 생성할 수 있습니다.
  * `tab`키를 눌러서 하위 항목을 생성할 수 있고 `shift + tab` 키를 눌러서 상위 항목으로 이동 할 수 있습니다.
* 순서가 있는 목록
  * `-` (하이픈)을 쓰고 스페이스바를 누르면 생성할 수 있습니다
  * `tab` 키를 눌러서 하위 항목을 생성할 수 있고 `shift + tab` 키를 눌러서 상위 항목으로 이동 할 수 있습니다.



1. 순서가 있는 항목
2. 순서가 있는 항목
   1. 순서가 있는 하위 항목
   2. 순서가 있는 하위 항목



+ 순서가 없는 항목
+ 순서가 없는 항목
  + 순서가 없는 하위 항목
  + 순서가 없는 하위 항목



### 1.3 Code Block

> 코드 블럭은 작성한 코드를 정리하거나 강조하고 싶은 부분을 나타낼 때 사용합니다. 인라인과 블럭 단위로 구분할 수 있습니다.

+ Inline
  + 인라인 블럭으로 처리하고 싶은 부분을 `(백틱)으로 감싸줍니다.
+ Block
  + `` `(백틱) 을 3번 입력하고 `Enter` 를 눌러 생성



`add`한 요소를 remote 저장소에 올리려면 `$ git push origin master`를 터미널에 입력하니다.

```bash
$ git add.
$ git commit -m "first commit"
$ git push origin master
```



### 1.4 Image

> 로컬에 있는 이미지를 삽입하거나 이미지 링크를 활요하여 이미지를 나타낼 때 사용합니다.

+ `![]()`을 작성하고 `()`안에 이미지 주소를 입력합니다. `()`안에는 이미지 파일의 이름을 작성합니다.
+ 로컬에 이미파일을 저장한 경우 절대 경로가 아닌 상대 경로를 사용하여 이미지를 저장합니다.

![](data:image/png;base64,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)  ![](https://www.tangunsoft.com/storage/product_category/20180514071520.png)



### 1.5 Link

> 특정 주소로 링크를 걸 때 사용합니다.

+ `[]()`을 작성하고 `()` 안에 링크 주소를 작성하고 `[]`안에 어떤 링크 주소인지 작성합니다.

[git 공식문서](https://git-scm.com/)

[github 공식문서](https://github.com/)



### 1.6 Table

> 표를 작성하여 요소를 구분할 수 있습니다.

* `|`(파이프) 사이에 컬럼을 작성하고 `enter`를 입력합니다.
* 마지막 컬럼을 작성하고 뒤에 `|`를 붙여줍니다.

| working directory | statging area | remoe repo |
| ----------------- | ------------- | ---------- |
| working tree      | index         | history    |
| working copy      | cache         | tree       |



### 1.7 기타

#### 인용문

+ `>`을 입력하고 `enter`키를 누릅니다.

> git은 컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 파일들의 작업을 조율하기 위한 분산 버전 관리 시스템이다.

+ 인용문 안에 인용문을 작성하면 중첩해서 사용할 수 있습니다.

> $ git add.
>
> > $ git commit -m "fitst commit"
> >
> > > $ git push origin master



#### 수평선

+ `---`,`***`,`___`을 입력하여 작성합니다.

Working Directory

---

Staging Area

---

Remote Repository

---



#### 강조

+ 이탤릭체는 해당 부분을 `*` 혹은 `_` (언더바) 로 감싸줍니다.
+ 보드체는 해당 부분을 `**` 혹은 `__` (언더바 2개)로 감싸줍니다.
+ 취소선은 `~~` 표시를 사용합니다.

이것은 *이탤릭체*입니다.

이것은 **보드체**입니다.

이것은 ~~취소선~~입니다.



### 2. 과제

> 현재의 pdf **문서**를 마크다운 문법을 활용하여 `00_markdown_basic.md`로 만들어 보세요.













