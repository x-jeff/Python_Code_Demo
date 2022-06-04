from sklearn.datasets import load_iris

iris = load_iris()

import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt

# dendrogram = sch.dendrogram(sch.linkage(iris.data, method='ward', optimal_ordering=False))
# plt.title('Dendrogram')
# plt.xlabel('Iris')
# plt.ylabel('Euclidean distances')
# plt.show()

from sklearn.cluster import AgglomerativeClustering

hc = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')
y_hc = hc.fit_predict(iris.data)

# plt.scatter(iris.data[y_hc == 0, 2], iris.data[y_hc == 0, 3], s=100, c='red', label='Cluster1')
# plt.scatter(iris.data[y_hc == 1, 2], iris.data[y_hc == 1, 3], s=100, c='blue', label='Cluster2')
# plt.scatter(iris.data[y_hc == 2, 2], iris.data[y_hc == 2, 3], s=100, c='green', label='Cluster3')

plt.scatter(iris.data[iris.target == 0, 2], iris.data[iris.target == 0, 3], s=100, c='red', label='Cluster1')
plt.scatter(iris.data[iris.target == 1, 2], iris.data[iris.target == 1, 3], s=100, c='blue', label='Cluster2')
plt.scatter(iris.data[iris.target == 2, 2], iris.data[iris.target == 2, 3], s=100, c='green', label='Cluster3')

plt.title('Clusters of Iris')
plt.xlabel('Petal.Length')
plt.ylabel('Petal.Width')
plt.legend()
plt.show()
