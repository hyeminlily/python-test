import numpy as np

a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 8, 10]

c = a + b
print(c)

a2 = np.array(a)
b2 = np.array(b)

c2 = a2 + b2        # vector operation
print(list(c2))

d = a2 ** b2        # vector operation
e = a2 > 5          # broadcasting
print(list(d))
print(list(e))

