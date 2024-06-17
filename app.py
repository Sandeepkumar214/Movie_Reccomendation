import streamlit as st
import pickle
import pandas as pd
import requests
import os


# Function to download the file from Google Drive if it doesn't exist

with open('similiarity.pkl', 'rb') as file:
    similarity = pickle.load(file)

def fetch_poster(movie_id):
    try:
        response = requests.get(
            f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=84d2e1d5bb60330d8b713f9d6886e564&language=en-US')
        data = response.json()
        return f"https://image.tmdb.org/t/p/w500/{data['poster_path']}"
    except Exception as e:
        st.error(f"Error fetching poster: {e}")
        return ""


def recommend(movie):
    if movie not in movies['title'].values:
        return "Movie not found in the dataset.", []

    index = movies[movies['title'] == movie].index[0]


    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:11]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters


# Load the movies dictionary
try:
    with open('movie_dict.pkl', 'rb') as file:
        movies_dict = pickle.load(file)

except Exception as e:
    st.error(f"Error loading the movie dictionary: {e}")
    st.stop()

movies = pd.DataFrame(movies_dict)


st.title('Movie Recommender System')
st.header('made by Sandeep')
option = st.selectbox("Choose a movie", movies['title'].values)

if st.button('Suggest movies'):
    names, posters = recommend(option)
    if isinstance(names, str):
        st.error(names)
    else:
        cols = st.columns(10)
        for col, name, poster in zip(cols, names, posters):
            with col:
                st.text(name)
                st.image(poster)
