# -*- coding: utf-8 -*-
"""Thanakorn_scrap.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ur6S6CGDtMSjS19KalRi-wS6kp9J6cqL
"""

pip install bs4

pip install songline

pip install requests

pip install pandas

pip install openpyxl

import pandas as pd
import bs4
import requests
import openpyxl

page = 1
name_list = []
genre_list = []
rating_list = []
down_list = []
size_list = []
while page <= 126:
  data = requests.get('https://roms-download.com/roms/gameboy-advance/'+str(page)+'-page')
  soup = bs4.BeautifulSoup(data.text)
  v = 0
  for c in soup.find_all('tr'):
    if v != 0:
      name_list.append(c.find('td',{'class':'mobile-14'}).find('a').text.replace(' ',''))
      genre_list.append(c.find('td',{'class':'hidden-xs'}).text.replace(' ',''))
      temp=c.findAll('td')
      rating_list.append(temp[2].text.replace(' ',''))
      temp=c.findAll('td')
      down_list.append(temp[3].text.replace(' ',''))
      temp=c.findAll('td')
      size_list.append(temp[4].text.replace(' ',''))
    v+=1
  print('Complete page number:',page)
  page+=1
table = pd.DataFrame([name_list, genre_list, rating_list, down_list, size_list]).transpose()
table.columns = ['name', 'genre', 'rating', 'download', 'size']
table.set_index('name')
table.to_excel('All Game Boy Advance.xlsx', engine='openpyxl')

def All_game(row):
  text = f'\nชื่อเกม : {name_list[row-1]} \nประเภทเกม : {genre_list[row-1]} Rating : {rating_list[row-1]} ยอดดาวน์โหลด : {down_list[row-1]} ขนาดเกม : {size_list[row-1]} '
  return text
print(All_game(1))

import songline
token = 'nAoODTQCcSwrsSb1d16RqeuKlXx2LvNJOEa4n05zsbi'
messenger = songline.Sendline(token)
messenger.sendtext(All_game(1))
messenger.sendimage('https://roms-download.com/imgs/roms/gameboy-advance/p/pokemon-emerald-version-usa.jpg')