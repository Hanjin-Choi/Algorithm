cnt = 0
idn = 1
f = int(input())
for i in range(3):
    s = int(input())
    if idn and s != f:
        idn = 0
    if s > f:
        cnt += 1
        idn = 0
    elif s < f:
        cnt -= 1
        idn = 0
    f = s
if cnt == 3:
    print('Fish Rising')
elif cnt == -3:
    print('Fish Diving')
elif idn:
    print('Fish At Constant Depth')
else:
    print('No Fish')
