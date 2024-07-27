n=int(input())

i=1
t=0
while True:
    t=i*(i+1)//2
    if t>n:break
    i+=1
print(i-1)