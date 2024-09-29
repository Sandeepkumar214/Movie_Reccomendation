# Movie Recommendation System

Welcome to the Movie Recommendation System! This project uses machine learning techniques to recommend movies based on user preferences. Below is a detailed overview of how the system works, along with setup instructions.

## Table of Contents
1. [Jupyter Notebook Overview](#jupyter-notebook-overview)
2. [Python Implementation](#python-implementation)
3. [Deployment](#deployment)
4. [How to Use](#how-to-use)
5. [License](#license)

---

## Jupyter Notebook Overview

1. **Dataset Loading**:
   - The dataset was sourced from Kaggle using the Kaggle API.

2. **Data Cleaning**:
   - Performed data cleaning as the dataset was in an unstructured format:
     - **Extract Main Actor**: Created a `convert` function to extract the name of the main actor from the cast column.
     - **Extract Director**: Developed a `fetch_director` function to extract the name of the director from the crew column.
     - **Feature Engineering**: Separated the overview column into multiple features: overview, keywords, cast, crew, and genres.

3. **Text Processing**:
   - Applied Porter Stemmer from NLTK on the tags column for better text normalization.

4. **Vectorization**:
   - Used TF-IDF vectorization from sklearn to convert text data into vectors.

5. **Sparse Matrix Formation**:
   - Created a sparse matrix of vectors to optimize memory usage.

6. **Cosine Similarity Calculation**:
   - Calculated cosine similarity between vectors and saved the result as a pickle file.

7. **Recommendation Logic**:
   - Developed logic to get the movie index via movie name, calculate distances using cosine similarity, sort the results in descending order, and return the top 10 movie indices with their distances.

8. **Index Dictionary**:
   - Prepared a dictionary of movie names and their corresponding index numbers, saved as a pickle file.

---

## Python Implementation

1. **Loading Similarity Data**:
   - Load the saved similarity pickle file for further processing.

2. **Poster Fetching**:
   - Created a `fetch_poster` function to retrieve movie posters using the themoviedb.org API.

3. **Recommendation Function**:
   - Developed a recommendation function that calculates cosine similarity between the input movie and all movies, sorting the results in descending order.

---

## Deployment

The Movie Recommendation System is deployed using Streamlit. You can access the live app [here](https://sandeep-movie-recommendation.streamlit.app/).

---

## How to Use

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/movie-recommendation-system.git
   cd movie-recommendation-system
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Jupyter Notebook**:
   - Open the Jupyter Notebook to explore the data processing and model training.

4. **Run the Streamlit App**:
   ```bash
   streamlit run app.py
   ```

---

## License

This project is licensed under the MIT License. See the LICENSE file for more information.

![image](https://github.com/user-attachments/assets/e16b26af-62b9-457e-89e1-be9b88087774)

Video : 


https://github.com/user-attachments/assets/2aa061e4-daf9-4245-913b-93f00bd65341



---

Feel free to contribute to the project or reach out with any questions or suggestions! Enjoy exploring your movie recommendations!
