from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

iris = load_iris()
clf = LogisticRegression()
clf.fit(iris.data, iris.target)

clf.predict(iris.data)

import numpy as np
import matplotlib.pyplot as plt

X = iris.data[:, [2, 3]]
y = iris.target

clf = LogisticRegression()
clf.fit(X, y)

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))

plt.plot()
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
#参数alpha为透明度
#参数cmap为colormap
plt.contourf(xx, yy, Z, alpha=0.4, cmap=plt.cm.rainbow)
#参数c为颜色
#参数alpha为透明度
#参数cmap为colormap
plt.scatter(X[:, 0], X[:, 1], c=y, alpha=1, cmap=plt.cm.YlOrRd)
plt.title('Logistic Regression')
plt.xlabel('Petal.Length')
plt.ylabel('Petal.Width')
plt.show()