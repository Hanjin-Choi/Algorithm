N, M = map(int,input().split())
L = list(map(int,input().split()))
L.sort()
S = []
def bruteforce():
    max_sum=0
    for i in range(N-2):# 전체 순회해서 최대인 값을 출력하기
        for j in range(i+1, N-1):
            for k in range(j+1,N):
                ssum = L[i] + L[j] + L[k]
                if max_sum < ssum<=M:
                    max_sum =ssum
                elif ssum>M:
                    break
    return max_sum
print(bruteforce())