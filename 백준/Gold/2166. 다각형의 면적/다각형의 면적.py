n=int(input())
lst= [tuple(map(int,input().split())) for _ in range(n)]
ans =0
x0,y0 = lst[0]
for i in range(1,n-1):
    x1,y1 = lst[i]
    x2,y2 = lst[i+1]
    ans += x0*y1+x1*y2+x2*y0-x1*y0-x2*y1-x0*y2
ans=abs(ans)
ans/=2

if ans*100 - int(ans*100)>=5:
    ans=(int(ans*10)+1)/10
else:
    ans=int(ans*10)/10
print(ans)