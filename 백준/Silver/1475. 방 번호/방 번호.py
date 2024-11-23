di = { i:0 for i in range(10)}
n=input()
for num in n:
    di[int(num)] +=1
di[6]+=di[9]
di[9]=0
if di[6]%2:
    di[6]//=2
    di[6]+=1
else:
    di[6]//=2
maxy=0
for i in range(10):

    if di[i]>maxy:
        maxy=di[i]
print(maxy)