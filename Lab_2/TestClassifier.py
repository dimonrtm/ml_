# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 01:40:49 2018

@author: dim
"""

from KNNClasses import KNNClassifier
import pandas as pd
from sklearn.metrics import accuracy_score 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
libra=pd.read_csv("libra.csv")
feature_names = ['LW', 'LD', 'RW', 'RD']
X = libra[feature_names].values
y = libra['label'].values
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3,random_state=0)
print("My Classifier")
classifier=KNNClassifier(20,X_train,y_train)
prediction=classifier.predict(X_test)
print(accuracy_score(y_test,prediction))
print("sklearn Classifier")
classifier=KNeighborsClassifier(n_neighbors=20)
classifier.fit(X_train,y_train)
prediction=classifier.predict(X_test)
print(accuracy_score(y_test,prediction))
