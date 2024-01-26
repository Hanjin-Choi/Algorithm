n = int(input())
def line_point(n):
    if n ==1:
        return 2
    else:
        return 2*line_point(n-1)-1
print(line_point(n+1)**2)
