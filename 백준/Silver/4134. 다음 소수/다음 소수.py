import sys
input = sys.stdin.readline

t=int(input())
num_list=[int(input()) for _ in range(t)]
maxx=int((4*10**9)**0.5)+1
era=[0,0]+[1]*(maxx-1)
prime=[]
for i in range(2,maxx):
    if era[i]:
        prime.append(i)
        for j in range(i*i,maxx,i):
            era[j]=0
ans = [0]*t
for idx in range(t):
    if num_list[idx]<=maxx and era[num_list[idx]]:
        ans[idx]=num_list[idx]
    elif num_list[idx]<=prime[-1]:
        find = num_list[idx]
        while era[find]==0:
            find +=1
        ans[idx]=find
    else:
        find =num_list[idx]
        while True:
            for divi in prime:
                if find % divi:
                    continue
                else:
                    break
            else:
                ans[idx]=find
                break
            find += 1

print(*ans,sep='\n')

