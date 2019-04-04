import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Data/scores.csv')
df.index = df['name']       # 학생의 이름을 key로 설정
del df['name']              # df에서 name column 삭제
# print(df)

# print(df)
# print(df.loc['henry'])
# print(df.loc['henry'].values)

# print(df.loc['andrew':'paul'])
# print(df.iloc[1:7])               # iloc()의 last index는 미포함

# print(df.loc[['adam', 'dan', 'walter']])

# print(df.loc[df.index[:5], 'kor'])
# print(df.loc[:'dan', 'kor'])
# print(df.iloc[:5]['kor'])
# print(df.iloc[:5, 1])       # fancy indexing

# print(df.loc[df.index[:5], ['kor', 'mat']])
# # print(df.iloc[:5][['kor', 'mat']])
# # print(df.iloc[:5, [1, 3]])

print(df.loc[['adam', 'dan', 'walter'], ['kor', 'eng', 'mat']])
print(df.loc[['adam', 'dan', 'walter']][['kor', 'eng', 'mat']])

names = [0, 4, 7]
print(df.iloc[names, 1:-1])

