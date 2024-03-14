from collections import deque

N, K = map(int, input().split())
graph = [0] * 100001

q = deque()
q.append(N)

while q:
    n = q.popleft()

    if n == K:
        print(graph[n])
        break

    for nx in [n-1, n+1, n*2]:
        if 0 <= nx <= 100000 and not graph[nx]:
            q.append(nx)
            graph[nx] = graph[n] + 1