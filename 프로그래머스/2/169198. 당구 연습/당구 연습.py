def solution(m, n, startX, startY, balls):
    answer = []
    for ball in balls:
        x,y=ball[0],ball[1]
        leng=abs(startX-x)**2+abs(startY-y)**2
        l=abs(startX+x)**2+abs(startY-y)**2
        r=abs(startX-(2*m-x))**2+abs(startY-y)**2
        u=abs(startX-x)**2+abs(startY-(2*n-y))**2
        d=abs(startX-x)**2 + abs(startY+y)**2
        dae1=abs(startX+x)**2+abs(startY+y)**2
        dae2=abs(startX-(2*m-x))**2+abs(startY-(2*n-y))**2
        dae3=abs(startX+x)**2+abs(startY-(2*n-y))**2
        dae4=abs(startX-(2*m-x))**2+abs(startY+y)**2
        
        if startX==x:
            if y<startY:
                d=float('inf')
            else:
                u=float('inf')
        if startY==y:
            if x<startX:
                l=float('inf')
            else:
                r=float('inf')
        if x==y and startX==startY and dae2>dae1:
            dae1=float('inf')
        if m-x==n-y and m-startX==n-startY and dae2<dae1:
            dae2=float('inf')
        if x==n-y and startX==n-startY and dae3<dae4:
            dae3=float('inf')
        if m-x==y and m-startX==startY and dae4<dae3:
            dae4=float('inf')
        print(l,r,u,d,dae1,dae2,dae3,dae4)
        answer.append(min(l,r,u,d,dae1,dae2,dae3,dae4))
    return answer