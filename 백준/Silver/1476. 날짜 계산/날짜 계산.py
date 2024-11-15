e,s,m = map(int,input().split())
# 15, 28, 19
for time in range(28*19):
    cal = time*15 +e
    if cal%28 != s%28 :
        continue
    if cal %19 != m%19 :
        continue
    break
print(cal)