import sys,collections
input = sys.stdin.readline

n= int(input()) # 라운드 수
for i in range(n): # 라운드만큼 진행
    a, *A = map(int,input().split()) # a와 A의 딱지를 리스트로 저장
    b, *B = map(int,input().split()) # a와 A의 딱지를 리스트로 저장
    Acount = collections.Counter(A)
    Bcount = collections.Counter(B)
    for j in range(4,0,-1): # 각 딱지의 개수 파악, 별부터 시작
        if Acount[j] > Bcount[j]: # A가 많으면 A 승리
            print('A')
            break
        elif Acount[j] < Bcount[j]: # B가 많으면 B승리
            print('B')
            break
        elif j==1: # 둘이 같은 경우 중 마지막 까지 같으면
            print('D')
