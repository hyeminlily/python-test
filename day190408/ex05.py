import numpy as np
import pandas as pd
import bitUtil

df = bitUtil.getMovies()
cnt_500 = bitUtil.get_500_movie()

# print(cnt_500.index)        # title
# print(cnt_500.columns)      # rating

a = df.pivot_table(values='rating', index='title', columns='gender', fill_value=0, aggfunc='mean')
b = a.loc[cnt_500.index]
# print(b)
# print(len(cnt_500))

# b['diff'] = (b['F'] - b['M']).abs()
# c = b.sort_values(by='diff', ascending=False)
# print(c.head())

# b['mdiff'] = b['M'] - b['F']
# c = b.sort_values(by='mdiff', ascending=False)
# print(c.head())

# b['wdiff'] = b['F'] - b['M']
# c = b.sort_values(by='wdiff', ascending=False)
# print(c.head())


r = df.pivot_table(values='rating', index='title').sort_values(by='rating', ascending=False).h
print(r)