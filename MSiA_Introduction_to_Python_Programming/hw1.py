
#################Excise 1###########################
#p function using quicksort algorithm, return the leftmark which is q

def p(l, i, j):
    pivotvalue = l[i]

    leftmark = i
    rightmark = j-1


    while rightmark >= leftmark:

        while l[leftmark] < pivotvalue:
            leftmark = leftmark +1

        while l[rightmark] > pivotvalue:
            rightmark = rightmark - 1

        if leftmark <= rightmark:
            temp = l[leftmark]
            l[leftmark] = l[rightmark]
            l[rightmark] = temp
            leftmark = leftmark +1
            rightmark = rightmark - 1

    return leftmark

#test the function p#
#l=[54,26,93,17,77,31,44,55,20]
#p(l,0,7)

####################Excise 2#########################

import random
import time

### used list ##
list_len = []
time_used = []

#run difference n for difference list length
for n in range(100000,1000000,100000):
    list_len.append(n)
    l = list(range(n)) # create a list with numbers 0 ... to n-1
    time_one_len = 0
    print(n)
#run 5 times to find average time for each list length
    for i in range(1,5,1):
        random.shuffle(l) # randomize the list
        timeStamp = time.process_time() # get the current cpu time
        p(l, 0, n) # run p function
        timeLapse = time.process_time() - timeStamp
        time_one_len = time_one_len + timeLapse
    time_ave = time_one_len / 5 #get the average time
    time_used.append(time_ave)

### used numpy ##
import numpy as np
list_len = []
time_used_np = []

for n in range(100000,1000000,100000):
    list_len.append(n)
    l = np.array(range(n)) # create a array
    time_one_len = 0
    print(n)
    for i in range(1,5,1):
        random.shuffle(l) # randomize the list
        timeStamp = time.process_time() # get the current cpu time
        p(l, 0, n) # run p function
        timeLapse = time.process_time() - timeStamp
        time_one_len = time_one_len + timeLapse
    time_ave_np = time_one_len / 5
    time_used_np.append(time_ave_np)

import matplotlib.pyplot as plt
#plot lines of list and array together, blue is for list and red is for array
plt.plot(list_len,time_used, '-bs',list_len,time_used_np,'-ro')
plt.xlabel("list length")
plt.ylabel("time")
plt.show()
#from plots of list & numpy, using numpy arrays needs more time to process


########################## Excise 3 ############################
def foo(a, i, j):
    if j-i>1:
        q=p(a,i,j)
        foo(a,i,q)
        foo(a,q,j)

#test function foo
#a=[54,26,93,17,77,31,44,55,20]
#foo(a,0,len(a))

#plot for list and array:

#give range list
a = [5, 10, 50,100,500, 1000, 2000,3000,4000,8000, 10000,20000,40000, 60000]

#used list#
def get_time_list():
    list_len = []
    time_used_ratio = []

    for n in a:
        list_len.append(n)
        l = list(range(n)) # create a list with numbers 0 ... to n-1
        time_sum_p = 0
        time_sum_foo = 0
        print(n)
        for i in range(1,50,1): #run 50 times to get the average time of function p for each list length
            random.shuffle(l) # randomize the list
            timeStamp_p = time.process_time() # get the current cpu time
            p(l, 0, len(l)) # run p function
            timeLapse_p = time.process_time() - timeStamp_p
            time_sum_p = time_sum_p + timeLapse_p
            
        for b in range(1,25,1): #run 25 times to get the average time of function foo for each time length
            random.shuffle(l)
            timeStamp_foo = time.process_time() # get the current cpu time
            foo(l,0,len(l)) # run p function
            timeLapse_foo = time.process_time() - timeStamp_foo
            time_sum_foo = time_sum_foo + timeLapse_foo
            
        time_ave_p = time_sum_p / 50
        time_ave_foo = time_sum_foo/25
        time_ave = time_ave_foo / time_ave_p #get  the ratio of average time of p and foo
        time_used_ratio.append(time_ave)
    return [list_len, time_used_ratio]

#used array#
def get_time_array():
    list_len = []
    time_used_ratio = []

    for n in a:
        list_len.append(n)
        l = np.array(range(n)) # create a array
        time_sum_p = 0
        time_sum_foo = 0
        print(n)
        for i in range(1,50,1):
            random.shuffle(l) # randomize the list
            timeStamp_p = time.process_time() # get the current cpu time
            p(l, 0, len(l)) # run p function
            timeLapse_p = time.process_time() - timeStamp_p
            time_sum_p = time_sum_p + timeLapse_p
            
        for b in range(1,25,1):
            random.shuffle(l)
            timeStamp_foo = time.process_time() # get the current cpu time
            foo(l,0,len(l)) # run p function
            timeLapse_foo = time.process_time() - timeStamp_foo
            time_sum_foo = time_sum_foo + timeLapse_foo
            
        time_ave_p = time_sum_p / 50
        time_ave_foo = time_sum_foo/25
        time_ave = time_ave_foo / time_ave_p
        time_used_ratio.append(time_ave)
    return [list_len, time_used_ratio]

time_used_list = get_time_list()
time_used_array = get_time_array()


import matplotlib.pyplot as plt
plt.plot(time_used_list[0],time_used_list[1],'-bs', time_used_array[0], time_used_array[1],'-ro')
plt.xlabel("list length")
plt.ylabel("time(foo)/time(p)")
plt.show()



########################## Exercise 4 ################################
def bar(a,i,j,k):
    if j-i==1:
        return a[i]
    q = p(a,i,j);
    if k<q:
        return bar(a,i,q,k)
    else:
        return bar(a,i,q,k)

#test bar:
#bar(a,0,len(a),3)

#plot time vs. len(a)
#usef fixed k = 100 by randomly choosing K in (0,len(a))
def get_time_length():
    list_len = []
    time_used = []

    for n in range(1000000,10000000,1000000):
        list_len.append(n)
        l = list(range(n)) # create a list with numbers 0 ... to n-1
        time_sum = 0
        k = 100 #pick a fixed k

        for i in range(1,5,1):
            random.shuffle(l) # randomize the list
            timeStamp = time.process_time() # get the current cpu time
            bar(l, 0, len(l),k) # run p function
            timeLapse = time.process_time() - timeStamp

            time_sum = time_sum + timeLapse

        time_ave = time_sum / 5
        time_used.append(time_ave)
    return [list_len, time_used]

time_used = get_time_length()
import matplotlib.pyplot as plt
plt.plot(time_used[0],time_used[1],'-bs')
plt.xlabel("list length")
plt.ylabel("time(bar)")
plt.show()


#plot time vs. k
#used fixed n = 1000, randomly chosed K in range(0,len(n))
def get_time_k():
    n = 1000
    choose_k = []
    time_used = []

    for k in range(100,1000,58): #randomly chosed K in range(0,len(n))
        choose_k.append(k)
        l = list(range(n)) # create a list
        time_sum = 0

        print(k)
        for i in range(1,5,1):
            random.shuffle(l) # randomize the list
            timeStamp = time.process_time() # get the current cpu time
            bar(l, 0, len(l),k) # run p function
            timeLapse = time.process_time() - timeStamp

            time_sum = time_sum + timeLapse

        time_ave = time_sum / 5
        time_used.append(time_ave)
    return [choose_k, time_used]
    
    
time_used_k = get_time_k()
import matplotlib.pyplot as plt
plt.plot(time_used_k[0],time_used_k[1],'bs')
plt.xlabel("K")
plt.ylabel("time(bar)")
plt.show()