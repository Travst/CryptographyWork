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
           allx.append(A * cp - baB[tmp]) # 如果 a 的 A*cp 次方 == b*（a的B次方），计算出x存于allx中
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
    g = min_origin(p)
    allc = BSGS(g**a, b, p)
    allx = list()
    for c in allc:
        allx.append(g**c)
    print(allx)

a, b, p = 2, 3, 11
primefun(a, b, p)
#print(factor(8))
#print(factor(11))
#a, b, p = 5, 3, 11
#print(BSGS(a, b, p))
#a, b, p = map(int, input().split())
