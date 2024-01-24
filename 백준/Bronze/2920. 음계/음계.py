L = list(map(int,input().split()))
ascend = 0
descend = 0
for i in range(7):
    if L[i] < L[i+1]:
        ascend += 1
    elif L[i] > L[i+1]:
        descend +=1
if ascend ==7:
    print("ascending")
elif descend ==7:
    print("descending")
else:
    print("mixed")