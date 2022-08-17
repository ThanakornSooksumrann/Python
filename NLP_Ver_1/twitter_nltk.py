# -*- coding: utf-8 -*-
"""Twitter_NLTK.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1I-2pdvgouxPsgUJ96jlwlbgLIAm2bvDl
"""

import nltk                              
from nltk.corpus import twitter_samples    
import matplotlib.pyplot as plt            
import random      
import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize

nltk.download('twitter_samples')
nltk.download('punkt') 
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

all_positive_tweets = twitter_samples.strings('positive_tweets.json')
all_negative_tweets = twitter_samples.strings('negative_tweets.json')

df = pd.DataFrame(all_positive_tweets,columns=['Tweets'])
df

tweetText = df['Tweets']
df['Token'] = tweetText.apply(word_tokenize)
df

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def stop_word(text):
  stop_words = set(stopwords.words('english'))

  filtered_sentence = []

  for w in text:
    if w not in stop_words:
      filtered_sentence.append(w)

  return(filtered_sentence)

df['Stop_Word'] = df['Token'].apply(stop_word)
df

nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag

wordnet = WordNetLemmatizer()

def Lemma(tokens):
  filtered_sentence = [] 
  for token,tag in pos_tag(tokens):
      pos=tag[0].lower()

      if pos not in ['a', 'r', 'n', 'v']:
          pos='n'

      filtered_sentence.append(wordnet.lemmatize(token,pos))
  return filtered_sentence

df['Lemmatization'] = df['Token'].apply(Lemma)
df

from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 

ps = PorterStemmer()
tweetText = df['Tweets']
df["Token"]  = tweetText.apply(word_tokenize)
def Stem(Name):
  ps = PorterStemmer()
  sent = Name
  ps_sent = [ps.stem(words_sent) for words_sent in sent]
 
  return  ps_sent

df["Porter_Stemmer"]  = df['Token'].apply(Stem)
df