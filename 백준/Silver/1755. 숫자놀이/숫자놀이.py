import math
m,n = map(int,input().split())
lst=[]
d = {'0':'zero' ,'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7': 'seven','8':'eight','9':'nine'}
for i in range(m,n+1):
    temp = list(str(i))
    res=''
    for let in temp:
        res +=d[let]+' '
    lst.append((i,res))

lst.sort(key=lambda x :(x[1]))
cnt=0
for i in range(n-m+1):
    if cnt!=0 and not cnt %10:
        print()
    print(lst[i][0],end =' ')
    cnt+=1
