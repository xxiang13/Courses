# -*- coding: utf-8 -*-
"""
Created on Tue May 24

@author: Xiang Li
"""

"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""

class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def peek(self):
        return(self.storage[0])

    def dequeue(self):
        first = self.storage[0]
        # first in first out
        self.storage = self.storage[1:]
        return first

#%%
# Setup
if __name__ == '__main__':
    q = Queue(1)
    q.enqueue(2)
    q.enqueue(3)
    
    # Test peek
    # Should be 1
    print(q.peek())
    
    # Test dequeue
    # Should be 1
    print(q.dequeue())
    
    # Test enqueue
    q.enqueue(4)
    # Should be 2
    print(q.dequeue())
    # Should be 3
    print(q.dequeue())
    # Should be 4
    print(q.dequeue())
    q.enqueue(5)
    # Should be 5
    print(q.peek())