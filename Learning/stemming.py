from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

random_words = ['hazard', 'hazardous', 'swimming', 'swims']

for word in random_words:
    print(ps.stem(word))


def stemming(text):
    stemmed_text = []
    words = word_tokenize(text)
    ps = PorterStemmer()

    for word in words:
        stemmed_text.append(ps.stem(word))

    print(stemmed_text)

ex_text = 'Lok Sabha Election Results: Lok Sabha Election results of UP, Andhra Pradesh, Bihar, MP, TN, Telangana, Karnataka, Kerala, WB, Odisha, Maharashtra, J&K'
