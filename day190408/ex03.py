import bitUtil

df = bitUtil.getMovies()

r_mean = df.pivot_table(values='rating', index='gender', aggfunc='mean')
print(r_mean)

r_mean2 = r_mean.unstack()      # index → columns
print(r_mean2)

r1 = df.pivot_table(values='rating', index=['gender', 'age'], aggfunc='mean')
print(r1)

r2 = r1.unstack()
print(r2)

