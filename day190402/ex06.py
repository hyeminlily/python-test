import numpy as np

a = np.arange(3)
print(a)
print(a + 1)      # broadcasting
print(a > 1)      # broadcasting
print(a[a > 1])   # []안을 만족(True)하는 결과값만 출력

# 같은 표현으로 만드는 2차원 배열
b = np.arange(6).reshape(-1, 3)
c = np.arange(6).reshape(2, -1)
d = np.arange(6).reshape(2, 3)

print(b)
print(c)
print(d)

print(b + 1)
print(b > 1)      # broadcasting: b의 요소만큼 비교하여 True, False 반환
print(b[b > 1])   # broadcasting을 만족(True)하는 결과값만 출력

