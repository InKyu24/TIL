## Python

Python and Atom 설치

+ 파이썬 3.5.2 설치
  + Add Python 3.5 to Path 체크
  + 커맨드 창 ➡ python 입력 ➡ print('hello world') 입력
  + 출력 결과 확인

+ Atom Editor (개발자용 텍스트 에디터) 설치
  + print('hello from a file') 작성
  + File ➡ Save as ➡ 바탕화면, 새폴더 py4e ➡ frist.py 저장
  + 커맨드 창 ➡ py4e 폴더로 경로 이동 ➡ python frist.py 입력
  + 출력 결과 확인



> 프로그래밍 : 사용자의 욕구를 충족시키기 위해 컴퓨터 내에 있는 자원에게 내리는 명령문들의 집합

> 사카이(Sakai) :  오픈소스 학습관리 시스템



파이썬을 사용해 소프트웨어를 개발하면 문법 에러(Syntax Errors)를 자주 만나게 될 것이다. 문법 에러에 익숙해져야 한다. 그렇기 위해서는 파이썬이 받아들일 수 있는 언어를 배워야 한다.



Elements of Python

+ Vocabulary / Words - Variables and Reserved words

  + 예약어 (Reserved Words)
    + 예약어는 일종의 약속으로 지정한 의미로만 쓰이는 단어를 의미한다.
    + cmd ➡ python ➡ help() ➡ keywords ➡ 예약어 목록 확인

+ Sentence structure - vaild syntax patterns

  + 문장 (Sentences or Lines)

    ```python
    x = 2
    x = x + 2
    print(x)
    ```

+ Story structure - constructing a program for a purpose

  + 문단 (Programming Paragraphs)
    + 대화형으로 python을 이용하는 경우에는 코드가 작성한 대로 작동하는 지 테스트하기에 좋다. 하지만 3~4줄을 넘어가서 실수를 할 경우에 처음부터 다시 작성해야 하는 불편함이 있다. 따라서 프로그램이 길어지는 경우에는 스크립트로 작성하는 것이 편리하다.
    + 파일(.py)에 프로그램을 짜면 python이 코드를 순서대로 읽기 시작한다.



+ 순차문 - 시작에 따라 순서대로 진행
  + 하나의 명령문이 끝나면 다음 명령문으로 넘어간다.
+ 조건문 - 특정 부분을 건너뛰어 진행
  + 예약어 if를 사용하여, 어떤 것이 참일 경우에만 실행하도록 한다.
+ 반복문 - 특정 부분을 계속 반복 진행 (반복할 문구를 저장하기도 한다.)
  + 예약어인 while문을 사용하여, 특정 조건에 해당하는 경우 반복 실행하도록 한다.

```python
name = input('Enter file:')
handle = open(name, 'r')

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts(word) = counts.get(word, 0) + 1
        
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount in None or count > bigcount:
        bigword = word
        bigcount = count
        
print(bigword, bigcount)
```

