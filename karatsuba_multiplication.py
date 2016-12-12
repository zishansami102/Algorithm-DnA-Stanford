import random
import sys
import os

def karatsuba( x, y):
    n = 0
    p = x
    while( p != 0):
        n = n + 1
        p = p // 10

    if n > 1:
        a = x // ( 10**(n//2))
        b = x % ( 10**(n//2))
        c = y // ( 10**(n//2))
        d = y % ( 10**(n//2))

        ac = karatsuba( a, c)
        bd = karatsuba( b, d)
        abcd = karatsuba((a+b), (c+d))
        
        xy = (10**((n//2)*2))*ac + (10**(n//2))*(abcd - ac - bd) + bd
        return xy
    else:
        return x*y

prod = karatsuba(123, 456)

print ("%d\n" %(prod))
