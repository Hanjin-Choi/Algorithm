n=int(input())
if n %2:
    s=(n+1)//2
    e= n+1
else:
    s=n//2
    e=n+1
max_count=0
max_list =[]
for i in range(s,e):
    temp = [n]
    count_list=1 # 2개가 들어있으니깐
    a=n
    b=i
    while b>=0:
        temp.append(b)
        count_list += 1
        a, b= b,a-b
    if count_list> max_count:
        max_count =count_list
        max_list=temp[:]
print(max_count)
print(*max_list)