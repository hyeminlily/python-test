import numpy as np

# a = np.arange(3)
# b = np.arange(3)
# c = a + b       # vector operation
#
# print(a)
# print(b)
# print(c)

# d = np.arange(3)
# e = np.arange(6)
# f = d + e
#
# print(f)    # ValueError!
# # operands could not be broadcast together with shapes (3,) (6,)

d = np.arange(3)
e = np.arange(6)
g = np.arange(3).reshape(-1, 3)
h = np.arange(6).reshape(-1, 3)
i = np.arange(3).reshape(3, -1)

# print(d + e)    # ValueError!
print(d + g)      # vector operation
print(d + h)      # broadcasting & vector operation
print(d + i)      # vector operation
print('-' * 20)

# print(e + g)    # ValueError!
# print(e + h)    # ValueError!
print(e + i)      # vector operation
print('-' * 20)

print(g + h)      # broadcasting & vector operation
print(g + i)      # broadcasting

# print(h + i)    # ValueError!

