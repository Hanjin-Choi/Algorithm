from math import comb
n,k=map(int,input().split())
print(comb(k+n-1,n)%1000000000)