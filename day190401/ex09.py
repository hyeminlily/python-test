import numpy as np

arr = [[1, 2, 3], [4, 5, 6]]

# Teacher ver.
a = np.array(arr).reshape(6)
b = list(a)

print(a)
print(b)

# My ver.
r1 = np.array(arr).flatten()
print(list(r1))

r2 = np.array(arr).ravel()
print(list(r2))

