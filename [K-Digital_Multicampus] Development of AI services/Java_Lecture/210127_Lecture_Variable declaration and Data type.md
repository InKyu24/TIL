# Data Type

![img](https://1.bp.blogspot.com/-J5Jy934OYgA/YBobEcKiieI/AAAAAAAAGTs/GFwCUp1AcM8Wob0eWT9s_X0SeiGmr-HwgCLcBGAsYHQ/w640-h203/%25EA%25B7%25B8%25EB%25A6%25BC1.png)



> 객체는 메모리에 "주소"가 들어간다.
> 즉, 같은 데이터여도 "주소"가 다르다면, 다른 데이터로 인식



# 변수의 선언

\- 변수의 선언: *타입* **변수이름;**
  ex) *int* **age;**, *double* **value;**

\- 변수 이름을 위한 명명 규칙
  첫 글자는 문자, $, _로 시작하고, 숫자로 시작할 수 없다.
  영어 대소문자가 구분된다.
  자바 예약어는 사용할 수 없다.
  문자 수(길이)의 제한은 256문자.
  첫문자는 영어 소문자로 시작하고, 다른 단어가 붙을 때 대문자로 붙이는 것이 관례
  (ex. maxSpeed, firstName, carBodyColor)



\- 변수값 저장의 두 가지 방법
  int score; 변수 선언
  score=90; 값 저장(초기화)

  int score=90; 변수 선언 및 값 저장(초기화)

 \* 변수 선언과 값 저장(초기화)의 구분은 Member Data에서는 할 수 없다. Local Data 한정.

 \* Member Data에서는 아래와 같이 작성 가능. (value 값을 0으로 초기화하여 진행하기 때문)
  int value;
  int result=value+10;

\- 리터럴 (Literal): 소스 코드 내에서 직접 입력된 변수의 초기값
  정수 리터럴, 실수 리터럴, 문자 리터럴, 문자열 리터럴, 논리 리터럴

\- 변수는 중괄호 블록 { } 내에서 선언되고 사용
  서로 독립적으로 존재하는 블록 간의 변수는 사용 불가



# 데이터 타입 변환

\- 데이터 타입 변환 (묵시적 자동 타입 변환) : Promotion

[![img](https://lh3.googleusercontent.com/-67Q4c5NzfLI/YBEiOT8RvZI/AAAAAAAAGKo/58lGw8IBoKsDU7nAFca5SNZHBMOnItGiQCLcBGAsYHQ/w400-h231/image.png)](https://lh3.googleusercontent.com/-67Q4c5NzfLI/YBEiOT8RvZI/AAAAAAAAGKo/58lGw8IBoKsDU7nAFca5SNZHBMOnItGiQCLcBGAsYHQ/image.png)



\- 데이터 타입 변환 (명시적 강제 타입 변환) : Casting



[![img](https://lh3.googleusercontent.com/-oHfq_jo1fpM/YBEiuCKDUqI/AAAAAAAAGKw/cp6HSllfae82CwS8k60HE6rnYVldorHIwCLcBGAsYHQ/w400-h213/image.png)](https://lh3.googleusercontent.com/-oHfq_jo1fpM/YBEiuCKDUqI/AAAAAAAAGKw/cp6HSllfae82CwS8k60HE6rnYVldorHIwCLcBGAsYHQ/image.png)

[![img](https://lh3.googleusercontent.com/-4F4Ersetl8Q/YBEkgeUxQzI/AAAAAAAAGK8/HYFBzXk6tZEje0HObzdikjkc7oQ4lrymQCLcBGAsYHQ/w400-h189/image.png)](https://lh3.googleusercontent.com/-4F4Ersetl8Q/YBEkgeUxQzI/AAAAAAAAGK8/HYFBzXk6tZEje0HObzdikjkc7oQ4lrymQCLcBGAsYHQ/image.png)

   \* Casting에서는 데이터 유실의 위험이 있다.

  \* byte(1) < short(2) < int(4) < long(8) < float(4) < double(8)