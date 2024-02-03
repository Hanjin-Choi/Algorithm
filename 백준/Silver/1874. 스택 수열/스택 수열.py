import sys
input = sys.stdin.readline

N = int(input())
L = [0]*N
arr = []
ans = ''
for i in range(N):
    L[i] = int(input())
count =0
for j in range(N):
    if count<L[j]:
        for x in range(count+1,L[j]+1):
            count+=1
            arr.append(x)
            ans +='+\n'
        arr.pop()
        ans += '-\n'
    else:
        if len(arr)==0:
            ans +='NO'
        else:
            while len(arr):
                a= arr.pop()
                if a == L[j]:
                    ans += '-\n'
                    break
                else:
                    ans += '-\n'
if "NO" in ans:
    print('NO')
else:
    print(ans[:-1])
