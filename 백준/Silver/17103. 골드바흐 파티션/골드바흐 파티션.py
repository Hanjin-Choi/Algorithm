import sys,collections
input = sys.stdin.readline

maxx = int(1000001)
era = [0, 0] + [1] * (maxx - 1)
prime = []
def findprime(maxx):
    for i in range(2, maxx):
        if era[i]:
            prime.append(i)
            for j in range(i ** 2, maxx, i):
                era[j] = 0
findprime(maxx)
leng = len(prime)
t = int(input())
for _ in range(t):
    goal = int(input())
    ans =0
    for idx in range(leng):
        p =prime[idx]
        if p >goal//2:
            break
        aim = goal-p
        if era[aim]:
            ans+=1
    print(ans)
