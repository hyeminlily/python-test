# one-hot Encoding: 기계 학습을 위해서는 값의 범위가 큰 것보다는 작은 것이 더 효율적. (0과 1로 만듦)
# function: 1) get_dummies (1,2차원 모두 및 column 이름 생성) (by pandas)
#              → 만약 일차원 배열인 경우) 숫자 or 문자든 one-hot Encoding을 만들어 줌.
#              → But 2차원(DataFrame)일 경우) feature(기본적으로 숫자)는 one-hot Encoding에서 제외됨
#                 만약 숫자의 feature도 one-hot Encoding 원하면 형변환 먼저 수행
#                 DataFrame[속성명] = str(DataFrame[속성명])
#           2) preprocess - binarizer (2차원 배열) & labelBinarizer (1차원 배열 및 문자) (by sklearn)

import numpy as np
import pandas as pd
from sklearn import model_selection, linear_model

# adult.data.txt를 읽어들여 연봉을 결정하는 중요한 7개의 속성으로만 추려내고,
# 숫자 속성을 제외하고 one-hot Encoding으로 변경하여 생성된 컬럼을 확인함
# 7개의 속성 = 나이, 직업 분류, 학력, 성별, 주당 일하는 시간, 직업, 수입

names = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship',
         'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']
df = pd.read_csv("adult.data.txt", header=None, names=names)
df = df[['age', 'workclass', 'education', 'occupation', 'sex', 'hours-per-week', 'income']]


# df를 one-hot Encoding하면 생성될 feature의 개수
print(len(df['workclass'].unique()))

# workclass의 값의 종류의 수
new_df = pd.get_dummies(df)
# print(new_df.head())
# print(new_df.columns)

# 문제와 답을 분리
x = new_df.iloc[:, :44]
y = new_df.iloc[:, -1]
# print(x.shape)    # 2차원
# print(y.shape)    # 1차원

# 문제와 답을 훈련에 참여시킬 데이터와 검증을 위한 데이터로 분리
train_x, test_x, train_y, test_y = model_selection.train_test_split(x, y)

lr = linear_model.LogisticRegression()
lr.fit(train_x, train_y)
r = lr.predict(test_x)

result = r == test_y        # 예측 결과와 검증을 위한 데이터(답)을 비교
a = result.values           # 결과가 Series이기 때문에 value만 추출
b = a[a == True]            # True만 추출

print("정답률 : ", len(b) / len(test_y) * 100)

# 정답률 계산 → LogisticRegression()의 score()
c = lr.score(test_x, test_y)
print(c)
