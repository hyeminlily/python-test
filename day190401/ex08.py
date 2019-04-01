import numpy as np

a = np.arange(0, 6, 1)
b = a.reshape(2, 3)

print(a)
print(b)

c = [[0, 1, 2],[3, 4, 5]]
d = np.array(c)

print(c)
print(d)

e = [0, 1, 2, 3, 4, 5]
f = np.array(a).reshape(2,3)

print(e)
print(f)

g = np.arange(6).reshape(2, -1)
h = np.arange(6).reshape(-1, 3)

print(g)
print(h)

