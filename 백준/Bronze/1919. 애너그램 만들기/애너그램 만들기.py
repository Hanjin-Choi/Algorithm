aset= {chr(k):0 for k in range(97,123)}
bset= {chr(k):0 for k in range(97,123)}
a=input()
b=input()
for l in a:
    aset[l]+=1
for m in b:
    bset[m]+=1
ans=0
for i in range(97,123):
    ans += abs(aset[chr(i)]-bset[chr(i)])
print(ans)