while True:
    N = int(input())
    if N == 0:
        break
    else:
        str_N = str(N)
        lst_N = list(str_N)
        reverse_N=lst_N[:]
        reverse_N.reverse()
        if lst_N == reverse_N:
            print("yes")
        else:
            print("no")