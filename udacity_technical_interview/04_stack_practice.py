# -*- coding: utf-8 -*-
"""
Created on Tue May 24

@author: Xiang
"""

"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.

You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.

Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?
=> append needs to iterate all element until the end O(n),
   but insert_first always insert at the beginning O(1)"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        # insert new element at first position in linked list    
        new_element.next = self.head
        self.head = new_element

        
        
    def delete_first(self):
        # delete new element at first position in linked list, 
        # return none if there is no element left
        if self.head:
            current = self.head
            self.head = current.next
            return current
        else:
            return None

#%%
class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        return self.ll.insert_first(new_element)

    def pop(self):
        return self.ll.delete_first()
    
#%%
# Test cases
# Set up some Elements
if __name__ == '__main__':
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)
    
    # Start setting up a Stack
    stack = Stack(e1)
    
    # Test stack functionality
    stack.push(e2)
    stack.push(e3)
    print(stack.pop().value)
    print(stack.pop().value)
    print(stack.pop().value)
    print(stack.pop())
    stack.push(e4)
    print(stack.pop().value)