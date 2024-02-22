def solution(n, lost, reserve):
    answer = 0
    clothes =[1]*n
    for reser in reserve:
        clothes[reser-1] +=1
    for lo in lost:
        clothes[lo-1] -=1
    for i in range(n):
        if i<n-1 and clothes[i]==2 and clothes[i+1]==0:
            clothes[i] -=1
            clothes[i+1]+=1
        elif i<n-1 and clothes[i]==0 and clothes[i+1]==2:
            clothes[i] +=1
            clothes[i+1] -=1
    s=0
    for i in range(n):
        if clothes[i]:
            s +=1
            
        answer =s
    return answer