import numpy as np

# int 자료형의 배열을 float 자료형의 배열로 생성 가능
# 단, 바꾸려는 자료형으로 변경이 가능해야 함!

a = [0, 1, 2, 3, 4, 5]
b = np.array(a, dtype='float64')
print(b)

c = [0, 1, 2, 'hi', 3, 4]
d = np.array(c, dtype='float64')
print(d)    # 오류 발생!

