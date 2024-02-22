def solution(s):
    answer = ''
    leng = len(s)
    if leng%2:
        answer = s[leng//2]
    else:
        answer = s[leng//2-1:leng//2+1]
    return answer