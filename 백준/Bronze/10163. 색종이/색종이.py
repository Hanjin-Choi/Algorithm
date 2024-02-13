import sys
input = sys.stdin.readline

n=int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
ans=[0]*n # 답저장할 리스트
set_area = set() # 면적 저장할 세트
for i in range(n-1,-1,-1): # 뒤로 순회
    r,c,w,h = arr[i]
    comp_set = set()
    for row in range(r,r+w): # 윗장면적
        for col in range(c,c+h):
            comp_set.add((row,col))
    ans[i]=len(comp_set-set_area) # 윗장 면적을 빼준 면적
    set_area=comp_set|set_area # 면적 저장
print(*ans,sep='\n')

