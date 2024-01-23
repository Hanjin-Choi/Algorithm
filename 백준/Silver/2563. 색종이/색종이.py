N= int(input())
white = []
paper_area = []
area = 0
for i in range(100):
    white.append([0]*100)
for paper_num in range(N):
    left, bottom = map(int,input().split())
    paper_area.append([left,bottom])
for paper in paper_area:
    for left in range(paper[0],paper[0]+10):
        for bottom in range(paper[1],paper[1]+10):
            white[left][bottom] = 1
for i in range(100):
    area += sum(white[i])
print(area)