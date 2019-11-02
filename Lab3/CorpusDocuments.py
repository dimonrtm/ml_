# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 12:26:08 2018
ivan@sha.run
@author: dim
"""
import pandas as pd
import numpy as np
from Docunent import Document
class CorpusDocuments:
    
    def __init__(self,dataset,n_documents):
        self._dataset=dataset
        self._n_documents=n_documents
        self._documents=[]
        self._dictionary=set()
        for i in range(self._n_documents):
            doc=Document(dataset.iloc[i,:]["text"])
            dictio=doc.get_dictionary()
            self._documents.append(doc)
            self._dictionary.update(dictio)
    
    def get_matrix_freq(self):
        matrix=[]
        frequencies=[]
        words=list(self._dictionary)
        for doc in self._documents:
            for w in words:
                freq=doc.get_frequency_word(w)
                frequencies.append(freq)
            matrix.append(frequencies)
            frequencies=[]
        ndw=pd.DataFrame(data=matrix,columns=words)
        return ndw
    
    def get_documents(self):
        return self._documents
    
    def get_dictionary(self):
        return self._dictionary