# Import necessary modules
from operator import length_hint
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

#Read TXT file
f = open("scene_one.txt", "r")
scene_one = f.read()
#print(scene_one)

sentences = sent_tokenize(scene_one)
print(sentences[3])
#ตัดเป็นประโยค

tokenized_sent = word_tokenize(sentences[3])
print(tokenized_sent)
#ตัดเป็นคำ ๆ

unique_tokens = set(word_tokenize(scene_one))
print(len(unique_tokens))
#คำที่ไม่ซ้ำกัน

import re
match = re.search("coconuts",scene_one)
print(match.start(),match.end())
#เจอตั้งแต่ตัวไหนถึงตัวไหน charecter จำนวนในคำ

pattern1 = r"\[.*.\]"
print(re.search(pattern1,scene_one))
#คือเอาคำที่มี สีเหลี่ยมครอบ ทั้งหมด

pattern2 = r"[\w\s]+:"
print(re.match(pattern2, sentences[3]))