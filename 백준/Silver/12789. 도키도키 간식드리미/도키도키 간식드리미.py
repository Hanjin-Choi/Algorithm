n = int(input())
l = list(map(int, input().split()))
stack = []
flag = 1
for i in range(n):
    if l[i] == flag:
        flag += 1
    elif stack and stack[-1]==flag:
        while stack and flag == stack[-1]:
            stack.pop()
            flag += 1
        stack.append(l[i])
    elif flag != l[i]:
        stack.append(l[i])

while stack and flag == stack[-1]:
    stack.pop()
    flag+=1

if stack:
    print('Sad')
else:
    print('Nice')

