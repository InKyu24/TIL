# 최종 정리

## 관리 도구로서의 github

git bash를 통해 TIL 폴더로 진입하고, cd 명령어와 init 명령어를 통해 TIL 폴더 내에 .git이라는 숨긴 폴더를 심게 되면 github에 TIL 폴더 내 모든 폴더와 파일을 버전 관리할 수 있게 된다. 이 때 TIL폴더를 작업 중인 폴더 (Working Directory 또는 Working Tree)라고 한다.



![](https://lh3.googleusercontent.com/-7FJs726iuwI/YBljC4S2PtI/AAAAAAAAGTQ/z_hx-achJDklVpvq1u2sRAXrEL1nT4B3wCLcBGAsYHQ/w400-h260/image.png)



작업 중인 폴더 내 파일을 github에서 관리할 수 있도록 하기 위해서는 먼저 git 내 add 명령어를 사용하여 스테이지(Staging Area 또는 Index) 위로 올려놓는 작업이 필요하다. 스테이지 위에 올라온 파일은 commit을 대기하고 있게 된다. commit -m "commit message"명령어를 이용하면 스테이지 위에 올려놓은 파일에 메시지가 기록된다. 그리고 push 명령어를 사용하면 github(원격 저장소)에 파일을 올릴 수 있게 된다.

>  나는 이 과정을 정형외과에서 X-ray를 촬영하는 상황으로 이해하였다.



![](https://lh3.googleusercontent.com/-ox5zYpbULTE/YBljE8dUhJI/AAAAAAAAGTU/1_HIhx3CV5EUS5bZrzPBPdSQkMiib_DGQCLcBGAsYHQ/w640-h186/image.png)



더 나아가 스테이지에 올라간 파일을 git rm --cached 명령어로 다시 뺄 수도 있다.



## 배포 및 협업 도구로서의 github

github는 코드 관리 뿐만 아니라 배포 및 협업을 가능케 하는 도구로 쓰인다.



### 협업에 필요한 명령어

+ 원격 저장소에서 **최초로**  가져오기

  > 누구의 것도 자유롭게 가져올 수 있다. 단, Push 시에는 마스터의 초대가 필요하다.

```bash
$ git clone [원격 저장소 주소]
```



+ 원격 저장소에서 차이만 가져오기

```bash
$ git pull origin master
$ git pull origin main
```



+ 스테이지에 올라간 파일 내리기

```bash
$ git rm --cached [파일 이름]
```



+ 원격 저장소에 갖다주기

```bash
$ git push origin master
$ git push origin main
```



### 코드를 협업하는 세 가지 방법

#### 협업의 전제

협업은 수직적 독재에 가깝다고 익숙해진 뒤에 수평적인 협업을 익히는 것이 효율적이다.

#### (1) Push & Pull 협업 모델

> 끝말 잇기

##### Push & Pull 의 장점

+ 단순함, 기본적인 git 활용만으로 협업 가능



##### Push & Pull 의 단점

+ 꼭 공유를 해야 협업이 가능함

+ synchronoes한 협업 모델

  + 한 사람의 일이 끝나야 다른 사람이 시작할 수 있다.

    > 즉, 무전기처럼 1명이 수정하게 되면 Push하는 경우,
    >
    > 코드가 꼬일 가능성이 있기 때문에 다른 사람들은 수정을 하면 안된다.



#### (2) Fork & PR 협업 모델

> 전공 입력하기

##### Fork & PR 의 장점

+ Asynchronous한 협업이 가능함

  + 오픈 소스 협업에 주로 쓰이며, master가 요청한 PR을 검토하여 수락하는 방식이다.

  

##### Fork & PR의 단점

+ master가 이해하지 못하면, 좋은 제안도 받아들여지지 않을 수 있다.
+ master가 일일이 확인하기 귀찮다.



#### (3) Branch & PR 협업 모델

1. Fast-forward

배포 가능한 master branch에서 새 branch(feature-A)를 생성하여,  master branch에서 feature-A로  branch를 변경한다. 만약 feature-A branch에서 commit을 진행했고, master에서 별도의 commit이 없다면 master branch로 Fast-forward병합을 진행한다.



2. Merge commit

만약 feature-A branch에서 commit을 진행했고, master에서도 commit을 진행했다면, merge commit을 진행한다.



3. Non Fast-forward

Fast-forwarding 상황에서도 commit을 발생시키는 옵션.

> Non fast-forward 옵션을 사용할 경우, Branch가 그대로 남기 때문에 작업 확인 및 관리 측면에서 더 유용할 수 있다.



3. Rebase

만약 feature-A branch에서 commit을 진행했고, master에서도 commit을 진행했다면, merge commit을 진행한다.



> Rebase와 Merge는 최종 결과는 같으나, commit history가 다르게 형성된다.
>
> Merge : 변경 이력이 모두 그대로 남기 때문에 이력이 복잡해짐
>
> Rebase : 이력이 단순해져서 정확한 이력을 남기기 어려워짐



##### Branch 관련 명령어

```bash
$ git branch [branch name]	//브랜치 생성
$ git checkout [branch name] // 브랜치 이동
$ git checkout -b [branch name] // 브랜치 생성 및 이동
$ git branch // 브랜치 목록
$ git branch -d [branch name] // 브랜치 삭제

$ git checkout - // 방금 사용하던 브랜치로 이동
```

각 branch에서 작업한 후에 이력을 합치기 위해서는 일반적으로 merge 명령어를 사용한다.

서로 다른 commit 사이에서 동일한 파일을 수정한 경우, 병합 시 충돌이 발생할 수 있다. 이 경우는 오류가 발생한 것이 아니라 불가피한 충돌으로 반드시 직접 수정으로 해소해야 한다.

##### Branch & PR 의 장점

+ Asynchronous한 협업이 가능함

  + 오픈 소스 협업에 주로 쓰이며, master가 요청한 PR을 검토하여 수락하는 방식이다.

  

##### Branch & PR의 단점

+ 
+ master가 일일이 확인하기 귀찮다.



## QnA

#### 오픈 소스에 기여하는 방법

+ 다양한 방법이 있지만 tensorflow의 번역에 참여하는 방법부터 시작하면 좋은 습관이 될 것 같다.



#### 채용을 목표로 프로젝트에 참여하는 방법

+ 채용 전에 Toy Project를 하면서 다양한 경험을 쌓아보기
+ if(kakao), AWS re:Invent 등과 같은 기업들의 기술 컨퍼런스에 관심 갖기



#### 코딩 테스트 공부 방법

+ [Programmers](Programmers.co.kr)에서 1~2 level 도전
+ [SWEA](swexpertacademy.com)에서 Samsung IM level 도전, 나아가 A level(중급)까지
+ Kakao 문제 1~2번 도전, 나아가 3~4번(중급)까지



#### 협업 방식 중에 가장 많이 사용하는 방식

+ Branch & PR 방식



#### Github 내 모범사례 될 수 있는 페이지

+ 개발 커뮤니티를 통해 Search 해볼 것
+ 타인을 위한 코드를 작성해서 올리도록 노력하는 것이 중요



#### IDE와 Git의 연동 가능한 지

+ 이클립스도 가능하기 때문에 방법을 찾아볼 것



#### 강동주 강사님께 추가로 궁금한 사항있다면

- Email: john@hphk.kr 으로 질문!



## 강의를 수강하고 느낀 점

이제부터 시작이라는 느낌이 많이 들었다. 강의를 수강하기 전에는 낮설고 두려웠던 마음이 더 컸지만 강의를 수강한 후 자신감이 생겼고, 뭐든지 해낼 수 있을 것 같다. 지금까지 배운 것은 빙산의 일각이지만, 더 많이 배우고 싶게 되었다.



