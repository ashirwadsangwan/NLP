import nltk
import random
from nltk.corpus import movie_reviews

documents = []

for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        documents.append((list(movie_reviews.words(fileid)), category))

random.shuffle(documents) # for training and test purpose.

all_words = []
for word in movie_reviews.words():
    all_words.append(word.lower())

all_words = nltk.FreqDist(all_words)

print(all_words.most_common(10))
print(all_words['beautiful'])
