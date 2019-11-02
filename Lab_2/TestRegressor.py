# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 10:40:27 2018

@author: dim
"""

from KNNClasses import KNNRegressor
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.neighbors import KNeighborsRegressor 

data=pd.read_csv("carbon_nanotubes.csv",sep=";",decimal=",")
data_train=data.iloc[:7505]
data_test=data.iloc[7505:]
X_train=data_train[["Chiral indice n","Chiral indice m","Initial atomic coordinate u",
                   "Initial atomic coordinate v","Initial atomic coordinate w"]].astype(float).values
y_train_1=data_train[["Calculated atomic coordinates u'"]].astype(float).values
y_train_2=data_train[["Calculated atomic coordinates v'"]].astype(float).values
y_train_3=data_train[["Calculated atomic coordinates w'"]].astype(float).values
X_test=data_test[["Chiral indice n","Chiral indice m","Initial atomic coordinate u",
                   "Initial atomic coordinate v","Initial atomic coordinate w"]].astype(float).values
y_test_1=data_test[["Calculated atomic coordinates u'"]].astype(float).values
y_test_2=data_test[["Calculated atomic coordinates v'"]].astype(float).values
y_test_3=data_test[["Calculated atomic coordinates w'"]].astype(float).values
print("My KNNREgresoor")
regressor_1=KNNRegressor(20,X_train,y_train_1)
prediction_1=regressor_1.predict(X_test)
print(mean_absolute_error(y_test_1,prediction_1))
regressor_2=KNNRegressor(20,X_train,y_train_2)
prediction_2=regressor_2.predict(X_test)
print(mean_absolute_error(y_test_2,prediction_2))
regressor_3=KNNRegressor(20,X_train,y_train_3)
prediction_3=regressor_3.predict(X_test)
print(mean_absolute_error(y_test_3,prediction_3))
print("sklearn KNNRegressor")
regressor_1=KNeighborsRegressor(n_neighbors=20)
regressor_1.fit(X_train,y_train_1)
prediction_1=regressor_1.predict(X_test)
print(mean_absolute_error(y_test_1,prediction_1))
regressor_2=KNeighborsRegressor(n_neighbors=20)
regressor_2.fit(X_train,y_train_2)
prediction_2=regressor_2.predict(X_test)
print(mean_absolute_error(y_test_2,prediction_2))
regressor_3=KNeighborsRegressor(n_neighbors=20)
regressor_3.fit(X_train,y_train_3)
prediction_3=regressor_3.predict(X_test)
print(mean_absolute_error(y_test_3,prediction_3))