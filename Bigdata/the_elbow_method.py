# -*- coding: utf-8 -*-
"""The Elbow Method.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1at7N_jFmSK_T_mqjwg2s53Cy3CECofW5

## **ข้อ 1**
"""

import pandas as pd
import os 
import pandas as pd
from google.colab import files
import io
uploaded = files.upload()
ecoli = pd.read_csv(io.BytesIO(uploaded['ecoli.csv']))
ecoli.tail()

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
points = ecoli.iloc[:, :].values
x = points[:,0]
y = points[:,4]
plt.scatter(x, y, s=50, alpha=0.7)
plt.xlabel('mcg')
plt.ylabel('acc')

from sklearn.cluster import KMeans
points = ecoli.iloc[:, :].values
inertia = []
for i in range(1, 15):
    kmeans = KMeans(n_clusters = i,  max_iter = 300, random_state = 0)
    kmeans.fit(points)
    inertia.append(kmeans.inertia_)
plt.plot(range(1, 15), inertia,'bx-')
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=7, random_state=0)
kmeans.fit(points)
ecoli['Cluster'] = kmeans.labels_
ecoli

kmeans.labels_

kmeans.cluster_centers_

kmeans.inertia_

from sklearn.decomposition import PCA
pca = PCA(n_components=2).fit(ecoli)
pca_2d = pca.transform(ecoli)
newecoli = pd.DataFrame(pca_2d);
newecoli['Cluster'] = kmeans.labels_
newecoli

sns.scatterplot(x=newecoli[0], y=newecoli[1], hue="Cluster", data=newecoli, palette='Paired', s=90, alpha = 0.5,cmap = 'viridis');
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left');

X=[[0.98,0.43,0.48,0.8,0.47,0.69,0.32]] 
C_clustered=kmeans.predict(X)
print("The unseen data [0.98,0.43,0.48,0.8,0.47,0.69,0.32] is clustered as ", C_clustered)

"""## **ข้อ 2**"""

uploaded = files.upload()
retail = pd.read_csv(io.BytesIO(uploaded['test_retail2.csv']),header=None)
retail.tail()

!pip install mlxtend

retail = retail.apply(lambda x: ', '.join(x.dropna()),axis=1)
retail = pd.DataFrame(retail,columns=['products'])
retail

retail = list(retail["products"].apply(lambda x : x.split(',')))

from mlxtend.preprocessing import TransactionEncoder
te = TransactionEncoder()
te_data = te.fit(retail).transform(retail)
retail = pd.DataFrame(te_data,columns=te.columns_)
pd.set_option('display.max_columns', None)
retail

from mlxtend.frequent_patterns import apriori
freq_items = apriori(retail,min_support=0.07,use_colnames = True )
freq_items

from mlxtend.frequent_patterns import association_rules
df_res = association_rules(freq_items, metric = "confidence", min_threshold = 0.7)
df_res

conf_max = df_res['confidence'].max()
conf_max

conf_min = df_res['confidence'].min()
conf_min

df_filt = df_res[ (df_res["confidence"] == conf_min) | (df_res["confidence"] == conf_max) | (df_res["confidence"] == 0.5 )]
df_filt.sort_values("confidence",ascending = True)