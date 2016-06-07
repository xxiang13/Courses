'''
Author: Xiang Li
IDE: python 3.0 Spider
''' 


'''
Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print
Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
Longest substring in alphabetical order is: abc
'''

def find_alphabetical_substr(s)
	max_sub = ''
	left = 0
	right = 1
	while right < len(s):
	    if s[right] >= s[right-1]:
	        sub = s[left:right+1]
	        right += 1
	        if len(sub) > len(max_sub):
	            max_sub = sub
	    else:
	        left = right
	        right += 1 
	        
	if max_sub == '': #if max_sub is null => first char is larest one, return itself
	    max_sub = s[0]
	print("Longest substring in alphabetical order is: "+ max_sub)


s = 'azcbobobegghakl'
find_alphabetical_substr(s)