n = int(input())

for t in range(1, n + 1):
    d = {chr(i + 97): 0 for i in range(26)}
    s = input()
    s = s.lower()
    for letter in s:
        if letter in d:
            d[letter] += 1
    mini = 4
    for i in range(26):
        if d[chr(i + 97)] < mini:
            mini = d[chr(i + 97)]
    if mini >= 3:
        print(f'Case {t}: Triple pangram!!!')
    elif mini == 2:
        print(f'Case {t}: Double pangram!!')
    elif mini == 1:
        print(f'Case {t}: Pangram!')
    else:
        print(f'Case {t}: Not a pangram')
