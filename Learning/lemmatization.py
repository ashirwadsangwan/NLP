from nltk.stem import WordNetLemmatizer
import nltk
lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize('better', pos='a'))
text = 'Sam has three cats and many dogs but he likes to do coding.'
tokens = nltk.word_tokenize(text)

lemmatized = []
for word in tokens:
    lemmatized.append(lemmatizer.lemmatize(word))
print(lemmatized)
