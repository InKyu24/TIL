## Python

##### while 반복문

while 루프는 기능적으로 if 구문과 매우 비슷하다.  참 또는 거짓으로 답이 나오는 질문을 통해 반복하기 때문이다.

if 구문의 작동 방식과 다른 점은 코드를 한 번 실행한 후, 다시 올라가서 만족하는 답변을 얻을 때까지 질문을 반복한다는 것이다.

각 루프마다 변하는 반복 변수를 가지고 있다. 아래 코드에서는 n이 이에 해당한다.

```python
n = 5
while n > 0 :
	print(n)
    n = n - 1
print('Blastoff')
print(n)
```

반복문에서는 반복 변수를 제대로 활용하는 것이 중요하다. 만약 반복 변수를 제대로 사용하지 못한다면 아래 코드와 같이 무한 루프에 빠지게 되는 오류를 범할 수 있다.

```python
n = 5
while n > 0 :
    print('Lather')
    print('Rinse')
print('Dry off!')
```

또 다른 오류는 반복 변수의 잘못된 설정으로 반복문의 역할을 제대로 하지 못하는 것이다. 아래와 같은 코드는 어떠한 것도 실행하지 못하고 끝나버리게 된다. 하지만 이를 조건문의 역할 대신으로 사용하기도 한다.

```python
n = 0
while n > 0
	print('Lather')
    print('Rinse')
print('Dry off!')
```

루프에서 빠져나오기 위한 방법에는 몇 가지가 있다.  아래에서는 `while True`로 작성이 되어있기 때문에 무한루프에 빠지게 된다. 만약 입력값에 'done'를 입력하게 되면, break 구문을 만나게 된다.

break 구문은 현재 루프를 끝내고, 루프의 마지막 줄 다음 구문으로 빠져나오게 된다. 여기서 중요한 것은 break를 만나게 되면 더 이상 반복을 하지 않고 해당 루프는 끝이 난다는 것이다.

```python
while True:
    line = input('> ')
    if line == 'done' :
        break
    print(line)
print('Done!')
```

break와 같은 루프 제어문으로는 continue가 있다. 하지만 continue는 break와는 다르게 작동한다. break는 루프에서 나가라고 하지만 continue는 이번 회차의 실행을 멈추는 역할을 한다. continue를 만나게 되면, 루프의 제일 위로 올라간다.

```python
while True:
    line = input('> ')
    if line[0] == '#' :
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')
```

while 루프는 조건문이 거짓이 되기 전까지 계속 실행되기 때문에 '불확정 루프'라고 부른다. 지금까지 본 루프는 종료가 불가능한 '무한 루프'인지 아닌지 확인하기 쉬웠다. 그러나 가끔은 루프가 종료가 가능한 지 확인하기 어려운 경우가 있다.



##### for 반복문

for 반복문은 유한 루프이다. 유한 루프는 어떤 집합의 원소들에 대해 반복문을 실행하는 것이다. 유한 루프는 네 가지의 키워드를 사용한다.    

```python
for i in [5, 4, 3, 2, 1] :
    print(i)
print('Blastoff!')
```

```python
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends
	print ('Happy New Year:', friend)
print('Done!')
```

for 반복문은 명시된 반복 변수를 가지고 있으며, 각 루프를 통과할 때마다 값이 변한다. 이 반복 변수는 시퀀스나 집합의 원소를 따라 이동하며 값이 변한다.  



>== : 값만을 비교하는 연산자
>
>```python
>print(0 == 0.0) # True
>```
>
>is : 값과 자료형 모두를 비교하는 연산자
>
>```python
>print(0 is 0,0) # False
>```



```python
sum = 0
count = 0
val = None
while True:
    val = input('Enter a number:')
    if val == 'done':
        break
    try:
        fval = float(val)
    except:
        print('Invalid input')
        continue
    
    sum += fval
    count += 1

print(sum, count, sum/count)
```

