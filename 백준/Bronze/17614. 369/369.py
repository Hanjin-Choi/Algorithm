from collections import Counter
n=int(input())
num = []
for i in range(1,n+1):
    num+= list(str(i))
dic = Counter(num)
clap = dic['3']+dic['6']+dic['9']
print(clap)
