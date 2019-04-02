import numpy as np

a = ['160.7', '180.5', '145.8', '175.5', '170.7', '165.8']
b = np.array(a, dtype='float64')
c = b[b >= 170]

print(b)
print(c)

