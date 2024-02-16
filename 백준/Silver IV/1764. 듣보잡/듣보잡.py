n, m = map(int, input().split())
d = {input() for i in range(n)}
b = {input() for i in range(m)}
l = list(d&b)
l.sort()
print(len(l))
for k in l:
    print(k)