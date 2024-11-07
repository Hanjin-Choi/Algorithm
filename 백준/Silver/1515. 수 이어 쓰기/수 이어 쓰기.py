n=input()
leng = len(n)
idx=0
cnt=0
while idx<leng:
    cnt+=1
    for i in str(cnt):
        if n[idx]==i:
            idx+=1
        if idx==leng:
            break
print(cnt)