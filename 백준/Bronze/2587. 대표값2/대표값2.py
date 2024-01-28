L=[]
for _ in range(5):
    L.append(int(input()))
L.sort()
print(sum(L)//5)
print(L[2])