def solution(numbers, hand):
    answer = ''
    row_dict = {'1':1,'2':1,'3':1,'4':2,'5':2,'6':2, '7':3,'8':3,'9':3,'*':4,'0':4,'#':4}
    col_dict = {'1':1,'2':2,'3':3,'4':1,'5':2,'6':3, '7':1,'8':2,'9':3,'*':1,'0':2,'#':3}
    l='*'
    r='#'
    for num in numbers:
        if str(num) in '147*':
            answer += 'L'
            l = str(num)
        elif str(num) in '369#':
            answer += 'R'
            r = str(num)
        else:
            move_left = abs(row_dict[l]-row_dict[str(num)]) +abs(col_dict[l]-col_dict[str(num)])
            move_right = abs(row_dict[r]-row_dict[str(num)]) +abs(col_dict[r]-col_dict[str(num)])
            if move_left<move_right:
                answer +='L'
                l=str(num)
            elif move_left > move_right:
                answer += 'R'
                r = str(num)
            elif hand =='left':
                answer +='L'
                l=str(num)
            else:
                answer += 'R'
                r = str(num)
                
    return answer