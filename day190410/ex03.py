import numpy as np
import pandas as pd

# pandas의 get_dummies는 만약 1차원 배열을 매개변수로 받으면 숫자 or 문자든 one-hot 인코딩을 실행
# BUT DataFrame을 매개변수로 받게 되면 기본적으로 숫자 데이터는 제외하고 one-hot 인코딩 실행
# 만약 숫자도 포함하여 hot-encoding을 실행하려면 DataFrame의 숫자 속성을 문자로 변경한 후 실행해야 함.
# ex) DataFrame['속성명'] = DataFrame['속성명'].astype(str)

member = pd.read_csv("member.dat")
member['age'] = member['age'].astype(str)

b_member = pd.get_dummies(member)
print(b_member)

# adult.data.txt를 읽어들여 연봉을 결정하는 중요한 7개의 속성으로만 추려내고,
# 숫자 속성을 제외하고 one-hot Encoding으로 변경하여 생성된 컬럼을 확인함
# 7개의 속성 = 나이, 직업 분류, 학력, 성별, 주당 일하는 시간, 직업, 수입