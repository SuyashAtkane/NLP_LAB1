#Name- Atkane Suyash Santosh
#Batch- B1
#Roll No- 03
#Title-Implement Bag of Words
#Assignment no. - 02

#Import the libraries
#Bag of words-1
import gensim
from gensim import corpora

#Take the input
text1 = ["""I want to go to school . I am going to school now ."""]

tokens1 = [[item for item in line.split()] for line in text1]
g_dict1 = corpora.Dictionary(tokens1)

#Count number of tokens
print("The dictionary has: " +str(len(g_dict1)) + " tokens\n")
print(g_dict1.token2id)

#Bag of words
g_bow =[g_dict1.doc2bow(token, allow_update = True) for token in tokens1]
print("Bag of Words : ", g_bow)

#outout

#The dictionary has: 9 tokens

#{'.': 0, 'I': 1, 'am': 2, 'go': 3, 'going': 4, 'now': 5, 'school': 6, 'to': 7, 'want': 8}
#Bag of Words :  [[(0, 2), (1, 2), (2, 1), (3, 1), (4, 1), (5, 1), (6, 2), (7, 3), (8, 1)]]

#TFIDF-2
import gensim
import pprint
from gensim import corpora
from gensim.utils import simple_preprocess
doc_list = [
   "Hello, how are you?", "How do you do?", 
   "Hey what are you doing? yes you What are you doing?"
]
doc_tokenized = [simple_preprocess(doc) for doc in doc_list]
dictionary = corpora.Dictionary()
BoW_corpus = [dictionary.doc2bow(doc, allow_update=True) for doc in doc_tokenized]
for doc in BoW_corpus:
   print([[dictionary[id], freq] for id, freq in doc])
import numpy as np
tfidf = models.TfidfModel(BoW_corpus, smartirs='ntc')
for doc in tfidf[BoW_corpus]:
   print([[dictionary[id], np.around(freq,decomal=2)] for id, freq in doc])













#Word2vec
from gensim.models.word2vec import Word2Vec
from multiprocessing import cpu_count

data = [
    "Open Visual Studio Code.",
    "Import the NLTK library",
    "Apart from individual data packages",
    "word2vec is a popular word",
]

# Tokenize the text data (split sentences into words)
tokenized_data = [sentence.split() for sentence in data]

# Create a Word2Vec model
w2v_model = Word2Vec(tokenized_data, min_count=0, workers=cpu_count())

# Find the most similar words to 'word'
similar_words = w2v_model.wv.most_similar('word')

for word, score in similar_words:
    print(f"{word}: {score}")
    
#output
#a: 0.21883945167064667
#Apart: 0.21617142856121063
#data: 0.0931011214852333
#NLTK: 0.09291722625494003
#individual: 0.07963486760854721
#from: 0.06285078823566437
#is: 0.05433003976941109
#library: 0.0270574688911438
#the: 0.016134677454829216
#popular: -0.01083916611969471