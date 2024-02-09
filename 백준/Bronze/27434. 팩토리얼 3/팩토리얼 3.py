import sys
sys.setrecursionlimit(10**9)
n = int(input())

def fact(num):
    if num ==0:
        return 1
    return num * fact(num-1)

print(fact(n))