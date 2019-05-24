import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

text_file = state_union.raw('2005-GWBush.txt')


def applyChunking(corpus):

    tokenized = PunktSentenceTokenizer().tokenize(corpus)

    try:
        for sent in tokenized:
            words = nltk.word_tokenize(sent)
            tagged = nltk.pos_tag(words)

            chunkGram = '''Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}'''
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)

            print(chunked.draw())

    except Exception as e:
        print(str(e))

applyChunking(text_file)
