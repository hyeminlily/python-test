from sklearn import preprocessing
import numpy as np

# 수집한 데이터의 결측치 처리 → imputer

x = [[1, 2], [np.nan, 3], [7, 6]]

imp = preprocessing.Imputer(missing_values="NaN", strategy="mean")
x2 = imp.fit(x).transform(x)
print(x2)

help(preprocessing.Imputer)

