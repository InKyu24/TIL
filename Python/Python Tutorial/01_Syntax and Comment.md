### Python Syntax

##### Python Indentation

들여쓰기는 코드 라인의 시작 부분에 있는 공백을 나타낸다. 다른 프로그래밍 언어에서 코드의 들여쓰기는 가독성을 위한 것이지만 파이썬의 들여쓰기는 매우 중요하다. 왜냐하면 파이썬은 들여쓰기를 사용하여 코드의 블록을 나타내기 때문이다.

아래의 두 코드처럼 공백의 크기에는 제한이 없으며, 하적어도 한 칸의 공백만 있으면 된다.

```python
if 5 > 2:
	print("5 is greater than 2!")
	print("hello")

# [결과]
# 5 is greater than 2!
# hello
```

```python
if 3 > 2:
 print("3 is greater than 2!")

# [결과]
# 3 is greater than 2!
```

하지만 들여쓰기를 실행하지 않거나 동일한 코드 블록에서 동일한 수의 공백을 사용하지 않으면, IndentationError가 발생한다.

```python
if 5 > 2:
	print("5 is greater than 2!")
 print("hello")

# [결과]
# IndentationError: unexpected indent
```



### Python Comment

파이썬에는 코드 내 일부를  문서화 할 수 있도록 주석 기능을 지원한다.

+ 주석은 파이썬 코드를 설명하는 데, 사용할 수 있다.
+ 주석을 사용하여 코드를 더 쉽게 읽을 수 있다.
+ 코드를 테스트할 때 실행에서 제외시키고 싶은 부분에 대하여 주석을 사용할 수 있다.

##### Creating a Comment

주석은 #으로 시작하고 파이썬은 주석처리 되지 않은 부분만을 렌더링하게 된다.

```python
#This is a comment
print("Hello, world!")
```

주석은 줄 끝에도 배치할 수 있다.

```python
print("Hello, world!") #This is a comment
```

주석은 코드를 설명하는 텍스트일 필요는 없다. 파이썬 코드이더라도 주석처리를 해서 실행하지 못하게 할 수 있다.

```python
#print("Hello, World!")
print("Cheers, Mate!")
```

##### Multi Line Comment

파이썬은 한 줄을 초과하는 부분에 대한 주석을 지원하지 않는다. 따라서 여러 줄을 주석으로 하기 위해서는 각 줄마다 #을 추가해야 한다.

```python
#This is a comment
#written in
#more than just one line
print("Hello")
```

또는 파이썬에서 의도된 방법은 아니지만 multiline string을 사용할 수도 있다.

파이썬은 변수로 할당되지 않은 string literals를 무시하기 때문에, 코드에 multiline string으로 지정하는 방식으로 주석을 넣을 수도 있다. 여기서 multiline string을 지정하는 방법은 따옴표(큰 따옴표 또는 작은 따옴표) 세 개를 연속으로 사용하는 것이다.

문자열에 변수에 할당되지 않은 한 파이썬은 코드를 읽게 되지만 그 코드들을 무시하게 된다.

```python
"""
This is a comment
written in
more than just one line
"""
print("Hello, world")
```

```python
'''
This is a comment
written in
more than just one line
'''
print("Hello, world")
```

만약 multiline string이 변수로 할당된다면, 변수값으로 내용이 저장되게 된다.

```python
a="""
This is a comment
written in
more than just one line
"""
print(a)

# [결과 내용]
# This is a comment
# written in
# more than just one line
```
