from ast import pattern
import re
my_string = "Let's write RegEx!  Won't that be fun?  I sure think so.  Can you find 4 sentences?  Or perhaps, all 19 words?"
patterns1 = r"[.!?]"

print(re.split(patterns1,my_string))
#คือแบ่งประโยคจาก . ! ? สามตัวนี้และสร้างเป็น Array

patterns2 = r"[A-Z]\w+"
print(re.findall(patterns2,my_string))
#เอาแค่ตัวพิมพ์ใหญ่ที่อยู่ข้างหน้า

patterns3 = r"\s+"
print(re.split(patterns3,my_string))
#ตัดจากช่องว่าง

patterns4 = r"\d+"
print(re.findall(patterns4,my_string))
#เอาตัวเลข