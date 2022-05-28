import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import pickle
import requests

user = 14

# Loading the Pickle Files into our Application

movies_dict=pickle.load(open('movies.pkl','rb'))
all_movies=pd.DataFrame(movies_dict)

object_similarity=pickle.load(open('recommend_1.pkl','rb'))
user_ratings=pickle.load(open('recommend_2.pkl','rb'))

#--------------------------------------------------------
# Defining a function to retrieve Movie Poster from given Movie ID using the IMDB API
#--------------------------------------------------------
def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=b6276f25a72128d4d93877a8b540e2c6&language=en-US'.format(movie_id))
    data=response.json()
    return "http://image.tmdb.org/t/p/w500/"+data['poster_path']

#--------------------------------------------------------
# Defining a function to find Top Rated Movies by Popularity and User Rating
#--------------------------------------------------------
def recommend_0(col):

    movies_list=all_movies.sort_values(by=col, ascending=False, inplace=False)
    movies_list=movies_list.iloc[0:10]

    recommended_movies=[]
    recommended_posters=[]

    for i in range(len(movies_list)):
        id=movies_list.iloc[i,0]
        recommended_movies.append(all_movies[all_movies['id']==id].iloc[0,1])
        recommended_posters.append(fetch_poster(id))
    
    return recommended_movies,recommended_posters

#--------------------------------------------------------
# Defining a function to implement Content-Based Recommendation.
#--------------------------------------------------------
def recommend_1(movie):

    movie_index=(all_movies[all_movies['title']==movie].index[0])
    distances=object_similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies=[]
    recommended_posters=[]

    for i in movies_list:
        recommended_movies.append(all_movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(all_movies.iloc[i[0]].id))
    
    return recommended_movies,recommended_posters
#--------------------------------------------------------
# Defining a function to implement Collaborative Recommendation.
#--------------------------------------------------------
def recommend_2(userID):

    movies_list=user_ratings.iloc[userID:userID+1].sort_values(by=userID, ascending=False)

    recommended_movies=[]
    recommended_posters=[]

    for i in range(0,5):
        movieId=movies_list.columns.values.tolist()[i]
        recommended_movies.append(all_movies.iloc[movieId].title)
        recommended_posters.append(fetch_poster(all_movies.iloc[movieId].id))
    
    return recommended_movies,recommended_posters

st.title("Movie Recommender")

#--------------------------------------------------------
# 1. SIDEBAR NAVIGATION
#--------------------------------------------------------
with st.sidebar:
    page = option_menu(
        menu_title = None,
        options = ["Home","Search"],
        icons = ["house","search"],
    )

#--------------------------------------------------------
# 2. HOME PAGE
#--------------------------------------------------------

if page == "Home":

    st.header("Most Popular Movies")

    names,posters=recommend_0('popularity')

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
    
    with col1:
        st.text(names[5])
        st.image(posters[5])
    with col2:
        st.text(names[6])
        st.image(posters[6])
    with col3:
        st.text(names[7])
        st.image(posters[7])
    with col4:
        st.text(names[8])
        st.image(posters[8])
    with col5:
        st.text(names[9])
        st.image(posters[9])

    st.header("Highest Rated Movies")

    names,posters=recommend_0('vote_average')
    
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
    
    with col1:
        st.text(names[5])
        st.image(posters[5])
    with col2:
        st.text(names[6])
        st.image(posters[6])
    with col3:
        st.text(names[7])
        st.image(posters[7])
    with col4:
        st.text(names[8])
        st.image(posters[8])
    with col5:
        st.text(names[9])
        st.image(posters[9])

#--------------------------------------------------------
# 3. SEARCH PAGE 
#--------------------------------------------------------

if page == "Search":

    selected_movie=st.selectbox(
        'Choose a movie.',
        all_movies['title'].values
    )

    if st.button("Recommend"):

        st.header("Movies Like This")

        names,posters=recommend_1(selected_movie)
    
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

        st.header("Users Also Liked")

        names,posters=recommend_2(user)
    
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