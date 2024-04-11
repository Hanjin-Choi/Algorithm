import sys
input = sys.stdin.readline

def plane(n):
    if gate[n]==n:
        return n
    else:
        gate[n] =plane(gate[n])
        return gate[n]
g=int(input())
p=int(input())
visit = set()
gate = [i for i in range(g+1)]
cnt =0
for _ in range(p):
    gi = int(input())
    res=plane(gi)
    if res==0:
        break
    else:
        gate[res]=plane(res-1)
        cnt+=1

print(cnt)