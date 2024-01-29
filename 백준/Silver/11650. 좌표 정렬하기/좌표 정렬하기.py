n= int(input())
L=[]
for i in range(n):
    L.append(list(map(int,input().split())))
L.sort(key=lambda x :(x[0],x[1]))    
for _ in L:
    print(_[0],_[1])
    