N= int(input())
sum_l=0
length= len(str(N))
if length ==1:
    print(N)
else:
    for i in range(1,length):
        sum_l += 9 * 10**(i-1) *i
    sum_l += (N-10**(length-1)+1)*length
    print(sum_l)