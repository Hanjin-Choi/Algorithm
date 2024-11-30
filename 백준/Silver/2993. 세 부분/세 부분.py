s = input()
lst =[]
leng= len(s)
for i in range(1,leng-1):
    for j in range(i+1,leng):
        first = s[:i]
        second= s[i:j]
        third = s[j:]
        lst.append(first[::-1]+second[::-1]+third[::-1])
        
lst.sort()
print(lst[0])