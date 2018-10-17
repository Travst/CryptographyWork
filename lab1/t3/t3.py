
def egcd(a,b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while(b):
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0-q*x1
        y0, y1 = y1, y0-q*y1
    return a, x0, y0

def modulequation(a, b, n):
    d, x, y = egcd(a, n)
    if b % d == 0:
        x0 = (x*(b / d)) % n
        for i in range(d):
            print((x0 + i*(n / d)) % n, end = " ")
        print("")
    else:
        print("no solution")

#a = int(input())
#b = int(input())
#n = int(input())
a, b, n = 14, 30, 100
modulequation(a, b, n)
a, b, n = 35, 10, 50
modulequation(a, b, n)
a, b, n = 893, 266, 2432
modulequation(a, b, n)