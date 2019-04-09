from sklearn import preprocessing
import numpy as np

# 데이터의 범위를 축소해야할 때 값의 범위가 작은 것이 큰 것보다 기계학습에 효율적
# 문자 < 숫자 데이터, 이진화된 숫자의 범위가 기계 학습에 훨씬 효율적

x = [[1, -1, 3], [2, 0, 0], [0, 1, -1]]
binarizer = preprocessing.Binarizer()
print(binarizer)
print(type(binarizer))

r = binarizer.fit(x)
b = r.transform(x)
print(b)

