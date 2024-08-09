def back(num,cnt,s):
    if cnt ==m:
        print(s.strip())
    else:
        for i in range(1,n+1):
            back(i,cnt+1,s+' '+str(i))
n,m = map(int,input().split())
back(1,0,'')