# -*- coding: utf-8 -*-
"""
Created on Thu May 05 13:02:37 2016

@author: eforte1

Eric Forte
5/5/2016
CMSC 441
Project 2 Part 2
---------------------------------------------------------------------------------------------------------
    How to run code:
        python CMSC441Project2Part2.py
        
        NOTE: this file uses gmpy2 for python 2.7 and is required to run it
        It can be obtained from https://pypi.python.org/pypi/gmpy2
        
---------------------------------------------------------------------------------------------------------   

Algorithm notes:

    Pollard P-1 is useful as it exploits a weakness in psudo primes where p and q
    are close togother. 

---------------------------------------------------------------------------------------------------------   

"""
import random
import gmpy2
import sys
import random
import thread
from random import randint
from gmpy2 import mpz
from gmpy2 import gcd

#call with input number n and upper bound of factors B
#returns the factor or 0
def PollardP_1(n, B):
    n = mpz(n)
    B = mpz(B)
    a = mpz(2)
    j = mpz(2)
    while j < B:
        a = pow(mpz(a),mpz(j),mpz(n))
        j =j + 1
    d = gcd(a-1,n)
    if( 1 < d and d < n):
        print("P-1 Factor")
        print(d)
        return d
    else:
        #print("Failure")
        return 0
#call with input number n 
#return True if factor found, prints the two factors    
def pollardRho(n):
    n = mpz(n)
    i = mpz(1)
    x = randint(0, (n-1))
    y = x
    k = mpz(2)
    while True:
        i = i +1
        x = pow(x,2,n) -1 % n
        if(x < 0):
            x = n -1
        d = gcd((y-x),n)
        if(d != 1 and d != n):
            print "The factor is: "
            print d
            print "And "
            print n/d
            return True
        if i == k:
            y = x
            k = 2*k
    


def main():
    '''
    MAIN FOR POLLARD P-1
    def main():
        #n =15770708441
        #tricky 1 
        n = mpz(96556172908641654504511151071082647301593169217460027816420983050055113960138717703802394373492697717122752219504541168876406985625769404010541446562470892696132790278371966490591842264224461753618670976877446631874573179689675823598229633753860888609511141791163342020339350779848533390955947534109433161223)
        B = n/3 * 2
        test = 0
        while(test == 0 and B < n):
            test = PollardP_1(n,B)
            
        print(test)
        
    main()
        
    '''    
    '''
    multithreaded main for pollardRho, used but not found to be worth while    
    TestNum = 1238094
    try:
        thread.start_new_thread(pollardRho, (TestNum))
        thread.start_new_thread(pollardRho, (TestNum))
        thread.start_new_thread(pollardRho, (TestNum))
        thread.start_new_thread(pollardRho, (TestNum))
    except:
        print "Unable to start Thread"
    
    return 0 
    '''
    
    #Test80
    #TestNum = 118444866376306827062213   
    #print("PollardRho results")
    #pollardRho(TestNum)
    #a known test number with answer of 135979
    #print("Pollard P-1 results")
    n =15770708441
    B = 180
    #test = PollardP_1(n,B)
    
    Rho = False
    Minus = False    
    
    Default = True;
    
    if len(sys.argv) > 1 :
        n = sys.argv[1]
        Rho = True
        Default = False
    else:
        print "NOT a valid Input"
        
    if len(sys.argv) > 2:
        B = sys.argv[2]
        Rho = False
        Minus = True
        Default = False
    else:
        print "NOT a valid Input"

    
    valid = False
    #test to see if valid int 
    try: 
        int(n)
        valid = True
    except ValueError:
        print "n not valid"
 
    if(Minus):
        try: 
            int(B)
            valid = True
        except ValueError:
            print "B not valid"
            valid = False

    if(valid == False or Default == True):
        print("Input not valid using default test for both algorithms")
        #Test80
        TestNum = 118444866376306827062213
        print("Test Number:")
        print(TestNum)
        print("PollardRho results")
        pollardRho(TestNum)
        print
        #a known test number with answer of 135979
        print("Pollard P-1 results")
        print("N, B")
        print(n, B)
        n =15770708441
        B = 180
        test = PollardP_1(n,B)
    if(Rho):
        print("PollardRho results")
        pollardRho(n)
    if(Minus):
        print("Pollard P-1 results")
        test = PollardP_1(n,B)

    return True  
main()