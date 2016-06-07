# -*- coding: utf-8 -*-
"""
Created on Tue Nov  14

@author: Xiang Li
"""

import os
os.chdir("/Users/apple/Documents/MSiA/Fall 2015/Text analytics/HW/hw3")

from nltk.corpus import stopwords
import re
from stanford_corenlp_pywrapper import CoreNLP
import pandas as pd
import numpy as np
from sklearn.metrics import pairwise_distances
from scipy.spatial.distance import cosine
from numpy import unravel_index
import math
import sys
#%% read file
with open ("classbios.txt", "r") as myfile:
    data=myfile.read()
    
text = data.decode("ascii" , "ignore").encode("utf-8")

#%% get file names
file_names = re.findall(r"==>.+<==", text)
names = []

for i in range(len(file_names)):
    file_names[i] = file_names[i].replace("-late"," ")
    m = re.search(r"\b[a-z]+-+[a-z]+(?:-+[a-z]+)?", file_names[i])
    file_names[i] = m.group(0)

#%% save doc with its file name
doc = re.split(r"==>.+<==", text)
doc.pop(0)

files = dict()

os.makedirs("bio_output")
os.chdir(os.path.join(os.getcwd(),"bio_output"))

for i in range(len(doc)):
    files[file_names[i]] = doc[i].replace("\n"," ")
    file = open(file_names[i]+".txt", "w")
    file.write(doc[i])
    file.close()

#%% check set of non-word characters and stopword
os.chdir("/Users/apple/Documents/MSiA/Fall 2015/Text analytics/HW/hw3")

proc = CoreNLP("pos", corenlp_jars=["/Users/apple/corenlp/stanford-corenlp-full-2015-04-20/*"])

for i in files.keys():
    text = files[i]
    parsed = proc.parse_doc(text)
    to_flat = [x["lemmas"] for x in parsed["sentences"]]
    words = [item for sublist in to_flat for item in sublist]
    files[i] = words
#%%
#import stopwords from nltk stopwords, add 'I' since it is also counted as a stopword
stopWord = set(stopwords.words('english'))
stopWord.add("I")
all_words = []
nonWords = re.compile(r"^\b[a-zA-Z]+-?[a-zA-z]+$")

for i in files.keys():
    text = files[i]
    words = []
    for w in text:
        if nonWords.match(w):
            if w not in stopWord:
                words.append(w)
                all_words.append(w)
                
    files[i] = words

uniq_words = list(set(all_words))

#%% raw frequency matrix & binary term_doc matrix
series = pd.Series(uniq_words)
series_count = series.count

freq_count = dict()


for i in file_names:
    series = pd.Series(files[i])
    counts = series.value_counts()    
    freq_count[i] = counts

freq_matrix = pd.DataFrame(freq_count).fillna(0)

binary_matrix  = freq_matrix.copy(deep = True)
binary_matrix[binary_matrix > 1] = 1  #convert values > 1 to 1 to create binary variables
#%% get similarity matrix
def convertSimi(matrix = np.zeros([1769, 30])):
    transpose = matrix.transpose()
    simi_matrix = 1-pairwise_distances(transpose, metric="cosine")
    return simi_matrix

#%%convert binary_matrix to binary_simi matrix: simi_matrix
simi_matrix = convertSimi(binary_matrix)
#save similarity matrix to text file
np.savetxt("boolean.txt", simi_matrix , fmt='%.3f', delimiter = " ")
#%%find top K with most similaryty
def mostSimilar(ma = np.zeros([30,30]), TopK = 3):
    matrix = ma.copy()
    topSimilar = dict()
    np.fill_diagonal(matrix,-1)

    for i in range(1,TopK+1):
        (row, col) = np.unravel_index(np.argmax(matrix), matrix.shape)
        topSimilar[i] = (row, col)
        matrix[row,col] = -1
        matrix[col,row] = -1
    return topSimilar

#%%find top K with least similarity
def leastSimilar(ma = np.zeros([30,30]), K = 3):
    matrix = ma.copy()
    leastSimilar = dict()
    np.fill_diagonal(matrix,2)

    for i in range(1,K+1):
        (row, col) = np.unravel_index(np.argmin(matrix), matrix.shape)
        leastSimilar[i] = (row, col)
        matrix[row,col] = 2
        matrix[col,row] = 2
    return leastSimilar
    
#%%find 3 most similar
boolean_most = mostSimilar(simi_matrix,3)
#%%find 3 least similar
boolean_least = leastSimilar(simi_matrix,3)

#%% turn freq_matrix into tf-idf_simi_matrix
w_in_docs = []
for index, row in binary_matrix.iterrows():
    w_in_docs.append(float(sum(row)))

N = len(file_names)
tf_idf = freq_matrix.copy(deep = True)

for i in tf_idf.columns:
    for a in range(len(tf_idf[i])):
        if tf_idf[i][a] != 0:
            #print('a '+ str(tf_idf[i][a]))
            tf = 1+math.log10(tf_idf[i][a])
            idf = math.log10(N/w_in_docs[a])
            #print tf,idf
            tf_idf[i][a] = tf*idf
        else:
            tf_idf[i][a] = 0
#%%convert tf-idf to tf_idf_simi matrix
tf_idf_simi = convertSimi(tf_idf)
np.savetxt("tf_idf.txt", tf_idf_simi , fmt='%.3f', delimiter = " ")

#%%find 3 most similar
tf_if_most = mostSimilar(tf_idf_simi,3)
#%%find 3 least similar
tf_if_least = leastSimilar(tf_idf_simi,3)
#%%save result function
def output(dic_most = dict(),dic_least = dict(),file_names = [1,2],
           simi_matrix = np.zeros([2,2]),
           file_name = 'boolean_output.txt'):


    orig_stdout = sys.stdout
    f = open(file_name, 'w')
    sys.stdout = f
    
    print("\n")
    print("\n*****************Most*****************\n")
    
    for i in dic_most.keys():
        (a,b) = dic_most[i]
        print(str(i)+': '+file_names[a]+' '+file_names[b]+', similarity = '+str(simi_matrix[a][b])+'\n')
    
    print("\n*****************Least*****************\n")
    
    for i in dic_least.keys():
        (a,b) = dic_least[i]
        print(str(i)+': '+file_names[a]+' '+file_names[b]+', similarity = '+str(simi_matrix[a][b])+'\n')
    
    print("\n")
    print("Output files saved in: {}\n".format(os.getcwd()))
                                           
    f.close()
    sys.stdout = orig_stdout

#%%output results
output(boolean_most,boolean_least,file_names,
           simi_matrix,
           'boolean_output.txt')
   
output(tf_if_most,tf_if_least,file_names,
           tf_idf_simi,
           'tf_idf_output.txt')
   
    

