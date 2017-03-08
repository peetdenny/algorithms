import math

def carrot(x, y):

    #Test for base case
    #Get length of X and Y. If > 2, not base case

    lenX = len(str(x))
    lenY = len(str(y))

    n = lenX # TODO generalise this to unequal n

    baseCase = True
    if( lenX > 2 ):
        baseCase = False

    #Find index of middle of number
    divisor = (10 ** (n/2))

    # derive a thru d

    a = x/divisor
    b = x%divisor
    c = y/divisor
    d = y%divisor

    t1 = a * c if baseCase else carrot(a,c)
    t2 = b * d if baseCase else carrot(b,d)
    t3 = (a+b) * (c+d) if baseCase else carrot((a+b), (c+d))
    t4 = t3 - t2 -t1
    t5 = (t1 * (10 ** n)) +(t2) + (t4 * 10 ** (n/2))
    return t5
