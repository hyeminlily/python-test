import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
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
# print(age_mean)

age_gender_mean = df.pivot_table(values='rating', index='age', columns='gender', aggfunc='mean')
# print(age_gender_mean)

gender_age_mean = df.pivot_table(values='rating', index='gender', columns='age', aggfunc='mean')
#print(gender_age_mean)

age_gender_mean.index = ["under 18", "18-24", "25-34", "35-44", "45-49", "50-55", "56+"]
# age_gender_mean.plot(kind="bar")    # default는 선 그래프!
# plt.show()

r_mean = df.pivot_table(values='rating', index='gender', columns='age', fill_value=0, aggfunc='mean')
print(r_mean)

