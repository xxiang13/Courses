# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10

@author: Xiang Li

IDE: Spyder Python 3.4
"""
'''
Lec5 problem 7:
For this problem, write a recursive function, lenRecur, which computes the length of an input argument (a string), 
by counting up the number of characters in the string.
'''
def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    print(aStr)
    if aStr == '':
        return 0      
    else:
        return 1+ lenRecur(aStr[:-1])
#%%test
lenRecur('abc')
#%%
