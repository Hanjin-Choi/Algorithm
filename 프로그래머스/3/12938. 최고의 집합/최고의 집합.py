def solution(n, s):
    d,m = divmod(s,n)
    answer = [d]*n
    for i in range(m):
        answer[i]+=1
    answer.sort()
    if not answer[0]:
        answer=[-1]
    return answer