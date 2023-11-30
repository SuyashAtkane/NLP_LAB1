'''
Name- Suyash S Atkane
Roll no- 03
Batch- B1
Practical no.6 -Implement Dependency Parsing of textual input using spacy library.
'''







import spacy
nlp = spacy.load("en_core_web_sm")
piano_text = """The quick brown fox jumped over the lazy dog.
                The dog that chased the cat is black
                I saw the man that you saw on the street"""
piano_doc = nlp(piano_text)
for token in piano_doc:
    print(
        f"""
TOKEN: {token.text}
=====
{token.tag_ = }
{token.head.text = }
{token.dep_ = }"""
    )


'''
Output-

TOKEN: The
=====
token.tag_ = 'DT'
token.head.text = 'fox'
token.dep_ = 'det'

TOKEN: quick
=====
token.tag_ = 'JJ'
token.head.text = 'fox'
token.dep_ = 'amod'

TOKEN: brown
=====
token.tag_ = 'JJ'
token.head.text = 'fox'
token.dep_ = 'amod'

TOKEN: fox
=====
token.tag_ = 'NN'
token.head.text = 'jumped'
token.dep_ = 'nsubj'

TOKEN: jumped
=====
token.tag_ = 'VBD'
token.head.text = 'jumped'
token.dep_ = 'ROOT'

TOKEN: over
=====
token.tag_ = 'IN'
token.head.text = 'jumped'
token.dep_ = 'prep'

TOKEN: the
=====
token.tag_ = 'DT'
token.head.text = 'dog'
token.dep_ = 'det'

TOKEN: lazy
=====
token.tag_ = 'JJ'
token.head.text = 'dog'
token.dep_ = 'amod'

TOKEN: dog
=====
token.tag_ = 'NN'
token.head.text = 'over'
token.dep_ = 'pobj'

TOKEN: .
=====
token.tag_ = '.'
token.head.text = 'jumped'
token.dep_ = 'punct'

TOKEN:

=====
token.tag_ = '_SP'
token.head.text = '.'
token.dep_ = 'dep'

TOKEN: The
=====
token.tag_ = 'DT'
token.head.text = 'dog'
token.dep_ = 'det'

TOKEN: dog
=====
token.tag_ = 'NN'
token.head.text = 'is'
token.dep_ = 'nsubj'

TOKEN: that
=====
token.tag_ = 'WDT'
token.head.text = 'chased'
token.dep_ = 'nsubj'

TOKEN: chased
=====
token.tag_ = 'VBD'
token.head.text = 'dog'
token.dep_ = 'relcl'

TOKEN: the
=====
token.tag_ = 'DT'
token.head.text = 'cat'
token.dep_ = 'det'

TOKEN: cat
=====
token.tag_ = 'NN'
token.head.text = 'chased'
token.dep_ = 'dobj'

TOKEN: is
=====
token.tag_ = 'VBZ'
token.head.text = 'saw'
token.dep_ = 'ccomp'

TOKEN: black
=====
token.tag_ = 'JJ'
token.head.text = 'is'
token.dep_ = 'acomp'

TOKEN:

=====
token.tag_ = '_SP'
token.head.text = 'black'
token.dep_ = 'dep'

TOKEN: I
=====
token.tag_ = 'PRP'
token.head.text = 'saw'
token.dep_ = 'nsubj'

TOKEN: saw
=====
token.tag_ = 'VBD'
token.head.text = 'saw'
token.dep_ = 'ROOT'

TOKEN: the
=====
token.tag_ = 'DT'
token.head.text = 'man'
token.dep_ = 'det'

TOKEN: man
=====
token.tag_ = 'NN'
token.head.text = 'saw'
token.dep_ = 'dobj'

TOKEN: that
=====
token.tag_ = 'WDT'
token.head.text = 'saw'
token.dep_ = 'dobj'

TOKEN: you
=====
token.tag_ = 'PRP'
token.head.text = 'saw'
token.dep_ = 'nsubj'

TOKEN: saw
=====
token.tag_ = 'VBD'
token.head.text = 'man'
token.dep_ = 'relcl'

TOKEN: on
=====
token.tag_ = 'IN'
token.head.text = 'saw'
token.dep_ = 'prep'

TOKEN: the
=====
token.tag_ = 'DT'
token.head.text = 'street'
token.dep_ = 'det'

TOKEN: street
=====
token.tag_ = 'NN'
token.head.text = 'on'
token.dep_ = 'pobj'
'''