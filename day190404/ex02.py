import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv("Data/scores.csv")
# print(df)
# print(type(df))

# df = pd.DataFrame([[1, 2, 3], [4, 5, 6]])
# print(df)
# print(type(df))

df = pd.read_csv("Data/scores.csv")
# print(df.index)             # key(index) 확인
# print(df.columns)           # column명 확인
# print('-' * 20)

# print(df.values)
# print(type(df.values))
# print('-' * 20)
#
# print(df['kor'])
# print(df[2])                # 불가능

# Pandas의 DataFrame에서 행에 접근하려면: loc() 또는 iloc() 함수 이용
# 키값 부여하지 않은 상태에서 행에 접근하려면 index로 접근함: loc()과 ilod() 차이가 없음

print(df)
print(df.loc[2])
print(df.iloc[2])

