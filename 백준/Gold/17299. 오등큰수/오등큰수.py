import sys
input = sys.stdin.readline

n=int(input())
L = list(map(int,input().split()))
D = {}
for d in range(n):
    if L[d] not in D:
        D.setdefault(L[d],1)
    else:
        D[L[d]] +=1
ans= ['-1']*n
stack=[]
for i in range(n-2,-1,-1):
    if D[L[i]]<D[L[i+1]]:
        ans[i] = str(L[i+1])
        stack.append(i+1)
    else:
        if stack:
            if D[L[stack[-1]]]>D[L[i]]:
                ans[i]=str(L[stack[-1]])
            else:
                stack.pop()
                while stack:
                    if D[L[stack[-1]]] > D[L[i]]:
                        ans[i]=str(L[stack[-1]])
                        break
                    stack.pop()
print(' '.join(ans))