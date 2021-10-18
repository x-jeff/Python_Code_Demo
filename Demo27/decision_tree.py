from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)

# 产生预测结果
predicted = clf.predict(iris.data)

# 绘制成树形图
from sklearn import tree

tree.export_graphviz(clf, out_file='tree.dot')
