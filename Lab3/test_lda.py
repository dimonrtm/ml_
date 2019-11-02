# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 16:13:05 2018

@author: dim
"""

import pandas as pd
import numpy as np
from Docunent import Document
from CorpusDocuments import CorpusDocuments
from LDA import LDA
lenta=pd.read_csv("lenta_ru.csv")
topics=len(set(lenta["topic"]))
corp=CorpusDocuments(lenta,17)
lda=LDA(corp,topics,100)
lda.lda_method()
lda.get_top20_words_in_topic()
#print(lenta.iloc[0,:])