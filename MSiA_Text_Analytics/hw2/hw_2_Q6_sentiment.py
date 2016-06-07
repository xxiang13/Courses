# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 19:47:20 2015

@author: apple
"""
import re
import os
import math
import pandas as pd
from matplotlib import pylab as pl
from sklearn.metrics import confusion_matrix
path = "/Users/apple/Documents/MSiA/Fall 2015/Text analytics/HW/hw2/"
#%% read all positive review files into a dictionary
os.chdir(os.path.join(path,"review_polarity/","txt_sentoken/","pos/"))

pos = dict()
allW_pos = 0

files_pos = [f for f in os.listdir('.') if re.match(r'[A-Z0-9a-z_]+.txt', f)]

for i in range(len(files_pos)): 
    print(i)
    lines = [line.strip() for line in open(files_pos[i], 'r')]
    lines = [line.split(" ") for line in lines]
    tokens = [item for sublist in lines for item in sublist]
    allW_pos += len(tokens)
    pos[i] = tokens     

#%% read all negative review files into a dictionary
os.chdir(os.path.join(path,"review_polarity/","txt_sentoken/","neg/"))

neg = dict()
allW_neg = 0

files_neg = [f for f in os.listdir('.') if re.match(r'[A-Z0-9a-z_]+.txt', f)]

for i in range(len(files_neg)): 
    print(i)
    lines = [line.strip() for line in open(files_neg[i], 'r')]
    lines = [line.split(" ") for line in lines]
    tokens = [item for sublist in lines for item in sublist]
    allW_neg += len(tokens)
    neg[i] = tokens 

#%% train model
def senti_class(file_start = 0, file_end = 100):
    
## step 1: freq of every word in vocabulary in each class (bag of words of each class)
    pos_bag = dict()
    neg_bag = dict()
    
    for i in range(file_start,file_end):  
        for a in pos[i]:
            if a in pos_bag.keys():
                pos_bag[a] = pos_bag[a] + 1
            else:
                pos_bag[a] = 1
                
        for b in neg[i]:     
            if b in neg_bag.keys():
                neg_bag[b] = neg_bag[b] + 1
            else:
                neg_bag[b] = 1
                
    #get all vocabularies from all classes
    v = set(pos_bag.keys()+neg_bag.keys())
    all_v = len(set(pos_bag.keys()+neg_bag.keys()))
    
    ## step 2: add 1 to all word frequencies in each class, 
    #and then normalize the frequencies to get probabilities
    model = dict()
    
    for i in v:
        
        if i in pos_bag.keys():
            word_freq_pos = pos_bag[i]
        else: 
            word_freq_pos = 0
        
        if i in neg_bag.keys():
            word_freq_neg = neg_bag[i]
        else: 
            word_freq_neg = 0
            
        word_prob_pos = (word_freq_pos + 1)/float((allW_pos+all_v))
        word_prob_neg = (word_freq_neg + 1)/float((allW_neg+all_v))
        
        model[i] = [math.log(word_prob_pos),math.log(word_prob_neg)]       
    
    return model

#%% evaluate model with file cv6*.txt, cv7*.txt
def test_model(file_start = 600, file_end = 800, model= model ,prob_pos_log = 0.5,prob_neg_log=0.5):
    test_pos = dict()
    test_neg = dict()
    
    for i in range(file_start,file_end):  
        print(i)
        test_pos[i] = pos[i]
        test_neg[i] = neg[i]
    
    pos_pre = []
    neg_pre = []
    
    for i in test_pos.keys():
        prob_pos = prob_pos_log
        prob_neg = prob_pos_log
        
        for a in test_pos[i]:
            if a in model:
                prob_pos += model[a][0]
                prob_neg += model[a][1]
                
        if prob_pos > prob_neg:
            pos_pre.append(1)
        else:
            pos_pre.append(0)
        
        for a in test_neg[i]:
            if a in model:
                prob_pos += model[a][0]
                prob_neg += model[a][1]
        
        if prob_pos > prob_neg:
            neg_pre.append(1)
        else:
            neg_pre.append(0)
    
    return pos_pre+neg_pre
    
    

#%% evaluate result
def senti_analysis(train_start = 0, train_end = 100, test_start = 600, test_end = 800,prob_pos = 0.5,prob_neg = 0.5):
    prob_pos_log = math.log(prob_pos) #log prob of class posiive
    prob_neg_log = math.log(prob_neg) #log prob of class negative
    pos_value = [1]*200
    neg_value = [0]*200
    
    y_actu = pos_value+neg_value
    model = senti_class(train_start,train_end) 

    y_pred = test_model(test_start,test_end,model,prob_pos_log,prob_neg_log)
    
    y = pd.Series(y_actu, name='y_actu')
    y_hat = pd.Series(y_pred, name='y_pred')
    df_confusion = pd.crosstab(y, y_hat)
    
    Precision = df_confusion[1][1]/float(sum(df_confusion[1]))  #tp/(tp + fp)
    Recall = df_confusion[1][1]/float((df_confusion[0][1]+df_confusion[1][1])) #tp/(tp + fn)
    
    F_score = (2*Precision*Recall)/(Recall+Precision)   #F=2PR/(P+R)
    
    return (Precision,Recall,F_score)

#%% compare different models

# for input senti_analysis(): train_start = 0, train_end = 100, test_start = 600, test_end = 800,prob_pos = 0.5,prob_neg = 0.5

result1 = senti_analysis(0,100,600,800,0.5,0.5)
#result2 = senti_analysis(0,200,600,800,0.5,0.5)
result3 = senti_analysis(0,300,600,800,0.5,0.5)
result4 = senti_analysis(0,500,600,800,0.5,0.5)
result5 = senti_analysis(0,600,600,800,0.5,0.5)

p_line = pl.plot([100,300,500,600], [result1[0],result3[0],result4[0],result5[0]],label='precision') #plot for precision cross models
r_line = pl.plot([100,300,500,600], [result1[1],result3[1],result4[1],result5[1]],label='recall') #plot for recall cross models
f_line = pl.plot([100,300,500,600], [result1[2],result3[2],result4[2],result5[2]],label='f_score') #plot F score cross models
pl.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,ncol=3, mode="expand", borderaxespad=0.)
pl.xlabel('number of files in training set')
pl.ylabel('evluation metrics')

#%% final prediction on file cv8, cv9
result_final = senti_analysis(0,800,800,1000,0.5,0.5)