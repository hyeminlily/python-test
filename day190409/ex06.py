from sklearn import datasets, svm, neighbors, model_selection

# sklearn의 dataset이 제공하는 iris 데이터 읽음
iris = datasets.load_iris()

print(iris)             # 'data'와 'target'으로 데이터를 나누어 제공함
print(type(iris))

# 문제와 답을 훈련용 / 테스트용 데이터로 분리
train_x, test_x, train_y, test_y = model_selection.train_test_split(iris['data'], iris['target'])
print(len(train_x), len(test_x))        # 약 75% 훈련 / 약 25% 테스트
print(len(train_y), len(test_y))

# 학습을 위한 neighbors 객체 생성
knn = neighbors.KNeighborsClassifier()
knn.fit(train_x, train_y)

r = knn.predict(test_x)
print(r == test_y)

label = iris['target_names']
x = [[4.6, 3.6, 1, 0.2]]
r = knn.predict(x)
rs = label[r]
print(rs)

