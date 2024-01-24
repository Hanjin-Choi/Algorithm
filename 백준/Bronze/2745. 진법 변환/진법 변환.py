alpha_dict = dict()
for i in range(ord('A'),ord('Z')+1):
    temp_dict = {chr(i) : i-55}
    alpha_dict.update(temp_dict)
N,B = input().split()
list_N = list(N)
jin = int(B)
ten_jin = 0
i=0
while list_N:
    num = list_N.pop()
    if alpha_dict.get(num) != None:
        ten_jin += alpha_dict[num]*(jin**i)
        i += 1
    else:
        ten_jin += int(num)*(jin**i)
        i += 1
print(ten_jin)