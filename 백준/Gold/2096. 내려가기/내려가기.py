import sys
input = sys.stdin.readline
n= int(input())
first = list(map(int,input().strip().split()))
lst_max=first[:]
lst_min=first[:]
temp_max = [0, 0, 0]
temp_min = [0, 0, 0]
for _ in range(n-1):
    temp = list(map(int,input().strip().split()))
    temp_max[0]=temp[0]+max(lst_max[0],lst_max[1])
    temp_max[1]=temp[1]+max(lst_max)
    temp_max[2]=temp[2]+max(lst_max[1],lst_max[2])
    temp_min[0] =temp[0]+ min(lst_min[0],lst_min[1])
    temp_min[1] =temp[1]+ min(lst_min)
    temp_min[2] =temp[2]+ min(lst_min[1],lst_min[2])
    lst_max=temp_max[:]
    lst_min =temp_min[:]
print(max(lst_max),min(lst_min))