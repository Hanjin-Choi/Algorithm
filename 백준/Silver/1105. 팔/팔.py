l,r =input().split()

length=len(r)
l=l.zfill(length)
lst=[0]*length
cnt=0
for i in range(length):
    if l[i]==r[i]:
        lst[i]=1
    if sum(lst)==i+1 and l[i]==r[i]=='8':
        cnt+=1

print(cnt)