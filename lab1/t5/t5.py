'''
import math
def BSGS(a, b, p):
    cp = math.ceil(math.sqrt(p))    #根号p向上取整
    baB = dict()
    allx = list()
    # 0 <= A,B <= cp
    for B in range(cp + 1):
        baB[(b*(a**B)) % p] = B #枚举B,计算 b*（a的B次方）
    for A in range(cp + 1):
        tmp = a**(A * cp) % p
        if(baB.get(tmp)):
            x = A * cp - baB[tmp]   # 0 < x <= p
            if(x > 0 and x <= p):
                allx.append(x) # 如果 a^(A*cp) == b* a^B，计算出x存于allx中
    allx.sort()
    return allx

def factor(n):  # n的所有因子
    f = list()
    i = 2
    while(i*i < n):
        if n % i == 0:
            f.append(i)
            n //= i
            f.append(n)
        i += 1
    f.sort()
    return f

def min_origin(p):
    f = factor(p-1)
    i = 2
    flag = True
    while i < p and flag:
        flag = False
        for k in f:
            if (i**k)% p == 1:
                flag = True
                break
        if flag:
            i += 1
    return i

def primefun(a, b, p):
    if b >= p:
        print("no sulution")
        return None
    g = min_origin(p)
    allc = BSGS(g**a, b, p)
    if len(allc) == 0:
        print("no sulution")
        return None
    x = set()
    for c in allc:
        x.add(g**c % p)
    print("{0}^{1} = {2} mod {3}".format(x,a,b,p))

a, b, p = 131, 758, 1073
primefun(a, b, p)
#print(factor(8))
#print(factor(11))
#a, b, p = 5, 3, 11
#print(BSGS(a, b, p))
#a, b, p = map(int, input().split())

'''
#   v1.0   exhaustive
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
#a, b, p = map(int, input().split())
a, b, p = 131, 758, 1073
exhaustive(a, b, p)

