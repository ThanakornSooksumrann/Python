# -*- coding: utf-8 -*-
"""Porter and Snowball NLTK.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Eu1LkbqOP-H9lkDjRSUzQoQ-XIXJpn6W
"""

import nltk
nltk.download('punkt') 
nltk.download('averaged_perceptron_tagger') 
nltk.download('stopwords')

from nltk.stem import PorterStemmer 
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize 
   
ps = PorterStemmer()
sb = SnowballStemmer("english")
sentence = "It’s like you’re really standing there,” said Baptiste Chide, a planetary scientist who studies data from the microphones at L’Institut de Recherche en Astrophysique et Planétologie in France. “Martian sounds have strong bass vibrations, so when you put on headphones, you can really feel it. I think microphones will be an important asset to future Mars and solar system science."

sent = word_tokenize(sentence)
print("Before Word Tokenization:\n",sent)
print("Total No of Word Tokens: ",len(sent))
print()
ps_sent = [ps.stem(words_sent) for words_sent in sent]
print("After doing Porter Stemmer ")
print(ps_sent)
print(len(ps_sent))
print()
sb_sent = [sb.stem(words_sent) for words_sent in sent]
print("After doing Snow Ball")
print(sb_sent)
print(len(sb_sent))