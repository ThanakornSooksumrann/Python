ทำการติดตั้ง 
# Web
pip install Flask
pip install markdown
pip install Flask-Markdown
# NLP
pip install gensim
pip install nltk
pip install itertools
pip install spacy
# เป็น Model SpyCy ที่ถูก Train มาแต่ละขนาด ขนาดยิ่งใหญ่ยิ่งจับ tag highlight ในข้อความได้เยอะ
# ในไฟล์โค้ดที่ชื่อ upload.py ใช้ขนาดนี้อยู่ "en_core_web_lg" แต่สามารถไปแก้เป็นขนาดเล็กกว่านี้ได้ถ้าจะใช้ขนาดอื่นสามารถไปแก้ได้
# แก้ได้ที่ส่วนบนของไฟล์โค้ดชื่อ upload.py ในส่วนที่เขียนว่า nlp = spacy.load("แก้ขนาดตรงส่วนนี้")
python -m spacy download en_core_web_sm # ขนาด 12 MB
python -m spacy download en_core_web_md # ขนาด 40 MB 
python -m spacy download en_core_web_lg # ขนาด 560 MB

และสามารถกด Run ได้เลย โดยไปที่ ไฟล์ upload.py แล้วกด ctrl + F5 หรือ กด Run Terminal ที่ VS Code ได้เลย
