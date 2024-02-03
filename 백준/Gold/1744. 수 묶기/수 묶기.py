N = int(input())
L=[0]*N
count_negative =0
count_positive =0
count_one =0
mookki =0
for i in range(N):
    L[i]=int(input())
    if L[i] >1:
        count_positive +=1
    elif L[i]<=0:
        count_negative +=1
    elif L[i]==1:
        count_one +=1
L.sort()
if count_negative %2==0:
    for j in range(0,count_negative-1,2):
        mookki+=L[j]*L[j+1]
else:
    for j in range(0,count_negative-2,2):
        mookki += L[j]*L[j+1]
    mookki += L[count_negative-1]

if count_positive %2==0:
    for k in range(N-1,N-count_positive,-2):
        mookki +=L[k]*L[k-1]
else:
    for k in range(N - 1, N - count_positive+1, -2):
        mookki += L[k] * L[k - 1]
    mookki += L[N-count_positive]
mookki += 1 * count_one
print(mookki)