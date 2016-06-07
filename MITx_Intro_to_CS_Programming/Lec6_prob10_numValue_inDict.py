# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 

@author: Xiang Li
"""

def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    sumValue = 0
    for i in aDict.keys():
        sumValue = sumValue + len(aDict[i])
    return sumValue
    
#%%test
howMany({ 'a': [1,2,3], 'b': [1], 'c': [1,2]})