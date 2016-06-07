# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10
@author: Xiang Li
IDE: Spyder Python 3.4
"""

'''
A semordnilap is a word or a phrase that spells a different word when backwards
 ("semordnilap" is a semordnilap of "palindromes"). Here are some examples:

nametag / gateman
dog / god
live / evil
desserts / stressed
Write a recursive program, semordnilap, that takes in two words and says if they are semordnilap.
'''

def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    if len(str1) == len(str2):    # two strings not same length => return False
        if str1 =='' and str2 =='': # if equal => sclicing string until empty => return True
            return True
            
        if str1[0] != str2[-1]:  # not equal => return False
    
            return False
        if str1 != '' and str2 != '' and str1[0] == str2[-1]:
    
            return semordnilap(str1[1:], str2[:-1])
    else:
        return False

#%%
def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)
    
    
#%%test
semordnilapWrapper('baa', 'aaa')