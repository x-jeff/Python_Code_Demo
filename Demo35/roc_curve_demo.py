from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve

# 数据读取与编码转换
iris = load_iris()
X = iris.data[50:150, ]

le = preprocessing.LabelEncoder()
y = le.fit_transform(iris.target[50:150])
print(y)

# 建立预测模型
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.33, random_state=123)
clf = DecisionTreeClassifier()
clf.fit(train_X, train_y)

# 计算ROC Curve参数
probas_ = clf.fit(train_X, train_y).predict_proba(test_X)
probas_[:, 1]

fpr, tpr, thresholds = roc_curve(test_y, probas_[:, 1])

# 绘制ROC Curve
import matplotlib.pyplot as plt

plt.plot(fpr, tpr, label='ROC curve')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc='lower right')
plt.show()

# 计算AUC分数
from sklearn.metrics import auc

roc_auc = auc(fpr, tpr)
print("AUC : %f" % roc_auc)
