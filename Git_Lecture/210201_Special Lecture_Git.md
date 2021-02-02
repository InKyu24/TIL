## Git / Github 특강

## Github

> 코드 관리, 저장, 협업이 가능한 공간이자 나아가서는 개발자들의 이력서가 될 수 있다. 따라서 이제부터는 Github를 나의 SNS로 만들자!



### tensorflow (오픈소스 프로젝트)

> 특정 업체의 생산한 기술을 독점하는 것이 아니라, 기술 이해만 있다면 누구든 활용 가능한 형태



### MOOC (Massive Open Source Online Courses)

1. Coursera - Andrew Ng의 Deep Learning 강의

2. Edx – CS50(기초) 강의

3. Udacity - Machine Leaning 강의

4. K-MOOC



### 코딩 관련 플랫폼

1. Codecademy – Java learn

2. Code School

3. Code Avergers

4. Team Treehouse
5. Kaggle - 코딩 대회



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



# Git

> 코드 관리, 협업, 배포 도구
> Git은 **버전**을 통해 **코드**를 관리하는 도구

+ SCM(Source Code Management): 코드 관리
  + 프로그래밍 (소스) 코드? 컴퓨터에게 명령 (Java -> Computer)
+ VCS(Version Control System): 버전 관리



# CLI

Command Line Interface

커맨드(명령어)를 통해 작동하는 인터페이스

<-> GUI(Graphic User Interface, 보통의 프로그램)



#### GUI vs. CLI

+ GUI(Graphic User Interface): 컴퓨터 사용을 그래픽으로 함
+ CLI(Command Line Interface): 컴퓨터 사용을 **명령어**(줄)로 함



## 기초 명령어

> CLI 명령어 : Unix 계열 명령어(Linux, Mac)
>
> * Git은 **폴더 단위**로 코드를 관리



### (1) `pwd`

+ `pwd`(print working directory): 현재 폴더의 경로
+ `-`(home directory): 홈 디렉토리(git bash를 처음 열면 나오는 기본 폴더)



### (2) `ls`

+ `ls`(list): 내용물을 출력



### (3) `cd [폴더명]`

+ `cd`(change directory): 폴더를 변경
+ `cd ..` : 상위 폴더로 이동
+ `cd .` : 현재 폴더로 이동



### (4) `mkdir [폴더명]`

+ `mkdir(`make directory): 폴더를 생성



### (5) `rm [파일명]`

+ `rm`(remove): 파일을 삭제



### (6) `rm -r [폴더명] `

+ `-r` : recursively(재귀적으로) 폴더를 삭제



### (7) `touch [파일명]`

+ touch : 파일 생성



### (8)`cp [파일명] [위치]`

+ `cp`(copy): 파일 복사



### (9) `cp -r [파일명] [위치]`

+ 폴더를 복사



### (10)`mv [파일/폴더명] [바꿀파일/폴더명]`

+ `mv`(move): 파일/폴더명 변경
+ `mv [파일/폴더명] [위치]` : 파일 또는 폴더를 **이동**



# Github TIL

## 1. TIL?

> + TIL은 **T**oday **I** **L**earned의 줄임말로 개발자 사이에서 매일 자신이 학습한 내용을 commit(기록)하는 것
> + github, bitbucket, gitlab과 같은 원격 저장소에서 제공하는 1commit-1grass의 흥미 요소 제공

## 2. TIL 세팅

### (1) Git으로 프로젝트 관리 시작 : `git init`

> .git이라는 비밀스러운 하위 디렉토리 생성

+ 자신이 앞으로 학습한 내용을 기록할 `TIL` 폴더를 하나 생성한다. 이때 해당 폴더는 최상단에 생성한다.

+ `git bash`에서 `TIL`폴더로 이동한 이후에 아래의 명령어로 git 관리를 시작한다.

  ```bash
  $ git init
  ```



### (2) Commit을 위한 Staging : `git add`

+ 현재 코드 상태의 스냅샷을 찍기 위한 파일 선택 (==Staging Area에 파일 추가)

  ```bash
  $ git add [파일 이름] # .은 모든 변경 사항을 staging area로 올림
  ```



### (3) 버전 관리를 위한 스냅샷 저장 : `git commit`

+ 현재 상태에 대한 스냅샷을 `commit`하여, 버전 관리를 진행한다.

  ```bash
  $ git commit -m "커밋 메시지"
  ```



### (4) 원격 저장소 정보 추가 : `git remote`

+ Github 원격(remote) 저장소(repository)를 생성하고 `TIL` 폴더와 연결한다.

+ 새로운 원격 저장소가 추가될 때만 입력한다.

  ```bash
  $ git remote add origin (github 원격 저장소 주소)
  ```



### (5) 원격 저장소로 코드 `git push`

+ 최종적으로 Github 원격 저장소에 push한다.

  ```bash
  $ git push origin master
  ```



### (6) 그 외 명령어

+ 현재 `git`의 상태를 조회 `git status`

  ```bash
  $ git status
  ```

+ 버전 관리 이력을 조회 [Author, Date, Message, Commit hash]

  ```bash
  $ git log
  ```

  + 버전 관리 이력 한줄로 짧게 조회

  ```bash
  $ git log --oneline
  ```

+ git 설정 (user.name & user.email) : **최초 1회 설정**

  ```bash
  $ git config --global user.name "InKyu CHOI"
  $ git config --global user.email "484342@gmail.com"
  ```

+ 현재 상태과 commit 버전과의 차이 확인

  ```bash
  $ git diff
  ```

  

## 3. `README.md`

> 원격(remote) 저장소(repository)에 대한 정보를 기록하는 마크다운 문서. 일반적으로 해당 프로젝트를 사용하기 위한 방법 등을 기재한다.

### (1) `README.md` 파일 생성

+ `README.md` 파일을 `TIL` 폴더(최상단)에 생성한다. 이름은 반드시 **README.md**로 설정한다.

  ```bash
  $ touch README.md
  ```

  

### (2) (자신만의) TIL 원칙에 대한 간단한 내용 추가

+ 마크다운 작성법 pdf에서 배우고 실습한 내용을 토대로 `README.md` 파일을 작성한다.
+ 형식은 자유롭게 작성하되 마크다운 문법(의미론적)을 지켜서 작성한다.



### (3) 저장 후 버전관리 : `add`, `commit`, `push`

+ 작성이 완료되면 아래의 명령어를 통해 commit 이력을 남기고 원격 저장소로 push한다.

  ```bash
  $ git add README.md
  $ git commit -m "add README.md"
  $ git push origin master
  ```

  

## 4. 추가 학습 내용 관리

### (1) 추가 내용 관리

+ `TIL` 폴더 내에서 학습을 원하는 내용의 폴더를 생성하고 파일들을 생성한 후 작업을 진행한다.

  ```bash
  $ mkdir python
  ```



### (2) 변경 사항을 저장하고, 원격저장소로 옮긴다.

+ 업데이트가 완료되면 아래의 명령어를 통해 commit 이력을 남기고 원격 저장소로 push한다.

  ```bash
  $ git add .
  $ git commit -m "학습 내용 추가"
  $ git push origin master
  ```

  

## 5. Commit message convention

+ 정해진 규칙은 없다. (company by company) 그렇기 때문에 GitHub 컨벤션을 따르면서 배울 것

+ 항상 일관적인 규칙과 간결함을 유지하자.

+ 동사원형 + 목적어 (ex. [docs] Add my age.)

+ 제목 앞에 타입을 붙이고, 마지막에 마침표 붙일 것.

  > feat : 새로운 기능 추가
  > fix : 버그 수정
  > refacor : 코드 리펙토링
  > style : 코드 형식, 정령, 주석 등의 변경 (동작에 영향 없음)
  > test : 테스트 추가, 테스트 리펙토링 (제품 코드 수정 없음, 테스트 코드에 관련된 모든 변경)
  > docs : 문서 수정  (제품 코드 수정 없음)
  > chore : 빌드 업무 수정, 패키지 매니저 설정 등 위에 해당하지 않는 것들