# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 19:36:02 2015

@author: Xiang Li
"""

import os
os.chdir("/Users/apple/Documents/MSiA/Fall 2015/Text analytics/HW/hw2")

from nltk.corpus import stopwords
import re

#%% count unigram and give 20 words with the most frequency
def uniCount(list, stop = stopWord,pattern = nonPunc,k = 20):
    wordFreq = dict()
    
    for i in list:
        if i not in stop and pattern.match(i) != None:
            if i in wordFreq.keys():
                wordFreq[i] = wordFreq[i] + 1
            else:
                wordFreq[i] = 1
    
    wordList = []
    for key, value in wordFreq.items():
        temp = (key,value)
        wordList.append(temp)
    #other way: wordList = list(wordFreq.items())
   
    #find top freq and return corresponding words   
    topKwords = []
    ignorIndex = []
    find = False
    
    while not find:       
        max = 0
        toCheck = set(range(len(wordList))).difference(ignorIndex)
        
        for i in toCheck:
            if wordList[i][1] > max:
                max = wordList[i][1]
                max_index = i
        
        ignorIndex.append(max_index)                       
        
        if len(topKwords) <= k-1:
            topKwords.append(wordList[max_index])
            find = False              
        elif len(topKwords) > k-1 and max != wordList[max_index][1]:
            find = True

    return topKwords
 
uniCount(words,k= 20)
#len(uniCount(words))   
#%% count bigram and give 20 words with the most frequency
def biCount(list, stop = stopWord,pattern = nonPunc,k = 20):
    wordFreq = dict()
    
    i = 0
    while i < len(list)-1:
        if (list[i] not in stop and list[i+1] not in stop and pattern.match(list[i]) != None 
        and pattern.match(list[i+1]) != None):
            biGram = list[i] +" "+ list[i+1]
            if biGram in wordFreq.keys():
                wordFreq[biGram] = wordFreq[biGram] + 1
            else:
                wordFreq[biGram] = 1
        i += 1
    
    wordList = []
    for key, value in wordFreq.items():
        temp = (key,value)
        wordList.append(temp)
    #other way: wordList = list(wordFreq.items())
   
    #find top freq and return corresponding words   
    topKwords = []
    ignorIndex = []
    find = False
    
    while not find:       
        max = 0
        toCheck = set(range(len(wordList))).difference(ignorIndex)
        
        for i in toCheck:
            if wordList[i][1] > max:
                max = wordList[i][1]
                max_index = i
        
        ignorIndex.append(max_index)                       
        
        if len(topKwords) <= k:
            print(len(topKwords))
            topKwords.append(wordList[max_index])
            find = False 
             
        elif len(topKwords) > k and max != wordList[max_index][1]:
            find = True        
    

    return topKwords

biCount(words, k= 20)
    
#%% read file line by line into list
infile = open('hw_2_Q3_output.txt', 'r')
text = [line.decode("ascii" , "ignore").encode("ascii") for line in infile]

words = []

#read each word into a list by filtering out all punctuation
for line in text:
    line = line.strip().split(" ")
    print(line)
    [words.append(word) for word in line if word not in ("\n","")]      

print(len(words)) #total 9513 words  

#%% check set of punctuation and stopword

#import stopwords from nltk stopwords, add 'I' since it is also counted as a stopword
stopWord = set(stopwords.words('english'))
stopWord.add("I")

nonPunc = re.compile(r"[0-9a-zA-Z]-?[0-9a-zA-Z]")

topWords = 20

#%% find top 20 words with the most frequency
uniCount(words)

#%% find top 20 words with the most frequency
biCount(words)
