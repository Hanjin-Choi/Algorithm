#Equilateral :  세 변의 길이가 모두 같은 경우
#Isosceles : 두 변의 길이만 같은 경우
#Scalene : 세 변의 길이가 모두 다른 경우

while True:
    a,b,c = map(int,input().split())
    if a==b and b==c and a==0:
        break
    elif a+b<=c or a+c<=b or b+c<=a:
        print('Invalid')
    elif a==b and b==c:
        print('Equilateral')
    elif a==b or b==c or c==a:
        print('Isosceles')
    else:
        print('Scalene')