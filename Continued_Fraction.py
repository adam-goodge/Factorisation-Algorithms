import numpy
from fractions import Fraction

def continued_fraction(x):
    i = 0
    q0 = numpy.floor(x)
    q = numpy.array([q0])
    f = x - q0
    x = 1/f
    print(x)

    while (f > 0) :
        i += 1
        qi = numpy.floor(x)
        f = x - qi
        x = 1/f
        q = numpy.append(q,qi)
    return q

a = 3.245
q = continued_fraction(a)
print(q)
