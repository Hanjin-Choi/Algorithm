N = int(input())
D = {}
for i in range(N):
    word = input()
    D.setdefault(word,len(word))
    
sort_d=sorted(D.items(),key = lambda x:(x[1],x[0]))
for x in range(len(sort_d)):
    print(sort_d[x][0])