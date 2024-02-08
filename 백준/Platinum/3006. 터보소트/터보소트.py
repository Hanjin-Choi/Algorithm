import sys
input = sys.stdin.readline

n = int(input())
num_list =[int(input()) for _ in range(n)]
move_list=['0']*n
for i in range(0,n):
    if i == n-1:
        continue
    elif i %2 ==0:
        s = i//2
        j=num_list.index(s+1)
        move_list[i] = str(j)
        num_list.pop(j)
    else:
        e = n-1 -i//2
        j = num_list.index(e+1)
        move_list[i] = str(n-1-i-j)
        num_list.pop(j)

print("\n".join(move_list))