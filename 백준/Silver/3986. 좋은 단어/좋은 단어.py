import sys
input = sys.stdin.readline
def good_word(string):
    leng = len(string)
    st=[]
    if leng %2:
        return 0
    else:
        for i in range(leng):
            if i ==0:
                st.append(string[i])
            else:
                if st and st[-1]==string[i]:
                    st.pop()
                else:
                    st.append(string[i])
        if st:
            return 0
        else:
            return 1

n = int(input())

ans = 0
for _ in range(n):
    s = input().strip('\n')
    ans += good_word(s)
print(ans)