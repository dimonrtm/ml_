# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 12:54:29 2018

@author: dim
"""

import pandas as pd
import numpy as np
from Docunent import Document
from CorpusDocuments import CorpusDocuments
from PLSA import PLSA
lenta=pd.read_csv("lenta_ru.csv")
topics=len(set(lenta["topic"]))
corp=CorpusDocuments(lenta,17)
plsa=PLSA(corp,topics,30)
plsa.plsa_method()
plsa.get_top20_words_in_topic()
#print(lenta.iloc[0,:])
