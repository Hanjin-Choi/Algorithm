n = int(input())
nl = list(map(int, input().split()))
m = int(input())
ml = list(map(int, input().split()))
dict_n = {}
for i in range(n):
    if nl[i] in dict_n:
        dict_n[nl[i]] +=1
    else:
        dict_n[nl[i]] = 1
for j in range(m):
    print(dict_n.get(ml[j],0),end=' ')