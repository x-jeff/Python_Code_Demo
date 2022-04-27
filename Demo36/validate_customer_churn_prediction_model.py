# 读取客户流失数据
import pandas

df = pandas.read_csv("customer_churn.csv", index_col=0, header=0)
print(df.head())

# 数据前处理
df = df.iloc[:, 3:]
cat_var = ['international_plan', 'voice_mail_plan', 'churn']

for var in cat_var:
    df[var] = df[var].map(lambda e: 1 if e == "yes" else 0)
y = df.iloc[:, -1]
X = df.iloc[:, :-1]

# 区分训练与测试数据集
from sklearn.model_selection import train_test_split

train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.33, random_state=123)

# 使用决策树建立分类模型
from sklearn import tree

clf = tree.DecisionTreeClassifier(max_depth=3)
clf.fit(train_X, train_y)
predicted = clf.predict(test_X)

# 产生混淆矩阵以及其他评估指标
from sklearn.metrics import accuracy_score

print(accuracy_score(test_y, predicted))

from sklearn.metrics import confusion_matrix

m = confusion_matrix(test_y, predicted)
print(m)

from sklearn.metrics import classification_report

print(classification_report(test_y, predicted))

# 使用ROC曲线比较模型
from sklearn.tree import DecisionTreeClassifier

clf1 = DecisionTreeClassifier()
clf1.fit(train_X, train_y)

from sklearn.svm import SVC

clf2 = SVC(probability=True, kernel='linear', cache_size=7000, max_iter=10000)
clf2.fit(train_X, train_y)

from sklearn.linear_model import LogisticRegression

clf3 = LogisticRegression()
clf3.fit(train_X, train_y)

from sklearn.ensemble import RandomForestClassifier

clf4 = RandomForestClassifier()
clf4.fit(train_X, train_y)

import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

plt.figure(figsize=[20, 10])
for clf, title in zip([clf1, clf2, clf3, clf4], ['Decision Tree', 'SVM', 'LogisticRegression', 'RandomForest']):
    probas_ = clf.fit(train_X, train_y).predict_proba(test_X)
    fpr, tpr, thresholds = roc_curve(test_y, probas_[:, 1])
    plt.plot(fpr, tpr, label='%s - AUC:%.2f' % (title, auc(fpr, tpr)))

plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('False Positive Rate', fontsize=20)
plt.ylabel('True Positive Rate', fontsize=20)
plt.title('Receiver operating characteristic example', fontsize=20)
plt.legend(loc="lower right", fontsize=20)
plt.show()

# 评估特征重要性
print(clf1.feature_importances_)
print(train_X.columns[clf1.feature_importances_.argsort()[::-1]])

import matplotlib.pyplot as plt

importance = clf1.feature_importances_
names = train_X.columns
plt.title("Feature Importance")
plt.bar(range(0, len(names)), importance[importance.argsort()[::-1]])
plt.xticks(range(0, len(names)), names[importance.argsort()[::-1]], rotation=90)
plt.show()
