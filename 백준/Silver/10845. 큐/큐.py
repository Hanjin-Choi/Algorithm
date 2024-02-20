import sys
input = sys.stdin.readline

n=int(input())
st = [0]*10000
f = 0
rear = 0
for i in range(n):
    action = input().rstrip()
    if 'push' in action:
        act, num = action.split()
        st[rear]=int(num)
        rear +=1
    elif action =='front':
        if f==rear:
            print(-1)
        else:
            print(st[f])
    elif action == 'back':
        if f==rear:
            print(-1)
        else:
            print(st[rear-1])
    elif action == 'empty':
        if f==rear:
            print(1)
        else:
            print(0)
    elif action =='size':
        print(rear-f)
    elif action =='pop':
        if f==rear:
            print(-1)
        else:
            print(st[f])
            f+=1
