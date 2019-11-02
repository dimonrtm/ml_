# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 12:56:39 2018

@author: dim
"""
import re
from nltk.corpus import stopwords
import pymorphy2

class Document:
    
    def __init__ (self,text):
        self._text=text
        morph=pymorphy2.MorphAnalyzer()
        words_list=re.sub('[^A-Za-zА-Яа-я]+',' ',self._text).split(" ")
        self._filtered_words_list=[morph.parse(w.lower())[0].normal_form for w in words_list if w not in stopwords.words("russian")]
        self._dictionary=set(self._filtered_words_list)
    
    def get_frequency_word(self,word):
        i=0
        for w in self._filtered_words_list:
            if w==word:
                i+=1 
        return i
    
    def get_dictionary(self):
        return self._dictionary
    
    def get_nd(self):
        return len(self._filtered_words_list)
        