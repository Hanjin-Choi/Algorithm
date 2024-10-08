s =input()
cnt=0
a=''
for letter in s:
    a+=letter
    cnt+=1
    if cnt ==10:
        cnt=0
        print(a)
        a=''
print(a)