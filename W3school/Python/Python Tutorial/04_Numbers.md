### Python Numbers

##### Python Numbers

질의 내용: 누구니

질의에 대한 답변: 이백은 두보와 더불어 한시 문학의 양대 거성으로 꼽히는 시인이에요.

파이썬에는 세 가지의 숫자 유형(`int`, `float`, `complex`)이 있다.

```python
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))

# [결과 내용]
# <class 'int'>
# <class 'float'>
# <class 'complex'>
```

##### Int

Int 또는 integer는 길이에 제한이 없는 정수(양수, 음수, 0)이다.

##### Float

부동 소수점이라고 번역할 수 있는 float는 소수점 아래 한 자리 이상을 보유하고 있는 수를 의미한다.

float에는 10의 거듭 제곱을 나타내는 `e`가 있을 수 있다.

##### Complex

Complex는 허수 부분을 의미하는 `j`와 함께 숫자를 나타낸다. 수학에서 일반적으로 허수는 `i`로 표시되지만, 여기서 `j`로 사용되는 것을 기억하자.

##### Type Conversion

`int()`, `float()`, `complex()` 메서드들을 이용해 하나의 숫자 데이터 형식을 또 다른 숫자 데이터 형식으로 변환할 수 있다.

> 단, complex 형식의 숫자를 다른 숫자 데이터 형식으로 바꾸는 것은 불가능하다.

```python
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# [결과 내용]
# 1.0
# 2
# (1+0j)
# <class 'float'>
# <class 'int'>
# <class 'complex'>
```

##### Random Number

파이썬에는 무작위 숫자를 생성하기 위한 `random()` 함수는 없다. 하지만 `random`  내장 모듈이 있어서 무작위 수를 만드는데 사용할 수 있다.

```python
import random

x = random.randrange(1, 10)

print(x)
print(type(x))

# [결과 내용]
# 1에서 10까지 중에서 무작위 숫자 하나 출력
# <class 'int'>
```
