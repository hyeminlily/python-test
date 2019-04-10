import numpy as np
import pandas as pd

df = pd.read_csv("baseball.txt", sep=',')
# print(df)
print(df.head())


# 팀별로 우승한 횟수 출력
# win_cnt = df.pivot_table(values='Wins', index='Champion', aggfunc='count')
# print(win_cnt)
#

# 우승팀들의 평균 승률 출력

# 100승 이상 승리한 팀 출력

# New York Yankees의 평균 승률 출력

# 최다 우승 Top5 출력

# 월드시리즈 열리지 않는 연도 출력