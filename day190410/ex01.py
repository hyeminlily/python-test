import numpy as np
import pandas as pd
import xlrd

df = pd.read_excel("MLB World Series Champions_ 1903-2016.xlsx")
# print(df)
# print(df.head())
# print(df.columns)

# # 팀별로 우승한 횟수 출력
# win_cnt = df.pivot_table(values='Wins', index='Champion', aggfunc='count')
# print(win_cnt)

# 우승팀들의 평균 승률 출력
win_ratio = df.pivot_table(values='WinRatio', index='Champion', aggfunc='mean')
print(win_ratio)

# 평균 승률이 높은 상위 5개 팀 출력
# top5_mean = win_ratio.sort_values(by='WinRatio', ascending=False)
# print(top5_mean.head())

# 2000년 이후의 데이터 중 평균 승률이 가장 높은 상위 5개 팀 출력

# 100승 이상 승리한 팀 출력
# win_100 = df[df['Wins'] >= 100]
# print(win_100)

# New York Yankees의 평균 승률 출력
# nyy = df[df['Champion'] == 'New York Yankees']
# nyy_ratio = nyy.pivot_table(values='WinRatio', index='Champion', aggfunc='mean')
# print(nyy_ratio)

# 최다 우승 Top5 출력
# top5 = win_cnt.sort_values(by='Wins', ascending=False)
# print(top5.head())

# 월드시리즈 열리지 않는 연도 출력
