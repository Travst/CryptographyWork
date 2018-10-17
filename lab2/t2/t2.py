
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

def subgroup(n):
    g = multigroup(n).pop()
    k = list()
    for i in range(1, n):
        t = g**i % n
        if t in k:
            break
        else:
            k.append(t)
    print("a subgroup of Z{0}* :".format(n), k)
    if k[0]**len(k) % n == 1:
        print("the size of subgroup divides the size of Zn*")
    else:
        print("the size of subgroup can not divides the size of Zn*")

n = 11
print("Z{0}* :".format(n), multigroup(n))
subgroup(n)