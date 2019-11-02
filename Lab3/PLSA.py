# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 12:56:53 2018

@author: dim
"""
import pandas as pd
import numpy as np

class PLSA:
    
    def __init__(self,corpus,num_topics,n_iter):
        self._corpus=corpus
        self._num_topics=num_topics
        self._n_iter=n_iter
    
    def plsa_method(self):
        self._topics=["sbj "+str(i) for i in range(self._num_topics)]
        ndw=self._corpus.get_matrix_freq()
        self._phi=np.random.random(size=(ndw.shape[1],self._num_topics))
        for i in range(self._phi.shape[0]):
            self._normalization(self._phi[i])
        self._theta=np.random.random(size=(self._num_topics,ndw.shape[0]))
        for i in range(self._theta.shape[0]):
            self._normalization(self._theta[i])
        for i in range(self._n_iter):
            print("Iter"+str(i))
            nwt=np.zeros([ndw.shape[1],self._num_topics],dtype=np.float)
            ndt=np.zeros([ndw.shape[0],self._num_topics],dtype=np.float)
            nt=np.zeros(self._num_topics,dtype=np.float)
           
            for j in range(ndw.shape[0]):
                #Z=[0]*ndw.shape[1]
                for k in range(ndw.shape[1]):
                    Z=0.0
                    for t in range(self._num_topics):
                        Z+=self._phi[k,t]*self._theta[t,j]
                    #Z[k]=z
                    for t in range(self._num_topics):
                        if self._phi[k,t]*self._theta[t,j]>0:
                            delta=ndw.iloc[j,k]*self._phi[k,t]*self._theta[t,j]/Z
                            nwt[k,t]+=delta
                            ndt[j,t]+=delta
                            nt[t]+=delta
            for w in range(ndw.shape[1]):
                for t in range(self._num_topics):
                    self._phi[w,t]=nwt[w,t]/nt[t]
            for d in range(ndw.shape[0]):
                for t in range(self._num_topics):
                    self._theta[t,d]=ndt[d,t]/self._corpus.get_documents()[d].get_nd()
                    
    def get_top20_words_in_topic(self):
        for t in range(self._num_topics):
            print(self._topics[t])
            distr=self._phi[:,t]
            distr_indexies=distr.argsort()[::-1]
            for w in range(30):
                print(list(self._corpus.get_dictionary())[distr_indexies[w]],end=",")
            print()
            
    
    def _normalization(self,vec):
        s=0
        for i in range(vec.shape[0]):
            if vec[i]>=0:
                s+=vec[i]
        for j in range(vec.shape[0]):
            if vec[j]>=0:
                vec[j]=vec[j]/s
            else:
                vec[j]=0
                
                
    def get_phi(self):
        return self._phi
   
    def get_theta(self):
        return self._theta
    