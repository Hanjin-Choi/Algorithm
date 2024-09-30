import sys
input = sys.stdin.readline
idx=0
while True:
    idx +=1
    s = input().strip()
    cnt =0
    if '-'in s:
        break
    lst=[]
    for let in s:
        if let=='{':
            lst.append(let)
        elif not lst:
            lst.append('{')
            cnt +=1
        elif lst and lst[-1]=='{':
            lst.pop()
        elif lst and lst[-1]=='}':
            lst.pop()
            cnt +=1
    while lst:
        if lst[-1]=='{':
            cnt+=1
        if lst[-2]=='}':
            cnt+=1
        lst.pop()
        lst.pop()
    print(f'{idx}. {cnt}')