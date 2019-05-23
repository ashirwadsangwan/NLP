from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = 'I asked God for a bike, but I know God doesn’t work that way. So I stole a bike and asked for forgiveness.'

stop_words = set(stopwords.words('English'))
# because stopwords exist in many languages.
words  = word_tokenize(text)
#tokenizing words

def removing_stopwords(text):

    stop_words = set(stopwords.words('English'))
    words = word_tokenize(text)
    filtered_words = []

    for word in words:
        if word not in stop_words:
            filtered_words.append(word)

    print(filtered_words)

removing_stopwords(text)
