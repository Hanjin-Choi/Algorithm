a=input()
bin=set()
leng = len(a)
for i in range(leng):
    for j in range(leng):
        k=i+j+1
        if k<=leng:
            bin.add(a[i:k])
print(len(bin))