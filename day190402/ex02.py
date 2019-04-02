import numpy as np

a = [1, 2, 3, 4, 5]
b = [1.0, 2.0, 3.0, 4.0, 5.0]
c = ['a', 'b', 'c', 'd', 'e', 'hello', '우리나라 대한민국', '이순신 우리나라 대한민국 우리나라 대한민국 우리나라']
d = ['hello', 'java', 'python', 'oracle', 'mongo']
e = ['이필숙', '정연미', '박민서', '김경희', '이혜민']

arr1 = np.array(a)
arr2 = np.array(b)
arr3 = np.array(c)
arr4 = np.array(d)
arr5 = np.array(e)

print(arr1.dtype)
print(arr2.dtype)
print(arr3.dtype)       # 글자수가 증가할수록 ex. <U9 → <U28로 증가
print(arr4.dtype)
print(arr5.dtype)

