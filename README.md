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
```python

        import nltk

        tokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()

        txt = """ This is one sentence. This is another sentence."""
        tokenizer.tokenize(txt)

[out]: ' This is one sentence.', 'This is another sentence.']
```

Source: [Stackoverflow](https://stackoverflow.com/questions/35275001/use-of-punktsentencetokenizer-in-nltk)


## Chunking
Chunking in NLP is Changing a perception by moving a “chunk”, or a group of bits of information, in the direction of a Deductive or Inductive conclusion through the use of language.

Chunking up or down allows the speaker to use certain language patterns, to utilize the natural internal process through language, to reach for higher meanings or search for more specific bits/portions of missing information.

When we “Chunk Up” the language gets more abstract and there are more chances for agreement, and when we “Chunk Down” we tend to be looking for the specific details that may have been missing in the chunk up.

As an example if you ask the question “for what purpose cars?” you may get the answer “transport”, which is a higher chunk and more toward abstract.

If you asked “what specifically about a car”? you will start to get smaller pieces of information about a car.

Lateral thinking will be the process of chunking up and then looking for other examples: For example “for what intentions cars?”, “transportation”, “what are other examples of transportation?” “Buses!”

Chunking is a process of extracting phrases from unstructured text. Instead of just simple tokens which may not represent the actual meaning of the text, its advisable to use phrases such as “South Africa” as a single word instead of ‘South’ and ‘Africa’ separate words.

Chunking works on top of POS tagging, it uses pos-tags as input and provides chunks as output. Similar to POS tags, there are a standard set of Chunk tags like Noun Phrase(NP), Verb Phrase (VP), etc. Chunking is very important when you want to extract information from text such as Locations, Person Names etc. In NLP called Named Entity Extraction.
