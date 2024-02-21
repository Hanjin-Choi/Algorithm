n=int(input())
nd=set()
for i in range(n):
    name,status = input().split()
    if status=='enter':
        nd.add(name)
    else:
        nd.remove(name)
nd = list(nd)
nd.sort(reverse=True)
ans = '\n'.join(nd)
print(ans)