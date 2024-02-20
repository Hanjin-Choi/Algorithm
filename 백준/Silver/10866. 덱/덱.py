import sys, collections
input = sys.stdin.readline

dq = collections.deque() # deque 선언

n = int(input())
for i in range(n):
    action = input().rstrip()       # input에서 개행문자 제거
    if 'push' in action:            # push 면
        act, num = action.split()   # split해서 숫자를 받아옴
        if 'front' in act:
            dq.appendleft(int(num)) # front는 왼쪽
        else:
            dq.append(int(num))     # back은 오른쪽
    elif 'pop' in action:           # pop이면
        p, location = action.split('_') # _ 기준으로 나눠서 위치 받음
        if len(dq):
            if 'front' in location:
                a = dq.popleft()
            else:
                a = dq.pop()
            print(a)
        else:
            print(-1)
    elif action == 'size':
        print(len(dq))
    elif action =='empty':
        if len(dq):
            print(0)
        else:
            print(1)
    elif action == 'front':
        if len(dq):
            print(dq[0])
        else:
            print(-1)
    elif action == 'back':
        if len(dq):
            print(dq[-1])
        else:
            print(-1)