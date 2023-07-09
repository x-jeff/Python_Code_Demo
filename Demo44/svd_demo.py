import numpy as np
from scipy.linalg import svd
from sklearn.decomposition import TruncatedSVD

X = np.array([[1,1],
              [1,1],
              [0,0]])

U,S,V = svd(X, full_matrices=False)

svd = TruncatedSVD(1)
x = svd.fit_transform(X)