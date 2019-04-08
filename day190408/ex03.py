import bitUtil

df = bitUtil.getMovies()

r_mean = df.pivot_table(values='rating', index='gender', aggfunc='mean')
r_mean2 = r_mean.unstack()      # index → columns

# print(r_mean)
# print(r_mean2)

r1 = df.pivot_table(values='rating', index=['gender', 'age'], aggfunc='mean')
r2 = r1.unstack()

# print(r1)
# print(r2)

r3 = r2.stack()
print(r3)

