### Python Data Types

##### Built-in Data Types

프로그래밍에서 데이터 유형은 중요한 개념이다.

변수는 다른 유형의 데이터를 저장할 수 있으며, 유형 마다 수행할 수 있는 일들이 다르다.

파이썬에는 기본적으로 다음과 같은 카테고리의 데이터 유형이 내장되어 있다.

+ Text Type : `str`
+ Numeric Types : `int`, `float`, `complex`
+ Sequence Types : `list`, `tuple`, `range`
+ Mapping Type : `dict`
+ Set Types : `set`, `frozenset`
+ Boolean Type : `bool`
+ Binary Types : `bytes`, `bytearray`, `memoryview`

##### Getting the Data Types

`type()` 함수를 통해 객체의 데이터 유형을 얻을 수 있다.

```python
x = 5
print(type(x))

# [결과 내용]
# <class 'int'>
```

##### Setting the Data Types

파이썬에서는 변수에 값을 할당할 때 데이터 유형이 설정된다.

+ 텍스트 유형 : `str`

  ```python
  x = "Hello, world!"
  ```

+ 숫자 유형 : `int`, `float`, `complex`

  ```python
  x = 20
  y = 20.5
  z = 1j
  ```

+ 시퀀스 유형 : `list`, `tuple`, `range`

  ```python
  x = ["apple", "banana" , "cherry"]
  y = ("apple", "banana" , "cherry")
  z = range(6)
  ```

+ 매핑 유형 : `dict`

  ```python
  x = {"name" : "John", "age" : 36}
  ```

+ 세트 유형 : `set`, `frozenset`

  ```python
  x = {"apple" , "banana", "cherry"}
  y = frozenset({"apple" , "banana", "cherry"})
  ```

+ 부울 유형 : `bool`

  ```python
  x = True
  ```

+ 바이너리 유형 : `bytes`, `bytearray`, `memoryview`

  ```python
  x = b"Hello"
  y = bytearray(5)
  z = memoryview(bytes(5))
  ```

##### Setting the Specific Data Type

만약 데이터 유형을 특정하고 싶다면, 생성자 함수를 사용할 수 있다.

```python
a = str("Hello world")
b = int(20)
c = float(31.2)
d = complex(1j)
e = list(("apple", "banana", "cherry"))
f = tuple(("apple", "banana", "cherry"))
g = range(6)
h = dict(name="john", age=36)
i = set(("apple", "banana", "cherry"))
j = frozenset(("apple", "banana", "cherry"))
k = bool(5)
l = bytes(5)
m = bytearray(5)
n = memoryview(bytes(5))
```