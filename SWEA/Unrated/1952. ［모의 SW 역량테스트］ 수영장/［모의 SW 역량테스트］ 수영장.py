t=int(input())

def back(pl,m,cost):
    global mini
    temp=pl[:]
    if m==12:
        if mini>cost:
            mini=cost
    elif cost>mini:
        return
    else:
        if plan[m]:
            back(temp,m+1,cost+price[0]*temp[m])
            back(temp,m+1,cost+price[1])
            if m+2<12:
                temp[m+1]=temp[m+2]=0
                back(temp,m+1,cost+price[2])
            elif m+1<12:
                temp[m+1]=0
                back(temp,m+1,cost+price[2])
            else:
                back(temp,m+1,cost+price[2])
        else:
            back(temp,m+1,cost)


for tc in range(1,t+1):
    price = list(map(int,input().split()))# 1일 1달 3달 1년
    plan=list(map(int,input().split()))
    mini=price[-1]
    back(plan,0,0)
    print(f'#{tc} {mini}')