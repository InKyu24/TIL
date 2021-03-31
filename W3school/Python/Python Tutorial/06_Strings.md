### Python Strings

##### Strings

파이썬에서 String(문자열)은 작은 따옴표 또는 큰 따옴표로 둘러싸여 있다. 따라서`'hello'`와 "hello"는 같다.

문자열 형식의 데이터는 `print()` 함수를 통해 내용을 출력할 수 있다.

```python
print("Hello")
print('Hello')

# [결과 내용]
# Hello
# Hello
```

##### Assign String to a Variable

변수에 문자열을 할당하는 것은 변수 이름 뒤에 등호와 문자열을 사용하여 수행된다.

```python
a ="Hello"
print(a)

# [결과 내용]
# Hello
```

##### Multiline String

세 개의 따옴표(큰 따옴표 또는 작은 따옴표)를 사용하여 여러 줄의 문자열을 변수에 할당할 수 있다. 등호를 사용하지 않게 되면 주석으로 사용할 수 있다.

```python
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

b = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(b)

# [결과 내용]
# 모두 같은 내용 출력
# 결과 내용에서 줄 바꿈은 코드와 같은 위치에서 실행된다.
# Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.
```

##### Strings are Arrays

다른 많은 프로그래밍 언어와 마찬가지로 파이썬의 String은 유니코드 문자를 나타내는 바이트 배열이다. 그러나 파이썬에는 문자 데이터 유형이 없으며 단일 문자는 단순히 길이가 1인 String이다. 대괄호를 사용하여 문자열의 개체에 접근할 수 있다.

```python
a = "Hello, World!"
print(a[0])
print(a[1])

# [결과 내용]
# H
# e
```

##### Looping Through a String

String은 일종의 바이트 배열이다. 따라서 `for`를 사용한 반복문을 사용하여 문자를 반복할 수 있다.

```python
for x in "banana":
  print(x)

# [결과 내용]
# b
# a
# n
# a
# n
# a
```

##### String Length

String의 길이를 얻기 위해서는 `len()` 함수를 사용한다. `tab`, `\n`  모두 길이 1로서 취급된다.

```python
a = "Hello, World!"
print(len(a))

# [결과 내용]
# 13
```

##### Check String

특정 구문이나 문자가 문자열에 있는지 확인하기 위해 `in` 키워드를 사용할 수 있다.

```python
txt = "The best things in life are free!"
print("free" in txt)

# [결과 내용]
# True
```

이는 조건문으로도 활용할 수 있다.

```python
# txt에 "free"가 있는 경우에만 출력

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# [결과 내용]
# Yes, 'free' is present.
```

##### Check if NOT

특정 구문이나 문자가 String에 없는지 확인하기 위해서는 `not in` 키워드를 사용할 수 있다.

```python
txt = "The best things in life are free!"
print("expensive" not in txt)

# [결과 내용]
# True
```

이것도 물론 조건문으로 활용 가능하다.

```python
# txt에 "expensive"가 없는 경우에만 출력

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("Yes, 'expensive' is NOT present.")

# [결과 내용]
# Yes, 'expensive' is NOT present.
```

#### Slicing Strings

##### Slicing

슬라이스 구문을 사용하여 문자의 일부 범위를 선택해 반환할 수 있다. 문자열의 일부를 반환하려면 시작 index와 끝 index를 `콜론(:)`으로 구분하여 지정하면 된다.

> 첫 번째 문자 index는 0이다.
>
> 끝 index는 반환되는 문자에 포함되지 않는다.

```python
# 3번째 문자(index 2)부터 5번째 문자(index 5_포함되지 않음)까지를 가져온다.

b = "Hello, World!"
print(b[2:5])

# [결과 내용]
# llo
```

##### Slice From the Start

시작 index를 생략하면 가장 첫번째 문자인 index가 0인 문자에서부터 시작하게 된다.

```python
# 첫번째 문자(index 0)부터 4번째 문자(index 4_포함되지 않음)까지를 가져온다.

b = "Hello, World!"
print(b[:4])

# [결과 내용]
# Hell
```

##### Slice From the End

끝 index를 생략하게 되면 가장 끝 문자까지로 범위가 설정된다.

```python
# 세번째 문자(index 2)부터 끝까지 가져온다.

b = "Hello, World!"
print(b[2:])

# [결과 내용]
# llo, World!
```

##### Negative Indexing

index를 음수로 지정하게 되면, 문자열 끝에서부터 슬라이스를 시작하게 된다.

```python
# 끝에서 다섯번째 문자(index -5)에서 시작하여, 끝에서 세번째 문자(index -2)까지 가져온다.

b = "Hello, World!"
print(b[-5:-2])

# [결과 내용]
# orl

print(b[-1])
print(b[-5])
print(b[-5:-1])
print(b[-5:-2])
print(b[-5:-3])

# [결과 내용]
# !
# o
# orld
# orl
# or
```

#### Modify String

파이선에는 문자열에 사용할 수 있는 내장 메서드가 있다.

##### Upper Case

`upper()` 메서드는 문자열을 대문자로 반환한다.

```python
a = "Hello, World!"
print(a.upper())

# [결과 내용]
# HELLO, WORLD!
```

##### Lower Case

`lower()`  메서드는 문자열을 소문자로 반환한다.

```python
a = "Hello, World!"
print(a.lower())

# [결과 내용]
# hello, world!
```

##### Remove Whitespace

공백은 실제 텍스트 앞뒤에 존재하는 공백를 말하며, 이를 제거하기 위해서는 `strip()` 메서드를 이용한다.

```python
a = " 			Hello, World!		 "
print(a.strip())

# [결과 내용]
# Hello, World!
```

##### Replace String

`replace()` 메서드는 특정 문자열 다른 문자열로 바꾸게 해준다.

```python
a = "Hello, World!"
print(a.replace("Hello", "What's up?"))

# [결과 내용]
# What's up?, World!
```

##### Split String

이 `split()` 메서드는 지정한 구분 기호의 객체를 문자열에서 찾는다. 그리고 그 지정한 구분 기호를 기준으로, 하위 문자열로 분할하여 목록 항목을 만들어 그 목록을 반환한다.

```python
a = "Hello, World!"
b = a.split(",")
print(b)

# [결과 내용]
# ['Hello', ' World!']

a = "Hello, World!"
b = a.split("o")
print(b)

# [결과 내용]
# ['Hell', ', W', 'rld!']
```

#### String Concatenation

##### String Concatenation

두 문자열을 연결하거나 결합하기 위해서는 `+` 연산자를 사용할 수 있다.

```python
a = "Hello"
b = "World"
c = a + b
print(c)

# [결과 내용]
# HelloWorld

a = "Hello"
b = "World"
c = a + " " + b
print(c)

# [결과 내용]
# Hello World
```

#### Format - String

##### String Format

일반적으로 문자열 데이터와 숫자 데이터는 `+` 연산자를 이용해 결합할 수 없다. 따라서 파이썬에서는 문자열과 숫자를 결합하기 위해서는 `format()` 메서드를 사용하여야 한다. `format()`메서드는 전달된 매개변수를 가져와서, 형식을 지정하고, `자리표시자 {}`에 배치한다.

```python
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# [결과 내용]
# My name is John, and I am 36
```

`format()` 메서드에서 매개변수의 개수에는 제한이 없으며, 각각의 자리표시자`{}`에 배치된다.

```python
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# [결과 내용]
# I want 3 pieces of item 567 for 49.95 dollars.
```

인덱스 번호 `{0}`를 사용하여 매개변수를 올바른 자리표시자에 확실히 위치시킬 수 있다.

```python
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# [결과 내용]
# I want to pay 49.95 dollars for 3 pieces of item 567
```

#### Escape Characters

##### Escape Character

문자열 내부에 허용되지 않는 문자를 삽입하기 위해서는 escape 문자를 사용한다. escape 문자는 삽입하고자 하는 문자 앞에 백슬래시 `\` 를 의미한다.

허용되지 않는 문자의 가장 대표적인 예시는 큰 따옴표로 묶인 문자열 내부에 존재하는 큰 따옴표 이다.

```python
txt = "We are the so-called "Vikings" from the north."

# [결과 내용]
# SyntaxError: invalid syntax
```

이러한 문제를 해결하기 위한 방법 중에는 따옴표를 큰 따옴표와 작은 따옴표를 이용한 방법도 있다.

```python
txt = "We are the so-called 'Vikings' from the north."
print(x)

# [결과 내용]
# We are the so-called 'Vikings' from the north.
```

```python
txt = 'We are the so-called "Vikings" from the north.'
print(x)

# [결과 내용]
# We are the so-called "Vikings" from the north.
```

하지만 만약 `We are the so-called "Vikings" from the 'north'.`를 출력하고 싶은 경우에는 위와 같은 방법을 쓸 수 없게 된다. 이는 escape 문자인 `/"`으로 간단하게 해결할 수 있다.

```python
txt = "We are the so-called \"Vikings\" from the 'north'."
print(txt)

# [결과 내용]
# We are the so-called "Vikings" from the 'north'.
```

##### Escape Characters

파이썬에서 사용되는 다른 escape 문자들은 아래와 같다.

+ `\'` 작은 따옴표 표현

  ```python
  
  ```

+ `\\` 백슬래시 표현

  ```python
  txt = "This will insert one \\ (backslash)."
  print(txt)
  
  # [결과 내용]
  # This will insert one \ (backslash).
  ```

+ `\n` 줄 바꿈

  ```python
  txt = "Hello\nWorld!"
  print(txt) 
  
  # [결과 내용]
  # Hello
  # World!
  ```

+ `\r` 줄 바꿈(커서를 행의 앞으로 이동)

  ```python
  txt = "Hello\rWorld!"
  print(txt)
  
  # [결과 내용]
  # Hello
  # World!
  ```

+ `\t` 탭

  ```python
  txt = "HelloHello\tWorld!"
  print(txt) 
  
  # [결과 내용]
  # HelloHello	World!
  ```

+ `\b` 백스페이스

  ```python
  #This example erases one character (backspace):
  txt = "Hello \bWorld!"
  print(txt)
  
  # [결과 내용]
  # HelloWorld!
  
  txt = "Hello \bWorld!"
  print(txt)
  
  # [결과 내용]
  # HelloWorld!
  ```

+ `\f` 프린트 출력 시 다음 페이지로 넘기기

+ `\ooo` 8진수 값

  ```python
  #A backslash followed by three integers will result in a octal value:
  txt = "\110\145\154\154\157"
  print(txt) 
  
  # [결과 내용]
  # Hello
  ```

+ `\xhh` 16진수 값

  ```python
  #A backslash followed by an 'x' and a hex number represents a hex value:
  txt = "\x48\x65\x6c\x6c\x6f"
  print(txt) 
  
  # [결과 내용]
  # Hello
  ```

