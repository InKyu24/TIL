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

---

#### matplotlib 라이브러리를 이용한 시각화
+ 파이썬 시각화 모듈
+ 2D 형태의 그래프, 이미지 등을 사용할 때 적용

+ 실제 과학 

```python
import matplotlib.pyplot as plt
```

```python
# 메모리에 차트를 생성
plt.plot([10, 20, 30, 40])

# 차트 출력
plt.show()
```

```python
# 두 개의 차트 생성 후 출력하기
plt.plot([33, 12, 22, 9, 45], label='A_chart', color='skyblue', marker="o", linestyle="--")
plt.plot([50, 40, 30, 20, 10],'pink', label='B_chart')

# 차트 제목 설정
plt.title('plotting')

# 축 제목 설정
plt.xlabel("X-label")
plt.ylabel("Y-label")

# 범례 표시
plt.legend()

# 차트 출력
plt.show()
```

```python
# 차트 한글 제목 설정하기 (방법1)
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

# 한글 폰트 경로 및 이름 정의
font_path="C:/Windows/Fonts/malgun.ttf"
# 폰트 속성 변경
font_name=fm.FontProperties(fname=font_path).get_name()
# 차트 전체 폰트 속성 변경
plt.rc('font', family=font_name)

plt.plot([33,12,22,9,45], label='데이터', color='skyblue', marker="o", linestyle="--") 

plt.title("차트 그리기 실습") 
plt.xlabel("X-Label")      
plt.ylabel("Y-Label")      
plt.legend()           

plt.show()
```

```python
# 차트 한글 제목 설정하기 (방법2)
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

# 한글 폰트 경로 및 이름 정의
font_path="C:/Windows/Fonts/malgun.ttf"
# 폰트 속성 변경
font_name1=fm.FontProperties(fname=font_path, size=15)
font_name2=fm.FontProperties(fname=font_path, size=13)
font_name3=fm.FontProperties(fname=font_path, size=10)

plt.plot([33,12,22,9,45], label='데이터', color='skyblue', marker="o", linestyle="--") 

plt.title("차트 그리기 실습", fontproperties=font_name1)
plt.xlabel("X-Label", fontproperties=font_name2)
plt.ylabel("Y-Label", fontproperties=font_name3)
plt.legend()           

plt.show()
```

```python
# 생일에 따른 기온 변화 차트로 출력
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
import csv

f = open('./data/seoul.csv', encoding='cp949')
data = csv.reader(f)
header=next(data)

max_temp=[]
min_temp=[]
year_temp=[]

for row in data:
    if row[2]!='' and int(row[2].split('-')[0]) >= 1991 and row[2][-5:] == "02-04":
        max_temp.append(float(row[4]))
        min_temp.append(float(row[-3]))
        year_temp.append(row[2].split('-')[0])
        
print(max_temp)
plt.figure(figsize=(14,5))
plt.plot(year_temp, max_temp, label='최고기온', color='r', marker="+")
plt.plot(year_temp, min_temp, label='최저기온', color='b', marker="*")
plt.xticks(size=10, rotation=45)
plt.title("내 생일 기온 변화", size=20)
plt.xlabel("년도", size=15)
plt.ylabel("온도", size=15)
plt.legend(loc="best")
plt.grid(True)
plt.show()
```

```python
# 미션: 평균 데이터를 이용한 날짜별 차트 출력
# 1960년 이후 5월 15일 데이터를 기준으로 평균기온을 이용해 차트 작성
# 1960년 이후 1월 15일 데이터를 기준으로 평균기온을 이용해 차트 작성

import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
import csv

f = open('./data/seoul.csv', encoding='cp949')
data = csv.reader(f)
header=next(data)

augtemp=[]
jantemp=[]
year_temp=[]

for row in data:
    if row[2]!='' and int(row[2].split('-')[0]) >= 1960 and int(row[2].split('-')[0]) < 2020 and row[2][-5:] == "08-15":
        augtemp.append(float(row[3]))
        
    if row[2]!='' and int(row[2].split('-')[0]) >= 1960 and int(row[2].split('-')[0]) < 2020 and row[2][-5:] == "01-15":
        jantemp.append(float(row[3]))
        year_temp.append(row[2].split('-')[0])
        
plt.figure(figsize=(14,5))
plt.plot(year_temp, jantemp, label='01월', color='magenta', marker="+")
plt.plot(year_temp, augtemp, label='08월', color='pink', marker="+")
plt.xticks(size=10, rotation=45)
plt.title("연도별 기온 변화", size=20)
plt.xlabel("년도", size=15)
plt.ylabel("온도", size=15)
plt.legend(loc="best")
plt.grid(True)
plt.show()
```

---

#### 히스토그램

```python
plt.figure(figsize=(10,5))
plt.hist(augtemp, bins=12, label='8월')
plt.hist(jantemp, bins=12, label='1월')

plt.legend()
plt.show()
```

```python
# 주사위 1~6까지를 10번 던진 결과에 대한 히스토그램 출력
import matplotlib.pyplot as plt
import numpy as np

num_tmp=[np.random.randint(1, 7) for i in range(100)]

plt.figure(figsize=(10,5))
plt.hist(num_tmp, bins=6)
plt.show()
```

```python
# 히스토그램의 대표적인 네 가지 종류
weight = [68, 81, 64, 56, 78, 74, 61, 77, 66, 68, 59, 71,
        80, 59, 67, 81, 69, 73, 69, 74, 70, 65]
weight2 = [52, 67, 84, 66, 58, 78, 71, 57, 76, 62, 51, 79,
        69, 64, 76, 57, 63, 53, 79, 64, 50, 61]

plt.hist((weight, weight2), histtype='bar')
plt.title('histtype - bar')
plt.figure()
plt.show()

plt.hist((weight, weight2), histtype='barstacked')
plt.title('histtype - barstacked')
plt.show()

plt.hist((weight, weight2), histtype='step')
plt.title('histtype - step')
plt.figure()
plt.show()

plt.hist((weight, weight2), histtype='stepfilled')
plt.title('histtype - stepfilled')
plt.show()
```

---

#### 지역별 인구 구조 분석

```python
# 전국 남녀 연령별 인구 분포 분석
import csv
import matplotlib.pyplot as plt

f = open('./data/202105_인구현황.csv')
data = csv.reader(f)

for row in data:
    if '전국' in row[0]:
        tot_pop = [int(i.replace(",","")) for i in row[3:104]]
        man_pop = [int(i.replace(",","")) for i in row[106:207]]
        wom_pop = [int(i.replace(",","")) for i in row[209:310]]

plt.figure(figsize=(10, 5))
plt.style.use('ggplot')
plt.plot(tot_pop, label='tot')
plt.plot(man_pop, label='man')
plt.plot(wom_pop, label='wom')

plt.legend()
plt.show()
```

```python
# 전국 광역시, 연령별 인구 분포 분석
import csv
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

font_path="C:/Windows/Fonts/malgun.ttf"
font_name=fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

f = open('./data/202105_인구현황.csv')

local_lst = ['서울', '부산', '인천', '울산', '광주', '대전', '대구']

for loc_n in local_lst:
    data = csv.reader(f)
    for row in data:
        if loc_n in row[0]:
            tot_pop = [int(i.replace(",","")) for i in row[3:104]]

    plt.style.use('ggplot')
    plt.figure(figsize=(10, 3))
    
    plt.plot(tot_pop, label=loc_n)

    plt.legend()
    plt.show()
f.close()

# 한 차트에 같이 보기
import csv
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

font_path="C:/Windows/Fonts/malgun.ttf"
font_name=fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

local_lst = ['서울', '경기', '부산', '인천', '울산', '광주', '대전', '대구']

plt.style.use('ggplot')
plt.figure(figsize=(15, 5))    

for loc_n in local_lst:
    f = open('./data/202105_인구현황.csv')
    data = csv.reader(f)
    for row in data:
        if loc_n in row[0]:
            tot_pop = [int(i.replace(",","")) for i in row[3:104]]
            
    plt.plot(tot_pop, label=loc_n)
    f.close()
    
plt.legend()
plt.show()
```

---

#### 서울시 지역별 부동산 실거래 정보 분석

1. 구 단위 데이터 조회
   + 구 이름 입력
   + 파일에서 해당 구 이름을 기준으로 데이터 조회
   + '자치구명', '법정동명', '건물주용도', '건축년도', '건물면적', '층정보', '물건금액', '건물명' 리스트 데이터 추가

```python
# 사용자로부터 구명, 동명을 입력받아 조회
# 출력값 : '자치구명', '법정동명', '건물주용도', '건축년도', '건물면적', '층정보', '물건금액', '건물명'
#                3         5           15(-4)       17(-2)       11        13         16(-3)     18(-1)
import csv
import matplotlib.pyplot as plt

g_name = input('조회 구 이름 입력:')

f = open('./data/서울특별시_부동산_실거래가_정보_2020년.csv')
data = csv.reader(f)
header = next(data)

data_lst = []
for row in data:
    if g_name == row[3]:
        data_lst.append([row[3],row[5],row[-4],row[-2],row[11],row[13],row[-3],row[-1]])
        
f.close()
data_lst
```

2. 동 단위
   + 해당 구에 속한 동 리스트 조회
   + 해당 리스트를 이용해 동별 '아파트' 평균(합계/수량 or mean) 계산
   + 동별 평균 출력

```python
d_name = []
for lst in data_lst:
    if lst[1] in d_name:
        continue
    else:
        d_name.append(lst[1])
print(d_name)
```

```python
avg_lst = []
for dong in d_name:
    cnt = 0
    tot = 0
    for lst in data_lst:
        if lst[1] == dong and lst[2] == '아파트':
            tot += int(lst[-2])
            cnt += 1
    if cnt==0:
        avg_lst.append({"동이름":dong, "평균판매가":0, "거래건수":0})
    else:
        avg = tot/cnt
        avg_lst.append({"동이름":dong, "평균판매가":int(avg), "거래건수":cnt})
    
avg_lst
```

```python
import pandas as pd
df = pd.DataFrame(avg_lst)
df
```

```python
df1= df[df['평균판매가'] != 0]
df1 = df1.sort_values(by=['거래건수'], ascending=False)
df1
```

3. 동별 평균 값을 이용해 그래프 생성
   - 막대 그래프
   - box plot 그래프

```python
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

df1 = df1.sort_index()
df1['평균판매가'].plot()
plt.show()
```

```python
font_name=fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
plt.rc('font', family=font_name)

plt.figure(figsize=(20, 5))
plt.xticks(size=10, rotation=45)
plt.plot(df1['동이름'], df1['거래건수'])
plt.show()
```

```python
font_name=fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
plt.rc('font', family=font_name)

plt.style.use('ggplot')
plt.figure(figsize=(20, 5))
plt.xticks(size=10, rotation=45)
plt.bar(df1['동이름'], df1['평균판매가'])
plt.show()
```

```python
plt.boxplot(df1['평균판매가'])
plt.show()
```

---

서울시 지역별 부동산 실거래 정보 분석 [pandas 모듈 이용]

```python
import pandas as pd
df1 = pd.read_csv('./data/서울특별시_부동산_실거래가_정보_2020년.csv', encoding='cp949')

df1[df1['자치구명'] == '성북구'].head() # pandas 모듈에서 읽은 데이터에서 상위 5개만 출력
```

```python
# Series 구조
print(type(df1['자치구명']))
df1['자치구명']
```

```python
# DataFrame 구조
print(type(df1[['자치구명', '건물주용도']]))
df1[['자치구명', '건물주용도']]
```

```python
# index
print(type(df1.columns))
df1.columns
```

```python
# 데이터프레임 구조에서 원하는 필드값만 가져와 재정의
df1 = df1[['자치구명', '법정동명', '건물주용도', '건축년도', '건물면적', '층정보', '물건금액', '건물명']]
df1
```

```python
# 데이터프레임의 데이터 정보 확인하기
df1.info()
```

```python
# 특정 열의 NaN 값을 찾아 원하는 값으로 변경 후 저장
df1 = df1.fillna({'층정보':1, '건물명':'단독'})
df1.isnull().sum()
```

```python
# NaN 데이터 삭제: dropna() 함수 사용, 
# 옵션: how="any" => 기본옵션, NaN이 하나라도 존재하면 삭제
# 옵션: how="all" => 데이터 전체(행 전체)가 NaN인 데이터만 삭제

df1.dropna(how="all")
```

---

#### pandas.DataFrame 데이터 관리
* 단일조건: df[ df['열이름']==조건 ]
* 다중조건: df[ (df['열이름']==조건1) & (df['열이름']==조건2) ] => AND 연산
* 다중조건: df[ (df['열이름']==조건1) | (df['열이름']==조건2) ] => or 연산

```python
# 자치구명이 성북구인 데이터에서 법정동명을 가져와 고유값(중복제거) 출력
df1[df1['자치구명']=='성북구']['법정동명'].unique()
```

```python
# 자치구명이 성북구인 데이터에서 법정동명을 가져와 동별 개수를 체크해 출력
df1[df1['자치구명']=='성북구']['법정동명'].value_counts()
```

```python
# 자치구가 성북구이면서 건물주용도가 아파트인 데이터에 대한 법정동명 거래 건수 출력
df2=df1[ (df1['자치구명']=='성북구') & (df1['건물주용도']=='아파트')]['법정동명'].value_counts()
print(df2)
```

```python
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_name=fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
plt.rc('font', family=font_name)


df2.plot(kind='bar', figsize=(10, 3))
plt.show()
```

```python
# kind="" : bar, pie, hist, kde, box, scatter, area

df2.plot(kind='box', figsize=(5, 3))
plt.show()

df2.plot(kind='pie', figsize=(5, 3))
plt.show()

df2.plot(kind='area', figsize=(10, 3))
plt.show()
```

```python
df2=df1[(df1['자치구명']=='성북구')&(df1['건물주용도']=='아파트')].groupby('법정동명').mean()
df2['물건금액'].plot(kind='bar', figsize=(10, 5))
plt.show()
```

---

##### [미션] 구단위/동별 물건금액의 평균값 시각화
* 구이름, 건물주용도는 사용자에게 입력받아 진행
* 출력 평균은 동을 기준로 계산 및 출력

```python
import pandas as pd

df1=pd.read_csv('./data/서울특별시_부동산_실거래가_정보_2020년.csv', encoding='cp949')

df1=df1[['자치구명', '법정동명', '건물주용도', '건축년도', '건물면적', '층정보', '물건금액', '건물명']]

# 특정 열의 NaN 값을 찾아 원하는 값으로 변경 후 저장
df1=df1.fillna({'층정보':1, '건물명':'단독', '건축년도':0})
#print(df1.isnull().sum())

gu=input('구 이름:')
ju=input('건물용도:')

df2=df1[(df1['자치구명']==gu)&(df1['건물주용도']==ju)][['법정동명','물건금액']].groupby('법정동명').mean()
#print(df2)
df2.plot(kind="bar", figsize=(10, 5))
plt.savefig('./data/'+gu+"_"+ju+"_평균거래정보.png")
plt.show()
```

```python
gu=input('구 이름:')
ju=input('건물용도:')

df1[(df1['자치구명'].str.contains(gu)) & (df1['건물주용도'].str.contains(ju))]
```

---

#### pandas 모듈 이해 및 활용

```python
import pandas as pd
from numpy import random
import matplotlib.pyplot as plt

df1 = pd.Series(['AAA', 'BBB', 'CCC', 'DDD'], name="Name")
print(df1)
print(type(df1))

df2 = pd.Series([33, 28, 45, 41], name="Age")
print(df2)
print(type(df2))

print(pd.DataFrame(df1))
print(pd.DataFrame(df2))
```

concat: 두 개 이상의 데이터 프레임 또는 시리즈 구조의 데이터를 병합할 때 사용

 + 병합방법
    + 행 병합(행 추가) [기본] => axis=0
    + 열 병합(열 추가) => axis=1

```python
df0 = pd.concat([df1, df2], axis=1)
print(type(df0))
df0
```

```python
df2=pd.DataFrame(df2)
df0 = pd.concat([df1, df2], axis=1)
print(type(df0))
df0
```

#### pandas.DataFrame 생성

```python
# pandas.DataFrame 생성: 딕셔너리 구조 이용
df1 = pd.DataFrame({"Name":['AAA','BBB','CCC','DDD'],
                   "Age":[33, 28, 45, 41],
                   "Gender":['male', 'male', 'female', 'male']})
df1
```

```python
# pandas.DataFrame 생성: 리스트 구조 이용
df1 = pd.DataFrame((["AAA", 33, 'male'],
                   ["BBB", 28, 'male'],
                   ["CCC", 45, 'female'],
                   ["DDD", 41, 'male']), columns=["Name", "Age", "Gender"])

df1
```

```python
# pandas.DataFrame 생성: 딕셔너리 & 리스트 구조 동시 이용
df1 = pd.DataFrame([{'Name':'AAA', 'Age':33, 'Gender':'male'},
                   {'Name':'BBB', 'Age':28, 'Gender':'male'},
                   {'Name':'CCC', 'Age':45, 'Gender':'female'},
                   {'Name':'DDD', 'Age':41, 'Gender':'male'}])
df1
```

---

### 성적표.csv 파일을 이용한 데이터 추가/수정/삭제 등 관리

```python
df1 = pd.read_csv('./data/성적표_null.csv', encoding='cp949')
df1
```

```python
df1.isnull().sum()
```

```python
# NaN 값 처리: 모든 데이터 NaN인 데이터 행 삭제
# dropna() 옵션 : default(생략) => how='any': Nan인 모든 행 삭제
# dropna() 옵션 : default(how='all'): 행 전체가 NaN인 모든 행 삭제
df1.dropna()
df1.dropna(how="all")

# dropna() 옵션 : default(how='all'): 행 전체가 NaN인 열 삭제
df1.dropna(how="all", axis=1)

# dropna() 옵션 : thresh=결측치 개수 => 결측치 개수가 임계치 이상인 데이터 모두 삭제
df1 = df1.dropna(thresh=3) # NaN이 세 개 이상인 데이터 행 삭제
```

---

#### pandas.Series 구조

```python
# 이론, 실기 점수를 60~100 사이의 값으로 무작위 입력
df1['이론']=random.randint(60, 101, size=len(df1))
df1['실기']=random.randint(60, 101, size=len(df1))

df1
```

```python
# 성별에 따라 1, 2가 들어갈 리스트 변수 생성
gender_code = []
for xy in df1['남/여']:
    if xy == '남자':
        gender_code.append(1)
    elif xy == '여자':
        gender_code.append(2)

df1['성별코드']=gender_code

df1

# 성별에 따라 1, 2가 들어갈 리스트 변수 생성 [한줄쓰기]
df1['성별코드']=[1 if xy == "남자" else 2 for xy in df1['남/여']]
```

```python
# 열 위치 변경
df1 = df1[['순번', '이름', '학과', '남/여', '성별코드', '학년', '이론', '실기']]
```

```python
# 이론, 실기 점수 합계와 평균 추가
df1['합계']=df1['이론']+df1['실기']
df1['평균']=df1['합계']/2
```

---

#### pandas.DataFrame 저장
- csv.DataFrame.to_csv('경로 및 파일명.csv', index=False)
  - 구분자 기본은 쉼표(,)
  - index는 저장안함
- txt: DataFrame.to_csv('경로 및 파일명.txt', sep='\t', index=False)
  - 구분자(sep)를 탭으로 지정
- xls : DataFrame.to_excel('경로 및 파일명.xls', index=False)
  - xls: !pip install xlwt
  - xlsx : !pip install openpyxl
- html : DataFrame.to_html('경로 및 파일명.html', index=False, header=False)

```python
df1.to_csv('./data/성적1.csv', encoding="cp949")
df1.to_csv('./data/성적1.txt', sep='\t')
df1.to_excel('./data/성적1.xlsx', header=False)
df1.to_html('./data/성적1.html', index=False)
```

---

#### pandas.DataFrame 행/열 값 출력하기

+ 단일 행 출력
  + DataFrame.loc[index, '열이름']
+ 시작~ 종료 값 연속 다중 행 출력
  + DataFrame.loc[index시작값:index종료값] => 시작~종료값 다중 행 출력
+ 시작~종료값 불연속 행 다중 출력
  + DataFrame.loc[[index1, index2],['열이름1','열이름2']]

```python
# 단일 행 출력
df1.loc[1]
df1.loc[0,['이름']]
df1.loc[3, ['이름','학과','학년']]
```

```python
# 연속 다중 행 출력
df1.loc[1:6]
df1.loc[2:4, ['이름']]
df1.loc[9:16, ['이름','학과','학년']]
```

```python
# 불연속 행 다중 출력
df1.loc[[4, 8, 6, 1]]
df1.loc[[0, 1, 0, 7, 3]] # 중복도 가능
df1.loc[[0, 2, 4, 8],['이름','남/여']]
```

+ 행렬 위치에 따른 데이터 값

  + DataFrame.iloc[행위치, 열위치]

  + DataFrame.iloc[행시작위치:행종료위치, 열시작위치:열종료위치]

```python
df1.iloc[0,0]
df1.iloc[5:13, 1:6]
df1.iloc[[1,5,4,3],[1,2,3,4,5]]

df1.iloc[[1,3],1:6]
df1.iloc[1:3,[4,3,1]]
```

---

#### 데이터 정렬

+ DataFrame.sort_values(by=['열 이름'], ascending=True)
+ DataFrame.sort_index()

```python
# DataFrame 값을 기준으로 정렬
df1 = df1.sort_values(by=['학년'])
display(df1.head())
df1.sort_values(by=['평균'], ascending=False, inplace=True)
display(df1.head())
```

```python
# 복수의 정렬 조건
df1 =df1.sort_values(by=['학년','평균'], ascending=[True, False])

# 재정렬 후 차이 비교
df1.loc[0:9] # index 값이 0인 행부터 9인 행까지 출력
df1.iloc[0:9] # 0번째 행부터 9번째 행까지 출력
```

```python
# 인덱스 기준 정렬
df1.sort_index()

# 인덱스 재설정
df1.reset_index(drop=True)
```

####  데이터 행/열 삭제

+ DataFrame.drop(index)

```python
# index 값이 0인 데이터 행 삭제
df1.drop(0)
df1.drop(0, axis=0)
df1.drop(0, 0)
df1.drop(index=0, axis=0)

# index 값이 29, 33, 16인 데이터 행 삭제
df1.drop([29,33,16])
df1.drop(index=[29,33,16], axis=0)

# 특정 조건에 따른 데이터 행 삭제
drop_index = df1[df1['평균'] < 90].index
df1.drop(drop_index)

# 열 삭제
df1.drop(columns=['순번','학년'])
df1.drop(['평균'], axis=1)
df1.drop(['순번',['성별코드']], axis=1)

# 즉시 삭제
del df1['합계']
```

---

```python
# 구분자가 쉼표가 아닌 다른 구분자(탭:\t)를 사용한 데이터 읽어오기
# 제목행 선택
import pandas as pd

df1 = pd.read_csv('./data/서울시 인구현황_구.txt', sep='\t')
```

```python
# 특정 열에 대한 데이터만을 가져오는 세 가지 방법
df1[['기간', '자치구', '합계', '합계.1', '합계.2', '한국인', '한국인.1', '한국인.2',
       '등록외국인', '등록외국인.1', '등록외국인.2', '65세이상고령자']]

df1.loc[:,['기간', '자치구', '합계', '합계.1', '합계.2', '한국인', '한국인.1', '한국인.2',
       '등록외국인', '등록외국인.1', '등록외국인.2', '65세이상고령자']]

df1.iloc[:,[0,1,3,4,5,6,7,8,9,10,11,-1]]
```

```python
df1 = df1.iloc[1:,[0,1,3,4,5,6,7,8,9,10,11,-1]]
```

```python
df1.drop(0, inplace=True) # axis=0 생략
df1.head()
```

axis = 0은 dataframe 행 단위를 수정할 때 필요한 파라미터 값이다. axis = 1은 dataframe 열 단위를 수정할 때 필요한 파라미터 값이다. drop( ) 함수에 index, column이라는 파라미터를 사용하지 않는다면 axis=0 또는 axis=1 파라미터값을 넣어줘야 한다.

#####  열 이름 변경

- 전체 열 이름 일부 변경
  - df.rename(columns={'합계':'총인구', '합계.1':'총인구(남), ...}) 
- 다수의 열 이름 변경
  - df.rename(columns={df1.columns[2]:'총인구', df1.columns[2]:'총인구(남), ...})

```python
# 열 이름 변경
col_name=['년도', '자치구','총인구','총인구(남)', '총인구(여)', '내국인', '내국인(남)', '내국인(여)',
          '외국인', '외국인(남)','외국인(여)', '65세이상']

for i in range(len(col_name)):
    df1.rename(columns={df1.columns[i]:col_name[i]}, inplace=True)

df1.head(3)
```

```python
df1.info()
```

##### 연도별 총인구 값을 나타내는 그래프 작성

```python
df2=df1.iloc[:, 0:5]
df2.head()
df2.info()
```

```python
# pandas에서 데이터형을 원하는 데이터형으로 변겅: astype() 함수

df2['총인구'] = df2['총인구'].str.replace(',','')
df2['총인구(남)'] = df2['총인구(남)'].str.replace(',','')
df2['총인구(여)'] = df2['총인구(여)'].str.replace(',','')

df2.dtypes
```

```python
df2 = df2.astype({'년도':int,'총인구':int,'총인구(남)':int,'총인구(여)':int})

df2.dtypes
```

```python
df2.head()
```

```python
import matplotlib.pyplot as plt

gu = input('조회할 구 이름 입력:')

df3 = df2[df2['자치구']==gu]
```

```python
plt.plot(df3['년도'],df3['총인구'])
plt.show()
```

```python
plt.plot(df3['년도'],df3['총인구(남)'])
plt.plot(df3['년도'],df3['총인구(여)'])
plt.show()
```

```python
import matplotlib.font_manager as fm
font_name=fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
plt.rc('font', family=font_name)

df3.plot(kind='hexbin', x='총인구', y='년도', gridsize=20)  # 산점도 그래프
plt.show()
```

```python
df3.plot(kind='bar', x='년도', y=['총인구(남)', '총인구(여)'])  
plt.show()
```

```python
df1[df1['내국인'] != '…']
```



