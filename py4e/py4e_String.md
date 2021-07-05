## Python

##### 문자열 (Strings)

+ 문자열은 문자 시퀀스

+ 큰 따옴표나 작은 따옴표를 사용해서 표기한다.

+ 문자열에서 + 연산자는 '병합'을 의미한다.



문자열에 있는 어떤 문자든지 대괄호 안에 지정된 인덱스를 이용해 가져올 수 있다.

```python
fruit = 'banana'
letter = fruit[1]
print(letter)
# a

x = 3
w = fruit[x - 1]
print(w)
# n
```

만약 문자열 크기를 넘어선 인덱스에 접근하려고 하면 에러가 발생한다.



문자열의 길이를 파악하기 위해서는 내장 함수 len()을 이용한다.

```python
fruit = 'banana'
x = len(fruit)
print(x)
# 6
```



##### 문자열을 통한 루프

while 구문, 반복 변수, len 함수를 이용해서 문자열 내의 각 문자를 독립적으로 확인하는 반복문을 만들 수 있다.

```python
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index += 1
```

문자열을 통한 루프는 for 문을 이용하여 작성하는 것이 보다 깔끔하다.

```python
fruit = 'banana'
for letter in fruit:
	print(letter)
```



##### 문자열에 있는 'a'의 개수를 세는 반복문

```python
word = 'banana'
count = 0
for letter in word :
    if letter == 'a':
        count += 1
print(count)
```



#####  키워드 `in`

* 수학의 집합 개념을 생각해보면 이해가 쉽다.



##### 슬라이싱

* 대괄호 연산자를 사용하여 문자의 조각을 가져오는 것
* 마지막 인덱스는 포함하지 않는다.
* index보다 큰 수를 마지막 인덱스로 설정하더라도 오류가 나지 않는다.
* 첫 번째나 마지막 인덱스를 생략할 수 있다.

```python
s = 'Monty Python'
print(s[0:4]) # Mont
print(s[6:7]) # P
print(s[6:20]) # Python

print(s[:2]) # Mo
print(s[8:]) # thon
print(s[:]) # Monty Python
```



##### 문자열 병합(concatenation)

```python
a = 'Hello'
b = a + 'There'
print(b) # HelloThere

c = a + ' ' + 'There'
print(c) # Hello There
```



##### 논리 연산자로써 사용되는 in

```python
fruit = 'banana'
'n' in fruit # True
'm' in fruit # False
'nan' in fruit # True

if 'a' in fruit :
    print('Found it!')
```



##### 문자열 비교

+ 일반적으로 사전 순서상의 앞뒤를 구분한다.

```python
if word == 'banana':
    print('All right, bananas.')
    
if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana'
	print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.')
```



##### 문자열 라이브러리

+ 파이썬은 여러 개의 문자열 함수를 정의하는 문자열 라이브러리가 존재한다.
+ 문자열 함수는 모든 문자열에 내장되어 있으며, 함수를 문자열 변수에 붙임으로써 호출된다.

```python
greet = 'Hello Bob'
zap = greet.lower()
nnn = greet.upper()

print(zap) # hello bob
print(nnn) # HELLO BOB
print(greet) # Hellow Bob
print('Hi There'.lower()) # hi there
```



##### 문자열 찾기

find 함수는 하위 문자열을 문자열에서 탐색한다. 문자열에서 찾을 수 없는 경우 -1을 반환한다.

```python
fruit = 'banana'
pos = fruit.find('na')
print(pos) # 2

aa = fruit.find('z')
print(aa) # -1
```



##### 문자열 대체하기

replace 함수를 사용하여 바꾸기 전 문자열과 바꿀 문자열을 전달한다.

```python
greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')
	print(nstr)	# Hello Jane
nstr = greet.replace('o', 'X')
	print(nstr) # HellX BXb
```



##### 공백 제거하기

문자열에서 공백은 큰 문제를 야기하는 경우가 있다. 공백은 단순히 띄어쓰기 뿐만 아니라 출력되지 않는 다른 문자(\t, \n) 역시 포함한다. 

```python
greet = '	Hello Bob   '
greet.lstrip() # 'Hello Bob   '
greet.rstrip() # '	Hello Bob'
greet.strip() # 'Hello Bob'
```



##### 접두사

```python
line = 'Please have a nice day'
line.startswith('Please') # True
line.startswith('p') # False
```

 
