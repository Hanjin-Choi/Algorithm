n=int(input())

for _ in range(n):
    a,b = map(int,input().split())
    print(a,b)
    s = b+(a-1)*(b-2)
    print(s)