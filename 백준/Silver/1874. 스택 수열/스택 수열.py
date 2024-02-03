# 스택 수열
n = int(input())
stack = []
count = 1
result = []

for i in range(1, n + 1):
    num = int(input())
    while count <= num:
        stack.append(count)
        count += 1
        result.append("+")
    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        exit(0)

print("\n".join(result))