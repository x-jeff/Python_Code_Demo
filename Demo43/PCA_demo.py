from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
from matplotlib import pyplot as plt

iris = load_iris()
X = iris.data
y = iris.target
print(X.shape)

pca = PCA(n_components=2)
pca.fit(X)

X_reduced = pca.transform(X)
print(X_reduced.shape)

plt.scatter(X_reduced[:,0], X_reduced[:,1], c=y)
plt.show()

print(pca.components_)
for component in pca.components_:
    print(" + ".join("%.3f x %s" % (value,name) for value,name in zip(component, iris.feature_names)))

plt.bar(range(0,2), pca.explained_variance_)
plt.xticks(range(0,2),["component 1","component 2"])
plt.show()
