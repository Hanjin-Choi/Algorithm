n= int(input())
nl = list(map(int,input().split()))
nl.sort()
t=[0]*n
t[0]=nl[0]
time=t[0]
for i in range(1,n):
    t[i]=t[i-1]+nl[i]
    time +=t[i]
print(time)