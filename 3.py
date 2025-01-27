import numpy as np
from numpy.linalg import norm
import pandas as pd

reviews = pd.read_csv("data/derived/restaurant_reviews_textblob.csv", sep="\t")

x, y = [], []
for i, review in reviews.iterrows():
    x.append(len(review['Review']))
    y.append(review['Liked'])

cosine = np.dot(x, y) / (norm(x) * norm(y))
print("Cosine Similarity:", cosine)

r = np.corrcoef(x, y)
print(f'Pearson correlation coefficient: {r[0, 1]}')
