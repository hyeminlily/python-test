import numpy as np

arr1 = [0, 1, 2, 3, 4]
print(arr1, type(arr1))

arr2 = list(range(0,5))
print(arr2, type(arr2))

arr3 = np.array(arr1)
print(arr3, type(arr3))

arr4 = np.arange(5)
print(arr4, type(arr4))

arr5 = list(arr4)
print(arr5, type(arr5))

