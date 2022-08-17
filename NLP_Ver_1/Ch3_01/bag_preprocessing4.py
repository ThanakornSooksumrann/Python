# Import WordNetLemmatizer
from nltk.stem import WordNetLemmatizer
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#Read TXT file
f = open("Ch3\wiki_article.txt", "r")
article = f.read()

# Tokenize the article: tokens
tokens = word_tokenize(article)

# Convert the tokens into lowercase: lower_tokens ทำตัวเป็นพิมพ์เล็ก
lower_tokens = [t.lower() for t in tokens]

#อันใหม่

# Retain alphabetic words: alpha_only เอาแค่ตัวอัการ
alpha_only = [t for t in lower_tokens if t.isalpha()]

# Remove all stop words: no_stops ไม่เอา Stopword
no_stops = [t for t in alpha_only if t not in stopwords.words('english')]

# Instantiate the WordNetLemmatizer 
wordnet_lemmatizer = WordNetLemmatizer()

# Lemmatize all tokens into a new list: lemmatized root word ทำให้คำเป็นแบบต้นฉบับคือ root word
lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops]

# Create the bag-of-words: bow นับว่าในนั้นแต่ละคำซ้ำกี่ตัว
bow = Counter(lemmatized)

# Print the 10 most common tokens ดูอันดับว่าอันไหนเยอะสุด จะเอากี่อันดับก็ได้
print(bow.most_common(10))