import numpy as np
import pandas as pd
from sklearn import model_selection, linear_model

# feature가 그것을 결정하는 가장 중요한 요인인가를 파악하는 것이 중요함
# 그것을 결정하는데 필요한 데이터를 수집하는 것이 필요함

names = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship',
         'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']
df = pd.read_csv("adult.data.txt", header=None, names=names)
df = df[['age', 'workclass', 'education', 'occupation', 'sex', 'race', 'hours-per-week', 'income']]

new_df = pd.get_dummies(df)
x = new_df.iloc[:, :-2]
y = new_df.iloc[:, -1]

train_x, test_x, train_y, test_y = model_selection.train_test_split(x, y)
lr = linear_model.LogisticRegression()
lr.fit(train_x, train_y)

# 알고자 하는 데이터를 훈련시킨 feature의 수와 동일하게 하기 위해 원본 데이터의 맨 마지막에 추가시키고 one-hot Encoding 실행
n = pd.DataFrame([[47, ' Private', ' Prof-school', ' Prof-specialty', ' Female', ' White', 60, ' <=50K']],
                 columns=['age', 'workclass', 'education', 'occupation', 'sex', 'race', 'hours-per-week', 'income'])
df2 = df.append(n, ignore_index=True)

one_hot = pd.get_dummies(df2)
print(len(one_hot.columns))
print(len(new_df.columns))

pred_x = np.array(one_hot.iloc[-1, :-2]).reshape(1, -1)
pred_y = lr.predict(pred_x)
print(pred_y)

