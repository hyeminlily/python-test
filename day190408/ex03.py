import bitUtil
import numpy as np
import pandas as pd

df = bitUtil.getMovies()

# r_mean = df.pivot_table(values='rating', index='gender', aggfunc='mean')
# r_mean2 = r_mean.unstack()      # index → columns
#
# print(r_mean)
# print(r_mean2)
#
# r1 = df.pivot_table(values='rating', index=['gender', 'age'], aggfunc='mean')
# r2 = r1.unstack()
#
# print(r1)
# print(r2)
#
# r3 = r2.stack()         # columns → index
# print(r3)

# sum_mean = df.pivot_table(values='rating', index='age', columns='gender', aggfunc=['mean', 'sum'])
# sum_mean = df.pivot_table(values='rating', index='age', columns='gender', aggfunc=[np.mean, np.sum])
# print(sum_mean)

r1 = df.pivot_table(values='rating', index='age', columns='gender', aggfunc='mean')
r2 = df.pivot_table(values='rating', index='gender', columns='age', aggfunc='mean')

# r3 = pd.merge(r1, r2)       # 오류
r3 = pd.concat([r1, r2])
print(r3)

r4 = pd.concat([r1, r2], axis=1)
print(r4)

