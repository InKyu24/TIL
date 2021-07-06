import pandas as pd
import matplotlib.pyplot as plt
import os
import matplotlib.font_manager as fm

font_name = fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
plt.rc('font', family=font_name)

def file_read():
    # 입력한 이름의 폴더 내 모든 파일 하나로 만들기
    filePath = './subway/'
    fileName = os.listdir(filePath)

    df1 = pd.DataFrame()

    # # 파일 불러와지는지 확인
    # df2 = pd.read_csv(filePath + fileName[0], encoding='cp949')
    # df2.head()

    # 여러 파일 불러오기
    for fn in fileName:
        # encoding 형태가 다른 파일들이 있는 경우, try except 구문을 이용
        try:
            df2 = pd.read_csv(filePath + fn, encoding='cp949')
        except:
            df2 = pd.read_csv(filePath + fn, encoding='utf-8')
        # 데이터를 한 개의 파일로 만들기
        df1 = pd.concat([df1, df2])

    return df1

def subway_sch(dfdata, subway_name):
    df2 = dfdata[dfdata['역명'] == subway_name]
    #df2.plot(x='사용일자', y='승차총승객수')
    #plt.show()

# 사용자 함수 호출 부분
df1 = file_read()

subway_name = input('조회역 입력:')
subway_sch(df1, subway_name)