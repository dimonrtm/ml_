# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 20:45:07 2018

@author: dim
"""

import pandas as pd
import numpy as np
from Docunent import Document
from CorpusDocuments import CorpusDocuments
from LDA import LDA
from PLSA import PLSA
from Perplexity import Perplexity
import artm
lenta=pd.read_csv("lenta_ru.csv")
topics=len(set(lenta["topic"]))
corp=CorpusDocuments(lenta,17)
lda=LDA(corp,topics,100)
lda.lda_method()
plsa=PLSA(corp,topics,30)
plsa.plsa_method()
print("Перплексия myLDA: ",Perplexity(corp,lda.get_phi(),lda.get_theta(),topics).perplexity())
print("Перплексия myPLSA: ",Perplexity(corp,plsa.get_phi(),plsa.get_theta(),topics).perplexity())
batch_vectorizer=artm.BatchVectorizer(data_path="lenta.txt",
                                      data_format="vowpal_wabbit",
                                      target_folder="profstandards_batches",
                                     batch_size=10)
topic_names=["sbj"+str(i) for i in range(topics-1)]+["bcg"]
model_artm=artm.ARTM(num_topics=topics,topic_names=topic_names,
                     num_processors=2,class_ids={"text":1}
                     ,reuse_theta=True,cache_theta=True)
np.random.seed(1)
dictionary=artm.Dictionary("dictionary")
dictionary.gather(batch_vectorizer.data_path)
model_artm.initialize(dictionary=dictionary)
model_artm.scores.add(artm.PerplexityScore("perplexity",class_ids=["text"],dictionary=dictionary))
model_artm.num_document_passes=1
model_artm.fit_offline(batch_vectorizer=batch_vectorizer,
                       num_collection_passes=45)
print("Перплексия artmPLSA: ",model_artm.score_tracker["perplexity"].value[-1])
model_lda=artm.LDA(num_topics=topics,num_processors=2,cache_theta=True)
model_lda.initialize(dictionary=dictionary)
model_lda.num_document_passes=1
model_lda.fit_offline(batch_vectorizer=batch_vectorizer,
                       num_collection_passes=45)
print("Перплексия artmLDA: ",model_lda.perplexity_last_value)