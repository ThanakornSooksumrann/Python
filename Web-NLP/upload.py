#Web
from flask import Flask, render_template, request, url_for
import os, shutil
from flaskext.markdown import Markdown
#NLP
from gensim.models.tfidfmodel import TfidfModel
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from gensim.corpora.dictionary import Dictionary
from collections import defaultdict
import itertools
import spacy
from spacy import displacy
#current location file
from werkzeug.utils import secure_filename
import pathlib

app = Flask(__name__)
Markdown(app)
app.config["UPLOAD_PATH"] = f"{str(pathlib.Path(__file__).parent.resolve().as_posix())}/uploads/"
# สามารถแก้ขนาด Model SpyCy ได้ที่ตรงนี้ nlp = spacy.load("แก้ขนาดตรงส่วนนี้")
nlp = spacy.load("en_core_web_sm") #en_core_web_lg(560MB), en_core_web_md(40MB), en_core_web_sm(12MB)
bo = False
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/upload_file", methods=["GET","POST"])
def upload_file():
	if request.method == 'POST' and len(request.files.getlist('file_name')) != 0:
		path = f"{str(pathlib.Path(__file__).parent.resolve().as_posix())}/uploads/"
		for file in os.listdir(path) :
			try:
				if os.path.isfile(path+file) or os.path.islink(path+file):
					os.unlink(path+file)
				elif os.path.isdir(path+file):
					shutil.rmtree(path+file)
			except Exception as e:
				gg = 0
		#เซฟไฟล์ที่
		files = request.files.getlist('file_name')
		for file in files :
			filename = secure_filename(file.filename)
			path = f"{str(pathlib.Path(__file__).parent.resolve().as_posix())}/uploads/{filename}"
			file.save(path)

		articles = []
		result_spy = ""
		for file in files :
			filename = secure_filename(file.filename)
			path = f"{str(pathlib.Path(__file__).parent.resolve().as_posix())}/uploads/{filename}"
			f = open(path,"r")
			article = f.read()
			tokens = word_tokenize(article)
			lower_tokens = [t.lower() for t in tokens]
			alpha_only = [t for t in lower_tokens if t.isalpha()]
			no_stops = [t for t in alpha_only if t not in stopwords.words('english')]
			wordnet_lemmatizer = WordNetLemmatizer()
			lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops]
			articles.append(lemmatized)
			#spacy
			doc = nlp(article)
			text_html = displacy.render(doc, style="ent", page="true")
			text_html = text_html.replace("\n\n","\n")
			text_html = text_html.replace("<!DOCTYPE html>","")
			result_spy += text_html
		bo = True
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
		return render_template("index.html",top_word = sorted_word_count[:5],dictionary = dictionary, top_tfidf = top_tfidf, result_spy = result_spy, bo = bo)
	return render_template("index.html",msg="Please Choose a file")

@app.route('/search_word', methods=["GET","POST"])
def search_word():
	path = f"{str(pathlib.Path(__file__).parent.resolve().as_posix())}/uploads/"
	key_word = request.form['key_word']
	articles = []
	result_spy = ""
	for file in os.listdir(path) :
		f = open(path+file,"r")
		article = f.read()
		tokens = word_tokenize(article)
		lower_tokens = [t.lower() for t in tokens]
		alpha_only = [t for t in lower_tokens if t.isalpha()]
		no_stops = [t for t in alpha_only if t not in stopwords.words('english')]
		wordnet_lemmatizer = WordNetLemmatizer()
		lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops]
		articles.append(lemmatized)
		#spacy
		doc = nlp(article)
		text_html = displacy.render(doc, style="ent", page="true")
		text_html = text_html.replace("\n\n","\n")
		text_html = text_html.replace("<!DOCTYPE html>","")
		result_spy += text_html
	bo = True
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
	return render_template("index.html",top_word = sorted_word_count[:5],dictionary = dictionary,bool_search = bool_search,result_word = result_word, key_word = key_word, top_tfidf = top_tfidf,result_spy = result_spy, bo = bo)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)