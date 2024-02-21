def solution(a, b):
    if b<a:
        b,a=a,b
    answer = sum(range(a,b+1))

    return answer