# movie-recommendation-engine-streamlit

This is a Recommendation Engine that uses different Filtering Techniques to recommend movies to the user. This application works on Python and uses Streamlit for its web app. We will discuss the algorithms and implementation in detail.

Dataset - https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

Hosted on Heroku - https://recommender-engine-streamlit.herokuapp.com/


## HOSTING THE APP ON LOCALHOST

1. Clone the repository into your local environment using command `git clone https://github.com/dayitachaudhuri/movie-recommendation-engine-streamlit`
2. On the terminal, run `pip install -r requirements.txt` All the required packages will now be installed.
3. On the terminal, run `streamlit run app.py`.

The application will now be running on your [localhost.](http://localhost:8501/)

OR YOU CAN DIRECTLY ACCESS THE APPLICATION HOSTED ON HEROKU https://recommender-engine-streamlit.herokuapp.com/

## RECOMMENDATION ENGINE:

The basic and quite straighforward aim of a recommendation engine is to recommend items (in this case movies) to the user based on the data available. In this project, I have built from scratch 3 Recommendation Engine Models.

_The homepage of the application shows 20 general movie recommendations based on -_

#### 1. Popularity 

When we enter a car showroom, the first products the salesman shows us are the most popular vehicles. Similarly here we get popularity of each movie from out dataset. We recommend 10 most popular movies and 10 highest rated movies to the user.

_After that, we move to the search page, where we get more personalised recommendations. These are based on two techniques -_

#### 2. Content-Based Recommendation

Here we assume that if the user likes a movie of a particular type, he/she will like all movies of that type. We prepocess our data and create tags for all movies. Then we compare the tags for each movie and create Distance Vectors which show how similar any two movies are. The user is prompted to choose a movie they like, following which the engine recommends top 5 movies that are closest to it is the Similariy Vector Matrix, ie most similar to the chosen movie.

#### 3. Collaborative Filtering

Here we assume that if if two users like similar movies, they will keep liking similar movies. We process the user rating dataset and train a ML Model to predict how each user would rate each movie. The model itself identifies the relationship between most similar users and provides ratings accordingly. Then we eliminate movies that have already been rated by a user by making the ratings 0. Now we recommend the top 5 movies for the current user that the model has given highest predicted rating.

## USING THE INTERFACE

In the home page, you can find 10 most popular movies and 10 highest rated movies. This is the firsta nd most general of all recommendation systems.

![image](https://user-images.githubusercontent.com/77076578/170585862-e146667a-1c57-4442-93a1-cf25492e4185.png)
![image](https://user-images.githubusercontent.com/77076578/170586012-e236a6bb-4924-4634-95bb-18bf0634c3e4.png)

In teh Search Page (most important), the user can search for a movie or choose from the dropdown. Click on the Recommend Button. The application then recommends 5 movies using Content-Based Recommendation in "Movies Like This" section and 5 movies using Collaborative Filtering in "Users Also Liked" section.

![image](https://user-images.githubusercontent.com/77076578/170586080-514e5b8c-5140-4fe8-9f45-9fbf6568ced3.png)
![image](https://user-images.githubusercontent.com/77076578/170586252-d52371e7-8df9-4ef0-82b3-08689fe02677.png)

## IMPLEMENTATION

Project directory resembles the below - 

![image](https://user-images.githubusercontent.com/77076578/170717861-6bd78b5e-f11e-40a6-9fee-ced5bb8921d9.png)

#### recommendation-engine.ipynb

This is essentially the backend of our application.

1. We use the pandas library to import the datasets. We merge credits.csv into movies.csv on the basis of the id column. Next we merge the links.csv into the current movies.csv. After that we sort our the relevant columns from movies.csv and remove the rest. Relevant columns include -
- Movie ID (TMDB)
- Title
- Overview
- Keywords
- Genres
- Cast
- Crew
- Popularity
- Average Vote
- Movie ID (MovieLens)

2. We use the ast library to convert genres, keywords and cast fields to list format which will be easier to process. For cast, we keep only the first 5 names and remove the rest for relevance. Then we extract director's name from crew and place it as the only item in a list in crew field.
3. Since we need our model to identify cast and crew first and last names together as one entity, we remove all white spaces from cast and crew field entries. We also remove white spaces from keyword entries.
4. Overview is currently a long string. We split overview into a list of smaller strings (each word)
5. We introduce a new field 'tags' that incorporate all the members of 'overview', 'keywords', 'genres', 'cast', 'crew' fields. This is the actual field with which we wll compare and find relationship among movies.
6. Next we use the Natural Language Toolkit of Python (nltk) to transform the tags of teh movies to stem words. In thsi way, similar words will be identifies as similar by our algorithm.
