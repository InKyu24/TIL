### Python Variables

#### Python Variables

변수는 데이터 값을 저장하기 위한 공간이다.

##### Creating Variables

파이썬에는 변수를 선언하는 명령이 없다. 변수는 값을 처음 할당하는 순간 생성된다.

```python
x= 5
y = "Hello, world"
print(x)
print(y)

# [결과 내용]
# 5
# Hello, world
```

파이썬에서 변수는 특정 유형으로 선언할 필요가 없으며, 설정한 후에 유형을 변경할 수도 있다.

```python
x = 4 			# x is of type int
x = "Sally" 	# x is now of type str
print(x)

# [결과 내용]
# Sally
```

##### Casting

캐스팅을 통해 변수의 데이터 유형을 지정할 수 있다.

```python
x = str(3)		# x will be '3'
y = int(3)		# y will be 3
z = float(3)	# z will be 3.0
```

##### Get the Type

그리고 type() 함수를 사용하여 변수의 데이터 유형을 가져올 수 있다. 

```python
x = 5
y = "John"
print(type(x))
print(type(y))

# [결과 내용]
# <class 'int'>
# <class 'str'>

x = 5
y = "John"
print(type(x))
print(type(y))

# [결과 내용]
# <class 'str'>
# <class 'str'>

```

##### Single or Double Quotes?

파이썬에는 단일 문자열 변수가 없기 때문에 문자열 변수는 작은 따옴표 또는 큰 따옴표를 사용하여 선언할 수 있다.

```python
x = "John"
# is the same as
x = 'John'
```

##### Case-Sensitive

그리고 변수 이름은 대소문자를 구분한다.

```python
a = 4
A = "Sally"

# A will not overwrite a 
```

#### Variable Names

##### Variable Names

변수는 짧은 이름 뿐만 아니라 보다 설명적인 이름을 가질 수있다.

파이썬 변수명에 대한 규칙은 아래와 같다.

+ 변수 이름은 문자 또는 밑줄 문자로 시작해야 한다.
+ 변수 이름은 숫자로 시작할 수 없다.
+ 변수 이름에는 영숫자 문자와 밑줄 (A-Z, a-z,0-9 및 _)만을 포함할 수 있다.
+ 변수 이름은 대소문자를 구분한다. (age, Age, AGE는 각각의 세 가지 변수이다.)

```python
# 유효한 변수명
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
```

```python
# 잘못된 변수명
2myvar = "John"
my-var = "John"
my var = "John"
```

##### Multi words Variable Names

둘 이상의 단어가 포함된 변수 이름은 읽기 어려울 수 있다. 그래서 다음과 같은 몇 가지 기술을 사용한다.

+ 카멜 케이스 : 첫 번째 단어를 제외한 각 단어를 첫 글자를 대문자로 시작한다.

```python
myVariableName = "John"
```

+ 파스칼 케이스 : 각 단어를 대문자로 시작한다.

```python
MyVariableName = "John"
```

+ 스네이크 케이스 : 각 단어를 밑줄 문자로 구분한다.

```python
my_variable_name = "John"
```

#### Assign Multiple Values

##### Many Values to Multiple Variables

파이썬을 사용하면 한 줄에 여러 변수에 값을 할당할 수 있다.

```python
x, y, z = "Orange", "Banana", "Cherry", "a"
print(x)
print(y)
print(z)
```

##### One Value to Multiple Variables

한 줄의 코드로 같은 값을 여러 변수들에게 할당할 수도 있다.

```python
x = y = z = "Orange"
print(x)
print(y)
print(z)
```

##### Unpack a Collection

리스트, 튜플 등 값 모음이 있는 경우에 파이썬을 사용하면 값을 변수로 추출할 수 있다. 이것을 unpacking 이라고 한다.

```python
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# [결과 내용]
# apple
# banana
# cherry
```

#### Output Variables

파이썬의 `print` 문은 변수를 출력하는 데 사용된다.

텍스트와 변수를 결합하기 위해서는 `+` 문자를 사용한다.

```python
x = "awesome"
print("Python is " + x)

# [결과 내용]
# Python is awesome
```

물론 변수와 또 다른 변수를 결합할 수도 있다.

```python
x = "Python is "
y = "awesome"
z =  x + y
print(z)

# [결과 내용]
# Python is awesome
```

숫자의 경우에는, 수학적인 연산자로써 역할을 하게 된다.

```python
x = 5
y = 10
print(x + y)

# [결과 내용]
# 15
```

만약 string과 숫자를 결합한다면 에러가 발생한다.

```python
x = 5
y = "John"
print(x + y)

# [결과 내용]
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

#### Global Variables

함수 외부에서 생성된 변수를 전역 변수(Global Variables)라고 한다. 전역 변수는 함부 내부와 외부 모두에서 모든 사람이 사용할 수 있다.

```python
# function 외부에 생성된 변수를 function 내부에서 사용
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# [결과 내용]
# Python is awesome
```

만약 함수 내부에서 전역변수과 동일한 명칭의 변수를 생성한다면, 그 변수는 지역 변수(Local Variables)로 함수 내에서만 사용할 수 있다. 동일한 이름은 가진 전역 변수는 유지된다.

```python
# function 내부에 전역 변수와 같은 이름의 변수 생성 후 비교
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()					# Local 변수
print("Python is " + x)		# Global 변수

# [결과 내용]
# Python is fantastic
# Python is awesome
```



##### The global keyword

일반적으로 함수 내부에 변수를 만들면 해당 변수는 지역 변수이며 해당 함수 내에서만 사용할 수 있다. 함수 내부에 있는 지역  변수를 전역 변수로 만들기 위해서는 `global` 키워드를 사용할 수 있다. `global` 키워드를 사용하는 경우 변수는 전역 범위에 속하게 된다.

```python
x = "awesome"

def myfunc():
  global x
  x = "fantastic"
  print("Python is " + x)  

myfunc()
print("Python is " + x)

# [결과 내용]
# Python is fantastic
# Python is fantastic
```


