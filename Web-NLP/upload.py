#Web
from flask import Flask, render_template, request
import os, shutil
#NLP
from gensim.models.tfidfmodel import TfidfModel
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from gensim.corpora.dictionary import Dictionary
from collections import defaultdict
import itertools

app = Flask(__name__)

#****Path ของเครื่องตัวเอง C:/Users/ชื่อเครื่องตัวเอง/Desktop/Web-NLP/uploads****
app.config["UPLOAD_PATH"] = "C:/Users/thana/Desktop/Web-NLP/uploads"
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/upload_file", methods=["GET","POST"])
def upload_file():
	if request.method == 'POST' and len(request.files.getlist('file_name')) != 0:
    	#ลบไฟล์ในโฟลเดอร์ uploads ทั้งหมดเพื่อที่ตอนรูปอ่านชื่อไฟล์ในโฟลเดอร์จะได้ไม่ไปอ่านของเก่าด้วย
		#****Path ของเครื่องตัวเอง C:/Users/ชื่อเครื่องตัวเอง/Desktop/Web-NLP/uploads****
		for filename in os.listdir('C:/Users/thana/Desktop/Web-NLP/uploads'):
			file_path = os.path.join('C:/Users/thana/Desktop/Web-NLP/uploads', filename)
			try:
				if os.path.isfile(file_path) or os.path.islink(file_path):
					os.unlink(file_path)
				elif os.path.isdir(file_path):
					shutil.rmtree(file_path)
			except Exception as e:
				gg = 0
		#เซฟไฟล์ที่
		for f in request.files.getlist('file_name') :
			f.save(os.path.join(app.config["UPLOAD_PATH"],f.filename))
		#ทำการอ่านไฟล์ใน Folder uploads ทั้งหมด
		#****Path ของเครื่องตัวเอง C:/Users/ชื่อเครื่องตัวเอง/Desktop/Web-NLP/uploads****
		directory = 'C:/Users/thana/Desktop/Web-NLP/uploads'
		articles = []
		for i in os.listdir(directory) :
    		#****Path ของเครื่องตัวเอง C:/Users/ชื่อเครื่องตัวเอง/Desktop/Web-NLP/uploads****
			f = open(r'C:/Users/thana/Desktop/Web-NLP/uploads/'+str(i),"r")
			article = f.read()
			tokens = word_tokenize(article)
			lower_tokens = [t.lower() for t in tokens]
			alpha_only = [t for t in lower_tokens if t.isalpha()]
			no_stops = [t for t in alpha_only if t not in stopwords.words('english')]
			wordnet_lemmatizer = WordNetLemmatizer()
			lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops]
			articles.append(lemmatized)
		dictionary = Dictionary(articles)
		corpus = [dictionary.doc2bow(a) for a in articles]
		#bow
		total_word_count = defaultdict(int)
		for word_id, word_count in itertools.chain.from_iterable(corpus):
			total_word_count[word_id] += word_count
		sorted_word_count = sorted(total_word_count.items(), key=lambda w: w[1],reverse=True)
		#tfidf
		tfidf = TfidfModel(corpus)
		tfidf_weights = []
		for doc in corpus : tfidf_weights+=(tfidf[doc])
		top_tfidf = []
		sorted_tfidf_weights = sorted(tfidf_weights, key=lambda w: w[1], reverse=True)
		for term_id, weight in sorted_tfidf_weights[:5]:
			top_tfidf.append(f'{dictionary.get(term_id)}, {weight}')
		return render_template("index.html",top_word = sorted_word_count[:5],dictionary = dictionary, top_tfidf = top_tfidf)
	return render_template("index.html",msg="Please Choose a file")

@app.route('/search_word', methods=["GET","POST"])
def search_word():
    #****Path ของเครื่องตัวเอง C:/Users/ชื่อเครื่องตัวเอง/Desktop/Web-NLP/uploads****
	directory = 'C:/Users/thana/Desktop/Web-NLP/uploads'
	key_word = request.form['key_word']
	articles = []
	for i in os.listdir(directory) :
    	#****Path ของเครื่องตัวเอง C:/Users/ชื่อเครื่องตัวเอง/Desktop/Web-NLP/uploads****
		f = open(r'C:/Users/thana/Desktop/Web-NLP/uploads/'+str(i),"r")
		article = f.read()
		tokens = word_tokenize(article)
		lower_tokens = [t.lower() for t in tokens]
		alpha_only = [t for t in lower_tokens if t.isalpha()]
		no_stops = [t for t in alpha_only if t not in stopwords.words('english')]
		wordnet_lemmatizer = WordNetLemmatizer()
		lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops]
		articles.append(lemmatized)
	dictionary = Dictionary(articles)
	result_word = dictionary.token2id.get(key_word)
	bool_search = True
	if result_word == None :
		bool_search = False
	corpus = [dictionary.doc2bow(a) for a in articles]
	total_word_count = defaultdict(int)
	for word_id, word_count in itertools.chain.from_iterable(corpus):
		total_word_count[word_id] += word_count
	sorted_word_count = sorted(total_word_count.items(), key=lambda w: w[1],reverse=True)
	#tfidf
	tfidf = TfidfModel(corpus)
	tfidf_weights = []
	for doc in corpus : tfidf_weights+=(tfidf[doc])
	top_tfidf = []
	sorted_tfidf_weights = sorted(tfidf_weights, key=lambda w: w[1], reverse=True)
	for term_id, weight in sorted_tfidf_weights[:5]:
		top_tfidf.append(f'{dictionary.get(term_id)}, {weight}')	
	return render_template("index.html",top_word = sorted_word_count[:5],dictionary = dictionary,bool_search = bool_search,result_word = result_word, key_word = key_word, top_tfidf = top_tfidf)

if __name__ == "__main__":
	app.run(debug=True)