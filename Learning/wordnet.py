from nltk.corpus import wordnet

syns = wordnet.synsets('School')

print(syns[8])
print(syns[8].name())
print(syns[8].lemmas()[0].name()) # only the synonym
print(syns[8].definition())
print(syns[8].examples())


synonyms = []
antonyms = []

for syn in wordnet.synsets('kindness'):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())
        if lemma.antonyms():
            antonyms.append(lemma.antonyms()[0].name())

print(set(synonyms))
print('...............................................')
print(set(antonyms))
