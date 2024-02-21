def solution(lottos, win_nums):
    set_lotto = set(lottos) & set(win_nums)
    count_zero = lottos.count(0)
    len_set=len(set_lotto)
    max_len = len_set+count_zero if len_set<5 else 6
    dict_lotto = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    answer = [dict_lotto[max_len],dict_lotto[len_set]]
    return answer