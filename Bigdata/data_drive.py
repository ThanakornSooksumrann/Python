# -*- coding: utf-8 -*-
"""data_drive.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YUWcOFqyX249iWRmDimaLCZr7txyaV9P
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
path = '/content/drive/MyDrive/Colab Notebooks/dataset/wine_data.csv'
winedata = pd.read_csv(path) ## Dataset is now stored in a Pandas Dataframe
print ("Dataset Lenght:: ", len(winedata))
print ("Dataset Shape:: ", winedata.shape)
print(winedata)

features = ["Cultivator", "Alchol", "Malic_Acid", "Ash", "Alcalinity_of_Ash", "Magnesium", "Total_phenols", "Falvanoids", "Nonflavanoid_phenols", "Proanthocyanins", "Color_intensity", "Hue", "OD280", "Proline"]
winedata = pd.read_csv(path, names = features) #ถ้าถ้อ่านจาก อ่ drive ให้ให้ช้ ตัวแปร ตั path
#winedata = pd.read_csv('wine_data.csv', names = features) #้ถ้าไม่ได้อ่านจากไดรใช้อันนี้
winedata.head()
X = winedata.drop('Cultivator',axis=1)
y = winedata['Cultivator']
print(X)
print(y)

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler #สร้างออบเ ร้ จ็กต์ขึ้ต์ นจากคลาส ขึ้ StandardScaler
ss = StandardScaler() #ข้อข้มูลมู ดิบของ ดิ wine data ผ่านการ ผ่ ทํา data preprocessing แบบ StandardScale
#print(X)
X_scaled = ss.fit_transform(X)
# fit_transform ทํา การคํา นวณค่าเฉ ค่ ลี่ยและ ลี่ ส่วนเ ส่ บี่ยงเบนมาตรฐานของ บี่ ข้อข้มูลมู X และคืนคื ค่าค่ X ที่ทําที่ ทํา ให้เห้ป็นมาตรฐานแล้
print(X_scaled)

from sklearn import preprocessing
X_train = np.array([[ 1, -1, 2],
                            [  2,  0, 6],
                            [  0,  1,-1]])

min_max_scaler = preprocessing.MinMaxScaler()

X_train_minmax = min_max_scaler.fit_transform(X_train)

print(X_train_minmax)

scaler = ss.fit_transform(X_train)
print(scaler)

df = pd.DataFrame({
    'Part': ['Monitor', 'CPU', None, 'Mouse', None, 'Extensions', 'Table', 'Chair', 'Wifi'],
    'Feature': ['LED', 'i7', 'RGB', 'Wireless', 'Zebronics', None, 'Urban Clap', 'Apex Chairs', 'Airtel'],
    'Price': [12000, 3500, None, 1200, None, 250, 7000, 12000, 799]
})
print(df)

df.isnull()

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.NaN, strategy='mean')
# ถ้าถ้มีข้มี อข้มูลมู มีเมีพียงพี 1 มิติมิ ติ(Feature ที่ต้ที่ องการเป ต้ ลี่ยนลี่ มี Column เดียวดี ) ต้องต้ มีการ มี .reshape() ให้อห้ ยู่ในยู่ รูปรู 1 มิติมิ ก่ติอก่
df.Price= imputer.fit_transform(df['Price'].values.reshape(-1,1))[:,0] #-1,1 fix ทำกับ attribute เดียว  ทำให้กลายเป็น 1 มิติ โดยใช้ -1, 1
df

from sklearn.impute import SimpleImputer
print(df)
print()

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=None, strategy='most_frequent') #สังเกตตรง สั missing va

df.Feature= imputer.fit_transform(df['Feature'].values.reshape(-1,1))[:,0]

df.Part= imputer.fit_transform(df['Part'].values.reshape(-1,1))[:,0]

df

students = [[85, 'M', 'verygood'],
                [95, 'F', 'excellent'],
                [75, None,'good'],
                [np.NaN, 'M', 'average'],
                [70, 'M', 'good'],
                [np.NaN, None, 'verygood'],
                [92, 'F', 'verygood'],
                [98, 'M', 'excellent']]
df = pd.DataFrame(students)
df.columns =['score', 'sex', 'score_type']
print (df)

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=None, strategy='most_frequent')

df.sex= imputer.fit_transform(df['sex'].values.reshape(-1,1))[:,0]

df.score_type= imputer.fit_transform(df['score_type'].values.reshape(-1,1))[:,0]

imputer = SimpleImputer(missing_values=np.NaN, strategy='mean')

df.score= imputer.fit_transform(df['score'].values.reshape(-1,1))[:,0]
df

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Put dataset
df = pd.read_csv('https://raw.githubusercontent.com/mGalarnyk/Python_Tutorials/master/Kaggle/BreastCancerWisconsin/data/data.csv')
df

df['area_mean']

sns.boxplot(x=df['area_mean'])

df['area_mean'].quantile(0.25)

df['area_mean'].quantile(0.75)

Q1 = df['area_mean'].quantile(0.25)
Q3 = df['area_mean'].quantile(0.75)
IQR = Q3-Q1
IQR

df['area_mean'].quantile(0.75) #Q3

df['area_mean'].quantile(0.25) #Q1

lower_lim = Q1-1.5*IQR
lower_lim

upper_lim = Q3+1.5*IQR
upper_lim

from scipy.stats.mstats import winsorize
df_area_mean_win = winsorize(df['area_mean'],(0.1, 0.1 ))#(,0.1 = 0.9 และถ้า 0.25 = 0.75)
df_area_mean_win

df_area_mean_win.count()

sns.boxplot(x=df_area_mean_win)

customer = [[5, 'M', 'verygood'],
[20, 'F', 'excellent'],
[30, 'F','good'],
[16, 'M', 'average'],
[70, 'M', 'good'],
[25, 'M', 'verygood'],
[55, 'F', 'verygood'],
[36, 'M', 'excellent']]
df = pd.DataFrame(customer)
df.columns = ['age','sex','type']
df

df['binned']=pd.cut(x=df['age'], bins=[0,14,24,64,100])
df

category = ['Child', 'Young', 'Adults', 'Senior']
df['category']=pd.cut(x=df['age'], bins=[0,14,24,64,100], labels=category)
df

df['bin_freq']=pd.cut(df['age'], 3) #3 bin Min-Max Normalization
df

pd.value_counts(df['bin_freq'])

d = {'age': [18,67,78,67,78,24,25,45, 30,45,34,43, 20,27,28,31, 40, 55],
      'bad_loans': [18,67,78,67,78,24,25,45, 30,45,34,43, 20,27,28,31, 40, 55]}

df = pd.DataFrame(d)
df

category = ['Generation Z','Millennials', 'Generation X', 'Baby Boomers', 'The Silent Generation']

df['category']=pd.cut(x=df['age'], bins=[12,26,41,56,75,100],labels=category)
df

df['bin_freq']=pd.cut(df['age'], 5)
df

pd.value_counts(df['bin_freq'])

df['binned']=pd.cut(x=df['bad_loans'], bins=[0,30,50,100])
df