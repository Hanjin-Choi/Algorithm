N = int(input())
clap = 0
num = 1
while N:
    for i in [3,6,9]:
        if str(i) in str(num):
            clap += str(num).count(str(i))
    num +=1
    N -= 1
print(clap)
