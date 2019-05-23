# Natural Language Processing

## Tokenization

Tokenization is the act of breaking up a sequence of strings into pieces such as words, keywords, phrases, symbols and other elements called tokens. Tokens can be individual words, phrases or even whole sentences. In the process of tokenization, some characters like punctuation marks are discarded. The tokens become the input for another process like parsing and text mining.

**Tokenization** relies mostly on simple heuristics in order to separate tokens by following a few steps:

Tokens or words are separated by whitespace, punctuation marks or line breaks
White space or punctuation marks may or may not be included depending on the need
All characters within contiguous strings are part of the token. Tokens can be made up of all alpha characters, alphanumeric characters or numeric characters only.
Tokens themselves can also be separators. For example, in most programming languages, identifiers can be placed together with arithmetic operators without white spaces. Although it seems that this would appear as a single word or token, the grammar of the language actually considers the mathematical operator (a token) as a separator, so even when multiple tokens are bunched up together, they can still be separated via the mathematical operator.

## Stopwords

In computer search engines, a stop word is a commonly used word (such as "the") that a search engine has been programmed to ignore, both when indexing entries for searching and when retrieving them as the result of a search query. When building the index, most engines are programmed to remove certain words from any index entry. The list of words that are not to be added is called a stop list. Stop words are deemed irrelevant for searching purposes because they occur frequently in the language for which the indexing engine has been tuned. In order to save both space and time, these words are dropped at indexing time and then ignored at search time.

## [Stemming and Lemmetization](https://nlp.stanford.edu/IR-book/html/htmledition/stemming-and-lemmatization-1.html)




## [POS-Tagging](https://nlp.stanford.edu/software/tagger.html)

In corpus linguistics, [part-of-speech tagging](https://medium.freecodecamp.org/an-introduction-to-part-of-speech-tagging-and-the-hidden-markov-model-953d45338f24) (POS tagging or PoS tagging or POST), also called grammatical tagging or word-category disambiguation, is the process of marking up a word in a text (corpus) as corresponding to a particular part of speech, based on both its definition and its context — i.e., its relationship with adjacent and related words in a phrase, sentence, or paragraph. A simplified form of this is commonly taught to school-age children, in the identification of words as nouns, verbs, adjectives, adverbs, etc.


PunktSentenceTokenizer is an sentence boundary detection algorithm that must be trained to be used [1]. NLTK already includes a pre-trained version of the PunktSentenceTokenizer.

So if you use initialize the tokenizer without any arguments, it will default to the pre-trained version:

`<import nltk

tokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()

txt = """ This is one sentence. This is another sentence."""
tokenizer.tokenize(txt)

[out]:[' This is one sentence.', 'This is another sentence.']>`
