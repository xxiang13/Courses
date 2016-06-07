'''
Author: Xiang Li
IDE: Python 3.0 Spider
'''




'''
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 

For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
'''



def find_num_substring(string,target):
    num_bobs = 0
    
    for i in range(len(s)-len(target)+1):
        if s[i:i+len(target)] == target:
            num_bobs += 1
     
    print("Number of times bob occurs is: "+str(num_bobs))

    
s = 'azcbobobegghakl'
find_bobs(s,'bob')