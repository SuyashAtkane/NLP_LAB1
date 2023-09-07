#Assignment 1
#Name-Atkane Suyash Santosh
#Batch- B1
#Roll no-03
#Title - Implement tokenization, stopwords, lemmatization &POS

#Lemmatization
#import the libray
import spacy
nlp = spacy.load("en_core_web_sm")
#take the input
conference_help_text = (
    "Gus is helping organize a developer"
    " conference on Applications of Natural Language"
    " Processing. He keeps organizing local Python meetups"
    " and several internal talks at his workplace."
)
conference_help_doc = nlp(conference_help_text)
for token in conference_help_doc:
    if str(token) != str(token.lemma_):
        print(f"{str(token):>20} : {str(token.lemma_)}")

#Output for lemmatization
#is : be
#He : he
#keeps : keep
#organizing : organize
#meetups : meetup
#talks : talk

#Part of Speech
about_text = (
    "Gus Proto is a Python developer currently"
    " working for a London-based Fintech"
    " company. He is interested in learning"
    " Natural Language Processing."
)
about_doc = nlp(about_text)
for token in about_doc:
    print(
        f"""
TOKEN: {str(token)}
=====
TAG: {str(token.tag_):10} POS: {token.pos_}
EXPLANATION: {spacy.explain(token.tag_)}"""
    )

#output for POS


#Stop_words
spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
len(spacy_stopwords)

for stop_word in list(spacy_stopwords)[:10]:
    print(stop_word)
custom_about_text = (
    "Gus Proto is a Python developer currently"
    " working for a London-based Fintech"
    " company. He is interested in learning"
    " Natural Language Processing."
)
about_doc = nlp(custom_about_text)
print([token for token in about_doc if not token.is_stop])

#Output 
#[Gus, Proto, Python, developer, currently, working, London, -, based, Fintech, company, ., interested, learning, Natural, Language, Processing, .]

#Tokkenization

about_text = (
    "Gus Proto is a Python developer currently"
    " working for a London-based Fintech"
    " company. He is interested in learning"
    " Natural Language Processing."
)
about_doc = nlp(about_text)

for token in about_doc:
    print (token, token.idx)

#Output
#Gus 0
#Proto 4
#is 10
#a 13
# python 15
# developer 22
# currently 32
# working 42
# for 50
# a 54
# London 56
# - 62
# based 63
# Fintech 69
# company 77
# . 84
# He 86
# is 89
# interested 92
# in 103
# learning 106
# Natural 115
# Language 123
# Processing 132
# . 142





