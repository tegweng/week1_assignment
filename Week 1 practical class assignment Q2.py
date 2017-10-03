# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:31:53 2017

@author: fj803263
"""

#Exercise 2

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from math import log

def gaud(f,c,d,N):
    if (d-c) <=0:
        raise ValueError('Argument d must be greater than c')
    if N<=0:
        raise ValueError('Argument N must be greater than 0')
    if not(callable(f)):
        raise Exception('A callable function must be sent to gaud')
    
    I=c
    dx=( float(d) - float(c) ) / int(N)
    n=int(N)
    for i in xrange(0,n):
        I+= f(float(c) + (i+0.5)*dx )
    
    I *= dx
    
    return I

print gaud(np.sin,0,np.pi,20)
#Exercise 2a
for i in xrange(1,5):
    print gaud(lambda x: 3*x - 2,2,5,i)
#answer is not correct in any interval

#exercise 2b

def error(c,d,N1,m):
    "function that calculates the error between true integration \
    and gaussian  quadrature for sin(mx)"
    if (d - c) <=0:
        raise ValueError('Argument d must be greater than c')
    if N1<=0:
        raise ValueError('Argument N1 must be greater than 0')
    if not(isinstance(m,int)):
        raise TypeError('Argument m to error must be an integer')
    
    e=gaud(lambda x: np.sin(m * x),c,d,int(N1))
    ex=- (1 / m) * np.cos(d) + (1 / m) * np.cos(c)
    error=e - ex
    return error

#below is the error for for sin(x)
print error(0,np.pi,20,1)
#below is the error for sin(3x)
print error(0,np.pi,20,3)

#there is almost 3 times the error for sin3x. This is because it is varying 


#Exercise 3

n=np.zeros(4)

for i in xrange(4):
    n[i]= 4*10**(i+3)

#n is an array of the Ns that I want to compare

errorarray=np.zeros(4)

for i in xrange(4):
    errorarray[i] = error(0,np.pi,n[i],1)
    
#error array is an array that contains all the errors for N=4000,40000,400000,4000000

deltax=np.zeros(4)

for i in xrange(4):
    deltax[i]=(np.pi/n[i])
    
print deltax

plt.figure(0)
#a graph that shows the errors as a function of dx on a log-log scale
plt.plot(deltax,errorarray)
plt.xscale('log')
plt.yscale('log')
plt.show()

def ooc(c,d,N1,m,N2):
    "The function calculates the order of convergenge which tells you \
    the change in error relative to the change in resolution between two resolutions \
    dx1 and dx2"
    
    e1=abs(error(c,d,N1,m))
    e2=abs(error(c,d,N2,m))
    dx1=(d - c) / int(N1)
    dx2=(d - c) / int(N2)
    n=( np.log(e1) - log(e2) ) / ( log(dx1) - log(dx2) )
    return n
    

print ooc(0,np.pi,4e3,1,4e4)
print ooc(0,np.pi,4e4,1,4e5)
print ooc(0,np.pi,4e5,1,4e6)
#these should all be second order, but there is errors as you increase N1 and N2 because there is not enough space in the mantissa

#Test script
def test(f,c,d,N,N1,m,N2):
    try: 
        gaud(f,c,d,N)
    except ValueError as inst:
        #this means it will print the error instruction given in the first function
        print('gaud ' + str(inst))
        pass
    except not(callable(f)) as inst:
        print('guad ' + str(inst))
        pass
        
    else:
        #this gives an error if something has gone horribly wrong
        print("Error in gaud function")
    
    try:
        error(c,d,N1,m)
    except ValueError as inst:
        print('error ' + str(inst))
        pass
    except not(isinstance(m,int)) as inst:
        print('error ' + str(inst))
    else:
        print("Error in error function")
    
    try:
        ooc(c,d,N1,m,N2)
    except ValueError as inst:
        print('ooc ' + str(inst))
        pass
    except TypeError as inst:
        print('ooc ' + str(inst))
        pass
    else:
        print("Error in ooc function")
        
test(np.sin,5,3,-1,4.5,4,3)

        