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
import pprint
import numpy as np
from gensim import corpora,models
from gensim.utils import simple_preprocess
text = ["The food is excellent but the service can be better",
        "The food is always delicious and loved the service",
        "The food was mediocre and the service was terrible"]

g_dict = corpora.Dictionary([simple_preprocess(line) for line in text])
g_bow = [g_dict.doc2bow(simple_preprocess(line)) for line in text]

print("Dictionary : ")
for item in g_bow:
    print([[g_dict[id], freq] for id, freq in item])

g_tfidf = models.TfidfModel(g_bow, smartirs='ntc')
print(" ")
print("TF-IDF Vector:")
for item in g_tfidf[g_bow]:
    print([[g_dict[id], np.around(freq, decimals=2)] for id, freq in item])
    
    
#output
#Dictionary : 
#[['be', 1], ['better', 1], ['but', 1], ['can', 1], ['excellent', 1], ['food', 1], ['is', 1], ['service', 1], ['the', 2]]
#[['food', 1], ['is', 1], ['service', 1], ['the', 2], ['always', 1], ['and', 1], ['delicious', 1], ['loved', 1]]
#[['food', 1], ['service', 1], ['the', 2], ['and', 1], ['mediocre', 1], ['terrible', 1], ['was', 2]]
#TF-IDF Vector:
#[['be', 0.43], ['better', 0.43], ['but', 0.43], ['can', 0.43], ['excellent', 0.43], ['food', 0.09], ['is', 0.21], ['service', 0.09], ['the', 0.18]]
#[['food', 0.11], ['is', 0.26], ['service', 0.11], ['the', 0.21], ['always', 0.52], ['and', 0.26], ['delicious', 0.52], ['loved', 0.52]]
#[['food', 0.08], ['service', 0.08], ['the', 0.16], ['and', 0.2], ['mediocre', 0.39], ['terrible', 0.39], ['was', 0.78]]













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
