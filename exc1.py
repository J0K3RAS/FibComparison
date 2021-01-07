#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 15:51:01 2020

@author: charalampos
"""
import timeit

def fibonacci_1(n):
    if n<2: return n
    return fibonacci_1(n-1) + fibonacci_1(n-2)

def fibonacci_2(n):
    a = 0
    b = 1
    for i in range(2,n+1):
        c = b
        b = a+b
        a = c
    return b

def fibonacci_3(n):
    if n<2: return n
    array = [1,1,1,0]
    ans = [1,0,0,1]
    n = n-2
    while n>0:
        if n % 2 == 1:
            ans = multiply(ans, array)
        n = n//2
        array = multiply(array, array)
    return ans[0]+ans[1]

def multiply(A,B):
    ans = [ A[0]*B[0]+A[1]*B[2],A[0]*B[1]+A[1]*B[3],A[2]*B[0]+A[3]*B[2],A[2]*B[1]+A[3]*B[3] ]
    return ans

def t(s):
    return timeit.timeit(s, setup="from __main__ import fibonacci_1,fibonacci_2,fibonacci_3", number=1)

f = open('results.dat','a+')
for i in [5,10,15,20,25,30,35,40]:
    f.write("{}\t{}\t{}\t{}\n".format(i,
                                    t("fibonacci_1({})".format(i)),
                                    t("fibonacci_2({})".format(i)),
                                    t("fibonacci_3({})".format(i)) ))
f.close()

f = open('results2.dat','a+')
for i in [10,100,1000,10000,100000,200000,300000,400000,500000,600000,700000,800000,900000,1000000]:
    f.write("{}\t{}\t{}\n".format(i,
                                    t("fibonacci_2({})".format(i)),
                                    t("fibonacci_3({})".format(i)) ))
f.close()