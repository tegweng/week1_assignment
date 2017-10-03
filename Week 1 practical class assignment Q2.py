# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:31:53 2017

@author: fj803263
"""

#Exercise 2

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

def gaud(f,a,b,N):
    I=a
    dx=(b-a)/N
    n=int(N)
    for i in xrange(0,n):
        I+= f(a + (i+0.5)*dx )
    
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
    e=gaud(lambda x: np.sin(m*x),c,d,N1)
    ex=-(1/m)*np.cos(d) + (1/m)*np.cos(c)
    error=e-ex
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
    
print n
#n is an array of the Ns that I want to compare

errorarray=np.zeros(4)

for i in xrange(4):
    errorarray[i] = error(0,np.pi,n[i],1)
    
print errorarray
#error array is an array that contains 

deltax=np.zeros(4)

for i in xrange(4):
    deltax[i]=(np.pi/n[i])
    
print deltax

newarray=[errorarray,deltax]

newnew=np.vstack(newarray)
errorvsdx=np.std(newnew,axis=0)

plt.figure(1)
plt.plot(errorvsdx)

