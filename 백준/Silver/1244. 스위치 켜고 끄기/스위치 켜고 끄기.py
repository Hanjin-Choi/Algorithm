import sys
input = sys.stdin.readline

n= int(input()) #스위치 개수
arr = [0] + list(map(int,input().split())) # 스위치상태를 1번부터 받음
num = int(input()) #학생수
for i in range(num):
    gen,s_num = map(int,input().split()) # 성별, 스위치 번호
    if gen ==1: # 남자면
        for j in range(s_num,n+1,s_num): # 스위치의 배수만 상태 변경
            if arr[j]: # 해당 위치의 스위치 상태가 1이면
                arr[j]=0
            else: # 해당 스위치의 상태가 0이면
                arr[j]=1
    else: # 여자면
        for k in range(n-s_num,-1,-1): # 대칭이 큰 위치 부터 찾기 위해 거꾸로 탐색
            if s_num-k>=1 and s_num+k<=n:
                if arr[s_num-k:s_num+k+1]==arr[s_num-k:s_num+k+1][::-1]: #대칭이면
                    for l in range(s_num-k,s_num+k+1): # 대칭인 위치만큼 스위치 변경
                        if arr[l]:
                            arr[l]=0
                        else:
                            arr[l]=1
                    break # 반복종료
for j in range(1,n+1):
    print(arr[j], end=' ')
    if j % 20 == 0:
        print()