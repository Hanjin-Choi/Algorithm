t= int(input())
for tc in range(t):
    k = int(input())
    n = int(input())
    zero = [i for i in range(n+1)]
    next = [0]*(n+1)
    for floor in range(1,k+1):
        for room in range(1,n+1):
            if floor%2:
                next[room] = next[room-1] + zero[room]
            else:
                zero[room] = zero[room-1]+next[room]
    print(next[n] if k%2 else zero[n])