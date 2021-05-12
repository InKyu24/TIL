 

# JDK 및 IDE(Ecilpse) 설치 및 세팅

## 1. 압축파일을 받은 뒤, 관련 폴더에 압축 풀기

> JDK : Java Development Kit
> JRE : Java Runtime Environment
> JVM : Java Virtual Muchine 
>
> JDK > JRE > JVM



Java 특징

- Platform 독립적
- 객체지향적(Reusable)
- Memory management 자동화
- Multi-Thread 기능을 쉽게 지원
- Exception 처리가 쉽고 강력
- Security



## 2. 환경 변수 설정

+ Java jdk1.8.0_65 내 bin 폴더 상위폴더까지 경로를 복사 (영문 폴더로 생성할 것)

[![img](https://lh3.googleusercontent.com/-XXoorewmzug/YBAVNaAF8DI/AAAAAAAAGIg/a4db-ukOQlEmgM9Wzjw_mIOwRiBOOk71wCLcBGAsYHQ/s16000/image.png)](https://www.blogger.com/blog/post/edit/9180050484951786848/3503339350682850062#)

+ 내 컴퓨터 > 속성 > 고급 시스템 설정 > 환경 변수 > 시스템 변수 > 새로 만들기
  + 변수 이름: *JAVA_HOME*
  + 변수 값: *[복사한 경로]*

[![img](https://lh3.googleusercontent.com/-v4XR_FhiCas/YA_3oRaDCUI/AAAAAAAAGHY/vpNkL-82CUY2LSzSUGCxCaCN-Pq5OvDBQCLcBGAsYHQ/w640-h360/image.png)](https://www.blogger.com/blog/post/edit/9180050484951786848/3503339350682850062#)

+ 내 컴퓨터 > 속성 > 고급 시스템 설정 > 환경 변수 > 시스템 변수 > path 편집
  + *%JAVA_HOME%\bin* 추가

[![img](https://lh3.googleusercontent.com/-wlxwn4lnOb4/YBAV0_vtO7I/AAAAAAAAGIo/T3SBAv_EHPksUrzlWfmwpuKfXVV0hCtUACLcBGAsYHQ/w400-h381/image.png)](https://www.blogger.com/blog/post/edit/9180050484951786848/3503339350682850062#)

- 윈도우+R키를 눌러, cmd (명령 프롬프트) 열기
  - *javac -version*과 *java -version*을 쳐서 아래와 같은 결과값 얻기

[![img](https://lh3.googleusercontent.com/-cKuw6R-lM-M/YA_3HnrY-fI/AAAAAAAAGHI/LMLjU4zhrbUXes93NOQUtvB524YW59w8QCLcBGAsYHQ/w400-h266/image.png)](https://www.blogger.com/blog/post/edit/9180050484951786848/3503339350682850062#)



## 3. text 파일 이용한 프로그래밍 연습

- 메모장을 열어 아래와 같이 작성 후, Hello.java (확장자 변경)으로 저장

```java
public class Hello {
	public static void main(String[] args) {
		System.out.println("Hello");
	}
}
```

> <u>H</u>ello, <u>S</u>tring, <u>S</u>ystem 앞 글자 대문자로 쓸 것. 



- 명령 프롬프트를 실행

1. *cd [Hello.java를 저장한 폴더 경로*]

> 만일 D 드라이브에 Hello.java를 저장했다면, *d:* 을친 뒤에 1번부터 진행

2. *dir* 을 쳐서, 디렉터리 내용 확인
3. *javac Hello.java* 를 쳐서 컴파일링
4. *dir* 을 쳐서, class 파일 생성된 것을 확인
5. *java Hello* 를 쳐서, 결과값 확인

[![img](https://lh3.googleusercontent.com/-HO12q_sHPGM/YBAX1TYRg-I/AAAAAAAAGI0/ZrxkBETHT_4WFrFFp9on62n5q7dpbN4iwCLcBGAsYHQ/w400-h358/image.png)](https://www.blogger.com/blog/post/edit/9180050484951786848/3503339350682850062#)



java code -> compile(javac.exe) -> class(bytecode) -> JVM(any OS)

> 자바 코드를 컴파일해서 배포하면, 어디에서든 다시 컴파일할 필요없이 실행시킬 수 있다.
>
> 하지만 실행하려면 해당 조건에 맞는 JVM이 설치되어 있어야 한다.



## 4. Ecilpse 세팅

- 작업 폴더(workspace)를 생성

- Text file encoding 변경

  window > Preferences > General > Workspace 에서 텍스트 파일 인코딩을 UTF-8로 변경

[![img](https://lh3.googleusercontent.com/-q5SJZzeM0Tc/YA_9C1_oeHI/AAAAAAAAGIU/T_Qs45AE1ZosrINbAMKPk5iCL38gRIhOQCLcBGAsYHQ/w640-h506/image.png)](https://www.blogger.com/blog/post/edit/9180050484951786848/3503339350682850062#)



- Perspective에서 Java로 변환

> Java EE에서는 더 넓은 범위의 프로젝트들을 생성할 수 있으나, 현재는 Java로 연습



[![img](https://lh3.googleusercontent.com/-jbK--VFsuFY/YBAm_C_I-AI/AAAAAAAAGJA/-LKj5vzvVfcad_eIFwAuVGt1iieQc8adQCLcBGAsYHQ/w305-h400/image.png)](https://www.blogger.com/blog/post/edit/9180050484951786848/3503339350682850062#)



> 단축키:
>
> 폰트 사이즈 확대, 축소 : `Ctrl & +` `Ctrl & -`
>
> 행주석 설정 및 취소 : `Ctrl & /`
>
> 범위주석 설정, 취소 : `Ctrl & Shift & /`, `Ctrl & Shift & \`

