from gensim.models.tfidfmodel import TfidfModel
from gensim.corpora.dictionary import Dictionary
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
#TF IDF คือสูตรที่หาค่าน้ำหนักแต่ละคำใน Document ว่าเจอกี่ เปอร์เซนตั้งแต่ 0-1 สูตรคือ
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
# Create a Dictionary from the articles: dictionary
dictionary = Dictionary(articles)
# Create a Corpus: corpus
corpus = [dictionary.doc2bow(a) for a in articles]
# Save the second document: doc
doc = corpus[0]
#--------------------------------------------------------------
# Create a new TfidfModel using the corpus: tfidf
tfidf = TfidfModel(corpus)
# Calculate the tfidf weights of doc: tfidf_weights
tfidf_weights = tfidf[doc] #เอา document เข้าสูตร TF IDf 
# Print the first five weights
print(tfidf_weights[:5]) # 5 ค่าน้ำหนักแรก แต่ไม่ใช่ 5 คำแรกที่มากที่สุดแต่เป็น 5 คำแรกที่เจอ
#--------------------------------------------------------------
# Sort the weights from highest to lowest: sorted_tfidf_weights
sorted_tfidf_weights = sorted(tfidf_weights, key=lambda w: w[1], reverse=True)
# Print the top 5 weighted words
for term_id, weight in sorted_tfidf_weights[:5]:
    print(dictionary.get(term_id), weight)
# #--------------------------------------------------------------