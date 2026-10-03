import numpy
import math
import random

def miller_rabin(n, k):

    # Implementation uses the Miller-Rabin Primality Test
    # The optimal number of rounds for this test is 40
    # See http://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes
    # for justification

    # If number is even, it's a composite number

    if n == 2 or n == 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def add_to_count(dict,divisors):
    for q in divisors:
        if int(q) in dict:
            dict[int(q)] += 1
        else:
            dict[int(q)] = 1
    return dict


def Recursive_Two_Stage_Pollard(n,B1,B2):
    primes = [pi for pi in range(2,B1) if len([q for q in range(2,pi) if pi%q==0])==0]
    exponents = [math.floor(math.log(B1)/math.log(pi)) for pi in primes]
    divisors = numpy.array([])
    MB = math.prod([primes[i]**exponents[i] for i in range(0,len(primes))])
    divisors = numpy.append(divisors,Second_Stage_Pollard(int(n),B2,MB))
#    N = int(n/math.prod(divisors,start=1))
#    while N != 1 : divisors = numpy.append(divisors,Second_Stage_Pollard(N,B2,MB))
    return divisors



def Second_Stage_Pollard(n,B2,MB):
    Q = [pi for pi in range(B1,B2) if len([q for q in range(2,pi) if pi%q==0])==0]
    Q.insert(0, 0)
    divisors = numpy.array([])

    for a in range(2,B2):
        Aqi = 1;
        A = a**MB
        for i in range(1,len(Q)) :
            Aqi = (A**(Q[i]-Q[i-1])%n) * Aqi % n
            g = int(math.gcd(Aqi-1,n))
            if g > 1 and g < n :
                if miller_rabin(g,100): divisors = numpy.append(divisors,g)
                else: divisors = numpy.append(divisors,Recursive_Two_Stage_Pollard(g,2,20))
                break
        else: continue
        break

    if sum(divisors) == 0: n1 = n
    else: n1 = int(n/math.prod(divisors))

    if miller_rabin(n1,100): divisors = numpy.append(divisors,n1)
    elif n1 == n : divisors = numpy.append(divisors,Second_Stage_Pollard(n,B2*2,MB))
    elif n1 > 1 and n1 < n: divisors = numpy.append(divisors,Second_Stage_Pollard(n1,B2,MB))

    return divisors




def Pollards_Two_Stage(n,B1,B2):
    primes = [pi for pi in range(2,B1) if len([q for q in range(2,pi) if pi%q==0])==0]
    exponents = [math.floor(math.log(B1)/math.log(pi)) for pi in primes]
    Q = [pi for pi in range(B1,B2) if len([q for q in range(2,pi) if pi%q==0])==0]
    Q.insert(0, 0)
    MB = math.prod([primes[i]**exponents[i] for i in range(0,len(primes))])


    divisors = numpy.array([])

    for a in range(2,B2):
        print(a)
        Aqi = 1
        A = a**MB
        for i in range(1,len(Q)) :
            Aqi = (A**(Q[i]-Q[i-1])%n) * Aqi % n
            g = math.gcd(Aqi-1,n)

            if g > 1 and g < n and int(math.prod(g%divisors))!=0:
            #    for d in divisors:
            #        if int(g%d)==0:
                divisors = numpy.append(divisors,g)
                print(divisors)
        if math.prod(divisors) == n: return divisors

    #    if g > 1 and g < n: return g

    return divisors


n = 2**53 - 1
B1 = 10
B2 = 70

B1 = 10
B2 = 20
#n = 27089
#n = 42781

#n = 2**977 - 1
n = 26385769
n = 16318433
n = 6**175 - 1
print(n)
d = Recursive_Two_Stage_Pollard(n,B1,B2)
#d = Pollards_Two_Stage(n,B1,B2)
prime_factors = {}
prime_factors = add_to_count(prime_factors,d)
print(prime_factors)
print(int(math.prod(d)))


def Pollards_Two_Stage2(n,B1,B2):
    primes = [pi for pi in range(2,B1) if len([q for q in range(2,pi) if pi%q==0])==0]
    exponents = [math.floor(math.log(B1)/math.log(pi)) for pi in primes]
    Q = [pi for pi in range(B1,B2) if len([q for q in range(2,pi) if pi%q==0])==0]
    Q.insert(0, 0)
    MB = math.prod([primes[i]**exponents[i] for i in range(0,len(primes))])
    print(MB)

    for a in range(2,B2):
        MB = Aqi = 1
        for i,p in enumerate(primes):
            MB = (MB*(p**exponents[i]))
            g = math.gcd(a**MB%n-1,n)
            if g > 1 and g < n: return g
        print(MB)
        A = a**MB

        for i in range(1,len(Q)) :
            Aqi = (A**(Q[i]-Q[i-1])%n) * Aqi % n
            g = math.gcd(Aqi-1,n)
            if g > 1 and g < n: return g

    return g

def Pollards_Two_Stage1(n,B1,B2):
    primes = [pi for pi in range(2,B1) if len([q for q in range(2,pi) if pi%q==0])==0]
    exponents = [math.floor(math.log(B1)/math.log(pi)) for pi in primes]
    MB = 2
    for i,p in enumerate(primes):
        MB = (MB**(p**exponents[i]))%n
        g = math.gcd(MB-1,n)
        if g > 1 and g < n: return g
    Q = [pi for pi in range(B1,B2) if len([q for q in range(2,pi) if pi%q==0])==0]
    print(Q)
    MBqi = (Q[0]*MB)%n
    for i in range(len(Q)) :
        MBqi = ((Q[i]-Q[i-1])*MBqi)%n
        print(MBqi)
    return g
