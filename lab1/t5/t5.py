
def gcd(a, b):
    while(b):
        a, b = b, a % b
    return a

def phi(n):
    i, count = 1, 0
    while(i < n):
        if gcd(i, n) == 1:
            count +=1
        i +=1
    return count

#穷举小于n的满足条件的x
def exhaustive(a, b, n):
    if(b >= n):
        print("no solution")
        return -1
    a = a % phi(n)
    allx = list()
    i = 1
    while(i < n):
        if ((i**a) % n == b):
            allx.append(i)
        i += 1
    if not allx:
        print("no solution")
        return -1
    print(allx)
    return 1

#a, b, p = 2, 3, 11
a, b, p = map(int, input().split())
exhaustive(a, b, p)