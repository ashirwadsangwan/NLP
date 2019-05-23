import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

text = 'Tokens themselves can also be separators. For example, in most programming languages, identifiers can be placed together with arithmetic operators without white spaces.'

print(sent_tokenize(text))
print(word_tokenize(text))
