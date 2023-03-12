import pandas
from sklearn.feature_selection import VarianceThreshold
df = pandas.read_csv("customer_behavior.csv")
X = df[['bachelor','gender','age','salary']]
sel = VarianceThreshold()
X_val = sel.fit_transform(X)

names = X.columns[sel.get_support()]
print(names)
print(sel.variances_)

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
X = df[['bachelor','gender','age','salary']]
y = df['purchased'].values
clf = SelectKBest(chi2, k=2)
clf.fit(X, y)
print(clf.scores_)

X_new = clf.fit_transform(X, y)
print(X_new)

from sklearn.feature_selection import RFE
from sklearn.svm import SVC
clf = SVC(kernel='linear')
rfe = RFE(clf, n_features_to_select=1)
rfe.fit(X_val, y)
for x in rfe.ranking_:
    print(names[x-1], rfe.ranking_[x-1])

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators=10,random_state=123)

clf.fit(X_val, y)
for feature in zip(names,clf.feature_importances_):
    print(feature)

import matplotlib.pyplot as plt
plt.title('Feature Importance')
plt.bar(range(0,len(names)),clf.feature_importances_)
plt.xticks(range(0,len(names)),names)
plt.show()