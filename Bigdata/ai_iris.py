# -*- coding: utf-8 -*-
"""Ai_iris.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xeYb_FR35UF0TaK_MgsX2CJoIBrGhMJV
"""

import numpy as np
import pandas as pd

import io 
from google.colab import files
uploaded = files.upload()
dataset = pd.read_csv(io.BytesIO(uploaded['iris.csv']))

dataset.head(10)

X = dataset.iloc[:, 0:4]
Y = dataset.iloc[:, 4]

from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical
label_encoder = LabelEncoder()

Y = label_encoder.fit_transform(Y)
Y = pd.get_dummies(Y).values

from sklearn.preprocessing import StandardScaler

#sc = StandardScaler()
#X = sc.fit_transform(X)

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

!pip install keras
!pip install tensorflow

print(X_train)

from keras import Sequential
from keras.layers import Dense

classifier = Sequential()
#First Hidden Layer
classifier.add(Dense(200, activation='relu',kernel_initializer='random_normal', input_dim=4))
#Second Hidden Layer
classifier.add(Dense(200, activation='relu', kernel_initializer='random_normal'))
classifier.add(Dense(200, activation='relu', kernel_initializer='random_normal'))
classifier.add(Dense(200, activation='relu', kernel_initializer='random_normal'))
classifier.add(Dense(200, activation='relu', kernel_initializer='random_normal'))
#Output Layer
classifier.add(Dense(3, activation='softmax',kernel_initializer='random_normal'))
#output = activation(dot(input, kernel) + bias)

classifier.summary()

classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

history = classifier.fit(X_train, Y_train, batch_size=50, epochs=3, validation_data=(X_test,Y_test))

score = classifier.evaluate(X_train, Y_train, verbose = 0)
print('Train loss : ', score[0])
print('Train accuracy : ', score[1])

score = classifier.evaluate(X_test, Y_test, verbose = 0)
print('Test loss : ', score[0])
print('Test accuracy : ', score[1])

import matplotlib.pyplot as plt # For graphical representation

plt.plot(history.history['accuracy']) #train
plt.plot(history.history['val_accuracy']) #test
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc = 'upper left')
print(history.history.keys())

plt.show()

classifier.save("pima_model.h5")
print("Saved model.")

Y_pred = classifier.predict(X_test)
print(Y_pred)
Y_predNew = np.argmax(Y_pred,axis=1)

print(Y_predNew)
#print(Y_test)
Y_testNew = np.argmax(Y_test,axis=1)
print(Y_testNew)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_testNew, Y_predNew)
print(cm)