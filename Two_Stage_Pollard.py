import numpy
import math
import random


def miller_rabin(n, k):
    if n == 2 or n == 3: return True
    if n%2 == 0 or n%3 == 0: return False

    r = 0; s = n-1
    while s%2 == 0: r += 1; s //= 2

    for _ in range(k):
        a = random.randrange(2,n-1)
        x = pow(a, s, n)
        if x == 1 or x == n-1: continue

        for _ in range(r-1):
            x = pow(x,2,n)
            if x == n-1: break
        else:
            return False

    return True


def two_stage_pollard(n,B1,B2):
    primes = [pi for pi in range(2,B1) if len([q for q in range(2,pi) if pi%q==0])==0]
    exponents = [math.floor(math.log(B1)/math.log(pi)) for pi in primes]
    MB = math.prod([primes[i]**exponents[i] for i in range(0,len(primes))])
    Q = [pi for pi in range(B1,B2) if len([q for q in range(2,pi) if pi%q==0])==0]
    Q.insert(0, 0)

    print("\n MB = " + str(MB))

    for a in range(2,B2):
        print('\n a = ' + str(a) + ':')
        Aqi = 1; A = a**MB


        for i in range(1,len(Q)) :
            Aqi = (A**(Q[i]-Q[i-1])%n) * Aqi % n
            g = int(math.gcd(Aqi-1,n))
            print(' qi = ' + str(i) + '|| aqiMB = ' + str(Aqi) + ' || gcd = ' + str(g))
            if g > 1 and g < n and miller_rabin(g,100): return g


n = 2**53 - 1
B1 = 10x
B2 = 70
d = two_stage_pollard(n,B1,B2)
print(d)


n = 42781
B1 = 10
B2 = 20
d = two_stage_pollard(n, B1, B2)
print(d)