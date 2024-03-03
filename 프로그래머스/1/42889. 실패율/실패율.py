def solution(N, stages):
    count_arrive = [0]*(N+2)
    count_clear = [0]*(N+2)
    res=[[0,i] for i in range(N+1)]
    answer=[0]*N
    for user in stages:
        count_arrive[user] +=1 # 스테이지 막힌 인원
    count_clear[-1]=count_arrive[-1]
    for idx in range(N,0,-1):
        count_clear[idx] = count_clear[idx+1]+count_arrive[idx]  #스테이지 도달인원
        if count_clear[idx]:
            res[idx][0]=count_arrive[idx]/count_clear[idx] # 성공율
    
    res=res[1:N+1]
    res.sort(key=lambda x : (-x[0],x[1]))
    print(count_arrive)
    print(count_clear)
    print(res)
    for k in range(N):
        answer[k]=res[k][1]
        
        
    return answer