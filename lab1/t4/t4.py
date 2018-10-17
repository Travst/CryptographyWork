
def moduleInverse(a, n):
    r0, r1 = 1, 0
    d, k = a, n
    while(k):
        q, d, k = d // k, k, d % k
        r0, r1 = r1, r0-q*r1

    if 1 % d == 0:
        x0 = (r0*(1 / d)) % n
        print(x0)
    else:
        print("no solution")

#a = int(input())
#n = int(input())
a, n = 3, 5
moduleInverse(a, n)
a, n = 7, 10
moduleInverse(a, n)