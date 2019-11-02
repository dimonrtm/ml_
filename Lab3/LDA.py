# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 16:08:38 2018

@author: dim"""

import pandas as pd
import numpy as np

class LDA:
    
    def __init__(self,corpus,num_topics,n_iter):
        self._corpus=corpus
        self._num_topics=num_topics
        self._n_iter=n_iter
    
    def lda_method(self):
        self._topics=["sbj "+str(i) for i in range(self._num_topics)]
        ndw=self._corpus.get_matrix_freq()
        self._phi=np.random.random(size=(ndw.shape[1],self._num_topics))
        for i in range(self._phi.shape[0]):
            self._normalization(self._phi[i])
        self._theta=np.random.random(size=(self._num_topics,ndw.shape[0]))
        for i in range(self._theta.shape[0]):
            self._normalization(self._theta[i])
        alpha=50/self._num_topics
        beta=0.01
        nwt=np.zeros([ndw.shape[1],self._num_topics],dtype=np.float)
        ndt=np.zeros([ndw.shape[0],self._num_topics],dtype=np.float)
        nt=np.zeros(self._num_topics,dtype=np.float)
        tdwi=np.zeros([ndw.shape[0],ndw.shape[1],self._num_topics],dtype=np.float)
        for i in range(self._n_iter):
            print("Iter"+str(i))
            for j in range(ndw.shape[0]):
                #Z=[0]*ndw.shape[1]
                for k in range(ndw.shape[1]):
                    for m in range(ndw.iloc[j,k]):
                        if i!=0:
                           t=int(tdwi[j,k,m])
                           nwt[k,t]-=1
                           ndt[j,t]-=1
                           nt[t]-=1
                        pt=(ndt[j]+alpha)/(alpha*self._num_topics+self._corpus.get_documents()[j].get_nd())
                        pt*=(nwt[k]+beta)/(beta*ndw.shape[1]+nt[m])
                        self._normalization(pt)
                        t=np.random.multinomial(1,pt).argmax()
                        tdwi[j,k,m]=t
                        nwt[k,t]+=1
                        ndt[j,t]+=1
                        nt[t]+=1
                                                        
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