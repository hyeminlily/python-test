import numpy as np

# a = [1, 2, 3, 4, 5, 6]
# b = a + 1       # 불가능!
# print(b)

c = [1, 2, 3, 4, 5]
d = np.array(c)
e = d + 1         # broadcasting: 배열의 숫자만큼 연산을 하는 것을 지칭
print(e)

