import pandas
import jieba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
import numpy

# 读取新闻数据
df = pandas.read_excel('news.xlsx')
print(df.head())

# 使用jieba断词
titles   = []
articles = []
for rec in df.iterrows():
    articles.append(' '.join(jieba.cut(rec[1].content)))
    titles.append(rec[1].title)
print(len(articles))
print(len(titles))
print(titles[0])
print(articles[0])

# 建立词频矩阵
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(articles)
print(X.shape)

# 计算余弦距离(Cosine Similarity)
cosine_similarities  = cosine_similarity(X, X)
print(cosine_similarities.shape)
print(cosine_similarities)

# 使用KMeans++聚类
c = KMeans(n_clusters=10, init = 'k-means++', random_state=123)
k_data = c.fit_predict(cosine_similarities)

# 产生聚类结果
titles_ary = numpy.array(titles)
print(titles_ary[k_data == 9])