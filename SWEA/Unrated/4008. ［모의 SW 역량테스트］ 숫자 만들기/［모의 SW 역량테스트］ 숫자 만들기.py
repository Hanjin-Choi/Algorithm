def cal(n,c,s):
    if c==n:
        cal_list.append(s)
    else:
        for i in range(4):
            if oper[i] and i==0:
                oper[i]-=1
                cal(n,c+1,s+num_list[c])
                oper[i] += 1
                continue
            elif oper[i] and i==1:
                oper[i] -= 1
                cal(n,c+1,s-num_list[c])
                oper[i] += 1
                continue
            elif oper[i] and i==2:
                oper[i] -= 1
                cal(n,c+1,s*num_list[c])
                oper[i] += 1
                continue
            elif oper[i] and i==3:
                oper[i] -= 1
                if s<0:
                    cal(n,c+1,-1*(abs(s)//num_list[c]))
                else:
                    cal(n, c + 1, s // num_list[c])
                oper[i] += 1
                continue


t=int(input())

for tc in range(1,t+1):
    n = int(input())
    oper = list(map(int,input().split()))
    num_list = list(map(int,input().split()))
    cal_list =[]
    cal(n,1,num_list[0])
    ans = max(cal_list)-min(cal_list)
    print(f'#{tc} {ans}')