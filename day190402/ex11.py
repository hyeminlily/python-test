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

# # My ver.
# b = np.ones([5, 5], dtype=np.int32)
# b[[1, 2, 3], 1:4] = 0
# print(b)
#
# # Teacher ver.
# c = np.zeros([5, 5], dtype='int32')
# c[:, [0, -1]] = 1
# c[[0, -1], :] = 1
# print(c)

# # My ver.
# d = np.zeros([5, 5], dtype=np.int32)
# d[[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]] = 1
# print(d)
#
# g = np.eye(5, 5, dtype='int32')
# print(g)
#
# # My ver.
# e = [1, 3, 0, 3, 1]
# f = np.zeros([len(e), max(e)+1], dtype=np.int32)
#
# for ef in range(len(e)):
#     f[ef, e[ef]] = 1
# print(f)
#
# # Teacher ver.
# f[[range(len(e))], e] = 1
# print(f)
#
# i = np.eye(len(e), np.max(e)+1, dtype='int32')[e]
# print(i)

# h = [4, 3, 1, 5, 2]
# arr1 = np.array(h)
# arr1.sort()
# print(arr1)
#
# # argsort(): 정렬 후 index 순서대로 배열을 생성
# j = np.argsort(arr1)      # [2, 4, 1, 0, 3] = index 위치!
# print(j)
#
name = ['홍길동', '강감찬', '이순신', '유관순', '장영실']
score = [80, 90, 100, 70, 95]

arr_name = np.array(name)
arr_score = np.array(score)

k = np.argsort(arr_score)[::-1]     # 내림차순으로 index를 반환
# print(arr_name[k])

# My ver.
print(arr_name[k][0])

# Teacher ver.
l = np.argmax(arr_score)
print(arr_name[l])

# 동점 처리
name = np.array(['임꺽정', '홍길동', '강감찬', '이순신', '유관순', '장영실', '주시경'])
score = np.array([100, 80, 90, 100, 70, 95, 100], dtype=np.int32)
max = np.argwhere(score == np.amax(score))
print(name[max].ravel())

