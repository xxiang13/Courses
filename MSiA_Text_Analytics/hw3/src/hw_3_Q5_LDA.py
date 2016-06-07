# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 16:31:37 2015

@author: Xiang Shawn Li
"""

import os
os.chdir("/Users/apple/Documents/MSiA/Fall 2015/Text analytics/HW/hw3")
import json
import pandas as pd
import lda
import numpy as np
import time
import operator
#%%read termsFreq.json to dictionary
with open('termsFreq.json', 'r') as fp:
    termsFreq = json.load(fp)
    
#%%

freqDict = dict()
for i in termsFreq.keys():
    
    #get terms frequency of doc i
    freq = pd.Series(termsFreq[i])
    freqDict[i] = freq

# convert freqDict to pandas data frame, columns are doc name, rows are words
# fill missing value by zero
freqDF = pd.DataFrame(freqDict).fillna(0, inplace = False)

# overall matrixs generates 80MB csv file. the file is too large, 
# so generate first 1000 rows instead as a sample
freqDF[:1000].to_csv("termsFreqMatrix.csv",sep=",", header=True, index=True,encoding='utf-8')

#%%

# convert df to matrix

freqMa = freqDF.as_matrix()

#for lda function, row = doc, column = terms => transpose matrix
freqMaT = freqMa.transpose()
freqMaT2 = freqMaT.astype(np.int64)

terms = freqDF.index
doc = freqDF.columns

#generage lda function
model = lda.LDA(n_topics=100, n_iter=1500, random_state=1)

# before training/inference:
SOME_FIXED_SEED = 0124
np.random.seed(SOME_FIXED_SEED)

t0 = time.time()
model.fit(freqMaT2)

t1 = time.time()
print(t1-t0)

topicFeature = dict()
for i in range(len(model.nz_)):
    topicFreq = model.nz_[i]
    topicWord = model.topic_word_[i]   
    topicFeature[i] = [topicFreq,topicWord]


# find top n topics
topTopic = dict(sorted(topicFeature.iteritems(), key=operator.itemgetter(1), reverse=True)[:10])
for i in topTopic.keys():
    topTopic[i] = pd.Series(topTopic[i], index = ['Counts','topic_dist'])
    
topTopicDF = pd.DataFrame(topTopic)
topTopicDF2 = topTopicDF.transpose()
topTopicDF2 = topTopicDF2.sort(['Counts'], ascending=False)

n_top_words = 10

for i in topTopicDF2.index:
    topic_dist = topTopicDF2['topic_dist'][i]
    topic_words = np.array(terms)[np.argsort(topic_dist)][:-(n_top_words+1):-1]
    print('Topic {}: {}'.format(i, ' '.join(topic_words)))