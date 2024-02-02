M,N = map(int,input().split())
M_index =0

a = [0,0] + [1]*(N-1)
primes=[]
for i in range(2,N+1):
  if a[i]:
    if i>=M:
        primes.append(i)
    for j in range(2*i, N+1, i):
        a[j] = 0
print(*primes,sep='\n')