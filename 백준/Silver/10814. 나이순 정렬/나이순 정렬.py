N = int(input())
L=[]
for i in range(N):
    a,b=input().split()
    L.append([i,int(a),b])
L.sort(key=lambda x:(x[1],x[0]))

for i in L:
    print(i[1],i[2])