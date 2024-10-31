lst=list(input().split('.'))
s=[]
for let in lst:
    leng=len(let)
    m,r = divmod(leng,4)
    if r%2:
        s=['-1']
        break
    s.append('AAAA'*m + 'B'*r)

ans='.'.join(s)
print(ans)
