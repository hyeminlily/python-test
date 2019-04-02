import numpy as np

a = np.zeros(3, dtype='int32')
print(a)

b = np.zeros([3,4], dtype='int32')
print(b)

c = np.ones(10)
print(c)
print('-' * 20)

d = np.arange(12).reshape(-1, 4)
print(d)
print(np.sum(d))
print(np.sum(d, axis=0))
print(np.sum(d, axis=1))
print('-' * 20)

print(np.max(d))
print(np.max(d, axis=0))
print(np.max(d, axis=1))
print('-' * 20)

e = np.zeros_like(d)
f = np.zeros(d.shape, dtype='int32')
print(e)
print(f)

