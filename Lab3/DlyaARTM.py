# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 20:14:12 2018

@author: dim
"""

import pandas as pd
import numpy as np
import re
from nltk.corpus import stopwords
import pymorphy2

data=pd.read_csv("lenta_ru.csv")
texts=data["text"]
doc_text=""
for i in range(17):
    text=texts.iloc[i]
    print("Iter")
    doc_text+=" |text "
    morph=pymorphy2.MorphAnalyzer()
    words_list=re.sub('[^A-Za-zА-Яа-я]+',' ',text).split(" ")
    filtered_words_list=[morph.parse(w.lower())[0].normal_form for w in words_list if w not in stopwords.words("russian")]
    filtered_text=" ".join(filtered_words_list)
    doc_text+=filtered_text
    doc_text+="\n"
f=open("lenta.txt","w")
f.write(doc_text)
f.close()
