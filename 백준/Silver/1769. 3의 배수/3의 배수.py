cnt=0
n=input()
while len(n)!=1:
    n=str(sum(map(int,list(n))))
    cnt+=1
print(cnt)
if not int(n)%3 and int(n)!=0:
    print('YES')
else:
    print('NO')