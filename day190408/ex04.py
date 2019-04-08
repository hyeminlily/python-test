import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import bitUtil

df = bitUtil.getMovies()

count = df.pivot_table(values='rating', index='title', aggfunc='count')
# print(count)

# 평가 건수가 500개 이상인 영화 제목을 출력
print(count['rating'] >= 500)     # boolean 값을 반환

title_500 = count[count['rating'] >= 500]
print(title_500)

# 내림차순 정렬
title_500_sort = title_500.sort_values(by='rating', ascending=False)
print(title_500_sort)

