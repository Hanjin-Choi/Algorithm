n,m =map(int,input().split())

def cnt_video(value):
    idx=n-1
    cnt =0
    temp=0
    max_temp =0
    while idx>=0:
        if temp+lst[idx]<=value:
            temp +=lst[idx]
        else:
            if max_temp<temp:
                max_temp=temp
            temp=lst[idx]
            cnt+=1
        idx -=1
    if max_temp<temp:
        max_temp=temp
    cnt +=1
    return cnt, max_temp
lst = list(map(int,input().split()))
total =sum(lst)
if m ==1:
    print(total)
else:
    start = total//m
    end = total
    while start<=end:
        mid = (start+end)//2
        cnt,max_temp = cnt_video(mid)
        if cnt<=m:
            end =mid-1
        else:
            start = mid +1
    c,maxx=cnt_video(start)

    print(maxx)

