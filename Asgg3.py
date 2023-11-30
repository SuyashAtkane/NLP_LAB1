'''
Assignment No: 03 (Spacy)
Name: Suyash S Atkane
Roll: 01
Batch: B1
Title: Implements Named Entity Recognition(NER) on textual data using SpaCy or NLTK library.
'''



import spacy

raw_text=("In the bustling city of Techlandia, Dr. Emily Johnson, a brilliant scientist, unveiled her latest invention at the Quantum Expo. The Quantum Generator, a revolutionary device, promises to transform the way we harness energy."

"As the crowd marveled at the Quantum Generator, Mark Thompson, the CEO of FutureTech Inc., approached Dr. Johnson with a partnership proposal. They discussed the potential applications of the technology in various industries, including renewable energy and telecommunications."

"Meanwhile, Agent Sarah Miller of the top-secret organization CodeGuard observed the proceedings discreetly. She had received intel about a possible attempt to steal the Quantum Generator's blueprints by a group of notorious hackers known as the Binary Bandits."

"During the evening gala, Dr. Johnson was awarded the prestigious Innovation Excellence Award by Mayor Jessica Rodriguez. The event was covered by the leading tech journalist, Alex Turner, who praised Dr. Johnson's contribution to scientific advancements."

"However, little did they know that the Binary Bandits were already plotting their next move. In the shadows, their leader, known as Cipher, devised a plan to infiltrate FutureTech Inc. and steal the Quantum Generator's secrets."

"As the night unfolded, the city of Techlandia became the stage for a high-stakes game of innovation, corporate intrigue, and espionage."
)

NER = spacy.load("en_core_web_sm",disable=["tok2vec", "tagger", "parser", "attribute_ruler", "lemmatizer"])

text = NER(raw_text)

for x in text.ents:
    print(x.text,x.label_)

#spacy.displacy.render(text, style="ent", jupyter=True)

# spacy.explain(u"NORP")


'''
Output-

Techlandia GPE
Emily Johnson PERSON
the Quantum Expo FAC
The Quantum Generator ORG
the Quantum Generator ORG
Mark Thompson PERSON
FutureTech Inc. ORG
Johnson PERSON
Sarah Miller PERSON
CodeGuard ORG
the Quantum Generator's LAW
the Binary Bandits LAW
evening TIME
Johnson PERSON
Innovation Excellence Award ORG
Jessica Rodriguez PERSON
Alex Turner PERSON
Johnson PERSON
the Binary Bandits LAW
Cipher PERSON
FutureTech Inc. ORG
the Quantum Generator's ORG
Techlandia GPE


'''