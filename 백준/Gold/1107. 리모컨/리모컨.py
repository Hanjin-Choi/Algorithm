import sys
input = sys.stdin.readline

n=input().strip()
leng=len(n)
m=int(input())
if m:
    bk = set(map(int,input().split()))
    no = set(i for i in range(10))-bk
    pl=mi=zero=p=m=float('inf')
    if 1 in no:
        pl = int(str(1)+str(min(no))*leng)-int(n)+leng+1
    if no and leng>1:
        mi= int(n)-int(str(max(no))*(leng-1))+leng-1
    elif no:
        mi=abs(int(n)-max(no))+1
    if 0 in no:
        zero=int(n) +1

    for digit in range(leng):
        if int(n[digit]) in bk:
            break
    left=[]
    right=[]
    for i in no:
        if i <=int(n[digit]):
            left.append(i)
        else:
            right.append(i)
    if left and right:
        p=int(n[:digit]+str(min(right))+str(min(left))*(leng-digit-1))+leng-int(n)
        m=int(n)-int(n[:digit]+str(max(left))+str(max(right))*(leng-digit-1))+leng
    elif left and not right:
        m=int(n)-int(n[:digit]+str(max(left))*(leng-digit))+leng
        for i in left:
            if digit>0 and i >int(n[digit-1]):
                p=int(n[:digit-1]+str(i)+str(min(left))*(leng-digit))+leng-int(n)
                break
            elif digit==0 and i>int(n[0]):
                p=abs(int(str(i)+str(min(left))*(leng-1))-int(n))+leng
                break
    elif right and not left:
        p=int(n[:digit]+str(min(right))*(leng-digit))+leng-int(n)
        for i in right[::-1]:
            if digit>0 and i <int(n[digit-1]):
                m =int(n)-int(n[:digit - 1] + str(i) + str(max(right)) * (leng - digit)) + leng
                break
            elif digit==0 and i<int(n[0]):
                m = abs(int(n)-int(str(i)+str(max(right)*(leng-1))))+leng
                break
    print(min(pl,mi,zero,p,m,abs(100-int(n))))

else:
    print(min(len(n),abs(100-int(n))))
