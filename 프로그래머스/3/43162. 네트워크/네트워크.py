def solution(n, computers):
    answer = 0
    arr = [0]*n
    def dfs(a):
        arr[a]=1
        for i in range(n):
            if computers[a][i] and not arr[i]:
                dfs(i)
        return 1
    for idx in range(n):
        if not arr[idx]:
            answer +=dfs(idx) 
    return answer