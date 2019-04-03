import matplotlib.pyplot as plt
import numpy as np

qty = np.array([60, 100, 30, 40, 150])
plt.plot(qty)
plt.show()

# 수박에 대한 판매량의 정보를 차트로 나타내시오.
fruits = np.array([[1000, 1100, 1000, 900, 1500], [80, 80, 100, 50, 40], [60, 70, 40, 50, 60]])
plt.plot(fruits[1], "ro")
plt.show()

# 수박의 판매량에 대하여 평균 판매량과의 차이를 차트로 나타내시오.
avg = np.abs(fruits[1] - np.mean(fruits[1]))        # (판매량 - 평균 판매량)의 절대값 계산
plt.plot(fruits[1], avg, "bo")
plt.xlim(0, 10)
plt.ylim(0, 100)
plt.show()

height = np.array([170, 180, 160, 185, 167])
weight = np.array([80, 100, 65, 105, 73])

plt.plot(weight, height, "ro")
plt.xlim(50, 150)
plt.ylim(100, 200)
plt.show()

x = np.arange(-10, 11)
x2 = x ** 2
plt.plot(x, x2)
plt.show()

t1 = np.arange(0, 5, 0.1)
t2 = np.arange(0, 5, 0.02)

plt.figure(1)
plt.plot(t1, "ro")

plt.figure(2)
plt.plot(t2, "bo")

plt.show()

t1 = np.arange(0, 5, 0.1)
t2 = np.arange(0, 5, 0.02)

plt.subplot(211)    # 2행 1열 1번째
plt.plot(t1)

plt.subplot(212)    # 2행 1열 2번째
plt.plot(t2, "b")

plt.show()

a = np.arange(0.01, 2, 0.01)

plt.subplot(121)
plt.plot(np.exp(a), "y")

plt.subplot(122)
plt.plot(np.log(a), "b")

plt.show()

import matplotlib.font_manager as fm

font_list = fm.findSystemFonts(fontpaths=None, fontext='ttf')
path = 'C:/WINDOWS/Fonts/아리따M.ttf'
fontprop = fm.FontProperties(fname=path, size=18)

qty = [10, 20, 10, 30, 50]
plt.bar(range(5), qty, 0.4)
plt.title("요일별 과일판매량", fontproperties=fontprop)
plt.show()

import matplotlib.font_manager as fm

qty = [10, 20, 10, 30, 50]
plt.bar(range(5), qty, 0.4)
plt.title("요일별 과일판매량", fontproperties=fm.FontProperties(fname='C:/WINDOWS/Fonts/아리따M.ttf', size=18))
plt.show()

