def solution(s):
    l = list(s)
    answer =''
    s=''
    idx=1
    for i in range(len(l)):
        if l[i]==' ':
            idx=1
            answer +=l[i]
        else:
            if idx%2:
                answer += l[i].upper()
                idx+=1
            else:
                answer +=l[i].lower()
                idx+=1
    return answer