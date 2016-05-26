# -*- coding: utf-8 -*-
"""
Created on Mon May 23

@author: Xiang Li
"""

"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

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
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head

        if self.head: 
            i = 1
            while current.next and i < position:
                current = current.next
                i += 1
            if i == position:
                return current
            else:
                return None
        
        else:
            return None
    
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        
        if position == 1:
            new_element.next = self.head
            self.head = new_element
            
        else:
            if self.get_position(position): ## if the position exists
                current = new_element
                ## link after element first in case lose the relationship
                current.next = self.get_position(position)
                self.get_position(position-1).next = current ## link before element

    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        i = 1
        while self.get_position(i).value != value:
            print(self.get_position(i).value)
            i += 1
        
        if i == 1: ## if first element to be deleted, set self.head = 2nd element
            self.head = self.get_position(i+1)
        else: ## delete element by deleting links with before, after elements
            self.get_position(i-1).next = self.get_position(i+1)

#%%
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e4,3)
# Should print 4 now
print(ll.get_position(3).value)

# Test delete
ll.delete(1)
# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)
