# 복습
import numpy as np

a = np.zeros(10, dtype="int32")
b = np.ones(5, dtype=np.int32)
c = np.full(7, 100)

print(a)
print(b)
print(c)
print('-' * 20)

d = np.zeros([2, 3], dtype='int32')
e = np.ones([5, 5], dtype='int32')
f = np.full([5, 5], 100)

print(d)
print(e)
print(f)
print('-' * 20)

g = np.arange(10)
h = np.arange(1, 11)
i = np.arange(1, 11, 2)
j = np.arange(10, -10, -1)

print(g)
print(h)
print(i)
print(j)
print('-' * 20)

k = [1, 2, 3, 4, 5]
l = np.array(k)

print(k)
print(l)
print(k[2])
print(l[2])
print('-' * 20)

m = np.arange(10, -10, -1)
n = list(m)

print(m)
print(n)
print(type(m))
print(type(n))
print('-' * 20)

o = np.array([1, 2, 3, 4, 5])
p = np.array([10.5, 2.7, 3.5])
q = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(o)
print(p)

print(type(o))
print(type(p))
print(o.dtype)
print(p.dtype)

print(o.ndim)
print(p.ndim)
print(q.ndim)

print(o.shape)
print(p.shape)
print(q.shape)
print('-' * 20)

r = np.array([[1, 2, 3], [4, 5, 6]])
row, col = r.shape
s = r.reshape([col, row])
print(r)
print(s)