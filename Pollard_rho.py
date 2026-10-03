import math
import random
import numpy

def Pollards_Rho(n):
    b = 1
    f = lambda x,b,n : (x**2+b)%n
    tried = numpy.array([])

    for i in range(0,n):
        while True:
            s = random.randrange(0,n-1)
            if numpy.isin(s,tried): continue
            elif numpy.size(tried) == n : return "prime"
            else: tried = numpy.append(tried,s); break

        u = v = s
        g = 1
        print('u='+str(u)+ ' : v=' + str(v) + ' : g=' + str(g))

        while g == 1:
            u = f(u,b,n)
            v = f(f(v,b,n),b,n)
            g = math.gcd(u-v,n)
            print('u='+str(u)+ ' : v=' + str(v) + ' : g=' + str(g))

        if g != n: return g

d = Pollards_Rho(16318433)
print(d)
