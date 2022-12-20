import pandas

dataset = pandas.read_csv("customers.csv")
print(dataset.head())

X = dataset.iloc[:, [3, 4]].values

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
y_kmeans = kmeans.fit_predict(X)
print(kmeans.inertia_)  # WCSS值

import matplotlib.pyplot as plt

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title("The Elbow Method")
plt.xlabel("Number of clusters")
plt.ylabel("WCSS")
plt.show()

from sklearn import metrics

print("Silhouette Coefficient:%0.3f" % metrics.silhouette_score(X, y_kmeans))

sil = []
for i in range(2, 11):
    kmeans = KMeans(n_clusters=i, init="k-means++", random_state=42)
    y_kmeans = kmeans.fit_predict(X)
    sil.append(metrics.silhouette_score(X, y_kmeans))
plt.plot(range(2, 11), sil)
plt.xlim([0, 11])
plt.title("The Silhouette Method")
plt.xlabel("Number of Clusters")
plt.ylabel("Silhouette Coefficient")
plt.show()

from sklearn.cluster import AgglomerativeClustering

# 比较不同的聚类方法
# ward
ward = AgglomerativeClustering(n_clusters=5, affinity="euclidean", linkage="ward")
y_ward = ward.fit_predict(X)
# complete
complete = AgglomerativeClustering(n_clusters=5, affinity="euclidean", linkage="complete")
y_complete = complete.fit_predict(X)
# kmeans
kmeans = KMeans(n_clusters=5, init="k-means++", random_state=42)
y_kmeans = kmeans.fit_predict(X)

for est, title in zip([y_ward, y_complete, y_kmeans], ['ward', 'complete', 'kmeans']):
    print(title, metrics.silhouette_score(X, est))
