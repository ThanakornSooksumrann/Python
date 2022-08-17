from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from gensim.corpora.dictionary import Dictionary
from collections import defaultdict
import itertools

articles = []
for i in range(10) :
    #Read TXT file
    f = open(f".\wiki\wiki_article_{i}.txt", "r")
    article = f.read()
    # Tokenize the article: tokens
    tokens = word_tokenize(article)
    # Convert the tokens into lowercase: lower_tokens
    lower_tokens = [t.lower() for t in tokens]
    # Retain alphabetic words: alpha_only
    alpha_only = [t for t in lower_tokens if t.isalpha()]
    # Remove all stop words: no_stops
    no_stops = [t for t in alpha_only if t not in stopwords.words('english')]
    # Instantiate the WordNetLemmatizer
    wordnet_lemmatizer = WordNetLemmatizer()
    # Lemmatize all tokens into a new list: lemmatized
    lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops]
    #list_article
    articles.append(lemmatized)
# print(articles[1])
#--------------------------------------------------------------
# Create a Dictionary from the articles: dictionary
dictionary = Dictionary(articles)
print(dictionary)
#--------------------------------------------------------------
# Select the id for "computer": computer_id ใช้กับพวก Search Engine ShopHee
computer_id = dictionary.token2id.get("computer") # ค้นหาคำใน Dictionary
# Use computer_id with the dictionary to print the word
print(computer_id) #จะแสดงไอดีที่ค้นเจอถ้าไม่เจอจะขึ้น Non
print(dictionary.get(computer_id)) #แปลงไอดีคำใน Dictionary นั้นที่เราเอามาแปลงเป็นคำเดิม
#--------------------------------------------------------------
corpus = [dictionary.doc2bow(a) for a in articles] # loop เพื่อดูว่าแต่ละคำใน Arcticles มีคำไหนในไอดีไหนของ Dictionary เช่น คำที่ 424 มี 2 ตัว
print(corpus)
#--------------------------------------------------------------
# Save the second document: doc
doc = corpus[0] #corpus คือเอกสารทั้งหมดเรามี 10 ถ้าใส่ 1 ก็คือเอกสารที่ 1
# Sort the doc for frequency: bow_doc
bow_doc = sorted(doc, key=lambda w: w[1], reverse=True) #Back of word ก็คือ Reverse True คือ มากไปน้อย False คือ น้อยไปมาก
#--------------------------------------------------------------
# Print the top 5 words of the document alongside the count
for word_id, word_count in bow_doc[:10]: #แสดง top 10 คำที่เจอเยอะที่สุด
    print(dictionary.get(word_id), word_count)
print('')
#--------------------------------------------------------------
# Create the defaultdict: total_word_count
total_word_count = defaultdict(int) #สร้าง List Dictionary เปล่า ๆ มาใส่ Corpus ที่มีหลายเอกสารรวมเข้าด้วยกัน
for word_id, word_count in itertools.chain.from_iterable(corpus):
    total_word_count[word_id] += word_count
#--------------------------------------------------------------
# Create a sorted list from the defaultdict: sorted_word_count
sorted_word_count = sorted(total_word_count.items(), key=lambda w: w[1],reverse=True)
# Print the top 5 words across all documents alongside the count
for word_id, word_count in sorted_word_count[:10]: #แสดงของทุกเอกสารรวมกันว่าเจอคำไหนมากสุด
    print(dictionary.get(word_id), word_count)
#--------------------------------------------------------------
#TF IDF
from gensim.models.tfidfmodel import TfidfModel
tfidf = TfidfModel(corpus)
print(tfidf[corpus[0]])
#--------------------------------------------------------------