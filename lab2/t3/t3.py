import random

def gcd(a, b):
    while(b):
        a, b = b, a % b
    return a

def multigroup(n):
    m = list()
    for i in range(1, n):
        if gcd(i, n) == 1:
            m.append(i)
    return m

def cycgroup(p):
    q = (p - 1) // 2
    if q != (p - 1) / 2:
        print("wrong p")
        return None
    m = multigroup(p)
    m.remove(1)
    h = random.choice(m)
    g = h**q % p
    print("h = ", h, "q = ", q, "\ng =", g, "mod", p)
    cg = list()
    for i in range(1, p):
        t = g**i % p
        if t in cg:
            break
        else:
            cg.append(t)
    print("g's cyclic group:", cg,"\n  order",len(cg))

p = 11
cycgroup(p)