import numpy as np

# a = np.arange(12).reshape(-1, 4)
# print(a)
# print('-' * 20)
#
# print(a > 5)
# print(a[a > 5])             # bool Array
# print('-' * 20)
#
# print(a[0, 1])              # 0번째 행의 1번째 열
# print(a[0])                 # 0번째 행
# print(a[[0, 1]])            # 0번째 행, 1번째 행 // index Array
# print(a[[1, 0]])            # 1번째 행, 0번째 행 // index Array
# print('-' * 20)
#
# print(a[[1, 0], [0, 1]])    # 행, 행, 열, 열 순서!

# My ver.
b = np.ones([5, 5], dtype=np.int32)
b[[1, 2, 3], 1:4] = 0
print(b)

# Teacher ver.
c = np.zeros([5, 5], dtype='int32')
c[:, [0, -1]] = 1
c[[0, -1], :] = 1
print(c)

