def egcd(a,b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while(b):
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0-q*x1
        y0, y1 = y1, y0-q*y1
    d = {"x" : x0, "y" : y0}
    return a, d

#a=int(input("input a "))
#b=int(input("input b "))
a = 1759
b = 550
print(a,"&",b,"gcd is",egcd(a,b))
a = 2
b = 4
print(a,"&",b,"gcd is",egcd(a,b))