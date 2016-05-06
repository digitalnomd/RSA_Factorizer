#!/usr/bin/python

import sys
from math import log
from random import randrange
from fractions import gcd

#the following is a basic pollard rho implementation
#based on the pseudocode for the algorithm in
#the Introduction to Algorithms text by CLRS
def pollard_rho(n):
	i = 1
	x1 = randrange(0, n - 1)
	y = x1
 	k = 2
	while True:
		i += 1
		x2 = (x1*x1 - 1) % n
		d = gcd(y - x2, n)

		if d != 1 and d != n:
			print "Factor: " + str(d)
			return

		if i == k:
			y = x2
			k = 2*k

		x1 = x2

def main():
	n = int(eval(sys.argv[1]))
	print n

	#factor
	print "Factoring the modulus..."
	pollard_rho(n)

	return

main()
