lst = [i**2 for i in range(2,224)]
ans=[i for i in range(50001)]
for i in range(50001):
    for temp in lst:
        if temp+i<=50000:
            ans[i+temp]=min(ans[i+temp],ans[i]+1)
        else:break
n=int(input())
print(ans[n])