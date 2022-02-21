from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

# 1.留出法
print("留出法：")
# 引用数据与建立模型
iris = load_iris()
X = iris.data
y = iris.target

# 建立训练与测试数据集
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.33, random_state=123)
clf = DecisionTreeClassifier()
clf.fit(train_X, train_y)

# 产生准确度
predicted = clf.predict(test_X)
accuracy_score(test_y, predicted)
print(accuracy_score(test_y, predicted))

# 建立混淆矩阵
m = confusion_matrix(test_y, predicted)
print(m)

# 2.交叉验证法
print("交叉验证法(方法一)：")
from sklearn.model_selection import KFold

kf = KFold(n_splits=10)
for train, test in kf.split(X):
    train_X, test_X, train_y, test_y = X[train], X[test], y[train], y[test]
    clf = DecisionTreeClassifier()
    clf.fit(train_X, train_y)
    predicted = clf.predict(test_X)
    print(accuracy_score(test_y, predicted))

print("交叉验证法(方法二)：")
from sklearn.model_selection import cross_val_score

acc = cross_val_score(clf, X=iris.data, y=iris.target, cv=10)
print(acc)
print(acc.mean())

# 3.留一法
print("留一法：")

from sklearn.model_selection import LeaveOneOut

res = []
loo = LeaveOneOut()
for train, test in loo.split(X):
    train_X, test_X, train_y, test_y = X[train], X[test], y[train], y[test]
    clf = DecisionTreeClassifier()
    clf.fit(train_X, train_y)
    predicted = clf.predict(test_X)
    res.extend((predicted == test_y).tolist())
print(sum(res))
