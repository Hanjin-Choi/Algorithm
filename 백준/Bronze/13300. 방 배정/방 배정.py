import sys,math
input = sys.stdin.readline

n,k =map(int,input().split())
arr = [[0] for _ in range(12)] # 학년별 남여 인원수 저장 어레이
for i in range(n): # n명 데이터를 순회하면서 인원수 저장
    gen, grade = map(int,input().split())
    arr[(grade-1)*2 +gen][0] +=1
Room = 0 # 방개수
for room in arr:
    Room += math.ceil(room[0]/k)
print(Room)