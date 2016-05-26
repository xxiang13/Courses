# -*- coding: utf-8 -*-
"""
Created on Wed May 25 22:45:02 2016

@author: apple
"""

"""Implement a function recursivly to get the desired
Fibonacci sequence value.

The Fibonacci Sequence follows one rule: get the next 
number in the sequence by adding the two previous numbers.

Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    
    if position == 0 or position == 1:
        return position

    return get_fib(position-1)+get_fib(position-2)

#%%
# Test cases
print(get_fib(9))
print(get_fib(11))
print(get_fib(0))
