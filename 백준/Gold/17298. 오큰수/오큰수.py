import sys
input = sys.stdin.readline

N=int(input())
arr = list(map(int,input().split()))
L =['-1']*N
stack=[]
maxx = arr[-1]
for i in range(N-2,-1,-1):
    if arr[i]-arr[i+1]<0:
        stack.append(arr[i+1])
        L[i] = str(stack[-1])
    else:
        if stack and arr[i]<stack[-1]:
            L[i] = str(stack[-1])
        elif stack:
            stack.pop()
            while stack:
                if arr[i]<stack[-1]:
                    L[i]= str(stack[-1])
                    break
                stack.pop()

print(' '.join(L))