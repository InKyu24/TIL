### Python Casting

##### Specify a Variable Type

변수에 특정 데이터 유형을 지정해야 하는 경우가 있을 수 있다. 이는 캐스팅으로 수행할 수 있다. 파이썬은 객체 지향 언어이므로, 클래스를 사용하여 기본 데이터 형식을 포함한 데이터 형식을 정의한다.

따라서 파이썬에서의 캐스팅은 생성자 함수를 사용하여 수행된다.

+ `int ()` : 정수 형식, 소수점 형식(모든 소수점 제거) 또는 문자열 형식 (문자열이 정수를 나타내는 경우)에서 정수 데이터를 구성한다.
+ `float ()` :  정수 형식, 소수점 형식 또는 문자열 형식에서 소수점 데이터를 구성한다.
+ `str ()` : 정수 형식, 소수점 형식 또는 문자열 형식을 포함한 다양한 데이터 형식에서 문자열 데이터를 구성한다.

```python
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
```
