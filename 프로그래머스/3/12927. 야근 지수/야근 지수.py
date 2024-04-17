
def solution(n, works):
    answer = 0
    leng =len(works)
    maxx=max(works)
    dic ={i:0 for i in range(maxx+1)}
    for w in works:
        dic[w] +=1 
    for hour in range(n):
        if maxx>0:
            dic[maxx] -=1
            dic[maxx-1] +=1 
            if not dic[maxx]:
                maxx -=1
        else:
            break
    for num in dic:
        answer += num**2 * dic[num]  
    return answer