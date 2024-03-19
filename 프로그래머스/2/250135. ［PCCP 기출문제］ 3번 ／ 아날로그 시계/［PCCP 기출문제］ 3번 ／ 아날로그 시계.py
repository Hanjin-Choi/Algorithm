import math
def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    time = (h2-h1)*3600 +(m2-m1)*60 + s2-s1
    h_angle=(h1%12)*30+m1*0.5
    m_angle=m1*6
    s_angle=s1*6
    if s_angle<h_angle+0.01 and s_angle<m_angle+0.01:    # 아무것도 못 만났을때 0 시침만 만나면 1 분침만 만나면 2 시침분침 다만나면 3
        flag=0          
    elif s_angle>=h_angle+0.01 and s_angle<m_angle+0.01:
        flag=1
    elif s_angle>=m_angle+0.01 and s_angle<h_angle+0.01:
        flag=2
    else:
        flag=3
    while time >=0:
        h_angle=(h1%12)*30+m1*0.5 # 각도 표시
        m_angle=m1*6 
        s_angle=s1*6
        if s1 ==0: # 초침이 0 되면 초기화
            if flag==2 and h_angle>=354: # 초침이 0이됐는데 1개만 만났다면
                answer+=1
            elif flag==1 and m_angle>=354:
                answer+=1
            flag =0
        else:
            m_angle+=0.1 # 초침이 0이아니면 일부러 빗겨나가게 조정
            h_angle+=0.1
        if flag==0 and (s_angle>=h_angle and s_angle>=m_angle): # 둘이 같이 넘어가면
            if s_angle:
                answer+=2 
            else:
                answer+=1
            flag=3
        elif not flag%2 and  s_angle>=h_angle: # 아무것도 못만나거나 분침만 만났을경우 시침보다 초침이 높아지면
            answer +=1
            flag+=1
        elif flag<=1 and s_angle>=m_angle: # 아무것도 못만나거나 시침만 만났을 경우 분침보다 초침이 높아지면
            answer+=1
            flag+=2
        s1 +=1
        if s1==60:
            s1=0
            m1+=1
        if m1==60:
            h1 +=1
            m1=0
            print(answer)
        time -=1
    return answer