import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# # python 기본 배열을 Pandas의 1차원 배열로 변경
# a = [1, 2, 3, 4, 5]
# arr = pd.Series(a)
#
# print(a)
# print(arr)
# print(type(a))
# print(type(arr))

# # Pandas의 1차원 배열인 Series를 python 배열로 변경
# arr = pd.Series(['홍길동', '강감찬', '이순신', '유관순'])
# name = list(arr)
#
# print(type(name))
# print(type(arr))

# # Series 만들때 2차원 배열을 매개변수로 준다면 어떻게 되는지 확인
# arr = pd.Series([[1, 2, 3], [4, 5, 6]])
# print(arr)
# print(arr[0])
# print(type(arr[0]))
# print(arr[0][1])

# arr = pd.Series([['홍길동', '강감찬', '이순신', '유관순'], ['이순신', '유관순']])
# print(arr)

# Series는 자바의 map과 같이 key, value가 한쌍으로 이루어지는 자료 구조를 표현하기에 적합함
# key를 부여하지 않으면 차례대로 index가 부여됨. 필요하다면 key를 부여할 수 있음.

# a = pd.Series([5, 9, 3, 7, 6])
# print(a)
# print(a.values)
# print(type(a.values))

# # 각각의 값에 어떤 값을 의미하는지 key를 부여할 수 있음 / 생략 시 차례로 index 부여됨
# a = pd.Series([5, 9, 3, 7, 6], index=['이필숙', '정연미', '김경희', '박민서', '이혜민'])
#
# print(a)
# print(a['이혜민'])
# print(a[3])
# print(a.index)

# # Series의 키값으로 모두 뽑아온 후 key의 개수만큼 반복 수행하여 각 요소의 key의 value를 출력
# a = pd.Series([5, 9, 3, 7, 6], index=['이필숙', '정연미', '김경희', '박민서', '이혜민'])
# keys = a.index
# for key in keys:
#     print(key, a[key])

# Pandas의 Series는 python 배열을 갖고 key값을 부여해 보다 직관적 접근이 가능
# python dictionary로 Series 생성이 가능한지 확인
a = {'이필숙': 10, '정연미': 10, '김경희': 8, '박민서': 9, '이혜민': 7}
s = pd.Series(a)

print(s)

