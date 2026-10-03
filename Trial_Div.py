import numpy
import math

def trial_div(n):
    m = n
    p = 2
    primes = numpy.array[(p)]
    while p <= m**(1/2):
        if m%p==0 :
            print('p divides n')
            m = m/p
        else:
            if p == 2 : p = 3
            else:
                p += 2
                while int(math.prod(p%primes))==0: p += 2
                primes = numpy.append(primes,p)
        if m == n : print('n is prime')
        else if: m > 1 : print('m divides n')
