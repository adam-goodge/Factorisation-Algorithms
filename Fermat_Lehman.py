import math

def Fermats_L(x):
    n = x ** (1./3)
    n_c = math.ceil(n)
    n_f = math.floor(n)
    d = trial_div(x,n_c)

    for k in range(1,n_f):
        b1 = 2*math.sqrt(k*x)
        b2 = b1+(x**(1/6))/(4*math.sqrt(k))
        lower_b = math.ceil(b1)
        upper_b = math.floor(b2)

        for a in range(lower_b,upper_b+1):
            b = math.sqrt(a**2 - 4*k*x)
            print(b)
            if b.is_integer(): 
                
                return math.gcd(a+int(b),x)
    return

def trial_div(x,n):
    for d in range(2,n+1):
        if (x/d).is_integer(): return d
    return

#d = Fermats_L(26385769) # 4217
#print(d)

#d = Fermats_L(4847) # 131
#print(d)

d = Fermats_L(4897) # 59
print(d)

#d = Fermats_L(45511) # 641
#print(d)


import sys
print(sys.path)