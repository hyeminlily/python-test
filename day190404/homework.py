import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc, colors
import csv

rc('font', family=font_manager.FontProperties(fname='C:/WINDOWS/Fonts/H2GTRE.ttf').get_name())

f = open('gdp.txt', 'r', encoding='UTF-8')
f.readline()

names, money = [], []
list = csv.reader(f, delimiter=":")
for row in list:
    names.append(row[1])
    money.append(int(row[2].replace(',', '')))
f.close()

plt.bar(names[:10], money[:10], color='g')
plt.xticks(names[:10], names[:10], rotation='90')
plt.ylabel("GDP")
plt.title("2016년 GDP TOP10")
plt.show()

