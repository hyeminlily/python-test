import numpy as np
import pandas as pd
from sklearn import model_selection, linear_model

def check(list):
    names = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship',
             'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']
    df = pd.read_csv("adult.data.txt", header=None, names=names)
    df = df[['age', 'workclass', 'education', 'occupation', 'sex', 'race', 'hours-per-week', 'income']]

    ndf = pd.get_dummies(df)
    x = ndf.iloc[:, :-2]
    y = ndf.iloc[:, -1]

    train_x, test_x, train_y, test_y = model_selection.train_test_split(x, y)
    lr = linear_model.LogisticRegression()
    lr.fit(train_x, train_y)

    add = pd.DataFrame(list, columns=['age', 'workclass', 'education', 'occupation', 'sex', 'race', 'hours-per-week'])
    add_df = df.append(add, ignore_index=True)

    one_hot = pd.get_dummies(add_df)
    pred_x = np.array(one_hot.iloc[-1, :-2]).reshape(1, -1)
    pred_y = lr.predict(pred_x)
    print(pred_y)
    return pred_y

