from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
import numpy as np

digits = load_digits()
print(digits.DESCR)

fig = plt.figure(figsize=(8, 8))
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
for i in range(36):
    ax = fig.add_subplot(6, 6, i + 1, xticks=[], yticks=[])
    ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')
    ax.text(0, 7, str(digits.target[i]), color="red", fontsize=20)
plt.show()

print(digits.data.shape)
print(digits.data)

scaler = StandardScaler()
scaler.fit(digits.data)
X_sacled = scaler.transform(digits.data)

print(X_sacled)

mlp = MLPClassifier(hidden_layer_sizes=(30, 30, 30), activation='logistic', max_iter=100)
mlp.fit(X_sacled, digits.target)

predicted = mlp.predict(X_sacled)
fig = plt.figure(figsize=(8, 8))
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
for i in range(36):
    ax = fig.add_subplot(6, 6, i + 1, xticks=[], yticks=[])
    ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')
    ax.text(0, 7, str('{}-{}'.format(digits.target[i], predicted[i])), color="red", fontsize=20)
plt.show()

res = []
for i, j in zip(digits.target, predicted):
    res.append(i == j)
print(sum(res) / len(digits.target))
