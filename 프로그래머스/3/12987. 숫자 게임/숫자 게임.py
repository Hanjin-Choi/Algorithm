from heapq import heappop,heapify
def solution(A, B):
    answer = 0
    heapify(A)
    heapify(B)
    a=heappop(A)
    while B:
        b= heappop(B)
        if b>a:
            answer+=1
            if A:
                a=heappop(A)
            else:break
    return answer