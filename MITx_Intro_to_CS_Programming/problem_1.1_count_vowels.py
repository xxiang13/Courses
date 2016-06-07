'''
Author: Xiang Li
IDE: Python 3.0 Spider
'''

'''
Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
Number of vowels: 5
'''



num_v = 0
vowels = ['a', 'e', 'i', 'o', 'u']
for i in range(len(s)):
    if s[i] in vowels:
        num_v += 1
 
print("Number of vowels: "+str(num_v))