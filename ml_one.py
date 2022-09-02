# -*- coding: utf-8 -*-
"""ML_One.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oACBkb3y91dxVWqptA6EYUr-LEniUZB0

# 1) Probleme genel bakış

# 2) Veriyi Toplama

veri: https://www.kaggle.com/datasets/himanshunakrani/student-study-hours?resource=download
"""

import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


source = pd.read_csv("score.csv")

"""# 3) Veriyi İncelemek """

print(source.head())

source.shape

source.info()

# use the scatter method to create a scatter plot
plt.scatter(x= source['Hours'], y= source['Scores'], color='green')
#  label the axioms 
plt.xlabel("Hours")
plt.ylabel("Scores")

# Title of the plot

plt.title("Hours vs Scores")

plt.show()

"""#4) Veriyi Modele Uygun Hale Getir"""

# Splitting the data 
# btween dependant and features variables, x is the features and y is the dependent 
x = source["Hours"]
y = source["Scores"]

print(x)
print(y)

import sklearn.model_selection
X_train, X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(x, y, train_size= 0.8, test_size=0.2)

print(X_train) # the rows are automatically scrambled

print(Y_train)

print(X_train.shape) # it has to be an array for sklearn therefore we have to convert its type to array 
print(type(X_train)) # As you can see it is not an array 
X_train = np.array(X_train)
X_test = np.array(X_test) 
Y_train = np.array(Y_train)
Y_test = np.array(Y_test)
print(type(X_train))

X_train.shape

X_train = X_train.reshape(-1, 1) # this means reshape the array such that there is one column -1 means figure out how many rows to satisfy our condition 
print(X_train.shape)
X_test = X_test.reshape(5, 1)
Y_train = Y_train.reshape(-1, 1)
Y_test = Y_test.reshape(-1, 1)
print(Y_train.shape)

"""# 5) Model Seçimi ve modelin eğitilmesi

"""

import sklearn.linear_model
lin_model = sklearn.linear_model.LinearRegression()
lin_model.fit(X_train, Y_train) #train with the training features and the results based on them

"""#6) Modelin Optimizasyonu"""

import sklearn.metrics 
predictions = lin_model.predict(X_test)
print(predictions) # predicted results based on features
print(X_test) # features

for i in range(len(X_test)):
    print(f"{i}: Gerçek Değer: {Y_test[i]} - Tahmin: {predictions[i]} ") # the real values vs predictions

mae = sklearn.metrics.mean_absolute_error(Y_test, predictions) #find the mean absolute error between the real values and predictions
mse = sklearn.metrics.mean_squared_error(Y_test, predictions)  #find the mean squared error between the real values and predictions
r2 = sklearn.metrics.r2_score(Y_test, predictions) # accuaracy R^2
print(f"mean absolute error: {mae}")
print(f"mean squared error: {mse}")
print(f"R2: {r2}")

# For a specific value 
score_prediction = lin_model.predict([[5]]) # if a student studies 5 hours 
print(score_prediction) # As we can see the R^2 accuracy value which is constant for all elements, whatever score_prediction is it is 95 % accurate

# Now we are gonna do smth differently we are gonnna predict from the training set which is normaly a no no we do this to show
Y_predictions_For_Training_X = lin_model.predict(X_train)

# use the scatter method to create a scatter plot
plt.scatter(x= source['Hours'], y= source['Scores'], color='green')
plt.plot(X_train, Y_predictions_For_Training_X) # the predictions vs the dataset 

plt.scatter(x=5, y=lin_model.predict([[5]]), color="red")
#  label the axioms 
plt.xlabel("Hours")
plt.ylabel("Scores")

# Title of the plot

plt.title("Hours vs Scores")

plt.show()