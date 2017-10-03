# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:22:34 2017

@author: fj803263
"""

#Exercise 1

from __future__ import division

def summing(t,N,c=0.01):
    n=int(N)
    for i in xrange(0,n):
        t+=c
    return t
        
print summing(0,1e4)
print summing(0,1e7)

#there is not enough space in the mantissa for the second example
