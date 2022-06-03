# movie-recommendation-engine-streamlit

This is a Recommendation Engine that uses different Filtering Techniques to recommend movies to the user. This application works on Python and uses Streamlit for its web app. We will discuss the algorithms and implementation in detail.

Dataset - https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata


## HOSTING THE APP ON LOCALHOST

1. Clone the repository into your local environment using command `git clone https://github.com/dayitachaudhuri/movie-recommendation-engine-streamlit`
2. Enter the project directory `cd movie-recommendation-engine-streamlit`.
3. On the terminal, run `pip install -r requirements.txt` All the required packages will now be installed.
4. On the terminal, run `streamlit run app.py`.

The application will now be running on your [localhost.](http://localhost:8501/)

Or youcan directly access the hosted application on Heroku https://recommender-engine-streamlit.herokuapp.com/

## RECOMMENDATION ENGINE:

The basic and quite straighforward aim of a recommendation engine is to recommend items (in this case movies) to the user based on the data available. In this project, I have built from scratch 3 Recommendation Engine Models.

_The homepage of the application shows 20 general movie recommendations based on -_

#### 1. Popularity 

When we enter a car showroom, the first products the salesman shows us are the most popular vehicles. Similarly here we get popularity of each movie from out dataset. We recommend 10 most popular movies. We sort the movies in our dataset based on the popularity field and show the top 10.

#### 2. Rating 

We also get average user rating of each movie from out dataset. We recommend 10 highest rated movies. We sort the movies in our dataset based on the average field and show the top 10.

_After that, we move to the search page, where we get more personalised recommendations. These are based on two techniques -_

#### 3. Content-Based Recommendation

Here we assume that if the user likes a movie of a particular type, he/she will like all movies of that type. We prepocess our data and create tags for all movies. Then we compare the tags for each movie and create Distance Vectors which show how similar any two movies are. The user is prompted to choose a movie they like, following which the engine recommends top 5 movies that are closest to it is the Similariy Vector Matrix, ie most similar to the chosen movie.

#### 4. Collaborative Filtering

Here we assume that if if two users like similar movies, they will keep liking similar movies. We process the user rating dataset and train a ML Model to predict how each user would rate each movie. The model itself identifies the relationship between most similar users and provides ratings accordingly. Then we eliminate movies that have already been rated by a user by making the ratings 0. Now we recommend the top 5 movies for the current user that the model has given highest predicted rating.

## USING THE INTERFACE

In the home page, you can find 10 most popular movies and 10 highest rated movies. This is the firsta nd most general of all recommendation systems.

![image](https://user-images.githubusercontent.com/77076578/170788127-17ac9f9f-ef52-4d7d-b283-8418b29a1af8.png)
![image](https://user-images.githubusercontent.com/77076578/170788159-38abdd1e-d9b9-43dc-9cd2-eb22ef4485bc.png)


In the Search Page (most important), the user can search for a movie or choose from the dropdown. Click on the Recommend Button. The application then recommends 5 movies using Content-Based Recommendation in "Movies Like This" section and 5 movies using Collaborative Filtering in "Users Also Liked" section.

![image](https://user-images.githubusercontent.com/77076578/170788273-e528b54d-565a-4e30-963c-8c9321dc9aed.png)
![image](https://user-images.githubusercontent.com/77076578/170788330-aac72d0b-5b81-4906-b983-cc10de7995c2.png)


## IMPLEMENTATION

Project directory resembles the below - 

![image](https://user-images.githubusercontent.com/77076578/170717861-6bd78b5e-f11e-40a6-9fee-ced5bb8921d9.png)

### I. recommendation-engine.ipynb

This is the Python Notebook where we have Processed our Datasets and Trained our Models. The resultant Similarity Matrices are stored as Pickle Files, which are then accessed by our app.py

**PART 1: Content-Based Filtering**

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

2. We use the ast library to convert genres, keywords and cast fields to list format which will be easier to process. For cast, we keep only the first 5 names and remove the rest for relevance. Then we extract director's name from crew and place it as the only item in a list in crew field. Since we need our model to identify cast and crew first and last names together as one entity, we remove all white spaces from cast and crew field entries. We also remove white spaces from keyword entries. Overview is currently a long string. We split overview into a list of smaller strings (each word).

3. We introduce a new field 'tags' that incorporate all the members of 'overview', 'keywords', 'genres', 'cast', 'crew' fields. This is the actual field with which we wll compare and find relationship among movies.

4. Next we use the Natural Language Toolkit of Python (nltk) to transform the tags of teh movies to stem words. In this way, similar words will be identifies as similar by our algorithm.

5. Now that we have our tags ready, we use sklearn library to create a Similarity Vector Matric for our movies. This will provide us a similarity score for every movie to every movie. We store this Similarity Matrix in a pickle file which will be accessed by our streamlit application.

**PART 2: Collaborative Filtering**

Collaborative Filtering is oftwo types, User-Based collaborative Filtering and Item-Based Collaborative Filtering. The former model studies trends of similarity between current user and other users while the later studies similarity between items rated by all users. We have trained models for both algorithms and then compared their efficiency.

6. We use Pandas to import the ratings.csv dataset. We split the dataset into 70%:30% Training set:Testing Set ratio, and train the ML Model on the obtained training set. We create a dummy copy of the training and testing sets. In the dummy_train, we replace all ratings that exist by 0 and make unrated positions 1. In dummy_test we replace all ratings that exist by 1 and all unrated positions by 0. These dummy sets will be used later.

7. We use our trained model to create a user similarity matrix between users. We use the similarity matrix in our model to predict ratings for all unrated movies for all users.

8. Now our predicted ratings set contains all predicted as well as original given ratings. We cannot recommend movies that are already rated by the user. Hence we multiply the predicted ratings with our dummy training set. This makes all rated movies 0 and hence will not be considered while taking top 5. 

9. Similarly, we create a item similarity matrix between movies rated by users. We use the similarity matrix in our model to predict ratings for all unrated movies for all users. We also multiply the predicted ratings with our dummy training set so as to make all rated movies 0.

**PART 3: Evaluation**

We evaluate the Root Mean Square Error and Mean Absolute Error both User-based and Item-based Collaborative Filtering and the finidngs are as follows - 

* User Based Model : RMSE - 1.5635654266606624   MAE - 1.2116342196650216
* Item Based Model : RMSE - 2.512699212653213    MAE - 2.215407217950911

Hence User Based Model is about 50% more efficient than Item Based Model. So we used the User-Based Collaborative Filtering Model to Recommend 5 movies to the current User.

We store these Predicted Ratings in a Pickle File that can be accessed by our streamlit application.


### app.py

This is our actual streamlit application. Here we import the pickle files and define functions to extract data for each recommendation method. 

1. First we define a function `fetch_poster(id)` that uses the TMDB API to fetch movie poster from the movie ID given as argument.

2. For the Home Page, we simply create a function `recommend_0()` extract the movies with highest popularity and rating.

3. For the Search page, we define two functions. `recommend_0(movie)` is to implement Content-Based Filtering, where we find the 5 movies from our Movie Similarity Matrix that are closest to the given movie. `recommend_0(movieId)` is to implement Collaborative Filtering, where we find the 5 movies from our Prediicted Ratings Matrix in the given movieId column that have the highest predicted rating.

_For the sake of convenience we have set the user as User 1 in the source code. This value of user can be changed in the source code and experimented with. However it is possible to create a Sign-Up/Log-In page and store user details to give personalised recommendations in collaborative filtering. _

## FUTURE SCOPE

- Devising a method to collect user data like Search History, Most Liked Actors and Most Liked Genres to give more personalised recommendation on Content-Based Filtering.
- Creating a Registration/Login System and a rating system to expand our datasets and give personalised recommendations on Collaborative Filtering.
- We have evaluated our model and we can create corresponding deviations to make our modle more accurate to the case of the user.
