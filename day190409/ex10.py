from sklearn import preprocessing
import numpy as np

# 문자를 이진화 배열로 바꿈 → LabelBinarizer

x = ['yes', 'no', 'yes']
lb = preprocessing.LabelBinarizer()
bn = lb.fit_transform(x)
print(bn)

x2 = ['yes', 'no', 'yes', 'cancel']
lb2 = preprocessing.LabelBinarizer()
bn2 = lb2.fit_transform(x2)
print(bn2)

r = np.array([[0, 0, 1]])
s = lb2.inverse_transform(r)
print(s)

x3 = ['paris', 'tokyo', 'london', 'paris']
lb3 = preprocessing.LabelBinarizer()
b = lb3.fit_transform(x3)
print(b)

r2 = np.array([[1, 0, 0]])
result = lb3.inverse_transform(r2)
print(result)

