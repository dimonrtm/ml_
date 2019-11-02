# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 10:58:30 2018

@author: dim
"""

import numpy as np

class KNearestNeighborn:
    
    def __init__(self,n_neighbors,X,y,p=2):
        self.neighbors_=n_neighbors
        self.X_=X
        self.y_=y
        self.p_=p
    
    def calculate_distances(self,x):
        dataset_size=self.X_.shape[0]
        diff=np.tile(x,(dataset_size,1))-self.X_
        powerMatrix=diff**self.p_
        sumMatrix=powerMatrix.sum(axis=1)
        minkovsky=sumMatrix**(1/self.p_)
        return minkovsky
            
    def min_k_neighbors(self,x):
        distances=self.calculate_distances(x)
        min_index_distances=np.argsort(distances)
        min_k_neibors_indexies=min_index_distances[:self.neighbors_]
        min_k_distances=distances[min_k_neibors_indexies]
        min_k_X=self.X_[min_k_neibors_indexies]
        min_k_y=self.y_[min_k_neibors_indexies]
        weights=0.01**min_k_distances
        return weights,min_k_X,min_k_y
    
    def predict(self,X):
        pass
    
class KNNRegressor(KNearestNeighborn):
    
    def predict(self,X):
        preds=[]
        for x_i in X:
            weights,min_k_X,min_k_y=self.min_k_neighbors(x_i)
            predict=sum(weights.dot(min_k_y))/np.sum(weights)
            preds.append(predict)
        return np.array(preds)

class KNNClassifier(KNearestNeighborn):
    
    def predict(self,X):
        y_non_duplicates=set(self.y_)
        preds=[]
        for x_i in X:
            weights,min_k_X,min_k_y=self.min_k_neighbors(x_i)
            weight_sums=[]
            for y_i in y_non_duplicates:
                summa=0
                for index,y_i_min_k in enumerate(min_k_y):
                    summa+=(y_i_min_k==y_i)*weights[index]
                weight_sums.append(summa)
            weight_sums=np.array(weight_sums)
            y_pred=list(y_non_duplicates)[np.argmax(weight_sums)]
            preds.append(y_pred)
        return np.array(preds)