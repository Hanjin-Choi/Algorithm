import sys
input = sys.stdin.readline

k,n =map(int,input().split())
lst =[input().strip() for _ in range(k)]
lst.sort(key =lambda x:(-len(x),-int(x)))
plus = n-k
num = lst+[lst[0]]*plus
leng = len(lst[0])
num.sort(key = lambda x : x*leng ,reverse=True)
print(''.join(num))
