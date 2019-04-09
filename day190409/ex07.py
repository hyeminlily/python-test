from sklearn import preprocessing
import numpy as np

# 때에 따라 존재하지 않는 임의의 특징값(feature)을 만들어야 하는 경우가 있는데,
# 이 때, sklearn의 preprossing을 이용하여 임의의 특징값을 생성함

x = [[0, 1], [3, 5]]
x2 = preprocessing.add_dummy_feature(x)     # value 생략시 각 행마다 1을 추가함
print(x2)