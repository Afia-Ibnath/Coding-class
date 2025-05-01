import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample movie dataset (you can load a dataset like MovieLens for real data)
data = {
    'movieId': [1, 2, 3, 4, 5],
    'title': ['Toy Story', 'Jumanji', 'Grumpier Old Men', 'Waiting to Exhale', 'Father of the Bride Part II'],
    'genres': ['Adventure|Animation|Children|Comedy|Fantasy', 
               'Adventure|Children|Fantasy', 
               'Comedy|Romance', 
               'Comedy|Drama|Romance', 
               'Comedy|Drama'],
}

# Create a DataFrame
movies = pd.DataFrame(data)

# Vectorize the 'genres' column using TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(movies['genres'])

# Compute the cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to get movie recommendations
def get_recommendations(title, cosine_sim=cosine_sim):
    # Get the index of the movie that matches the title
    idx = movies.index[movies['title'] == title].tolist()[0]

    # Get the pairwise similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the indices of the top 3 most similar movies
    sim_scores = sim_scores[1:4]  # excluding the movie itself (it'll always have a score of 1)
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 3 most similar movies
    return movies['title'].iloc[movie_indices]

# Example usage
movie_title = 'Toy Story'
print(f"Movies recommended for '{movie_title}':")
print(get_recommendations(movie_title))

