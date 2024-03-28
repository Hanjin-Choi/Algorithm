n=int(input())
digit = [0]*26
for i in range(n):
    s=input()
    for idx, let in enumerate(s[::-1]):
        digit[ord(let)-65] += 10**idx
digit.sort(reverse=True)
k=9
total=0
while k>0:
    total += digit[9-k]*k
    k-=1
print(total)