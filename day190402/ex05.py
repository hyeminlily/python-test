import numpy as np

# 파이썬 배열을 numpy 배열로 변경
a = [1, 2, 3, 4, 5, 6]
b = np.array(a)
print(b, ' / ', type(b))

# numpy 배열을 파이썬 배열로 변경
c = np.arange(6)
d = list(c)
print(d, ' / ', type(d))

