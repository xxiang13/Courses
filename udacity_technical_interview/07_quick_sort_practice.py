# -*- coding: utf-8 -*-
"""
Created on Sat May 28

@author:Xiang Li
"""

"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def partition(array,left,right):
    
    pivot = array[left]
    low = left + 1
    
    while low < right:
        while array[low] < pivot:
            low += 1
            
        while array[right] > pivot:
            right -= 1
        
        
        if low < right:
            array[low], array[right] = array[right],array[low]
            low += 1
            right -= 1

    if low == right:
        if array[low] < pivot:
            array[low], array[left] = array[left],array[low]
            return low
        else:
            array[low-1], array[left] = array[left],array[low-1]
            return low-1
    elif low > right:
        array[right], array[left] = array[left],array[right]
        return right
    

def quick_sort(array,left,right):
    if left < right:
        p = partition(array,left,right)
        quick_sort(array,left,p-1)
        quick_sort(array,p+1,right)
        
def quicksort(array):
    quick_sort(array,0,len(array)-1)
    return array
#%%
if __name__ == '__main__':
    test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    print(quicksort(test))