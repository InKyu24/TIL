#### Python 가상환경 설정

##### 1. Miniconda 설치 [https://docs.conda.io/en/latest/miniconda.html]

##### 2. 가상환경 설정

conda create -n (projectName) python=3.9

##### 3. 생성된 가상환경 확인

conda info --envs

##### 4. 생성된 가상환경 삭제

conda remove --name (projectName) --all

##### 5. 생성된 가상환경 활성화

conda activate (projectName)

##### 6. jupyter notebook 설치 [활성화된 가상환경에 설치]

conda install jupyter

##### 7. jupyter notebook 실행 및 workspace 폴더 생성하여 데이터 생성 [new > python3]



##### * 가상환경 종료

conda deactivate

---

#### Python 기본 구조 및 Jupyter notebook 사용법

1. 주석문 - #으로 시작하며, 실행 코드에 영향을 주지 않아 설명하기 위해 사용하거나 특정 구문을 일시적으로 실행을 하지 않기 위해 사용한다.
2. 세미콜론`;` - 여러 구문을 한 줄로 쓰는 경우 사용
3. 코드 실행
   * `ctrl+enter` - 실행
   * `shift+enter` - 실행 후 아래 행 이동
   * `alt+enter` - 실행 후 아래 행 추가
4. 라인 번호 추가
   * `view > Toggle Line Numbers` or `shift+L`
5. 들여쓰기

---

#### 변수

변수는 이름이 주어진 메모리로 프로그래머가 직접 지정한 변수명을 통해 데이터를 저장하고 검색할 수 있다. 또한 대입문을 통해 변수 값을 변경할 수 있다. python에서는 마지막으로 지정한 데이터가 최종 데이터 타입 형태를 띈다.

- 변수명 규칙
  - 글자나 밑줄로 시작 (숫자나 특수문자로 시작하지 않는다.)
  - 글자, 숫자, 밑줄로 구성
  - 대소문자를 구분한다

---

#### 모듈

자주 사용되는 코드나 유용한 코드를 논리적으로 묶어 관리하고 사용할 수 있도록 하는 것으로 보통 하나의 파이썬 .py 파일이 하나의 모듈이 된다. 모듈 안에는 함수, 클래스, 변수들이 정의될 수 있으며 실행 코드를 포함할 수도 있다.

1. 모듈 설치 [활성화된 가상환경에서 설치]
   - conda install (모듈명) 또는 pip install (모듈명)
2. 모듈 연결
   * import (모듈명) as (모듈 별명) 또는 from (모듈명) import (모듈의 일부인 변수, 함수, 클래스)

* Jupyter notebook 내에서 모듈을 설치하고 연결하는 방법
  * import (모듈명)  as (모듈 별명) 또는 from (모듈명) import (모듈의 일부인 변수, 함수, 클래스)
  * !pip install (모듈명)

---

#### 파이썬 자료형

1. ##### 숫자형 데이터

   + int - 정수형, float - 실수형
   + type() - 데이터 형식을 출력
   + 정수와 실수의 연산 결과는 실수형 데이터로 나타난다.

2. ##### 문자형 데이터

   * 데이터 입력 시에는 인용부호로 '단일' 또는 "이중 따옴표"를 사용한다.

   * [문자 데이터 + 문자 데이터] 연산은 문자열을 연결해주는 연산으로 쓰인다.

   * 인덱싱(indexing)

     * 첫 번째 글자는 0번째부터 시작, 마지막 글자는 -1번째부터 시작

     * 공백도 하나의 인덱스

       print(str2[0]) => "파"

   * 슬라이싱(slicing) 

     * 인덱싱 위치 값을 기준으로 문자를 쪼개어 가져오는 것

       print(str2[0:3]) => "파이썬"

       print(str2[:3]) => "파이썬"

     + 뒤에서 앞을 빼면 추출할 글자 개수가 나온다고 생각하면 쉽다.

   * split("A") 

     * 문자열을 입력 기호(A)를 기준으로 텍스트 나누어 리스트 구조로 반환한다. 기본값은 스페이스
     * 원본 데이터에 영향을 주지 않는다.

   * replace("A", "B")

     * A값을 B값으로 치환한다.
     * 데이터 전처리 후 불필요한 데이터 제거할 때 많이 사용된다.

   * "-".join("ABCD")

     * A-B-C-D

3. ##### 리스트형 데이터

   * 복합형 데이터 입력 시 사용한다.

   + 데이터 입력 시 대괄호[ ]로 묶어서 입력하고, 요소는 쉼표(,)로 구분한다.
   + 리스트명 = [요소1, 요소2, 요소3, ...]
   + 인덱싱과 슬라이싱이 작동한다.
   + 인덱싱을 통해 특정 요소의 데이터를 수정할 수 있다.
   + 리스트에 요소로 리스트가 들어갈 수 있다.
   + [리스트 데이터 + 리스트 데이터] 연산은 리스트를 하나로 연결해주는 연산으로 쓰인다.
   + append(요소)
     + 리스트 구조의 마지막 데이터 뒤에 요소를 추가한다.
     + 원본 데이터에 바로 기록된다.

4. ##### 튜플형 데이터

   + 데이터 입력 시 소괄호( ) 로 묶어서 입력하고, 요소는 쉼표(,)로 구분한다.
   + 리스트의 요소는 변화가 가능하지만, 튜플 내 요소는 변하지 않는다.

5. ##### 딕셔너리형 데이터 (사전구조)

   + 데이터 입력 시 중괄호{ }로 묶어서 입력하고, 요소는 쉼표(,)로 구분한다.
   + 키 값 : 밸류 값이 한 쌍의 요소로 들어온다.

---

#### 반복문 (for)

##### 기본구조1

```python
for 변수명 in 객체명:
	반복실행문
```

```python
inName = ['홍길동', '박변수', '김수진', '허순이', '서정동']
for name in inName:
    print(f'안녕하세요. {name}님')
    
print(name) # 서정동
del name
```

##### 기본구조2

```python
for 변수명 in range():
	반복실행문
```

```python
inName = ['홍길동', '박변수', '김수진', '허순이', '서정동']
for i in range(5):
    print(f'안녕하세요. {inAge[i]}살의 {inName[i]}님 ')
    
print(inName[i]) # 서정동
del i
print(inName[i]) # i is not defined
```



>range(10) => 0부터 시작해서 10개의 정수형 숫자 생성 [0~9]
>
>range(5, 10) => 0부터 시작해서 10개의 정수형 숫자 생성 [0~9], 5부터 출력
>
>range(1,10,2) => 0부터 시작해서 10개의 정수형 숫자 생성 [0~9], 1부터 2씩 증가하면서 출력

---

#### input()

사용자로부터 데이터를 입력받고자 할 때 사용하는 함수로 모든 입력데이터는 무조건 문자형 자료로 저장된다.

따라서 필요한 경우에는 숫자로 변환하는 작업을 거쳐주어야 한다.

`inData = int(input('숫자를 입력하세요'))`

---

#### 제어문(if)

- break: 반복문 영역을 벗어남
- continue: 아래 문장을 실행하지 않고 for문으로 돌아가 다음 데이터 실행

```python
inData = int(input('숫자를 입력하세요:'))

if inData > 0 :
    print("0보다 큰 값입니다.")
elif inData < 0 :
    print("0보다 작은 값입니다.")
else :
    print("0이 입력되었습니다.")
```

---

#### numpy 난수 발생

* random 모듈을 이용한 난수 생성

* random.randint(시작값, 종료값) 
  * 시작값~종료값 범위에 있는 정수를 임의로 생성
  * range와 같이 종료값은 범위에 포함되지 않는다. 

```python
import numpy as np

# 10~20 사이의 정수를 임의로 생성 (10, 11, 12, ..., 19)
np.random.randint(10, 20)

# 0부터 50까지 무작위 정수를 10개 추출한 리스트 출력
rd_list = []
for i in range(10):
    rd_list.append(np.random.randint(0, 51))
print(rd_list)

# 0부터 50까지 무작위 정수를 10개 추출한 리스트 출력하는 두 가지 방법
print(np.random.randint(51, size=10))
print(np.random.randint(0, 51, 10)
```

##### 한 줄 쓰기

```python
# 한 줄 쓰기
# 0부터 50까지 무작위 정수를 10개 추출한 리스트 출력
rd_list = [np.random.randint(0, 51) for i in range(10)]
print(rd_list)

# words 데이터에서 글자수가 4개 이상인 데이터를 찾아 new_words에 리스트로 저장
words = ["멀티캠퍼스" ,"티스토리", "블로그", "파이썬", "for", "프로그래밍", "반복"]
new_words = []

for word in words:
    if len(word) > 3:
        new_words.append(word)
        
print(new_words)

# 한 줄 쓰기
# words 데이터에서 글자수가 4개 이상인 데이터를 찾아 new_words에 리스트로 저장
new_words = [word for word in words if len(word) > 3 ]
print(new_words)
```

```python
# words가 가지고 있는 단어 중 길이가 4 이상인 데이터만 new_words에 리스트로 추가
words = [ [ "이중 for문", "파이썬", "프로그래밍", "스터디" ], 
[ "Python", "NLP", "ML", "DL" ], [ "leetCode", "BaekJoon", "HackerRank" ], 
[ "멀티캠퍼스", "COMPAS", "DACON", "Kaggle" ] ]

new_words  = []
for each_word_lst in words:
    for word in each_word_lst:
        if len(word) > 3:
            new_words.append(word)
            
print(new_words)
```

```python
# 한 줄 쓰기
# 총 5개의 리스트, 각 리스트의 크기는 10~20개이며, 각 리스트의 요소는 0~50 사이의 값으로 구성
rd_lst=[list(np.random.randint(0,51,size=np.random.randint(10,21))) for i in range(5)]
print(rd_lst)
```

---

#### for문과 if문을 이용한 최대, 최소값 계산

```python
# 배열 내 최대값 구하기
data=[34, 23, 20, 43, 1, 5, 2, 14, 18, 24, 40, 18, 38, 4, 3, 22, 43, 6, 36, 13]
mxdata=data[0]
for dt in data:
    if dt > mxdata:
        mxdata=dt
print(mxdata)

# 배열 내 최소값 구하기
data=[34, 23, 20, 43, 1, 5, 2, 14, 18, 24, 40, 18, 38, 4, 3, 22, 43, 6, 36, 13]
mndata=data[0]
for dt in data:
    if dt < mndata:
        mndata=dt
print(mndata)

# 배열 전체 합계 구하기
data=[34, 23, 20, 43, 1, 5, 2, 14, 18, 24, 40, 18, 38, 4, 3, 22, 43, 6, 36, 13]
sumdata = 0
for dt in data:
    sumdata += dt
print(sumdata)
```

```python
lst = 	[[48, 1, 49, 20, 6, 40, 8, 36, 2, 16, 16, 39, 15],
		[39, 46, 39, 1, 4, 16, 49, 37, 45, 6, 26, 14, 28],
        [0, 21, 30, 24, 49, 18, 20, 49, 4, 7, 5, 26, 37],
		[34, 2, 28, 47, 10, 1, 22, 26, 30, 31, 26, 42, 16, 15, 45, 9, 48],
		[13, 20, 9, 37, 28, 16, 17, 2, 7, 22, 21, 39, 14, 27]]

# 최대값 구하기
mxdata = lst[0][0]
for dat in lst:
    for i in dat:
        if i >  mxdata :
            mxdata = i

# 최소값 구하기
mndata = lst[0][0]
for dat in lst:
    for i in dat:
        if i <  mndata :
            mndata = i

# 합계 구하기
sumdata = 0
for dat in lst:
    for i in dat:
        sumdata += i
        
print(f'최대값:{mxdata}, 최소값:{mndata}, 합계:{sumdata}')
```

##### 각 그룹별 계산

+ 그룹단위 최대, 최소, 합계
+ 전체 최대, 최소, 합계

```python
rd_lst=[list(np.random.randint(0,51,size=np.random.randint(10,21))) for i in range(5)]
print(rd_lst)
```

```python
G_lst=[]
Tot_lst=[0, rd_lst[0][0], rd_lst[0][0]]

for i in range(len(rd_lst)):
    group_lst = [0, rd_lst[i][0], rd_lst[i][0]]
    for data in rd_lst[i]:
        group_lst[0] += data      
        if data > group_lst[1]:
            group_lst[1] = data       
        if data < group_lst[2]:
            group_lst[2] = data    
    G_lst.append(group_lst)
    
    Tot_lst[0] += group_lst[0]
    if group_lst[1] > Tot_lst[1]:
        Tot_lst[1] = group_lst[1]ㄴ
    if group_lst[2]< Tot_lst[2]:
        Tot_lst[2] = group_lst[2]
   
print('그룹별\n',G_lst,'\n')
print(f'전체 합계:{Tot_lst[0]}, 전체 최대:{Tot_lst[1]}, 전체 최소:{Tot_lst[2]}')
```

---

#### 파일 관리

+ CSV 형식의 파일 읽어오는 방법
  + pandas 모듈을 이용하는 방법
  + csv 모듈을 이용하는 방법

```python
# 공공 데이터 포털에서 가져온 데이터 내용 화면에 출력
import csv

f = open('./data/seoul.csv', 'r', encoding='cp949')
data = csv.reader(f, delimiter=",")

header = next(data) #첫번째 행(제목행)을 header로 빼고, data에서는 제외

for row in data:
    print(row)

f.close()
```

```python
# 가장 더웠던 날에 대한 정보 찾기

import csv

f = open('./data/seoul.csv', 'r', encoding='cp949')
data = csv.reader(f, delimiter=",")

header = next(data)
print(header)

maxtem = ["",0, 0, 0]
for row in data:
    if row[4]!='' :
        if float(row[4]) > maxtem[1]:
            maxtem[0] = row[2]
            maxtem[1] = float(row[4])
            maxtem[2] = float(row[-3])
            maxtem[3] = float(row[-1])

print(maxtem)
f.close()
```

---

#### pandas 모듈을 이용한 csv 파일 관리

```python
import pandas as pd

df=pd.read_csv('./data/seoul.csv', encoding='cp949')

df['최고기온(℃)'].max()
df[df['최고기온(℃)'] == df['최고기온(℃)'].max()]

df.info()

df.columns

df[['지점명', '일시', '평균기온(℃)', '최고기온(℃)', '최저기온(℃)']]
```

---

```python
# 자신의 생일과 일치하는 날짜에 대한 날씨[평균, 최고, 최저기온] 출력

import csv

f = open('./data/seoul.csv', 'r', encoding='cp949')
data = csv.reader(f, delimiter=",")

header = next(data)

birth = []
for row in data:
    if (row[2]) != '' and int(row[2][:4]) >= 1991 and row[2][5:10] == '02-04':
        birth.append([row[2],float(row[3]),float(row[4]),float(row[6])])
f.close()

print(birth)
```



