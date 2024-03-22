def solution(n):
    answer = 0
    c=n//2
    alpha = [0,3,11]+[0]*(c-2)
    for i in range(3,c+1):
        alpha[i] +=alpha[i-1]*3+2
        for j in range(1,i-1):
            alpha[i]+=alpha[j]*2
            alpha[i]%=1000000007
        
    answer=alpha[c]
    return answer