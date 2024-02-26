n= int(input())
num_list =[0]*(n+1)
for idx in range(1,n+1):
    num = str(idx)
    res = ''
    for let in num:
        if let in '369':
            if len(res)>=1 and res[-1]=='-':
                res += '-'
            elif len(res)>=1:
                res = res[:-1] + '-'
            else:
                res += '-'
        elif '-' not in res:
            res += let
    num_list[idx] = res
print(' '.join(num_list[1:]))