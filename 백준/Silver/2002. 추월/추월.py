import sys
input = sys.stdin.readline

n = int(input())
dae =[input().strip() for _ in range(n)]
young  =[input().strip() for _ in range(n)]
idx =0
idx2=0
cnt=0
visit =set()
while idx<n-1 and idx2<n-1:
    if dae[idx]==young[idx2]:
        idx +=1
        idx2 +=1
    elif dae[idx] not in visit:
        visit.add(young[idx2])
        idx2+=1
        cnt+=1
    else:
        idx+=1
print(cnt)