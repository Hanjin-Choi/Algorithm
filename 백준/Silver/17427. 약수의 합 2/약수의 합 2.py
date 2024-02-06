import sys
input = sys.stdin.readline

N = int(input())
fn = 0
for i in range(1,N//2+1):
    if i<= N//2:
        m = N%i
        fn += N-m
if N %2 ==0:
    fn += (((N//2+1+N))*(N//2))//2
else:
    fn += (((N//2+1+N))*((N//2+1)))//2
if N ==1:
    fn =1
print(fn)