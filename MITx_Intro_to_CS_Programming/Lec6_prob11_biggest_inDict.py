# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 22:32:07 2016

@author: apple
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    if len(aDict.keys()) == 0:
        return None
    else:
        maxValue = -1
        i = int()
        for i in aDict.keys():
            if len(aDict[i]) > maxValue:
                maxValue = len(aDict[i])
                maxKey = i
        return maxKey
#%%test
biggest({ 'a': [1,2,3], 'b': [1,2], 'c': [3,2,3,3]})