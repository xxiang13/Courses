# -*- coding: utf-8 -*-
"""
@author: Xiang Li

Write a function to compute exponential: base^exp
"""


#%% problem 1: Interactive way

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    result = base
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        while exp > 1:
            result = result * base
            exp -= 1
        return result
        
        
#%% problem 2: Recursive way
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base*recurPower(base,exp-1)
        
#%% problem 3: seperate exp odd/even cases
        
def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    # Your code here
    if exp == 0:
        return 1

    if exp%2 == 0:
        if exp == 2:
            return base*base
        else:
            return (base*base)*recurPowerNew(base,exp-2)
    else:
        if exp == 1:
            return base
        else:
            return base*recurPowerNew(base,exp-1)

#%% test
iterPower(2,3)
recurPower(2,3)