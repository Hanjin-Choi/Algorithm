a,b=input().split()
lena =len(a)
lenb =len(b)
cnt=0
for i in range(lena):
    if a[i]!=b[i]:
        cnt+=1
if lena!=lenb:
    for i in range(1,lenb-lena+1):
        temp=0
        for j in range(lena):
            if a[j]!=b[i+j]:
                temp+=1
        if temp<cnt:
            cnt=temp
print(cnt)