import pandas as pd
import matplotlib.pyplot as plt
import os
import matplotlib.font_manager as fm
import csv

font_name = fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
plt.rc('font', family=font_name)


def Csv_reset(fn):
    f = open('./subway/'+fn, encoding='utf-8')
    data = csv.reader(f)
    # "사용일자"', '노선명', '역명', '승차총승객수', '하차총승객수', '등록일자'

    next(data)
    data_lst = []
    for row in data:
        data_lst.append(row[:6])

    df = pd.DataFrame(data_lst, columns=['사용일자', '노선명', '역명', '승차총승객수', '하차총승객수', '등록일자'])
    df.to_csv('./subway/'+fn, encoding='cp949', index=False)
    f.close()


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
            Csv_reset(fn)
            df2 = pd.read_csv(filePath + fn, encoding='cp949')
        # 데이터를 한 개의 파일로 만들기
        df1 = pd.concat([df1, df2])

    df1 = df1.reset_index(drop=True)

    return df1

def subway_sch(dfdata, subway_name):
    df2 = dfdata[dfdata['역명'] == subway_name]
    print(df2)
    df2 = df2.astype({'승차총승객수' : 'int64', '사용일자' : 'str'})
    df2 = df2.groupby('사용일자')[['승차총승객수', '하차총승객수']].sum()
    print(df2)
    df2.plot()
    plt.show()

# 사용자 함수 호출 부분
df1 = file_read()
subway_name = input('조회역 입력:')
subway_sch(df1, subway_name)