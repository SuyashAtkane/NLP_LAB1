#Name- Atkane Suyash Santosh
#Batch- B1
#Roll No- 03
#Title-Implement Bag of Words

#Import the libraries
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