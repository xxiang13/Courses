# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16

@author: Xiang Li

IDE: spyder Python 3.4
"""

"""
Write a function called ndigits, that takes an integer x (either positive or negative) as an argument. 
This function should return the number of digits in x.
"""

def ndigits(aInt):
    '''
    aInt: A integer

    returns: int, how many digits aInt contains
    '''
    aInt = abs(aInt)
    if aInt//10 == 0:
        return 1
    else:
        return 1 + ndigits(aInt//10)

#%%test
ndigits(123)
ndigits(-7834236)