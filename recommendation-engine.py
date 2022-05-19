import pandas as pd
import numpy as np
import ast
from sklearn.feature_extraction.text import CountVectorizer

movies=pd.read_csv('dataset/tmdb_5000_movies.csv')
credits=pd.read_csv('dataset/tmdb_5000_credits.csv')

'''
from pymongo import MongoClient
client = MongoClient()
db1 = client.moviesdatabase
movies = pd.DataFrame(list(db1.tmdb5000.find()))
db2 = client.creditsdatabase
credits = pd.DataFrame(list(db2.tmdb5000.find()))
'''

movies=movies.merge(credits, on='title')
movies=movies[['id','title','overview','genres','keywords','cast','crew']]

def convert(obj):
    L=[]
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L

movies['genres']=movies['genres'].apply(convert)
movies['keywords']=movies['keywords'].apply(convert)

def convert2(obj):
    L=[]
    count=0
    for i in ast.literal_eval(obj):
        if count!=3:
            L.append(i['name'])
            count+=1
        else:
            break
    return L

movies['cast']=movies['cast'].apply(convert2)

def convert3(obj):
    L=[]
    for i in ast.literal_eval(obj):
        if i['job']=='Director':
            L.append(i['name'])
            break
    return L

movies['crew']=movies['crew'].apply(convert3)
movies['keywords']=movies['keywords'].apply(lambda x: [i.replace(" ","") for i in x])
movies['cast']=movies['cast'].apply(lambda x: [i.replace(" ","") for i in x])
movies['crew']=movies['crew'].apply(lambda x: [i.replace(" ","") for i in x])
movies['overview']=movies['overview'].apply(lambda x: str(x).split())
movies['tags']=movies['overview']+movies['genres']+movies['keywords']+movies['cast']+movies['crew']
new_df=movies[['id','title','tags']]
new_df['tags']=new_df['tags'].apply(lambda x: " ".join(x))
new_df['tags']=new_df['tags'].apply(lambda x: x.lower())

import nltk
from nltk.stem.porter import PorterStemmer

ps=PorterStemmer()

def stem(text):
    y=[]
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)

new_df['tags']=new_df['tags'].apply(stem)

cv=CountVectorizer(max_features=5000, stop_words='english')
vectors=cv.fit_transform(new_df['tags']).toarray()

from sklearn.metrics.pairwise import cosine_similarity

similarity=cosine_similarity(vectors)
sorted(list(enumerate(similarity[0])), reverse=True, key=lambda x:x[1])[1:6]

def recommend(movie):
    movie_index=(new_df[new_df['title']==movie].index[0])
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    for i in movies_list:
        print(new_df.iloc[i[0]].title)
        
import pickle

pickle.dump(new_df,open('movies.pkl','wb'))
pickle.dump(new_df.to_dict(),open('movies_dict.pkl','wb'))
pickle.dump(similarity,open('recommended.pkl','wb'))
