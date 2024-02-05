import sys
input = sys.stdin.readline

N = int(input())
List_num = list(map(int,input().split()))
L = list(set(List_num))
L.sort()
s= ''
dict_num={x:i for i,x in enumerate(L)}
for j in List_num:
    print(dict_num[j],end=' ')

