# -*- coding: utf-8 -*-
"""
Assignment2
Date: 4/14/15
"""

import math
from scipy import optimize as op
import pandas
#%% Exercise 1 ###############################################################

def createPolynomial(parameter):
    
    def poly(x):
        p = 0
        i = 0
        while (i < len(parameter)):
            p += parameter[i]* (x**i)
            i += 1
        return p
    return poly #return funtion p

#%% Exercise 1 test

p = createPolynomial( (2, -4, 3) )
y = p(5)
print(y) # answer should be 57    

#%% Exercise 2 ###############################################################
'''
estderi function give a estimated first derivaritive of input funtion f
@ f: input function
@ d: paramter to estimate the derivative
     small value of d (relative to xtol)
'''

def estderi(f,d):
    
    def poly(x):
        fprime = (f(x+d)-f(x-d)) / (2*d)
        return fprime
    return poly
    
'''
Write a function fsolve(f, x0, fprime=None, xtol=1.49012e-08, maxiter=100)
112. that returns one real solution of the equation defined by f(x) = 0 given
113. a starting estimate x0 using Newton's method.

@f : callable(x)
     A function that takes exactly one number argument.

@x0 : float
      The starting estimate for the real root of f(x) = 0.

@fprime : callable(x), optional
          A function to compute the derivative of func. If the user does not supply
          an argument, estimate the derivative as (f(x+d)-f(x-d)) / (2*d) using a
          small value of d (relative to xtol).

@xtol : float, (optional) 
        The calculation will terminate if the relative error between two consecutive
'''
def fsolve(f,x0,fprime=None,xtol=1.49012e-08, maxiter=100):

    if (fprime == None): #check if fprime provided, if no, give estimated derivative
        d = xtol/2
        fprime = estderi(f,d) #call estderi function to get the estimated derivative
    
    error = 1  #give a large initial error
    x = x0
    i = 0
    
    # iterate until error in x within tolerance
    while (error > xtol):
        xnew = x - f(x)/fprime(x) #compute new x based on previous x
        error = abs(xnew - x)
        x = xnew #update new x
        i += 1
        if (i >100): #if interation larger than the max interation, throw exception
            raise RuntimeError("Exceed max number of iterations"+str(maxiter))
        print("iteration:"+str(i)+" "+"value:"+str(x))
    return x

#%% Exercise 3 ###############################################################
'''
Test the functions you wrote in the previous two exercises. In particular. 
What does your fsolve return with the following five inputs? 
How many iterations did it take?:
'''
  
def aSillyFunction(x):
    return x**x-10

# x = 2.506184145588769, iterations = 27    
v1 = fsolve(aSillyFunction, 1)

# x = 3.141592653589793, iterations = 6
v2 = fsolve(math.sin, 2)

# x = error (division by zero), stopped iteration = 4
# first derivative ~ zero for almost all big values
# solution should be a very big number (x=2^(128) = 3.4*10^(38))
v3 = fsolve(lambda x: math.log2(x)-128, 1)

# funtion = 8*x^6 + 1
# x = error (division by zero), stopped iteration 96
# first derivative ~ zero when x ~ 0 (starting point)
# solution should be complex number (no real solutions)
v4 = fsolve(createPolynomial( (1,0,0,0,0,0,8) ) , 1)

# funtion = 2*x^3 -2*x^2 + 3
# x = error (division by zero), stopped iteration 1
# first derivative ~ zero when x ~ 0 (starting point)
# solution should be -0.89070
v5 = fsolve(createPolynomial( (3,0,-2,2) ), 0)

#newton in the scipy optimization module
v1_sci = op.newton(aSillyFunction, 1)
v2_sci = op.newton(math.sin, 2)
v3_sci = op.newton(lambda x: math.log2(x)-128, 1)
v4_sci = op.newton(createPolynomial( (1,0,0,0,0,0,8) ) , 1) 
v5_sci = op.newton(createPolynomial( (3,0,-2,2) ), 0)

#fsolve in the scipy optimization module
v1_fs = float(op.fsolve(aSillyFunction, 1))
v2_fs = float(op.fsolve(math.sin, 2))
v3_fs = float(op.fsolve(lambda x: math.log2(x)-128, 1))
v4_fs = float(op.fsolve(createPolynomial( (1,0,0,0,0,0,8) ) , 1))
v5_fs = float(op.fsolve(createPolynomial( (3,0,-2,2) ), 0))

'''
put value of fsolve, optimze.newton and optimize.fslove into a same table
in order to easilier compared
'''
row1 = [v1,v1_sci,v1_fs]
row2=[v2,v2_sci,v2_fs]
row3 = ["NA",v3_sci,v3_fs]
row4 =["NA",v4_sci,v4_fs]
row5 = ["NA",v5_sci,v5_fs]
data = [row1,row2,row3,row4,row5]
rownames = ["v1","v2","v3","v4","v5"]
colnames = ['fsolve','optimize.newton',
            'optimize.fsolve']   
pandas.DataFrame(data,rownames,colnames)

'''
to see the advantge for giving fprime
'''
# the same
fsolve(lambda x: x**4, -100)
fsolve(lambda x: x**4, -100,lambda x: 4*x**3)

#without fprime, cannot converge; with fprime, can converge within maxiter = 100
op.newton(lambda x: x**4, -100,maxiter=100) 
op.newton(lambda x: x**4, -100, fprime = lambda x: 4*x**3,maxiter=100)

# with prime exactly zero and converge faster
op.fsolve(lambda x: x**4, -100)
op.fsolve(lambda x: x**4, -100, fprime = lambda x: 4*x**3)

#%% Exercise 4 ###############################################################
"""
initialX function compute the initial guess for finding the square root
    
@param x: input number, which wants the square root
@returns: initial guess
"""

def initialX(x):

    d = len(str(x)) # number of digits
    		
    # number of digits is even
    if(d%2==0):
        k = (d-2)/2
        return 6*10**k
    #otherwise odd
    k = (d-1)/2
    return 2*10**k
    

#%% modifiy fsolve function to output number of iterations
def fsolve2(f, x0, fprime=None, xtol=1.49012e-08, maxiter=100):
    
    # estimate derivative if not given
    if (fprime == None):
        d = xtol/2     
        fprime = estderi(f,d)
    
       
    error = 1   
    i = 0       
    x = x0      
  
    # iterate until error in x within tolerance
    while (error > xtol) :
        
        i += 1

        xnew = x - f(x)/fprime(x)  #compute new x based on previous x
        error = abs(xnew - x)      
        x = xnew                   #update new x
        
        #if interation larger than the max interation, thrwo exception
        if (i > maxiter):
            raise RuntimeError('Maximum Iterations ' + str(maxiter) +
            ' Exceeded')
    
    return (x,i) #return value and number of interation

#%%
"""
    Computes the (positive) square root of a positive number. 
    
    @param x: positive number
    @param x0: initial guess (optional, default = initial guess function)
    @param fprime: first derivative function (optional, default = none)
    @returns square root and iterations
    
    """
def sqrt2(x, x0=initialX(x), fprime=None):
    
    f = createPolynomial( (-x, 0, 1) ) # solve for s: s^2 -x =0
    
    if (fprime==None): #give estimate derivative if fprime not provided
        results =  fsolve2(f,x0)
         #get value and number of iternation from fsolve2 output
        return (abs(results[0]),results[1])
        
    results =  fsolve2(f,x0,fprime = lambda x: 2*x) #fprime provided = 2*x
    return (abs(results[0]),results[1]) 
    
    
#%%  test sqrt funcion non fprime vs fprime
value = [0, 10, 49, 100, 200, 400, 800, 1500]
sqrts = []
for x in value:
    results1 = sqrt2(x) #with fprime 2*x
    results2 = sqrt2(x,fprime=None) #without fprime
    sqrts.append([results1[0],results2[0],results1[1],results2[1]])

rownames = value
colnames = ['w fprime (val)','w/o fprime (val)',
            'w fprime (iter)','w/o fprime (iter)']   
pandas.DataFrame(sqrts,rownames,colnames)
