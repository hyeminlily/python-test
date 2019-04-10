import numpy as np
import pandas as pd
import xlrd

df = pd.read_excel("MLB World Series Champions_ 1903-2016.xlsx")
# print(df)
# print(df.head())
# print(df.columns)

# 팀별로 우승한 횟수 출력
win_cnt = df.pivot_table(values='Wins', index='Champion', aggfunc='count')
print(win_cnt)

# 우승팀들의 평균 승률 출력
win_ratio = df.pivot_table(values='WinRatio', index='Champion', aggfunc='mean')
print(win_ratio)

# 평균 승률이 높은 상위 5개 팀 출력
top5_mean = win_ratio.sort_values(by='WinRatio', ascending=False)
print(top5_mean.head())

# 2000년 이후의 데이터 중 평균 승률이 가장 높은 상위 5개 팀 출력
win_2000 = df[df['Year'] >= 2000]
mean_2000 = win_2000.pivot_table(values='WinRatio', index='Champion', aggfunc='mean')
top5_2000 = mean_2000.sort_values(by='WinRatio', ascending=False)
print(top5_2000.head())

# 100승 이상 승리한 팀 출력
win_100 = df[df['Wins'] >= 100]
only_win_100 = win_100['Champion'].unique()
print(len(only_win_100))
print(only_win_100)

# New York Yankees 팀이 처음 우승한 연도와 마지막으로 우승한 연도 출력
nyy_win = df[df['Champion'] == 'New York Yankees']
nyy_win_sort = nyy_win.sort_values(by='Year')

print(nyy_win_sort.iloc[0][0])
print(nyy_win_sort.iloc[-1][0])

print(nyy_win['Year'].min())
print(nyy_win['Year'].max())

# New York Yankees의 평균 승률 출력
nyy = df[df['Champion'] == 'New York Yankees']
nyy_ratio = nyy.pivot_table(values='WinRatio', index='Champion', aggfunc='mean')
print(nyy_ratio)

# 월드시리즈 열리지 않는 연도 출력
x = np.arange(int(df['Year'].min()), int(df['Year'].max()+1))
notYear = list(set(list(x)) - set(list(df['Year'])))
print(notYear)

a = np.arange(int(df['Year'].min()), int(df['Year'].max()+1))
b = np.array(df['Year'])
notYear_byT = np.setdiff1d(a, b)
print(notYear_byT)

# 최다 우승 Top5 출력, 순위가 동일한 여러 팀도 모두 출력
top5 = win_cnt.sort_values(by='Wins', ascending=False)
print(top5.head())