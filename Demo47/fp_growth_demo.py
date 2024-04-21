import pandas
import datetime
from pymining import itemmining

movie = pandas.read_csv("../Demo46/movies.csv")
print(movie.head())
movie_dic = {}
for rec in movie.iterrows():
    movie_dic[rec[1].movieId] = rec[1].title
print(movie_dic.get(1))

df = pandas.read_csv("../Demo46/ratings.csv")
print(df.info())
df = df[df["timestamp"] >= 1325376000]
print(df.info())

transactions = [ele for ele in df.groupby("userId")["movieId"].apply(list)]
fp_input = itemmining.get_fptree(transactions)
report = itemmining.fpgrowth(fp_input, min_support=30, pruning=True)

for ele in report:
    if len(ele) >=6:
        print(";".join([movie_dic.get(item) for item in ele]))