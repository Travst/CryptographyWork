
import matplotlib.pyplot as plt

#########
# gf2^8 #
#########
def gfmul(a, b):
    res = 0
    while b:
        if b & 1:
            res ^= a
        b >>= 1
        a <<= 1
        if a > 255:
            a ^= 283
    return res

def polyOrder(poly):
    v2str = '{:09b}'.format(poly)
    for i in range(9):
        if int(v2str[i]):
            return 9 - i
def gfdiv(a, b):
    if b == 0:
        print("fault operation: divide zero\n")
        return (-1, -1)
    if a < b:
        return (0, a) # remainder = a
    digree = polyOrder(a) - polyOrder(b)
    tmp = b << digree
    a = a ^ tmp
    gd = gfdiv(a, b)
    return ((1 << digree) | gd[0], gd[1]) # return (quotient,remainder)

# egcd and inverse
def gfegcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while(b):
        gd = gfdiv(a, b)
        q, a, b = gd[0], b, gd[1]
        x0, x1 = x1, x0 ^ gfmul(q, x1) #x0, x1 = x1, x0-q*x1
        y0, y1 = y1, y0 ^ gfmul(q, y1) #y0, y1 = y1, y0-q*y1
    d = {"x" : x0, "y" : y0}
    return (a, d)
def gfinv(a):
    if a == 0:
        return 0
    ge = gfegcd(a, 283)
    return ge[1]["x"]
#######
# ECC #
#######
def eccIsNt(p, q):
    # to judge whether p&q is negative to each other
    isnt = False
    if p[0] == q[0] and (q[1] == p[0] ^ p[1] or p[1] == q[0] ^ q[1]):
        isnt = True
    return isnt

def eccAdd(p, q, a = 2):
    # caculate p + q
    x, y = 0, 0
    if (p == (0, 0) and q == (0, 0)) or eccIsNt(p, q):
        return (x, y)
    elif p == (0, 0) and q:
        return q
    elif p and q == (0, 0):
        return p
    elif p == q:
        lm = p[0] ^ gfmul(p[1],gfinv(p[0])) # lambda = xp + yp * xp^-1
        x = gfmul(lm, lm) ^ lm ^ a  # x = lambda^2 + lambda + a
        y = gfmul(p[0], p[0]) ^ gfmul(x, lm^1)  # y = xp^2 + (lambda + 1) * x
    else:
        lm = gfmul(q[1] ^ p[1], gfinv(q[0] ^ p[0])) # lambda = (yq + yp) * (xq+xp)^-1
        x = gfmul(lm, lm) ^ lm ^ p[0] ^ q[0] ^ a    # x = lambda^2 + lambda + xp + xq + a
        y = gfmul(lm, p[0] ^ x) ^ x ^ p[1]    # y = lambda * (xp + x) + x + yp
    return (x, y)

def eccNp(n, p, a = 2):
    # caculate n * p, n is int, p is point in ECC
    res = (0, 0)
    while n:
        if n & 1:
            res = eccAdd(res, p, a)
        p = eccAdd(p, p, a)
        n >>= 1
    return res

def pointIn(a, b):
    pointV = list()
    pointV.append((0, 0))
    #a, b = 2, 3
    px = list()
    py = list()
    px.append(0)
    py.append(0)
    for i in range(0, 256):
        x2 = gfmul(i, i)
        x3 = gfmul(i, x2)
        ax2 = gfmul(a, x2)
        right = x3 ^ ax2 ^ b
        for j in range(0, 256):
            y2 = gfmul(j, j)
            xy = gfmul(i, j)
            if (y2 ^ xy == right):  # y^2 + x * y = x^3 + a * x^2 + b
                pointV.append((i, j))
                px.append(i)
                py.append(j)
    order = len(pointV)
    print("  E28({0},{1})'s order is {2}".format(a, b, order))
    #print(pointV)
    ### cycle group judgement
    msg = "不是循环群"
    for r in pointV:
        tmp = eccAdd(r, r, a)
        ode = 1
        while tmp != r:
            tmp = eccAdd(tmp, r, a)
            ode += 1
            #print(ode,":",tmp)
        if ode == order:
            msg = "是循环群，生成元是" + str(r)
            break
    print(msg)
    ### draw figure
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(0, 260)
    plt.ylim(0, 260)    # x&y 's range(0,260) in figure
    plt.xticks(range(0,280,20))
    plt.yticks(range(0,280,20)) # x&y 's interval is 20
    plt.scatter(px, py, s = 2, c = "red")
    plt.show()
    return None

a, b = 2,2
p = (2, 3)
q = (1, 1)
n = 2
print(p, " + ", p, " = ", eccAdd(p, p, a))
print(n, " * ", p, " = ", eccNp(n, p, a))
pointIn(a, b)
