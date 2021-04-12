### Python Lists

#### Lists

##### List

List는 단일 변수에 여러 항목을 저장하는 데 사용된다. List는 데이터 컬렉션을 저장하는 데 사용되는 파이썬의 4가지 기본 제공 데이터 유형 중 하나이다.

> 파이썬의 4가지 기본 제공 데이터 유형은 List, Tuple, Set, Dictionary로 구성되어 있다.

목록은 대괄호(`[]`)를 사용하여 생성한다.

```python
thislist = ["apple", "banana", "cherry"]
print(thislist)

# [결과 내용]
# ['apple', 'banana', 'cherry']
```

##### List Items

List 항목은 순서가 지정되고 변경 가능하며 중복값을 허용한다.

List 항목이 인덱싱되고 첫 번째 항목에는 `Index [0]`이 있고 두 번째 항목에는 `Index [1]`이 있다.

```python
thislist = ["apple", "banana", "cherry"]
print(thislist[0])

# [결과 내용]
# apple
```

##### Ordered

List가 정렬되었다고 하면 항목에 정의된 순서가 있으며 해당 순서가 변경되지 않음을 의미한다.

List에 새 항목을 추가하면 새 항목이 List의 끝에 배치된다.

> List 메서드를 이용하면 순서를 변경할 수 있으나, 일반적으로 List 항목의 순서는 변경이 불가능하다.

##### Changeable

List가 생성된 후에는 List 항목의 변경, 추가, 삭제 등을 할 수 있다.

##### Allow Duplicates

List는 인덱싱되므로, 각 항목들은 같은 값을 가질 수 있다.

즉, List는 중복 값을 허용한다.

```python
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# [결과 내용]
# ['apple', 'banana', 'cherry', 'apple', 'cherry']
```

##### List Length

`len()` 함수를 사용하면 list가 몇 개의 항목을 가지고 있는 지 확인 할 수 있다.

```python
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# [결과 내용]
# 3
```

##### List Items - Data Types

List 항목들에는 다양한 데이터 유형이 포함될 수 있다.

```python
# 문자열, 정수, 부울 값을 갖는 List
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# 문자열, 정수, 부울 값이 섞인 List
list4 = ["abc", 34, True, 40, "male"]
```

##### type()

파이썬의 관점에서 List는 데이터 유형이 'list'인 객체로 정의된다.

```python
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# [결과 내용]
# <class 'list'>
```

##### The list() Constructor

새 List를 만들 때는 `list()` 생성자를 사용할 수도 있다.

```python
# list() 생성자를 사용해 List 만들기
thislist = list(("apple", "banana", "cherry"))
print(thislist)

# [결과 내용]
# ['apple', 'banana', 'cherry']
```

##### Python Collection (Arrays)

파이썬에는 네 종류의 컬렉션 데이터 유형이 있다.

+ List는 순서가 있으며, 변경 가능한 컬렉션 데이터 유형으로 값의 중복을 허용한다.
+ Tuple은 순서가 있으나, 변경 불가능한 컬렉션 데이터 유형으로 값의 중복을 허용한다.
+ Set은 순서도 없으며, 변경도 불가능한 컬렉션 데이터 유형으로 값의 중복도 허용하지 않는다.
+ Dictionary는 순서는 없으나, 변경은 가능한 컬렉션 데이터 유형으로 값의 중복도 허용하지 않는다.

컬렉션 데이터 유형을 선택함에 있어서, 유형별 특징을 이해하는 것이 유용하다. 특정한 데이터 set에 올바른 유형을 선택하는 것은 의미 보존과 효율성 및 보안의 상승을 의미한다.

#### Access List Items

##### Access Items

List 항목들은 인덱싱되며, 인덱스 번호를 참조하여 접근할 수 있다.

```python
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# [결과 내용]
# banana
```

##### Negative Indexing

음수 인덱싱으로 끝에서부터 인덱스 번호를 참조하여 접근할 수 있다.

`-1`은 마지막 항목을 의미하며, `-2`는 마지막에서 두번째 항목을 의미한다.

```python
# List의 마지막 항목은 아래와 같은 방법으로 접근할 수 있다.
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
print(thislist[-2])

# [결과 내용]
# cherry
# banana
```

##### Range of Indexes

시작 위치와 종료 위치를 지정하여, 인덱스 범위를 지정할 수 있다.

범위를 지정하게 되면, 반환 값은 지정된 항목이 있는 새 List가 된다.

>  시작 위치는 포함하며, 종료 위치는 포함되지 않는다.

```python
# 세 번째[2], 네 번째[3], 다섯 번째[4] 항목을 반환한다.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# [결과 내용]
# ['cherry', 'orange', 'kiwi']
```

만약 시작위치 값을 생략하게 되면, 첫 번째 항목에서 시작하게 된다.

```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# [결과 내용]
# ['apple', 'banana', 'cherry', 'orange']
```

또한, 종료위치 값을 생략하면 범위는 List의 마지막 항목으로 종료된다.

```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

# [결과 내용]
# ['cherry', 'orange', 'kiwi', 'melon', 'mango']
```

##### Range of Negative Indexes

만약 List의 끝에서부터 검색을 시작하려면 음수 색인을 지정하면 된다.

```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# [결과 내용]
# ['orange', 'kiwi', 'melon']
```

##### Check if Item Exist

지정된 항목이 List에 있는지 확인하려면 `in` 키워드를 사용한다.

```python
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# [결과 내용]
# Yes, 'apple' is in the fruits list
```

#### Change List Items

##### Change Item Value

특정 항목의 값을 변경하려면 인덱스 번호를 참조하여야 한다.

```python
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"

print(thislist)

# [결과 내용]
# ['apple', 'blackcurrant', 'cherry']
```

##### Change a Range of Item Values

특정 범위 내 항목의 값을 변경하기 위해서는 새 값으로 목록을 정의하고 새 값을 삽입할 인덱스 번호 범위를 참조하여야 한다.

```python
# banana와 cherry의 값을 blackcurrant와 watermelon으로 값 변경
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# [결과 내용]
# ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']
```

만약 바꾸는 것보다 더 많은 항목을 삽입하게 되면, 지정한 위치에 새 항목이 삽입되고 나머지 항목은 그에 따라 밀려나게 된다.

```python
# 두 번째 값인 banana에 두 개의 새 값들로 대체
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# [결과 내용]
# ['apple', 'blackcurrant', 'watermelon', 'cherry']
```

> 이렇게 삽입되는 항목 수가 교체되는 항목 수와 일치하지 않으면 목록의 길이가 변경된다.

바꾸는 것보다 적은 항목을 삽입하게 되면, 지정한 위치에 새 항목이 삽입되고 나머지 항목은 그에 따라 당겨지게 된다.

```python
# 두 번째 및 세 번째의 값을 watermelon으로 대체
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# [결과 내용]
# ['apple', 'watermelon']
```

##### Insert Items

기존 값을 바꾸지 않고 새 목록 항목을 삽입하려면 `insert()` 메서드를 사용할 수 있다.

이 `insert()` 메서드는 지정된 인덱스에 항목을 삽입한다.

 ```python
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# [결과 내용]
# ['apple', 'banana', 'watermelon', 'cherry']
 ```

#### Add List Items

##### Append Items

List 끝에 항목을 추가하려면 `append()` 메서드를 사용한다.

```python
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# [결과 내용]
# ['apple', 'banana', 'cherry', 'orange']
```

##### Insert Items

List의 특정 위치에 항목을 추가하기 위해서는 `insert()` 메서드를 사용한다.

 ```python
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# [결과 내용]
# ['apple', 'orange', 'banana', 'cherry']
 ```

##### Extend List

다른 List의 요소를 현재 List에 추가하려면 `extend()` 메서드를 사용한다. 그러면 List 끝에 요소가 추가된다.

```python
# thislist[List]에 tropical[List]을 추가한다.
# tropical은 thislist의 끝에 붙게 된다.

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical)

print(thislist)

# [결과 내용]
# ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
```

##### Add Any Iterable

`extend()` 메서드는 꼭 List가 아니여도 가능하다. 어떠한 iterable 객체(Tuple, Set, Dictionary 등)라도 추가할 수 있다.

```python
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")

thislist.extend(thistuple)

print(thislist) 

# [결과 내용]
# ['apple', 'banana', 'cherry', 'kiwi', 'orange']
```

#### Remove List Items

##### Remove Specified Item

특정한 항목을 삭제하기 위해서는 `remove()` 메서드를 사용한다.

```python
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# [결과 내용]
# ['apple', 'cherry']
```

##### Remove Specified Index

`pop()` 메서드를 이용하면, 특정 인덱스를 통해 삭제할 수 있다.

```python
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# [결과 내용]
# ['apple', 'cherry']
```

만약 인덱스를 지정하지 않는다면, `pop()` 메서드는 가장 마지막 항목을 삭제하게 된다.

```python
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# [결과 내용]
# ['apple', 'banana']
```

`del` 키워드 또한 특정 인덱스를 통한 항목 삭제가 가능하다.

```python
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# [결과 내용]
# ['banana', 'cherry']
```

`del` 키워드를 사용하면 List 전체를 삭제할 수도 있다.

```python
thislist = ["apple", "banana", "cherry"]
del thislist

# [결과 내용]
# NameError: name 'thislist' is not defined
```

##### Clear the List

`clear()` 메서드를 List를 비운다. 즉, List 자체는 존재하지만, 항목이 전혀 없는 상태가 된다.

```python
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# [결과 내용]
# []
```

#### Loop Lists

##### Loop Through a List

`for문`을 활용한 Loop를 사용하면 List 항목을 반복할 수 있다.

```python
# List의 모든 항목을 하나씩 출력
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# [결과 내용]
# apple
# banana
# cherry
```

##### Loop Through the Index Numbers

List의 인덱스 번호를 통해 항목을 반복할 수도 있다.

`range()`와 `len()` 함수를 이용하면, 적절한 iterable을 생성할 수 있다.

```python
# List의 인덱스 번호를 통해 모든 항목들 출력
# [0, 1, 2]인 iterable이 생성된다.

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

# [결과 내용]
# apple
# banana
# cherry
```

##### Using a While Loop

`while` 반복문을 사용하여 List의 항목들을 반복할 수 있다.

`len()` 함수를 사용하여 List의 길이를 결정하고, 0에서부터 시작하여 해당 인덱스를 참조하여 List 항목을 반복한다. 그리고 반복할 때마다 인덱스를 1씩 증가시킨다.

```python
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
    
# [결과 내용]
# apple
# banana
# cherry
```

##### Looping Using List Comprehension

List Comprehension은 List를 반복하는 가장 짧은 구문을 제공한다.

```python
# for 반복문을 사용하여 List의 모든 항목 출력하는 가장 짧은 방법

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# [결과 내용]
# apple
# banana
# cherry
```

#### List Comprehension

##### List Comprehension

기존 List의 값을 기반으로 새로운 List를 생성하고자 할 때 List comprehension은 보다 짧은 구문을 제공한다.

만약 과일들로 List가 구성되어 있고, 과일 이름에 "a"가 포함된 새로운 List를 만들고자 한다고 가정해보자. List comprehension를 사용하지 않는 경우에는 아래와 같이 `for` 조건문을 이용해 작성해야 할 것이다.

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# [결과 내용]
# ['apple', 'banana', 'mango']
```

만약 List comprehension을 이용한다면, 단 한 줄로 위와 같은 함수를 아래와 같이 작성할 수 있다.

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# [결과 내용]
# ['apple', 'banana', 'mango']
```

##### The Syntax

List comprehension의 기본 구문은 아래와 같다. 여기서 반환 값은 새로운 List가 되며, 사용된 List는 변경되지 않는다.

```python
newlist = [expression for item in iterable if condition == True]
```

###### Condition

여기서 condition은 필터와 같은 역할을 하며, True로 평가되는 항목만들 받아들이게 된다. 조건에 `if x != "apple"`이 있다면 "apple" 외의 모든 항목들이 Ture 값을 반환하게 되고, 따라서 새로운 LIst에는 "apple"을 제외한 모든 항목들로 구성되게 된다. 조건은 선택 사항이며 생략할 수 있다.

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if x != "apple"]

print(newlist)

# [결과 내용]
# ['banana', 'cherry', 'kiwi', 'mango']
```

###### Iterable

iterable은 어떠한 iterable 객체(list, tuple, set 등)가 될 수 있다. `range()` 함수를 이용해 iterable을 생성할 수 있고, 조건문을 사용하면 아래와 같이 생성할 수도 있다.

```python
newlist = [x for x in range(10)]
print(newlist)

# [결과 내용]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

newlist = [x for x in range(10) if x < 5]
print(newlist)

# [결과 내용]
# [0, 1, 2, 3, 4]
```

###### Expression

Expression은 iteration에서 현재 항목이지만 물론 새로운 List의 항목이 결정되기 전에 조작할 수 있는 부분이다.

```python
# newlist의 모든 값을 대문자로 설정

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

# [결과 내용]
# ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']
```

```python
# newlist의 모든 값을 'hello'로 설정

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)

# [결과 내용]
# ['hello', 'hello', 'hello', 'hello', 'hello']
```

Expression도 물론 조건을 포함할 수 있지만 필터 역할과는 다르다. Expression에서 조건은 결과를 조작하는 역할을 한다.

```python
# banana가 아니면 반환, banana이면 orange 반환

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

# [결과 내용]
# ['apple', 'orange', 'cherry', 'kiwi', 'mango']
```

#### Sort List

##### Sort List Alphanumerically

List 객체는 기본적으로 알파벳 및 숫자 오름차순으로 List를 정렬하는 `sort()` 메서드가 있다.

```python
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# [결과 내용]
# ['banana', 'kiwi', 'mango', 'orange', 'pineapple']
```

```python
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# [결과 내용]
# [23, 50, 65, 82, 100]
```

##### Sort Descending

내림차순으로 정렬하려면 키워드 argument인 `reverse = True`를 사용하면 된다.

```python
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# [결과 내용]
# ['pineapple', 'orange', 'mango', 'kiwi', 'banana']
```

```python
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

# [결과 내용]
# [100, 82, 65, 50, 23]
```

##### Customize Sort Function

키워드 argument인 `key = function`을 이용하면, 자신만의 함수로 사용자 정의 방식으로 정렬할 수 있다.

```python
# 숫자가 50에 가까운 정도를 기준으로 목록을 정렬

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# [결과 내용]
# [50, 65, 23, 82, 100]
```

##### Case Insensitive Sort

기본적으로 `sort()` 메서드는 대소문자를 구분하므로, 모든 대문자가 소문자보다 먼저 정렬된다.

```python
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# [결과 내용]
# ['Kiwi', 'Orange', 'banana', 'cherry']
```

다행히도 list 정렬 시에 내장 함수들을 key function으로 사용할 수 있다. 그리고 대소문자를 구분하지 않는 정렬을 하고 싶다면  key function으로 `str.lower`을 사용하면 된다.

```python
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# [결과 내용]
# ['banana', 'cherry', 'Kiwi', 'Orange']
```



##### Reverse Order

만약 list의 순서를 알파벳 순서와 관계없이 현재 list 순서의 역순으로 하고 싶다면, `reverse()` 메서드를 사용하면 된다. `reverse()` 메서드는 현재 정렬된 list의 순서를 역순으로 만든다.

```python
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# [결과 내용]
# ['cherry', 'Kiwi', 'Orange', 'banana']
```

#### Copy Lists

##### Copy a List

단순히 `list2 = list1`와 같은 입력만으로는 List를 복사할 수 없다. 왜냐하면 list2가 단순히 list1을 호출하는 객체가 되기 때문이다. 따라서 list1에 변화가 생긴다면 list2에도 자동으로 변화가 적용된다.

```python
thislist = ["apple", "banana", "cherry"]
mylist = thislist
print(mylist)

print(mylist is thislist)

thislist.append("melon")
print(mylist)


# [결과 내용]
# ['apple', 'banana', 'cherry']
# True
# ['apple', 'banana', 'cherry', 'melon']
```

복사하기 위한 여러 방법 중 한 가지는 List의 내장 메서드인 `copy()`를 사용하는 것이다.

```python
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

print(mylist is thislist)

thislist.append("melon")
print(mylist)

# [결과 내용]
# ['apple', 'banana', 'cherry']
# False
# ['apple', 'banana', 'cherry']
```

복사본을 만드는 또 다른 방법은 내장 메서드인 `list()`를 사용하는 것이다.

```python
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

thislist.append("melon")
print(mylist)

# [결과 내용]
# ['apple', 'banana', 'cherry']
# ['apple', 'banana', 'cherry']
```

#### Join Lists

##### Join Two Lists

파이썬에서는 둘 이상의 List를 결합하거나 연결하는 여러가지 방법이 있다.

그 중 가장 쉬운 방법은 `+` 연산자를 사용하는 것이다.

```python
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# [결과 내용]
# ['a', 'b', 'c', 1, 2, 3]
```

두 목록을 결합하는 또 다른 방법은 list1에 list2의 모든 항목을 하나씩 붙이는 것이다.

```python
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

# [결과 내용]
# ['a', 'b', 'c', 1, 2, 3]
```

또는 `extend()` 메서드를 사용하는 것이다. `extend()` 메서드의 목적은 특정 list에 다른 list의 요소를  추가하는 것이다.

```python
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# [결과 내용]
# ['a', 'b', 'c', 1, 2, 3]
```





