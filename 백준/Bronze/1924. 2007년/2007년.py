M,D = map(int,input().split())
def exchange_M_D(m):
    global D
    if m ==1:
        return D
    elif m ==3:
        D += 28
        return exchange_M_D(m-1)
    elif m ==2 or m==4 or m==6 or m==8 or m==9 or m==11:
        D += 31
        return exchange_M_D(m-1)
    else:
        D += 30
        return exchange_M_D(m-1)
exchange_M_D(M)
rest = D % 7
if rest == 0:
    print("SUN")
elif rest == 1:
    print("MON")
elif rest == 2:
    print("TUE")
elif rest == 3:
    print("WED")
elif rest == 4:
    print("THU")
elif rest == 5:
    print("FRI")
elif rest == 6:
    print("SAT")