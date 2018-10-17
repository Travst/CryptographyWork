def gcd(a, b):
    while(b):
        a, b = b, a % b
    return a

a = int(input("input a "))
b = int(input("input b "))
print(a, "&", b, "gcd is", gcd(a, b))