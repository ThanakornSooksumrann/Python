# -*- coding: utf-8 -*-
"""chapter_7_KNN_Lab.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZLM0NcmLtkvUfL1odisCYSyrDk_YWOTd
"""

# getting our data playground ready
from sklearn import datasets

#https://scikit-learn.org/stable/modules/classes.html?highlight=neighbors#module-sklearn.neighbors
from sklearn import neighbors

iris =  datasets.load_iris()
# the dataset is loaded as a dictionary of key-value pairs

print(iris.keys()) #/ข้อมูล / เฉลย /รูปแบบ /ชื่อเฉลย

iris.data

iris.target_names

iris.feature_names

print(iris["DESCR"])
print("Feature names are: ", iris["feature_names"])
print("Target names are: ", iris["target_names"])

from sklearn.model_selection import train_test_split
X,y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.3, random_state = 42)

# Plot the data
import pandas as pd
iris_df = pd.DataFrame(X_train, columns=iris.feature_names)
pd.plotting.scatter_matrix(iris_df, c=y_train, figsize=(12,12), marker="x") # o is marker on graph

"""วิธีอ่าน Scatterplot matrix มีดังนี้:

Scatterplot matrix แสดงความสัมพันธ์ระหว่างตัวแปรสองตัว ซึ่งอาจจะเป็น Feature ทั้งสองตัว หรืออาจจะเป็น Feature กับ Label ก็ได้ โดยแสดงทุกคู่ความสัมพันธ์ที่เป็นไปได้อยู่ในภาพเดียวกัน เลยมีหน้าตาเป็น Matrix
จะเห็นว่า Matrix ช่องบนซ้ายแทยงลงมาช่องล่างขวา ไม่ได้แสดงเป็น Scatter plot แต่เป็น Distribution plot เพราะมันคือความสัมพันธ์ของตัวมันเอง โดย Distribution plot ก็มีประโยชน์ ทำเราจะได้เห็นว่ารายการข้อมูลทั้งหมดมีการกระจายตัวใน Feature นั้นอย่างไร เช่น ช่อง Sepal width พบว่ามีการกระจายตัวแบบ Normal distribution คือข้อมูลส่วนมากมีค่าอยู่กลางๆ แถวๆ Mean แล้วกระจายตัวออกทั้งด้านลบและด้านบวก
ส่วนช่องอื่นๆ เราสามารถกำหนดให้แยกสีตาม Label ได้ ทำให้เห็นว่าในแต่ละคู่ความสัมพันธ์ ข้อมูล Label ไหนอยู่ตรงไหน ตัวอย่างเช่น คู่ Petal length VS. Sepal length (แถว 3 คอลัมน์ 1) จะเห็นว่า Label แรกจะมี Petal และ Sepal length น้อย, Label ที่สองอยู่ตรงกลางๆ, และ Label ที่สามมีค่ามาก แต่เมื่อดู Sepal width VS. Sepal length (แถว 2 คอลัมน์ 1) พบว่า Label 2 และ 3 มีค่าผสมผสานกัน แยกกจากกันไม่เด็ดขาด เป็นต้น
สำหรับเรา ประโยชน์หนึ่งจากการอ่าน Scatterplot matrix คือการสร้างความเข้าใจในภาพรวมว่าชุดข้อมูลนี้น่าจะ "ยาก" หรือ "ง่าย" ในการสร้างโมเดล โดยถ้าข้อมูลแต่ละ Label แยกจากกันค่อนข้างชัด การสร้างโมเดลก็จะค่อนข้างง่ายและแม่นยำ
"""

# create the model
knn_model = neighbors.KNeighborsClassifier(n_neighbors=5)
# fit the model
knn_model.fit(X_train,y_train)

from sklearn.metrics import accuracy_score
print("Train data accuracy:",accuracy_score(y_true = y_train, y_pred= knn_model.predict(X_train)))
print("Test data accuracy:",accuracy_score(y_true = y_test, y_pred=knn_model.predict(X_test)))

from sklearn.metrics import confusion_matrix
y_pred = knn_model.predict(X_test)
confusion_matrix(y_test,y_pred)

X_test.shape

# model predictions
predictions = knn_model.predict(X_test)
prob_predictions = knn_model.predict_proba(X_test)
predictions = [iris.target_names[i] for i in predictions]
print("Predicted Probabilities ")
print("------------------------")
print(iris.target_names)
print(prob_predictions) #print prob of testset
print 
# as opposed to actuals
actuals = [iris.target_names[i] for i in y_test]
print("Prediction / Actual")
print("-------------------")
for i in range(len(y_test)):
    print(predictions[i] + " / " + actuals[i])

import matplotlib.pyplot as plt
plt.style.use('ggplot')

#Setup arrays to store training and test accuracies
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
neighbors = np.arange(1,9)
train_accuracy =np.empty(len(neighbors))
test_accuracy = np.empty(len(neighbors))

for i,k in enumerate(neighbors):
    #Setup a knn classifier with k neighbors
    knn = KNeighborsClassifier(n_neighbors=k)
    
    #Fit the model
    knn.fit(X_train, y_train)
    
    #Compute accuracy on the training set
    train_accuracy[i] = knn.score(X_train, y_train)
    
    #Compute accuracy on the test set
    test_accuracy[i] = knn.score(X_test, y_test)

#Generate plot
plt.title('k-NN Varying number of neighbors')
plt.plot(neighbors, test_accuracy, label='Testing Accuracy')
plt.plot(neighbors, train_accuracy, label='Training accuracy')
plt.legend()
plt.xlabel('Number of neighbors')
plt.ylabel('Accuracy')
plt.show()

"""# Exercise 7.1
ให้นักศึกษาทดลองจำแนกข้อมูล diabetes.csv (โรคเบาหวาน) โดย download ข้อมูลจากเว็บไซต์ https://www.kaggle.com/saurabh00007/diabetescsv/version/1
โดยข้อกำหนดดังต่อไปนี้
1.  explore data เพื่อดูรายละเอียดของข้อมูล และ plot graph 
2.  ทดลองจำแนกข้อมูลโดยใช้ค่า k ตั้งแต่ 1 3 5 7 9  เพื่อหาค่าที่มีประสิทธิภาพที่ดีที่สุด  แล้ว plot graphแสดงผล
3. นำโมเดลที่ได้จากค่า k ที่ดีที่สุดมาแสดงค่าประสิทธิภาพในรูปแบบของ Classification Report ที่แสดง precision recall f-measure 
4. นำโมเดลที่เลือกมาทดลองจำแนกกับชุดข้อมูลใหม่ (ให้หาเอง) ประมาณ 3 ตัวอย่าง แล้วแสดงผลการจำแนกให้ดู
"""

#เขียน code ตรงนี้นะจ๊ะ