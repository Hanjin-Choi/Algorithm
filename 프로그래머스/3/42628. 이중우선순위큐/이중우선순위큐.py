from collections import deque
def solution(operations):
    answer = []
    queue=[]
    min_idx=0
    max_idx=0
    for sent in operations:
        i, num = sent.split()
        num=int(num)
        if i =="I":
            queue.append(num)
        elif num==-1 and queue:
            queue.pop(queue.index(min(queue)))
        elif num==1 and queue:
            queue.pop(queue.index(max(queue)))
    if queue:
        answer=[max(queue),min(queue)]
    else:
        answer=[0,0]
    return answer