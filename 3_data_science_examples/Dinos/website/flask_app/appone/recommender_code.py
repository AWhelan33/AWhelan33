from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer
from numpy import dot
from numpy.linalg import norm
from scipy import spatial

df = pd.read_csv('cleaned_dino_data.csv')
df.drop(columns=df.columns[0], axis=1, inplace=True)

# Construct a reverse map of indices and dinosaur names
indices = pd.Series(df.index, index=df['name']).drop_duplicates()

# Function to convert all strings to lower case and strip names of spaces


def clean_data(x):
    if isinstance(x, list):
        return [str.lower(i.replace(" ", "")) for i in x]
    else:
        # Check if director exists. If not, return empty string
        if isinstance(x, str):
            return str.lower(x.replace(" ", ""))
        else:
            return ''


# Apply clean_data function to your features.
features = ['diet', 'lived_in', 'type', 'period_name']

for feature in features:
    df[feature] = df[feature].apply(clean_data)


def create_soup(x):
    return ' '.join(x['diet']) + ' '.join(x['lived_in']) + ' '.join(x['type']) + ' '.join(x['period_name'])


# Create a new soup feature
df['soup'] = df.apply(create_soup, axis=1)

# Import CountVectorizer and create the count matrix

count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(df['soup'])

# Compute the Cosine Similarity matrix based on the count_matrix

cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

# Reset index of your main DataFrame and construct reverse mapping as before
df = df.reset_index()
indices = pd.Series(df.index, index=df['name'])

# Function that takes in dinosaur name as input and outputs most similar dinosaur


def get_recommendations(name, cosine_sim2=cosine_sim2):
    # Get the index of the dinosaur that matches the name
    idx = indices[name]

    # Get the pairwsie similarity scores of all names with that dino
    sim_scores = list(enumerate(cosine_sim2[idx]))

    # Sort the dinosaurs based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 3 most similar dinosaurs
    sim_scores = sim_scores[1:4]

    # Get the movie indices
    dino_indices = [i[0] for i in sim_scores]

    # Return the top 3 most similar dinosaurs
    reccommendations = df['name'].iloc[dino_indices]
    reccommendations = reccommendations.values.tolist()
    return reccommendations
