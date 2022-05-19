from urllib import response
import streamlit as st
import pandas as pd
import pickle
import requests


movies_dict=pickle.load(open('movies_dict.pkl','rb'))
all_movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('recommended.pkl','rb'))


def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=b6276f25a72128d4d93877a8b540e2c6&language=en-US'.format(movie_id))
    data=response.json()
    return "http://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(movie):
    movie_index=(all_movies[all_movies['title']==movie].index[0])
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies=[]
    recommended_posters=[]

    for i in movies_list:
        recommended_movies.append(all_movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(all_movies.iloc[i[0]].id))
    
    return recommended_movies,recommended_posters


st.title("Movie Recommender")

selected_movie=st.selectbox(
    'Choose a movie.',
    all_movies['title'].values
)

if st.button("Recommend"):
    names,posters=recommend(selected_movie)
    
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
