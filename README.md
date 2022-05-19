# movie-recommendation-engine-streamlit

This is a Recommendation Engine that uses Content-Based Filtering to recommend movie titles. The engine has been built on Python and the interface has been implemented using Streamlit. It is a very light program with minimal customisation. 

Dataset - https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

## HOSTING THE APP ON LOCALHOST

1. Clone the repository into your local environment using command `git clone https://github.com/dayitachaudhuri/movie-recommendation-engine-streamlit`
2. Create a directory dataset inside the current directory. Import the TMDB 500 Movies datasets from the link given above and place them inside the dataset directory. The directory will now look somewhat like this -
  
  ![image](https://user-images.githubusercontent.com/77076578/169348033-d63755c7-e278-444a-921e-0e52a8928d48.png)

3. On the terminal, run `pip install -r requirements.txt` All the required packages will now be installed.
4. Run recommendation-engine.py. You will see three new .pkl files created in teh current directory. These are the preprocessed and cleaned data.
  
  ![image](https://user-images.githubusercontent.com/77076578/169348664-30194b5b-d618-4fab-970a-d5f470032f10.png)

6. On the terminal, run `streamlit run app.py`.

## USING THE INTERFACE

  ![image](https://user-images.githubusercontent.com/77076578/169349118-baf2250b-c09e-40a8-8dc9-1de48afbacfa.png)

Search for a movie by typing in the box and choose from the dropdown menu. Click on the Recommend Button. The app will show you five recommendations using Content-Based Filtering. You can use the app for 5000 movies registered in teh TMDB 500 Database, and can be extended further by including other databases.
