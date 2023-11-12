import pandas as pd
import datetime
from apyori import apriori

movie = pd.read_csv("movies.csv")
#print(movie.head())

movie_dic = {}
for rec in movie.iterrows():
    movie_dic[rec[1].movieId] = rec[1].title

df = pd.read_csv("ratings.csv")
df = df[df["timestamp"] >= 1325376000]
#print(df.info())

transactions = [ele for ele in df.groupby("userId")["movieId"].apply(list)]
rules = apriori(transactions, min_support=0.2, min_confidence=0.5, min_lift=3, min_length=2)

result = list(rules)
for rec in result:
    print([item for item in rec.items])
    #print([movie_dic.get(item) for item in rec.items])

for rec in result:
    left_hand = rec.ordered_statistics[0].items_base
    right_hand = rec.ordered_statistics[0].items_add
    #l = ';'.join([movie_dic.get(item) for item in left_hand])
    #r = ';'.join([movie_dic.get(item) for item in right_hand])

    l = ([item for item in left_hand])
    r = ([item for item in right_hand])
    print('{} => {}'.format(l, r))