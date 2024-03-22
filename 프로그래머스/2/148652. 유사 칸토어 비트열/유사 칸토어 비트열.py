def solution(n, l, r):
    answer = 0
    def make_usa(n,k):
        if n==1 and k==0:
            return 0
        elif n==1 and k==1:
            return 1
        elif n==1 and k==2:
            return 2
        elif n==1 and k==3:
            return 2
        elif n==1 and k==4:
            return 3
        elif n==1 and k==5:
            return 4
        else:    
            d = k//5**(n-1) 
            if d==0:
                return make_usa(n-1,k)
            elif d==1:
                return 4**(n-1) + make_usa(n-1,k-5**(n-1))
            elif d==2:
                return (4**(n-1))*2
            elif d==3:
                return (4**(n-1))*2 + make_usa(n-1,k-(5**(n-1)*3))  
            else:
                return (4**(n-1))*3 + make_usa(n-1,k-(5**(n-1)*4))
    print(make_usa(1,2),make_usa(1,1))
    answer= make_usa(n,r)-make_usa(n,l-1)
    return answer