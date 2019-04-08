import numpy as np
import pandas as pd
import bitUtil

df = bitUtil.getMovies()
# print(df.head())

# help(pd.DataFrame.pivot_table)
# pivot_table(self, values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True, margins_name='All')

gender_mean = df.pivot_table(values='rating', index='gender')   # index가 group by 역할!
gender_mean2 = df.pivot_table(values='rating', index='gender', aggfunc='mean')
gender_sum = df.pivot_table(values='rating', index='gender', aggfunc='sum')
gender_max = df.pivot_table(values='rating', index='gender', aggfunc='max')
gender_min = df.pivot_table(values='rating', index='gender', aggfunc='min')

# print(gender_mean)
# print(gender_mean2)
# print(gender_sum)
# print(gender_max)
# print(gender_min)

age_mean = df.pivot_table(values='rating', index='age')
print(age_mean)

