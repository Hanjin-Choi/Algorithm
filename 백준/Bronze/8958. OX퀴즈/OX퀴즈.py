test_case = int(input())
for test in range(test_case):
    point = 0
    answer = list(input())
    get = 0
    for i in range(0,len(answer)):
        if answer[i]=='O':
            point +=1
            point += get
            get += 1
        else:
            get =0
    print(point)