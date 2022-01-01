import pandas as pd

df = pd.read_csv("customer_churn.csv", header=0, index_col=0)
print(df.head())

# 去掉前三列
df = df.iloc[:, 3:]
print(df.head())
# one-hot编码
cat_var = ["international_plan", "voice_mail_plan", "churn"];
for var in cat_var:
    df[var] = df[var].map(lambda e: 1 if e == 'yes' else 0)
print(df.head())
y = df.iloc[:, -1]
X = df.iloc[:, :-1]

from sklearn import tree

clf = tree.DecisionTreeClassifier(max_depth=5)
clf.fit(X, y)
tree.export_graphviz(clf, out_file='tree.dot')

import numpy as np

acc = np.sum(y == clf.predict(X)) / len(y)
print(acc)

from sklearn.linear_model import LogisticRegression

clf2 = LogisticRegression()
clf2.fit(X, y)
acc = np.sum(y == clf2.predict(X)) / len(y)
print(acc)

from sklearn.svm import SVC

model = SVC()
model.fit(X, y)
acc = np.sum(y == model.predict(X)) / len(y)
print(acc)
