A=0
B=0
for i in range(3):
    A+=int(input())*(3-i)
for i in range(3):
    B+=int(input())*(3-i)
if A==B:
    print('T')
elif A>B:
    print('A')
else:
    print('B')
    