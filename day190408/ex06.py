import numpy as np
import pandas as pd

scores = pd.read_csv("Data/scores.csv")

# print(scores.mean(axis=1))
# print(scores[['kor', 'eng', 'mat', 'bio']].mean(axis=1))

# avg를 계산하여 scores에 추가
scores['avg'] = scores[['kor', 'eng', 'mat', 'bio']].mean(axis=1)
print(scores)

