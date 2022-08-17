# -*- coding: utf-8 -*-
"""CIFAR10_CNN_classifiy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WBP7ICb_oRAOLo8G1BpPcJg4bKZvoePW
"""

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Flatten, Conv2D, Dropout, MaxPooling2D

#โหลดชุดข้อมูล MNIST โดย TensorFlow ได้ฝัง MNIST ไว้ให้แล้ว เพราะเป็นชุดข้อมูลยอดนิยมที่เอาไว้ฝึกและทดสอบโมเดล
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

#เช็คมิติข้อมูลที่โหลดข้อมูลมา พบว่า Train set มี 60,000 รายการ ขนาด 28 x 28 Pixel ส่วน Test set มี 10,000 รายการ ส่วน Data Type เป็น uint8
# Check data dimension
print("X_train data shape is", train_images.shape)
print("y_train data shape is", train_labels.shape)
print("X_test data shape is", test_images.shape)
print("y_test data shape is", test_labels.shape)
print()
# Check data type
print("X_train data type is", train_images.dtype)
print("y_train data type is", train_labels.dtype)
print("X_test data type is", test_images.dtype)
print("y_test data type is", test_labels.dtype)

#เนื่องจากเรารู้ว่าข้อมูลเป็นภาพ เราสามารถใช้ Method .imshow ของ matplotlib แสดงภาพได้ทันที
img_index = 999
print("Train Label ",img_index," : ",train_labels[img_index])
plt.imshow(train_images[img_index])

plt.figure()
plt.imshow(train_images[9])
plt.colorbar()
plt.grid(True) 
plt.show()

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(train_labels[i])
plt.show()

plt.figure(figsize=(10,10))
for i in range(25):
  plt.subplot(5,5,i+1)
  plt.xticks([])
  plt.yticks([])
  plt.imshow(train_images[i])
  plt.xlabel(train_labels[i])
plt.show()

#เปลี่ยนมิติข้อมูลให้เป็น 4 มิติ คือ (จำนวนรายการ, Column, Row, จำนวน Layer สี) โดยข้อมูลของเราเป็นภาพขาวดำขนาด 28 x 28 ดังนั้นมิติคือ (จำนวนรายการ, 28, 28, 1)
train_images = train_images.reshape(train_images.shape[0], 28, 28, 1)
test_images = test_images.reshape(test_images.shape[0], 28, 28, 1)

#กำหนดตัวแปรมิติข้อมูล เพื่อเตรียมใช้ใน Argument input_shape ใน Layer แรกของ Model โดยไม่ต้องระบุจำนวนรายการ 
#ดังนั้น มิติข้อมูลสำหรับ Layer แรก คือ (28, 28, 1) อนึ่งเราต้องกำหนดมิติข้อมูลสำหรับ Layer แรกเท่านั้น ส่วน Layer อื่น TensorFlow จะอนุมานให้เอง
input_shape = (28, 28, 1)

#แปลง Data type ของข้อมูลให้เป็น Float เพื่อให้ Algorithm สามารถคำนวนและแสดงผลเป็นค่าทศนิยมได้
#เลือกข้อมูลแค่บางส่วนมาเทรนและทดสอบ เราจะไม่ใช้ทั้งหมดเพราะจะใช้เวลาเทรนนาน จึงเลือก Train set 2,000 รายการ และ Test set 400 รายการ
train_images = train_images[:2000, :, :, :].astype('float32')
test_images = test_images[:400, :, :, :].astype('float32')
train_labels = train_labels[:2000]
test_labels = test_labels[:400]

'''normalize to range 0-1
train_images= train_images / 255.0
test_images = test_images / 255.0'''
#Scale ข้อมูลโดยใช้วิธี Normalise ซึ่งก็คือการหารข้อมูลทุกรายการด้วย Range ของค่าความสว่างของแต่ละ Pixel นั่นก็คือ 255
train_images /= 255
test_images /= 255

print('X_train shape:', train_images.shape)
print('X_test shape:', test_images.shape)
print('y_train shape:', train_labels.shape)
print('y_test shape:', test_labels.shape)

model = Sequential()

#Step1
#Convolution+Relu 
model.add(Conv2D(64, kernel_size=(3, 3),
                 activation='relu',
                 padding='same',
                 input_shape=(28,28, 1)))
#Pooling
model.add(MaxPooling2D((2, 2)))

#Step2
#Convolution+Relu 
model.add(Conv2D(32, 
                 kernel_size=(3, 3), 
                 padding='same',
                 activation='relu'))
#Pooling
model.add(MaxPooling2D(pool_size=(2, 2)))

#Step3
#Flatten
model.add(Flatten())
#Fully connected
model.add(Dense(256, activation='relu'))
#Softmax
model.add(Dense(10, activation='softmax'))
model.summary()

#Dense(10, activation='softmax') ใช้ Softmax activation function ซึ่งทำให้โมเดลสามารถ Output แบบ Multiclass ได้ โดยเราต้องกำหนดจำนวน Neuron เท่ากับจำนวน Class ที่เป็นไปได้ ซึ่งก็คือ 10 นั่นเอง

model.compile(optimizer='adam',  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),  metrics=['accuracy']) # loss='sparse_categorical_crossentropy'

"""- epochs จำนวนรอบของการเทรน โดยแต่ละ Epoch จะทำให้ Loss ลดลง ในขณะที่ Accuracy เพิ่ม
- batch_size ขนาดของ Batch ซึ่งก็คือจำนวนรายการข้อมูลที่จะให้ Optimiser คำนวนในหนึ่งครั้ง เช่น ข้อมูลมี 2,000 รายการ ถ้ากำหนด Batch size เป็น 32 แปลว่า Optimiser จะต้องทำงาน 62.5 ครั้ง จึงจะครบทั้ง 2,000 รายการ และถ้ากำหนด Epoch เป็น 20 ก็หมายถึงการทำงาน 62.5 ครั้ง 20 รอบ การกำหนด Batch size จะมีผลโดยตรงกับความเร็วในการคำนวน ยิ่ง Batch ใหญ่ ยิ่งคำนวนเร็ว แต่ Batch ที่ใหญ่เกินไปอาจทำให้ข้อมูลที่คำนวนมีขนาดใหญ่เกินกว่า Memory ของเครื่องเราจะรองรับได้ ทั้งนี้ใน การกำหนด Batch size แบบต่างๆ จะมีชื่อเรียกเฉพาะ เช่น Batch gradient descent แปลว่า Batch size เท่ากับจำนวนรายการข้อมูล ไม่มีการแบ่ง, Mini-batch gradient descent คือการแบ่งข้อมูลออกเป็น Batch, ส่วน Stochastic gradient descent คือ Batch size เท่ากับ 1 
- validation split เราสามารถกัน Train set ส่วนหนึ่งไว้เป็น Validation set ซึ่งก็คือข้อมูลชุดที่โมเดลไม่เคยเห็น Keras จะคำนวน Loss และความแม่นยำกับ Validation set ทุกครั้งที่คำนวนจบ 1 Epoch และแสดงผลให้เราเห็น อนึ่งการแบ่ง Validation set จะตัดเอาส่วนสุดท้ายของ Train set มาเลยโดยไม่สุ่ม ดังนั้นเราจึงควรสุ่ม Shuffle ข้อมูลให้เรียบร้อยตั้งแต่แรก รายละเอียดเกี่ยวกับการแบ่งชุดข้อมูลออกเป็น Train / Validation / Test set
"""

#model.fit(train_images, train_labels, epochs=10)
#model.fit(X_train, y_train, epochs=20, batch_size=32, validation_split=0.2, verbose=1)
history = model.fit(train_images, train_labels, batch_size=32, epochs=30,validation_data = (test_images,test_labels),callbacks =None)

"""สังเกตว่าแต่ละ Epoch ที่เทรน Loss และ Validation loss จะลดลงเรื่อยๆ สอดคล้องกับ Accuracy และ Validation accuracy ที่เพิ่มขึ้นเรื่อยๆ ซึ่งในกรณีของเราไปหยุดที่ Validation accuracy 97% (val_accuracy: 0.9775) เราสามารถใช้ผลนี้เป็นตัวบ่งชี้ว่าควรจะปรับ Hyperparameter ต่างๆ ของโมเดลหรือไม่อย่างไร เพื่อทำให้โมเดลมีความแม่นยำมากขึ้น รวมทั้งสามารถวิเคราะห์ปัญหา Bias/variance ด้วยการเปรียบเทียบข้อมูลจากการเทรนกับข้อมูลจาก Validation set"""

print(history.history.keys())
plt.figure(figsize=(9,6))
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train','test'],loc = 'upper left')
plt.show()

test_loss, test_accuracy = model.evaluate(test_images,  test_labels, verbose=2)

print('\nTest accuracy:', test_accuracy)

"""- สุดท้าย เรามาลองพยากรณ์กันเลย โดยป้อนภาพที่มี Index ที่ต้องการจาก X_test ลงไปใน Method .predict โดยอย่าลืมแปลงมิติข้อมูลให้สอดคล้องกับตอนแรก นั่นก็คือ (จำนวนรายการ, 28, 28, 1) ซึ่งก็คือ (1, 28, 28, 1) นั่นเอง

- Method .predict จะ Output ออกมาเป็น Array ของความเป็นไปได้ การตีความก็คือเราจะเลือก Index ที่มีความเป็นไปได้สูงสุดเป็นคำตอบ เราสามารถใช้ Method .argmax ในการ Output index ที่มีค่าสูงสุดได้:
"""

# Make a prediction
image_index = 50
plt.imshow(test_images[image_index].reshape(28, 28),cmap='Greys')
pred = model.predict(test_images[image_index].reshape(1, 28, 28, 1))
print("อาร์เรย์ความน่าจะเป็นที่คาดการณ์คือ:")

count = 0

for i in pred.squeeze():
    print(count, ":", i)
    count += 1

print("จากทางเลือกทั้งหมดคะแนนสูงสุดคือ:", pred.argmax())

probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])

predictions = probability_model.predict(test_images)
predictions[2]

np.argmax(predictions[test_labels[2]]) #อันนี้คือตัวที่เอา model มาทำนายและไดคำตอบมาว่าเป็นประเภทที่เท่าไหร่

test_labels[test_labels[2]] #อันนี้คือเฉลยคำตอบดูว่าตรงกับที่ทำนายไหม