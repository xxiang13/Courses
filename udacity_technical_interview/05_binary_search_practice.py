# -*- coding: utf-8 -*-
"""
Created on Wed May 25

@author: Xiang Li
"""

"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.

Your function should take two inputs:
a Python list to search through, and the value
you're searching for.

Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.

Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    left = 0 # left mark
    right = len(input_array) # right mark
    middle = right//2 -1
    
    while input_array[left:right]: # iterate until slice empty array

        middle = (right+left)//2 # get middle index
        if input_array[middle] == value:
            return middle
        elif input_array[middle] > value:
            right = middle # update right mark
        elif input_array[middle] < value:
            left = middle+1 #update left mark

    return -1       


#%%
test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))