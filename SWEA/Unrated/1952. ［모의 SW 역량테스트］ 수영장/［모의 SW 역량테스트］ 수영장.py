t=int(input())

def back(m,cost):
    global mini
    if m==12:
        if mini>cost:
            mini=cost
    elif cost>mini:
        return
    else:
        if plan[m]:
            back(m+1,cost+price[0]*plan[m])
            back(m+1,cost+price[1])
            if m+3<12:
                back(m+3,cost+price[2])
            elif m==11:
                back(12,cost+price[2])
            else:
                back(12,cost+price[2])
        else:
            back(m+1,cost)


for tc in range(1,t+1):
    price = list(map(int,input().split()))# 1일 1달 3달 1년
    plan=list(map(int,input().split()))
    mini=price[-1]
    back(0,0)
    print(f'#{tc} {mini}')