import sys
input = sys.stdin.readline
t=int(input())
for _ in range(t):
    p=input().strip()
    leng =int(input())
    if leng:
        lst = list(map(int,input().strip().strip('[').strip(']').split(',')))
    else:
        input()
        lst=[]
    idx=0
    ridx=leng
    flag=0
    for act in p:
        if act=='R':
            flag +=1
        elif act=='D' and leng>0:
            leng -=1
            if flag%2:
                ridx-=1
            else:
                idx+=1
        else:
            leng-=1
    if leng>=0 and flag%2:
        print('['+','.join(map(str,lst[idx:ridx][::-1]))+']')
    elif leng>=0:
        print('['+','.join(map(str,lst[idx:ridx]))+']')
    else:
        print('error')
