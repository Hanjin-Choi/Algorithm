n=input()
if n=='0':
    print(0)
else:
    c=[]
    for cnt in n:
        c.append(bin(int(cnt))[2:].zfill(3))
    print(''.join(c).lstrip('0'))