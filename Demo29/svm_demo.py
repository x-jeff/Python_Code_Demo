from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt


def plot_estimator(estimator, X, y, plot_title):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))

    plt.plot()
    Z = estimator.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    # 参数alpha为透明度
    # 参数cmap为colormap
    plt.contourf(xx, yy, Z, alpha=0.4, cmap=plt.cm.rainbow)
    # 参数c为颜色
    # 参数alpha为透明度
    # 参数cmap为colormap
    plt.scatter(X[:, 0], X[:, 1], c=y, alpha=1, cmap=plt.cm.YlOrRd)
    plt.title(plot_title)
    plt.xlabel('Petal.Length')
    plt.ylabel('Petal.Width')
    plt.show()


iris = load_iris()

X = iris.data[0:100, [2, 3]]
y = iris.target[0:100]

clf1 = SVC(kernel="linear")
clf1.fit(X, y)

clf2 = LogisticRegression()
clf2.fit(X, y)

plot_estimator(clf1, X, y, "SVM")
plot_estimator(clf2, X, y, "LogisticRegression")
