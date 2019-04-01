from sklearn import svm, metrics
import random, re

csv = []
with open('iris.csv', 'r', encoding='UTF-8') as rd:
    for line in rd:
        line = line.strip()
        cols = line.split(',')
        rn = lambda n : float(n) if re.match('^[0-9\.]+$', n) else n
        cols = list(map(rn, cols))
        csv.append(cols)

del csv[0]
random.shuffle(csv)

train_data = []
train_label = []
test_data = []
test_label = []

for i in range(len(csv)):
    data = csv[i][:4]
    label = csv[i][4]

    if i < int(len(csv) * 2 / 3):
        train_data.append(data)
        train_label.append(label)
    else:
        test_data.append(data)
        test_label.append(label)

clf = svm.SVC()
clf.fit(train_data, train_label)
pre = clf.predict(test_data)

ac_score = metrics.accuracy_score(test_label, pre)
print("정답률: ", ac_score)

real_data = [[7.7, 3.0, 6.1, 2.3]]
r2 = clf.predict(real_data)
print(r2)

