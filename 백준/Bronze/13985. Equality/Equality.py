i = input()
lst = []
for letter in i:
    if letter.isnumeric():
        lst.append(int(letter))
if lst[0]+lst[1]==lst[2]:
    print('YES')
else:
    print('NO')