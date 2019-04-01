import numpy as np

a = np.arange(6)
b = a.reshape(2,3)      # 차원을 변경하는 함수 reshape()

print(a)
print(b)
print(a.shape)
print(b.shape)

c = np.arange(7)
d = c.reshape(2,3)

print(d)      # 차원을 변경하기 위해선 데이터의 수가 맞아야 함!

