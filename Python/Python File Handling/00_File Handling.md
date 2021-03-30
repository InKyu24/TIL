### Python File Handling

파일 처리는 모든 웹 응용 프로그램에서 중요한 부분이다. 파이썬에는 파일 생성, 읽기, 업데이트 및 삭제를 위한 여러 기능이 있다.

#### File Handling

파이썬에서 파일 작업을 위한 주요 기능은 `open()` 함수이다.

이 `open()` 함수는 두 개의 매개 변수(파일 이름, 모드)를 사용한다.

파일을 여는 모드에는 4가지가 있다.

+ "r"  기본값으로 파일을 읽기 위해 연다. 파일이 없으면 오류가 발생한다.
+ "a" 추가할 파일을 연다. 파일이 없는 경우에는 생성하게 된다.
+ "w" 쓰기를 위해 파일을 연다. 파일이 없는 경우에는 생성하게 된다.
+ "x" 지정된 파일을 만들고, 파일이 있으면 오류가 발생한다.

또한 파일을 바이너리 또는 텍스트 모드로 처리할지 여부를 지정할 수 있다.

+ "t" 기본값으로 텍스트 모드로 처리한다.
+ "b" 바이너리 모드로 처리한다. (예 : 이미지)

##### Syntax

파일을 읽기 위해 열려면, 파일 이름을 지정하면 된다.

```python
f = open("demofile.txt")
```

위의 코드는 기본값인 모드를 생략하고 있다. 따라서 다시 작성하면 아래와 같다.

```python
f = open("demofile.txt", "rt")
```

> 파일이 있는지 확인해야 한다. 그렇지 않으면 오류가 발생하기 때문이다.

#### Open/Read Files

##### Open a File on the Server

파이썬과 동일한 폴더에 아래와 같은 파일이 있다고 가정하자.

>  `demofile.txt`
>
> Hello! Welcome to demofile.txt
> This file is for testing purposes.
> Good Luck!

이 파일을 열기 위해서는 `open()` 함수를 사용해야 한다.

`open()` 함수는 파일 내용을 읽는`read()` 메서드를 가진 파일 객체를 반환한다.

```python
f = open("demofile.txt", "r")
print(f.read())
```

만약 파일이 다른 위치에 있는 경우, 다음과 같이 파일 경로를 지정해야 한다.

```python
f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())
```

##### Read Only Parts of the File

기본적으로 `read()` 메서드는 전체 텍스트를 반환하지만 반환할 문자의 수를 지정할 수도 있다.

```python
# 파일 내에서 가장 앞에 문자 5개를 반환 [Hello]

f = open("demofile.txt", "r")
print(f.read(5))
```

##### Read Lines

다음 `readline()` 메서드를 사용하여 한 줄을 반환할 수 있다.

```python
# 파일의 가장 앞에 한 줄 반환 [Hello! Welcome to demofile.txt]

f = open("demofile.txt", "r")
print(f.readline())
```

`readline()` 메서드를 두 번 호출하게 되면, 두 줄을 읽을 수 있다.

```python
# 출력 내용
# Hello! Welcome to demofile.txt
# This file is for testing purposes.

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())
```

Loop문을 이용하면 전체 파일을 한 줄씩 읽을 수 있다.

```python
# 파일 전체 내용을 출력

f = open("demofile.txt", "r")
for x in f:
  print(x)
```

##### Close Files

작업이 끝나면 항상 파일을 닫는 것이 좋다. 버퍼링으로 인해 파일 변경 사항이 파일을 닫을 때까지 표시되지 않을 수 있기 때문이다.

```python
f = open("demofile.txt", "r")
print(f.readline())
f.close()
```

#### Write/Create Files

##### Write to an Existing File

기존 파일에 쓰려면 `open()` 함수에 매개 변수를 추가해야 한다.

+ "a" 파일 끝에 추가한다.

```python
# "demofile2.txt" 파일을 열고 내용을 추가한다.

# 파일을 열어서 작성하기 (내용 추가)
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

# 파일을 열어서 읽기 (추가된 내용 확인)
#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
```

+ "w" 기존 콘텐츠를 덮어 쓴다.(전체 파일에 덮어쓰기가 된다.)

```python
# "demofile3.txt" 파일을 열고 내용을 덮어쓴다.

# 파일을 열어서 작성하기 (내용 덮어쓰기)
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

# 파일을 열어서 읽기 (덮어쓰기로 작성된 내용 확인)
#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())
```

##### Create a New File

파이썬으로 새로운 파일을 생성하기 위해서는 `open()`메서드를 이용하며, 아래의 매개변수를 사용한다.

+ "x" 파일을 생성하는데, 만약 기존에 파일이 존재하는 경우 에러가 발생한다.

```python
# "myfile.txt"가 없는 경우에 한하여, 내용없이 텅 빈 "myfile.txt" 파일이 생성된다.

f = open("myfile.txt", "x")
```

+ "a" 파일이 존재하지 않는다면 파일을 생성한다. (파일 존재하는 경우 그 뒤에 내용 추가)

```python
f = open("myfile.txt", "a")
```

+ "w" 파일이 존재하지 않는다면 파일을 생성한다. (파일 존재하는 경우, 모든 내용 삭제)

```python
f = open("myfile.txt", "w")
```

#### Delete Files

##### Delete a File

파일을 삭제하기 위해서는 OS module을 import해야 한다. 그리고 `os.remove()` 기능을 이용하면 된다.

```python
# "demofile.txt"를 삭제한다.

import os
os.remove("demofile.txt")
```

##### Check if File exist

만약 파일 삭제에 관해 에러가 발생하는 것을 피하고 싶다면 파일을 삭제하기 전에 해당 파일이 존재하는가를 확인할 필요가 있다.

```python
# "demofile.txt"의 존재를 확인하고 파일을 삭제한다.

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
```

##### Delete Folder

폴더를 삭제하기 위해서는, `os.rmdir()` 메서드를 사용한다.

다만 빈 폴더만 제거할 수 있다는 점에 유의해야 한다.

```python
# "myfolder"를 삭제한다.

import os
os.rmdir("myfolder")
```

