# -*- coding: utf-8 -*-
"""
Created on Sun May 01 15:06:53 2016

@author: AnimoEtFide
"""

import sys
import random
import threading
import gmpy2
from gmpy2 import mpz
from random import randint
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


#standard MillerRabin algorithm modified for gmp
#this function only runs the test num_times
#Returns TRUE if prime and FALSE if composite 
def MillerRabin(n, num_times):
    n = mpz(n)
    n_1 = n-1
    k = mpz(0)
    test = False
    while(test == False):
        m = (n_1 / (2**k) )
        if(m %2 == 1):
            test = True
        k = k + 1
        if(k > n):
            test = True
            #return "ERROR"
            print "Error"
            return False
    #number of checks
    for num in range(0,num_times):
        a = random.randint(1, n_1)
        a = mpz(a)
        #b = a ** m % n
        b = pow(a,m,n)
       
        '''
        Test if congruent
         b is conreunet to c (mod m).
         if (b-c)/m is an integer
         or if (b-c) % m == 0
        '''
        if(((b-1)%n) == 0):
            #return "n is prime"
            print "n is prime"
            return True
        for i in range(0, (k-1)):
            if(((b+1)%n) == 0):
                #return "n is prime"
                print "n is prime"
                return True
            else:
                #b = b**2 % n
                b = pow(b,2,n)
    #return "N is composite"
    print "n is composite"
    return False
    
def MultInverse(a,b):
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
    if(b_O != 1):
        return 0
    else:
        return t

def old_pollardRho(inNumber, startNum):
    fixedNumber = mpz(2) 
    cycleSize = mpz(2)
    startNum = mpz(startNum)
    factor = mpz(1)
    while (factor == 1):
		#for (int count=1;count <= cycle_size && factor <= 1;count++):
		#	x = (x*x+1)%number;
		#	factor = gcd(x - x_fixed, number);
		#}
        for count in range(1,cycleSize+1):
            startNum = (startNum*startNum+1)%inNumber
            factor = gcd(startNum - fixedNumber, inNumber)
        cycleSize *= 2;
        fixedNumber = startNum;
	
    otherNum = inNumber/ factor
    print ("The factor is ", factor, " The other number is ", otherNum)  
    print()

    return 0

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
    #test 80
    #pollardRho(118444866376306827062213,2)
    '''
    The factor is: 
    134899720349
    And 
    878021585737
    
    '''    
    #test 100
    '''The factor is: 
    91230686388571
    And 
    109696043954347
    '''
    '''
    kiwi:
    5
    And 
    109
    
    
    Cherry:
The factor is: 
569
And 
571    
    
    Guava:
    The factor is: 
22589783
And 
26241973

#grape:

The factor is: 
643797338422919
And 
999902890120703
    '''
    #test120 console 1 
    '''
    The factor is: 
479088404302759469
And 
332763801173729797
    '''
    #TestNum = 159423278514042926917753998089197793
    #test 140 console 2
    TestNum = 932400094547721378473055173769218038802437
    pollardRho(TestNum)
    '''
    TestNum = 1238094
    try:
        thread.start_new_thread(pollardRho, (TestNum, 3))
        thread.start_new_thread(pollardRho, (TestNum, 5))
        thread.start_new_thread(pollardRho, (TestNum, 7))
        thread.start_new_thread(pollardRho, (TestNum, 29))
    except:
        print "Unable to start Thread"
    
    return 0 
    '''
main()