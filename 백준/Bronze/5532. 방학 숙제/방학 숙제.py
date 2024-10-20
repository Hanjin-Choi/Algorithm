l=int(input())
a=int(input())
b=int(input())
c=int(input())
d=int(input())
first = a // c
second = b//d
if a%c:
    first +=1
if b%d:
    second +=1
print(l-max(first,second))
