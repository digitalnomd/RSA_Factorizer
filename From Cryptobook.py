# -*- coding: utf-8 -*-
"""
Created on Sun May 01 15:51:00 2016

@author: AnimoEtFide
"""

#from Crypto Book

import gmpy2
import sys
import random
import thread
from gmpy2 import mpz
from gmpy2 import gcd
#using extended euclidian algorithm, but only using it for computing gcd and not multiplicative inverse
def my_gcd(a, b):
    a = mpz(a)
    b = mpz(b)
    #only used for counting number of iterations for metrics
    count = mpz(0)
    a_O = a
    b_O = b
    t_O = mpz(0)
    t = mpz(1)
    q = f_div(a_O, b_O)
    r = sub(a_O, mul(q, b_O))
    while r > 0:
        temp = f_mod(sub(t_O,mul(q, t)), a)
        t_O = t
        t = temp
        a_O = b_O
        b_O = r
        q = f_div(a_O,b_O)
        r = sub(a_O,mul(q, b_O))
        count = add(1,count)
    #print("Number of iterations: " + str(count))
    #print str(t) + " " + str(t_O) + " " +  str(a_O) + " " +   str(b_O) + " " +   str(q) + " " +  str(r) + " " +   str(temp)
    return b_O

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def factors(start, end):
    n = end
    result = set()
    i = start 
    while(i < (isqrt(n) + 1)):  
        div, mod = divmod(n, i)
        if not mod:
            result |= {i, div}
        i = i + 1
    return result



def gmpy_factors(start, end):
    n = end
    result = set()
    n = mpz(n)
    i = start 
    while(i < (gmpy2.isqrt(n) + 1)):  
        div, mod = divmod(n, i)
        if not mod:
            result |= {mpz(i), div}
        i = i + 1
    return result



def fermat_factor(n):
    n = mpz(n)
    assert n % 2 != 0  # Odd integers only

    a = mpz(gmpy2.ceil(gmpy2.sqrt(n)))
    b2 = mpz(gmpy2.square(a) - n)
    while not gmpy2.isqrt(mpz(b2)):
        a += 1
        b2 = gmpy2.square(a) - n

    factor1 = a + mpz(gmpy2.sqrt(b2))
    factor2 = a - mpz(gmpy2.sqrt(b2))
    return mpz(factor1), mpz(factor2) 



def PollardP_1(n, B):
    n = mpz(n)
    B = mpz(B)
    a = mpz(2)
    for j in range(mpz(2),mpz(B)):
        a = pow(mpz(a),mpz(j),mpz(n))
    d = gcd(a-1,n)
    if( 1 < d and d < n):
        return d
    else:
        #print("Failure")
        return 0

def main():
    #n =15770708441
    #console 9 a 
    n = 118444866376306827062213
    B = 1
    test = 0
    while(test == 0 and B < n):
        test = PollardP_1(n,B)
        
    print(test)
    
main()
    
    
    
    