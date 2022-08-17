# from nltk.tokenize import regexp_tokenize
# from nltk.tokenize import TweetTokenizer
# tweets = ['This is the #nlp exercise! #python', '#NLP is super fun! <3 #learning', 'Thanks @fitmkmutnb :) #nlp #python']
# # Define a regex pattern to find hashtags: pattern1

# pattern1 = r"#\w+"
# # Use the pattern on the first tweet in the tweets list
# hashtags = regexp_tokenize(tweets[0], pattern1)
# print(hashtags)
# #คือการหา hashtags

# # Write a pattern that matches both mentions (@) and hashtags
# pattern2 = r"([@#]\w+)" #เช่น #python
# # Use the pattern on the last tweet in the tweets list
# mentions_hashtags = regexp_tokenize(tweets[-1], pattern2)
# print(mentions_hashtags)

# # Use the TweetTokenizer to tokenize all tweets into one list
# tknzr = TweetTokenizer()
# all_tokens = [tknzr.tokenize(t) for t in tweets]
# print(all_tokens)

# from nltk.tokenize import regexp_tokenize
# from nltk.tokenize import word_tokenize
# german_text = "Wann gehen wir Pizza essen? 🍕🍕 Und fährstdu mit Über? 🚕🚕"
# all_words = word_tokenize(german_text)
# print(all_words)

# print("")

# capital_words = r"[A-ZÜ]\w+"
# print(regexp_tokenize(german_text, capital_words))

# print("")

# emoji = "['\U0001F300-\U0001F5FF'|'\U0001F600-\U0001F64F'|'\U0001F680-\U0001F6FF'|'\u2600-\u26FF\u2700-\u27BF']"
# print(regexp_tokenize(german_text, emoji))

# print("")

# from matplotlib import pyplot as plt
# plt.hist([1, 5, 5, 7, 7, 7, 9])
# plt.show()

# print("")

# from matplotlib import pyplot as plt
# from nltk.tokenize import word_tokenize

# words = word_tokenize("This is a pretty cool tool!")
# word_lengths = [len(w) for w in words]
# plt.hist(word_lengths)
# plt.show()

print("")
import re
from nltk.tokenize import regexp_tokenize
from matplotlib import pyplot as plt
#Read TXT file
f = open("Ch2\holy_grail.txt", "r")
holy_grail = f.read()

# Split the script into lines: lines
lines = holy_grail.split('\n')

print("")

# Replace all script lines for speaker
pattern = "[A-Z]{2,}(\s)?(#\d)?([A-Z]{2,})?:"
lines = [re.sub(pattern,'', l) for l in lines]

# Tokenize each line: tokenized_lines
tokenized_lines = [regexp_tokenize(s,"\w+") for s in lines]
print(tokenized_lines)

# Make a frequency list of lengths: line_num_words
line_num_words = [len(t_line) for t_line in tokenized_lines]
plt.hist(line_num_words, color="c")
plt.show()