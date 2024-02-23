def solution(s):
    word = s
    di = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8', 'nine':'9', 'zero':'0'}
    for eng in di:
        if eng in word:
            word = word.replace(eng,di[eng])
    answer = int(word)
    
    return answer