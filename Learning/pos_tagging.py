import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw('2005-GWBush.txt')
sample_text = state_union.raw('2006-GWBush.txt')

sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = sent_tokenizer.tokenize(sample_text)

def process_content(corpus):

    tokenized = PunktSentenceTokenizer().tokenize(corpus)

    try:
        for sent in tokenized:
            words = nltk.word_tokenize(sent)
            tagged = nltk.pos_tag(words)
            print(tagged)
    except Exception as e:
        print(str(e))

process_content(train_text)
