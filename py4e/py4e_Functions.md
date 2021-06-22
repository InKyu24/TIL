## Python

#### 함수

재사용 가능한 코드 조각이다. 프로그래밍에서 중요한 한 가지는 같은 작업을 반복하고 싶지 않다는 것에 있다. 

```python
# 함수 정의
def thing() :
	print('Hello')
    print('python')
# 함수 호출
thing()
print('SAY AGAIN')
# 함수 재사용
thing()
```



Python에는 두 종류의 함수가 존재한다.

* 내장 함수(Built-in functions) : Python의 한 부분으로 제공되는 함수로 print(), input(), type(), float(), int() 등이 있다. 내장 함수의 이름은 변수명으로 사용할 수 없다.
* 직접 정의하고 사용하는 함수

Python 함수는 인자를 입력받고, 계산을 하고, 결과를 반환하는 재사용 가능한 코드이다. 함수를 정의할 때는 def 예약어를 사용한다. 그리고 함수 이름, 괄호, 인자를 이용해 함수를 호출한다.

def 키워드를 통한 함수의 정의를 할 때에는 본문을 들여쓰기 해야한다. 또한 함수의 정의는 함수의 본문을 실행하지는 않으며, 내용을 기억 및 저장하는 역할을 한다.



#### 인자(arguments)

아래의 spain, france, korea, ...과 같이 인자는 함수를 호출할 때 입력값으로 전달하는 값이다. 인자는 함수명 뒤 괄호 안에 작성되며, 함수가 다른 조건에서 호출되었을 때 각각 다른 일을 수행할 수 있도록 지시하는 역할을 한다.

```python
greet('spain')
# Hola 출력
greet('france')
# Bonjour 출력
greet('korea')
# 안녕하세요 출력
greet('en')
# Hello 출력
```



#### 매개변수(Parameters)

아래의 language는 매개변수이다. 매개변수는 함수 정의에 사용되는 변수이다. 특정 함수 호출에서 함수 안의 코드가 인자에 접근하기 위한 손잡이 역할을 한다.

함수 정의에는 한 개 이상의 매개변수를 정의할 수 있다.

```python
def greet(language):
    if language == 'spain':
    	print('Hola')
    elif language == 'france':
        print('Bonjour')
    elif language == 'korea':
    	print('안녕하세요')
    else:
        print('Hello')
```



#### 반환값

함수는 종종 인자를 받아서 계산을 하고 함수 호출 구문이 사용될 수 있도록 값을 반환한다. 이를 위해서는 return 키워드를 사용한다.

```python
def greet():
    return "Hello"

print(greet(), "InKyu")
# Hello Inkyu 출력
```



#### Void (non-fruitful) 함수

함수가 값을 반환하지 않는 경우를 void 함수라고 한다. 값을 반환하는 함수는 fruitful 함수라고 한다.