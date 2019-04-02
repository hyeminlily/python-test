import numpy as np

# a = np.zeros(10, dtype=np.int32)
# b = np.ones(10, dtype=np.int32)
# c = np.full(10, 3)
#
# print(a)
# print(b)
# print(c)
# print('-' * 20)
#
# d = np.zeros([3, 4], dtype=np.int32)
# e = np.ones([3, 4], dtype=np.int32)
# f = np.full([3, 4], 100)
#
# print(d)
# print(e)
# print(f)
# print('-' * 20)
#
# g = np.arange(12).reshape(-1, 4)
# print(g)
# print(np.cumsum(g))     # 누적 합
# print(np.cumsum(g, axis=0))
# print(np.cumsum(g, axis=1))
# print('-' * 20)
#
# print(g[0])
# print(g[1:])
# print(g[0][0])          # 맨 첫번째 행의 첫번째 열
# print(g[-1][-1])        # 마지막 행의 마지막 열
# print('-' * 20)
#
# print(g[1][2])          # [행][열]
# print(g[1])             # 1번째 행 모두
# print(g[1:3])           # 1행부터 3-1행까지
# print('-' * 20)
#
# print(g[:])             # 모든 행
# print(g[:][1])          # 모든 행의 1열
# print(g[:][1:3])        # 모든 행의 1열부터 3-1열까지
# print('-' * 20)
#
# print(g[::])
# print(g[::-1])          # 거꾸로 출력
# print(g[::-1, ::-1])    # 모든 행과 열을 거꾸로 출력

# h = np.ones([5, 5], dtype=np.int32)
# h[1:4, 1:4] = 0
# print(h)

i = np.arange(12).reshape(-1, 4)

for j in range(4):
    print(i[:, j])

k = i.transpose()          # 행렬을 바꿔주는 함수 transpose()
print(k)

