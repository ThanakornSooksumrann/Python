import re
print(re.match('abcd', 'abcdef'))
#ตัวหน้าคือ Keyword ที่เอาไปค้นหาในฝั่งซ้าย มันจะนับตั้งแต่ตัวแรกที่เจอจนตัวสุดท้าย
#ต้องเป็นตั้งแต่ตัว Character ตัวแรกจนตัวสุดท้ายที่เจอ
print(re.search('abcd', 'abcdef'))
#นับตัวแรกตัวไหนก้ได้ไล่ไปจนตัวสุดท้ายที่เจอ

word_regex = '\w+'
print(re.match(word_regex, 'hi theae!'))
#คือเอาแค่คำภาาาอังกฤษแบบไม่มีตัวเลขหรือตัวอักษรติดมาเลย

print(re.split('\s+', 'Split on spaces.'))
#คือสร้าง Array แล้วแบ่งจากช่องว่าง