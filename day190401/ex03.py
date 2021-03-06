import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

csv = pd.read_csv('iris.csv')
csv_data = csv[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
csv_label = csv["Name"]

# print(csv_data, csv_label)

train_data, test_data, train_label, test_label = train_test_split(csv_data, csv_label)

clf = svm.SVC()
clf.fit(train_data, train_label)
pre = clf.predict(test_data)

ac_score = metrics.accuracy_score(test_label, pre)
print("정답률 : ", ac_score)

real_data = [[5.8, 2.7, 4.1, 1.0]]
pre2 = clf.predict(real_data)
print(pre2)

