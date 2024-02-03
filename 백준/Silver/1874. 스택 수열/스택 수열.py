import sys
input = sys.stdin.readline

N = int(input())
stack = []
count_in =0
result = []
flag = 1

for i in range(N):
    end = int(input())
    if count_in<end:
        while count_in != end:
            count_in +=1
            stack.append(count_in)
            result.append('+')
    if end == stack[-1]:
        stack.pop()
        result.append('-')
    else:
        flag = 0
        break
if flag ==0:
    print('NO')
else:
    print("\n".join(result))