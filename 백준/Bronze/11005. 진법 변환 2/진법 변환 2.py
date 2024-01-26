num, jin = map(int,input().split())
num_list =[]
def jinbup(num, jinsoo):
    d, m = divmod(num,jinsoo)
    if d == 0:
        if m >= 10:
            num_list.insert(0,chr(m+55))
        else:
            num_list.insert(0,str(m))
    else:
        if m >= 10:
            num_list.insert(0,chr(m+55))
        else:
            num_list.insert(0,str(m))
        return jinbup(d, jinsoo)
jinbup(num,jin)
pp="".join(num_list)
print(pp)