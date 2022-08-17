from nltk.tokenize import word_tokenize
from collections import Counter
counter = Counter(word_tokenize("""The cat is in the box.
The cat likes the box. The box is over the cat."""))
print(counter)

count = counter.most_common(5)
print(count)