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

word_features = list(all_words.keys())[:3000]

def find_features(document):
    words = set(document)
    features = {}
    for word in word_features:
        features[word] = (word in words)

    return features

#print(find_features(movie_reviews.words('neg/cv000_29416.txt')))

featuresets = [(find_features(rev), category) for (rev, category) in documents]

training_set = featuresets[:1900]
test_set = featuresets[1900:]

'''
<h3>posterior = prior occurances * likelihood/evidence</h3>
'''

classifier = nltk.NaiveBayesClassifier.train(training_set)
print("NaiveBayesClassifier has an accuracy of", (nltk.classify.accuracy(classifier, test_set)))
classifier.show_most_informative_features
