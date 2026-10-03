import numpy
import math



def Pollards_p_minus_one(n,B):
    primes = [pi for pi in range(2,B+1) if len([q for q in range(2,pi) if pi%q==0])==0]
    exponents = [math.floor(math.log(B)/math.log(pi)) for pi in primes]

    print(primes)
    print(exponents)

    MB = 7
    for i,p in enumerate(primes):
        
        MB = (MB**(p**exponents[i]))%n
        g = math.gcd(MB-1,n)
        print( "p^e = " + str(p**exponents[i]) + "\t MB = "+str(MB)+"\tg = " + str(g) )
    if g > 1 and g < n: return g
    return

B = 15

n = 26219
print('n = '+str(n))
d = Pollards_p_minus_one(n,B) # 157
print(d)
print()

n = 32339
print('n = '+str(n))
d = Pollards_p_minus_one(n,B) # 73
print(d)
print()

n = 37627
print('n = '+str(n))
d = Pollards_p_minus_one(n,B) # 191
print(d)
print()







def Pollards_p_minus_one1(n,B):
    primes = [pi for pi in range(2,B+1) if len([q for q in range(2,pi) if pi%q==0])==0]
    print(primes)
    exponents = [math.floor(math.log(B)/math.log(pi)) for pi in primes]

#    primitives = numpy.array([5, 7, 10, 11, 14, 15, 17, 19, 20, 21])
    primitives = numpy.array([2,3,4,6,8,9,12,13,16,18])
#    primitives = [2]
#    MB = math.prod([primes[i]**exponents[i] for i in range(0,len(primes))])
#    for a in range(2,28):
    #    MB = a
    a = 3
#    N = (a**MB)%n
    #    print(N)
#    g = math.gcd(N-1,n)
    #    MB = N
    primitives = numpy.array([2, 6, 7, 8])
#    primitives = numpy.array([3,4,5,9,10])

#    MB = a

    for a in range(2,20):
        MB = 1
        for i,p in enumerate(primes):
            MB = MB*(p**exponents[i])
            X = (a**MB)%n
#            MB = MB**(p**exponents[i])
#            X = MB%n
    #        print(X)
    #
            g = math.gcd(X-1,n)
        print(str(a)+' : ' +str(g))
    if g > 1 and g < n: return g
    return