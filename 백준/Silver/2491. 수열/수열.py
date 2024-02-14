import sys
input = sys.stdin.readline

n=int(input())
L=list(map(int,input().split()))

temp_asc=1 # 개수 임시저장, 최대값 저장 변수
temp_desc=1
max_asc=1
max_desc=1

for i in range(n):
    if i>0: # Ascending
        if L[i]-L[i-1]>=0: # 오름차순이면
            temp_asc+=1 # 개수 하나 추가
        elif temp_asc>max_asc: # 오름차순이 아닐경우, 최대값과 비교
            max_asc =temp_asc #저장후
            temp_asc =1 # 초기화
        else: # 초기화
            temp_asc=1
    if i<n-1: # Descending
        if  L[i]-L[i+1]>=0:
            temp_desc +=1
        elif temp_desc>max_desc:
            max_desc = temp_desc
            temp_desc =1
        else:
            temp_desc=1
if temp_desc>max_desc:
    max_desc = temp_desc
if temp_asc>max_asc:
    max_asc =temp_asc
print(max(max_asc,max_desc))

