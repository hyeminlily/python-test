import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = a + 1           # broadcasting
print(b)

c = np.array([4, 5, 6, 7, 8])
d = a + c           # vector operation
print(d)

# indexArray
e = np.array([1, 3, 0, 7, 9, 5, 6])
print(e[[0, 2, 5]])

# 60점 이상 합격한 학생의 이름 출력
name = ['홍길동', '강감찬', '이순신', '유관순', '김유신']
score = [80, 60, 100, 40, 70]

re_name = np.array(name)
re_score = np.array(score)
print(re_name[re_score >= 60])

