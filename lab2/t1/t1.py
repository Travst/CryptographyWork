
def gcd(a, b):
    while(b):
        a, b = b, a % b
    return a

def phi(p):
    count = 0
    for i in range(1, p):
        if gcd(i, p) == 1:
            count += 1
    return count

def numgen(p):
    return phi(p-1)

def allgen(p):
    k = set()
    g = list()
    for i in range(1, p):
        j = 1
        k.clear()
        while( j < p):
            t = i**j % p
            k.add(t)
            print("{0:^3}".format(t),end = "")
            j += 1
        print("")
        
        if len(k) == p-1:
            g.append(i)
    return g

p = 11
print(p, phi(p), numgen(p))
print(allgen(p))
print("")
p = 13
print(p, phi(p), numgen(p))
print(allgen(p))