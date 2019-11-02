# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 14:22:35 2019

@author: dim
"""

import pandas as pd
import numpy as np
import artm

lenta=pd.read_csv("lenta_ru.csv")
topics=len(set(lenta["topic"]))
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
print("Перплексия artm без регуляризаторов: ",model_artm.score_tracker["perplexity"].value[-1])

model_artm=artm.ARTM(num_topics=topics,topic_names=topic_names,
                     num_processors=2,class_ids={"text":1}
                     ,reuse_theta=True,cache_theta=True)
dictionary=artm.Dictionary("dictionary")
dictionary.gather(batch_vectorizer.data_path)
model_artm.initialize(dictionary=dictionary)
model_artm.scores.add(artm.PerplexityScore("perplexity",class_ids=["text"],dictionary=dictionary))
model_artm.regularizers.add(artm.DecorrelatorPhiRegularizer(tau=1e4,class_ids="text",
                                                            topic_names=topic_names))
model_artm.fit_offline(batch_vectorizer=batch_vectorizer,
                       num_collection_passes=45)
print("Перплексия artm с хорошим регуляризатором: ",model_artm.score_tracker["perplexity"].value[-1])

model_artm=artm.ARTM(num_topics=topics,topic_names=topic_names,
                     num_processors=2,class_ids={"text":1}
                     ,reuse_theta=True,cache_theta=True)
dictionary=artm.Dictionary("dictionary")
dictionary.gather(batch_vectorizer.data_path)
model_artm.initialize(dictionary=dictionary)
model_artm.scores.add(artm.PerplexityScore("perplexity",class_ids=["text"],dictionary=dictionary))
model_artm.regularizers.add(artm.SmoothSparsePhiRegularizer(tau=-1e5,class_ids="text",
                                                            dictionary="dictionary",
                                                            topic_names=topic_names.remove('bcg')))
model_artm.fit_offline(batch_vectorizer=batch_vectorizer,
                       num_collection_passes=45)
print("Перплексия artm с плохим регуляризатором: ",model_artm.score_tracker["perplexity"].value[-1])


