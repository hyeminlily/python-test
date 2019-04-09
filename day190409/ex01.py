import numpy as np
import random
import matplotlib.pyplot as plt

# 0 ~ 10 사이의 난수 1개 발생
x = np.random.randint(10)
print(x)

x2 = random.randint(0, 10)
print(x2)

# 100 ~ 1000 사이의 난수 5개
x3 = np.random.randint(100, 1000, 5)
print(x3)

# 이미 있는 데이터들 중에서 임의로 하나 선택 → choice
data = [9, 7, 2, 1, 100, 3]
x4 = random.choice(data)
print(x4)

# 이미 있는 데이터들을 섞어서 임의로 여러개 선택 → sample (중복X)
x5 = random.sample(data, 3)
print(x5)

# 0 ~ 1 사이의 실수인 난수 1개 발생
x6 = np.random.rand()
print(x6)

# 0 ~ 1 사이의 실수인 난수 10개 발생
x7 = np.random.rand(10)
print(x7)

# 데이터의 흩어진 정도를 점을 찍어 나타내는 그래프 → scatter
x8 = np.random.rand(100)
y = np.random.rand(100)
plt.scatter(x8, y, c='r')
plt.show()

