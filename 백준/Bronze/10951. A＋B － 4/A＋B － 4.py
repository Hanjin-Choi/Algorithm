import sys
while True:
    L = sys.stdin.readline()
    if L =='':
        break
    else:
        A,B = map(int,L.split())
        print(A+B)