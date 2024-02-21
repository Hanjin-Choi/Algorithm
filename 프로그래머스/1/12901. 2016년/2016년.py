def solution(a, b):
    date=b-1
    date_dict = {0:'FRI',1:'SAT',2:'SUN',3:'MON',4:'TUE',5:'WED',6:'THU'}
    while a>1:
        if a==2 or a== 4 or a==6 or a==8 or a==9 or a==11:
            date +=31
        elif a==3:
            date +=29
        else:
            date+=30
        a-=1
    
        
    answer = date_dict[date%7]
    return answer