'''Name:Suyash Atkane
Batch:B1
Roll no:03
Pract no 4: Generating the n gram model using nltk'''
from nltk import ngrams

from nltk.util import ngrams

# unigram model
n = 1
sentence = 'In natural language processing (NLP), a unigram model is a language model that assumes each token is independent of the tokens before it. '
unigrams = ngrams(sentence.split(), n)

for item in unigrams:
    print(item)
# bigram model
n = 2
sentence = 'In natural language processing (NLP), a bigram is a two-word sequence.'
unigrams = ngrams(sentence.split(), n)

for item in unigrams:
    print(item)
# trigram model
n = 3
sentence = 'A trigram model in Natural Language Processing (NLP) is a three-word sequence of words. '
unigrams = ngrams(sentence.split(), n)

for item in unigrams:
    print(item)

# using text file input
from nltk import ngrams

file = open("/home/exam/Desktop/NLP_LAB75/al.txt")
for i in file.readlines():
    cumulative = i
    sentences = i.split(".")
    counter = 0
    for sentence in sentences:
        print("For sentence", counter + 1, ", trigrams are: ")
        trigrams = ngrams(sentence.split(" "), 3)
        for grams in trigrams:
            print(grams)
        counter += 1
        print()

# output
'''
#unigram
('In',)
('natural',)
('language',)
('processing',)
('(NLP),',)
('a',)
('unigram',)
('model',)
('is',)
('a',)
('language',)
('model',)
('that',)
('assumes',)
('each',)
('token',)
('is',)
('independent',)
('of',)
('the',)
('tokens',)
('before',)
('it.',)

#Bigram
('In', 'natural')
('natural', 'language')
('language', 'processing')
('processing', '(NLP),')
('(NLP),', 'a')
('a', 'bigram')
('bigram', 'is')
('is', 'a')
('a', 'two-word')
('two-word', 'sequence.')

#Trigram
('A', 'trigram', 'model')
('trigram', 'model', 'in')
('model', 'in', 'Natural')
('in', 'Natural', 'Language')
('Natural', 'Language', 'Processing')
('Language', 'Processing', '(NLP)')
('Processing', '(NLP)', 'is')
('(NLP)', 'is', 'a')
('is', 'a', 'three-word')
('a', 'three-word', 'sequence')
('three-word', 'sequence', 'of')
('sequence', 'of', 'words.')

'''
