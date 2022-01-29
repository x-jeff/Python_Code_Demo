from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

iris = load_iris()
clf = LogisticRegression()
clf.fit(iris.data, iris.target)

predicted = clf.predict(iris.data)
acc = sum(iris.target == predicted) / len(iris.target)
print("acc = ", acc)

from sklearn.metrics import accuracy_score

acc = accuracy_score(iris.target, predicted)
print("acc = ", acc)

from sklearn.metrics import confusion_matrix

m = confusion_matrix(iris.target, predicted)
print(m)

import seaborn

seaborn.heatmap(m)

from sklearn.metrics import classification_report

print(classification_report(iris.target, predicted))
