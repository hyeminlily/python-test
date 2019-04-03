import numpy as np

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = np.array(a)

print(a[-1])
print(b[-1])

# print(a[0, 3, 4])     → 파이썬 배열에서는 indexArray 사용 불가능!
print(b[[0, 3, 4]])

# print(a[False, True, False, False, True, False, False, False, False, False])
print(b[[False, True, False, False, True, False, False, False, False, False]])

print(a[0:10:2])        # step 부여가 가능!
print(b[0:10:2])

print(a[::2])
print(b[::2])

print(a[::-2])
print(b[::-2])
print('-' * 20)

# 2차원 배열에서의 slicing
c = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24]]
d = np.array(c)
e = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(c[1][2])
print(d[1][2])
print(e[8])

print(c[1:4])
print(d[1:4])
print(e[1:4])

print(c[:])
print(d[:])
print(e[:])
print('-' * 20)

# print(c[1, 2])     → python array는 fancy indexing 사용 불가!
print(d[1, 2])

# fancy indexing: 배열명[[index array], [index array]] / 배열명[[boolean array], [boolean array]]
print(d[1, ])
print(d[1:3, ])
print(d[[1, 2], ])
print('-' * 20)

# 연습
c = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24]
]
d = np.array(c)

print(d[:, 1:5])
print(d[:, [1, 3, 5]])
print(d[::2])
print(d[::2, 1:5])
print('-' * 20)

rows = [1, 1, 2, 2, 3, 3, 3]
cols = [2, 5, 1, 4, 1, 3, 4]
print(d[rows, cols])

one = np.ones([5, 5], dtype=np.int32)
one[1:-1, 1:-1] = 0
print(one)

zero = np.zeros([5, 5], dtype=np.int32)
zero[:, [0, -1]] = 1
zero[[0, -1], :] = 1
print(zero)

arr = np.zeros([8, 8], dtype=np.int32)
r = [0, 1, 2, 2, 3, 3, 4, 5, 5]
c = [5, 5, 4, 5, 3, 4, 3, 2, 3]
arr[r, c] = 1
print(arr)

# 판매량이 높은 순으로 출력
item = ['사과', '딸기', '수박', '메론', '바나나']
qty = [200, 1000, 10, 15, 300]

i = np.array(item)
q = np.array(qty)

s = np.argsort(q)[::-1]
print(i[s])

fruits = np.array([[1000, 1100, 1000, 900, 1500], [80, 80, 100, 50, 40], [60, 70, 40, 50, 60]])
print(np.sum(fruits, axis=0))   # 열의 합
print(np.sum(fruits, axis=1))   # 행의 합

