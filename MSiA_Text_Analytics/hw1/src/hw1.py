# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 13:17:06 2015

@author: Xiang Shawn Li

IDE: Spyder python 3.4
"""
import os
os.getcwd()
os.chdir('/Users/apple/Documents/MSiA/Fall 2015/Text analytics/HW/hw1')

#%% Sentence sliptting
import nltk

bio_file = 'classbios.txt'
test_file = 'test_data.txt'
f = open(bio_file,encoding='latin2')
bio = f.read()
bio2 = bio.split('\n')

sentence_list = []
for i in bio2:
    sentence_list.append(nltk.sent_tokenize(i))
    
    
sentence_list = list(filter(None, sentence_list))

sentence_list2 = [item for sublist in sentence_list for item in sublist]

#%%Regular Expression
import re

file = open("classbios_timepoints.txt", "w")

for line in sentence_list2:
    
   
    pattern1 = re.compile(r"\b(?:(?:(?:[Jj]an)(?:uary)?|(?:[Ff]eb)(?:ruary)?|(?:[Mm]ar)(?:ch)?|(?:[aA]pr)(?:il)?|(?:[mM]ay)|(?:[jJ]une)|(?:[jJ]uly)|(?:[aA]ug)(?:ust)?|(?:[sS]ep)(?:tember)?|(?:[oO]ct)(?:ober)?|(?:[nN]ov|[dD]ec)(?:ember)?))")
    pattern2 = re.compile(r"\b(?:[Tt]his|[Ll]ast|[pP]ast|[nN]ext)?(?:(?:[fF]all|[sS]pring|[sS]ummer|[wW]inter)|[iI]n|[qQ]uarter)")
    pattern3 = re.compile(r"[/.-]? [0-9]{4}")

    a = pattern1.search(line)
    b = pattern2.search(line)
    c = pattern3.search(line)
    
    
    if a is not None or b is not None:
        if c is not None:  
            line = line+"\n"
            file.write(line.encode('ascii', 'ignore').decode('ascii'))

file.close()