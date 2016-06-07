# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10

@author: Xiang Li
IDE: Spyder Python 3.4
"""

'''
We can use the idea of bisection search to determine if a character is in a string, 
so long as the string is sorted in alphabetical order.
'''

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here

    if aStr != '' and char == aStr[int(len(aStr)/2)]:
        return True
    if aStr == '':
        return False
    else:
        if char < aStr[int(len(aStr)/2)]:
            return isIn(char,aStr[:int(len(aStr)/2)])
        if char > aStr[int(len(aStr)/2)]:
            return isIn(char,aStr[int(len(aStr)/2)+1:])

#%%test
isIn('y', 'gtwy')
