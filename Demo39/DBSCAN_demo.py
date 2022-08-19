import numpy as np
from PIL import Image
from sklearn.preprocessing import binarize
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN

img = Image.open("handwriting.png")
img2 = img.rotate(-90).convert("L")
imgarr = np.array(img2)

imagedata = np.where(1 - binarize(imgarr, 0) == 1)
plt.scatter(imagedata[0], imagedata[1], s=100, c='red', label="Cluster 1")
plt.show()

X = np.column_stack([imagedata[0], imagedata[1]])
kmeans = KMeans(n_clusters=2, init="k-means++", random_state=42)
y_kmeans = kmeans.fit_predict(X)

plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s=100, c="red", label="Cluster 1")
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s=100, c="blue", label="Cluster 2")
plt.show()

dbs = DBSCAN(eps=1, min_samples=3)
y_dbs = dbs.fit_predict(X)

plt.scatter(X[y_dbs == 0, 0], X[y_dbs == 0, 1], s=100, c="red", label="Cluster 1")
plt.scatter(X[y_dbs == 1, 0], X[y_dbs == 1, 1], s=100, c="blue", label="Cluster 2")
plt.show()
