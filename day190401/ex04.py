def returnName(list):
    import pandas as pd
    from sklearn import svm, metrics
    from sklearn.model_selection import train_test_split

    csv = pd.read_csv('iris.csv')
    csv_data = csv[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
    csv_label = csv["Name"]

    train_data, test_data, train_label, test_label = train_test_split(csv_data, csv_label)

    clf = svm.SVC()
    clf.fit(train_data, train_label)
    pre = clf.predict(test_data)
    ac_score = metrics.accuracy_score(test_label, pre)

    new_list = []
    new_list.append(list)
    pre2 = clf.predict(new_list)
    name = pre2[0]

    return name, ac_score
