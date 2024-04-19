from math import log2,ceil
def makeword(k):
    a = int(log2(k))
    rest = k - 2**a
    if k==1:
        return 0
    elif k ==2:
        return 1
    elif not rest:
        return makeword(k-2**(a-2)*3)
    elif 0<rest<=2**(a-1):
        return makeword(2**(a-1)+rest)
    else:
        return makeword(k-2**(a-1)*3)


k =int(input())
res = makeword(k)

print(res)