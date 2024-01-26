start, end = map(int,input().split())
c = 1
def cal(start, end):
    global c
    if start==end:
        pass
    elif start> end:
        c = -1
    elif end % 10 ==1:
        c +=1
        return cal(start, end//10)
    elif end % 2 ==1:
        c = -1
    elif end %2 == 0:
        c +=1
        return cal(start, end//2)
cal(start,end)
print(c)