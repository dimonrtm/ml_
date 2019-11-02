# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 12:02:28 2018

@author: dim
"""
import numpy as np

class Perplexity:
    def __init__(self,corpus,phi,theta,num_topics):
        self._corpus=corpus
        self._phi=np.array(phi)
        self._theta=np.array(theta)
        self._num_topics=num_topics
    
    def perplexity(self):
        ndw=self._corpus.get_matrix_freq()
        N=0.0
        perp=0.0
        for d in range(ndw.shape[0]):
            for w in range(ndw.shape[1]):
                pwd=1e-100
                for t in range(self._num_topics):
                    pwd+=self._phi[w,t]*self._theta[t,d]
                N+=ndw.iloc[d,w]
                perp+=ndw.iloc[d,w]*np.log(pwd)
        perp=np.exp((-1/N)*perp)
        return perp
