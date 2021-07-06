# 연도별 인구현황 분석
# 사용자가 입력한 연도의 데이터를 이용해 외국인 현황
# x 축 자치구
# 막대그래프, 제목, x/y 축제목
# 외국인 남성/여성의 구성 비율

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy

df1 = pd.read_csv('./data/서울시 인구현황_구.txt', sep='\t', header=1)
df1 = df1.iloc[:, [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, -1]]
df1.drop(0, inplace=True)

col_name = ['년도', '자치구', '총인구', '총인구(남)', '총인구(여)', '내국인', '내국인(남)', '내국인(여)', '외국인', '외국인(남)', '외국인(여)', '65세 이상']
for i in range(len(col_name)):
    df1.rename(columns={df1.columns[i]: col_name[i]}, inplace=True)

df2 = df1.iloc[:, [0, 1, 8, 9, 10]]

# 1991년 데이터 제거
df2 = df2[df2['외국인'] != '…']

df2['외국인'] = [int(df2.loc[row_i, "외국인"].replace(',', '').replace('…', '0')) for row_i in df2.index]
df2['외국인(남)'] = [int(df2.loc[row_i, "외국인(남)"].replace(',', '').replace('…', '0')) for row_i in df2.index]
df2['외국인(여)'] = [int(df2.loc[row_i, "외국인(여)"].replace(',', '').replace('…', '0')) for row_i in df2.index]

df2 = df2.astype({'외국인': int, '외국인(남)': int, '외국인(여)': int})

df2['외국인(남자비율)'] = df2['외국인(남)'] / df2['외국인']
df2['외국인(여자비율)'] = df2['외국인(여)'] / df2['외국인']


font_name = fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
plt.rc('font', family=font_name)

year = input('조회: 연도를 입력하세요:')

df3 = df2[df2['년도'] == year]
guList = []
for gu in df3['자치구']:
    guList.append(gu)

plt.style.use('ggplot')
df3.plot(kind='bar', x='년도', y=['외국인(남자비율)', '외국인(여자비율)'], figsize=(15, 7))
plt.title('서울시 외국인 자치구별 인구 분석 그래프 (' + year + '년 기준)', size=15)
plt.xlabel('자치구')
plt.ylabel('인구수')

plt.show()

plt.figure(figsize=(10, 8))
plt.style.use('ggplot')
plt.xticks(size=10, rotation=45)
# plt.bar(df3['자치구'], df3['외국인'], label='외국인')
plt.bar(df3['자치구'], df3['외국인(남자비율)'], bottom=df3['외국인(여자비율)'], color='#ff80ab')
plt.bar(df3['자치구'], df3['외국인(여자비율)'], color='k')
plt.legend()
plt.title('서울시 자치구별 외국인 남녀비율 그래프  (' + year + '년 기준)', size=15)
plt.xlabel('자치구')
plt.ylabel('인구수')
plt.show()