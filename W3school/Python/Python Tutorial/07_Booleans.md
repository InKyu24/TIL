### Python Booleans

Boolean(부울)은 True 또는 False로 표현한다. 

##### Boolean Values

프로그래밍에서는 종종 표현이 참인지 거짓인지를 구분할 필요가 있다. 파이썬에서는 어떤 표현도 참과 거짓으로 답변을 얻어낼 수 있다. 두 값을 비교하는 경우, 표현식이 평가되고 파이썬은 부울값을 반환한다.

```python
print(10 > 9)
print(10 == 9)
print(10 < 9)

# [결과 내용]
# True
# False
# False
```

조건문에서 파이썬은 참과 거짓인지에 근간하여 메시지를 출력한다.

```python
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
    
# [결과 내용]
# b is not greater than a
```

##### Evaluate Values and Variables

`bool()` 함수를 이용하여 어떤 값을 평가할 수 있고, 참과 거짓으로 결과값을 반환한다.

```python
print(bool("hello"))
print(bool(""))
print(bool(15))
print(bool(0))

# [결과 내용]
# True
# False
# True
# False
```

```python
x = "World"
y = 15

# [결과 내용]
# True
# True
```

##### Most Values are True

어떤 내용이라도 있다면 거의 대부분의 값이 참으로 평가된다. 즉, 빈 문자열을 제외한 모든 문자열은 참을 반환하고, 0을 제외한 모든 숫자는 참을 반환하는 것이다. 그리고 list, tuple, set, dictionary 모두 비어있는 상태를 제외하고는 참을 반환하게 된다.

```python
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# [결과 내용]
# True
# True
# True
```

##### Some Values are False

사실 `()`, `[]`, `{}`,`숫자 0`,`None`과 같이 비어있는 값들을 제외하고 거짓을 반환하는 값은 많지 않다. 

```python
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# [결과 내용]
# False
# False
# False
# False
# False
# False
# False
```

아래와 같은 경우, 하나의 이상의 값 또는 객체가 거짓으로 평가된다. 즉, 0 또는 거짓으로 값을 반환하는 `__len__` 함수가 있는 클래스로 만든 객체가 있는 경우를 말한다.

```python
class myclass():
  def __len__(self):
    return 3

myobj = myclass()
print(bool(myobj))

# [결과 내용]
# True

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# [결과 내용]
# False
```

##### Function can Return a Boolean

부울 값을 반환하는 함수를 생성할 수도 있다.

```python
def myFunction() :
  return True

print(myFunction())

# [결과 내용]
# True
```

함수의 부울 결과 값에 따른 코드를 실행할 수 있다.

```python
# myFunction에서 True 값을 반환하기 때문에 True 조건의 실행문인 YES!가 출력된다.

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

# [결과 내용]
# YES!
```

파이썬은 부울 값을 반환하는 많은 내장 함수를 가지고 있다. 예를 들면 `isinstance()`와 같은 함수이다. `isinstance()` 함수는 특정 데이터 유형인지 확인하는데 사용할 수 있다.

```python
x = 200
print(isinstance(x, int))

 [결과 내용]
# True
```



