# Import Counter
from collections import Counter
from nltk.tokenize import word_tokenize
#Read TXT file
f = open("Ch3\wiki_article.txt", "r")
article = f.read()

# Tokenize the article: tokens
tokens = word_tokenize(article)

# Convert the tokens into lowercase: lower_tokens
lower_tokens = [t.lower() for t in tokens]

# Create a Counter with the lowercase tokens: bow_simple
bow_simple = Counter(lower_tokens)

# Print the 10 most common tokens
print(bow_simple.most_common(10))