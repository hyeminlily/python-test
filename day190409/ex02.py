import numpy as np
import matplotlib.pyplot as plt

x = []
y = []
ry = 0

for i in range(100):
    rx = np.random.randint(-1, 2)
    ry = ry + rx
    x.append(rx)
    y.append(ry)

# plt.subplot(211)
# plt.plot(x)
# plt.subplot(212)
# plt.plot(y)
# plt.show()

# 좀 더 간단한 코딩으로
data1 = np.random.randint(-1, 2, 100)
data2 = np.cumsum(data1)

print(len(plt.style.available))

# with plt.style.context('ggplot'):
#     plt.subplot(211)
#     plt.plot(data1)
#     plt.subplot(212)
#     plt.plot(data2)
#     plt.show()

s = plt.style.available

for a in range(len(s)-1):
    with plt.style.context(s[a]):
        plt.subplot(5, 5, a+1)
        plt.plot(data2)
        plt.title(s[a])
plt.show()

