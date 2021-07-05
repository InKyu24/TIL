import pandas as pd

df1 = pd.read_csv('./data/서울시 인구현황_구.txt', sep='\t', header=1)
# print(df1.head())

df1 = df1.iloc[:, [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, -1]]
# print(df1.head)

df1.drop(0, inplace=True)
col_name = ['년도', '자치구', '총인구', '총인구(남)', '총인구(여)', '내국인', '내국인(남)', '내국인(여)', '외국인', '외국인(남)', '외국인(여)', '65세 이상']

for i in range(len(col_name)):
    df1.rename(columns = {df1.columns[i]:col_name[i]}, inplace=True)
# print(df1.head(3))
# print(df1.dtypes)

# 현재 df1에서 필요한 것은 '년도', '자치구', '총인구', '내국인', '외국인', '65세 이상'
df2 = df1.iloc[:,[0, 1, 2, 5, 8, 11]]
# print(df2.dtypes)


df2 = df2[df2['내국인'] != '…']

# for row_i in df2.index:
#     df2.loc[row_i, "총인구"] = int(df2.loc[row_i, "총인구"].replace(',', ''))
#     df2.loc[row_i, "내국인"] = int(df2.loc[row_i, "내국인"].replace(',', '').replace('…','0'))
#     df2.loc[row_i, "외국인"] = int(df2.loc[row_i, "외국인"].replace(',', '').replace('…','0'))
#     df2.loc[row_i, "65세 이상"] = int(df2.loc[row_i, "65세 이상"].replace(',', '').replace('…','0'))


df2['총인구'] = [int(df2.loc[row_i, "총인구"].replace(',', '')) for row_i in df2.index]
df2['내국인'] = [int(df2.loc[row_i, "내국인"].replace(',', '').replace('…','0')) for row_i in df2.index]
df2['외국인'] = [int(df2.loc[row_i, "외국인"].replace(',', '').replace('…','0')) for row_i in df2.index]
df2['65세 이상'] = [int(df2.loc[row_i, "65세 이상"].replace(',', '').replace('…','0')) for row_i in df2.index]

print(df2.dtypes)
print(df2)