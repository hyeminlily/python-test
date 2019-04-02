import numpy as np

a = [0, 1, 2, 3, 4, 5]

b = np.arange(5)
c = np.array(a)

print(b)
print(type(b))
print(c)
print(type(c))

arr = np.array(a)
print(arr)

arr2 = arr.reshape(2,3)
print(arr2)

print(arr.shape)    # 차수를 확인하는 shape
print(arr2.shape)

print(arr.ndim)     # 몇 차원인지 확인하는 ndim
print(arr2.ndim)

print(arr.dtype)    # 배열의 자료형 확인하는 dtype
print(arr2.dtype)

