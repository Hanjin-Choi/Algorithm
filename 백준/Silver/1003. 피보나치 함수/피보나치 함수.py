import sys
input = sys.stdin.readline

t=int(input())
input_list=[int(input()) for _ in range(t)]
maxx=max(input_list)
ans=[[1,0] for _ in range(maxx+1)]
if maxx>=1:
    ans[1]=[0,1]
for idx in range(2,maxx+1):
    ans[idx][0]=ans[idx-1][0]+ans[idx-2][0]
    ans[idx][1]=ans[idx-1][1]+ans[idx-2][1]
for num in input_list:
    print(*ans[num])