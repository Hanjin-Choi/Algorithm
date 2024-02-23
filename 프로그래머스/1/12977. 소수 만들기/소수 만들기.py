def solution(nums):
    answer = 0
    era = [0,0] + [1]*max(nums)*3
    setnum=set()
    for e in range(2,max(nums)*3):
        if era[e]:
            setnum.add(e)
            for note in range(e*2,max(nums)*3,e):
                era[note] =0
    leng =len(nums)
    for i in range(leng-2):
        for j in range(i+1,leng-1):
            for k in range(j+1, leng):
                if (nums[i]+nums[j]+nums[k]) in setnum:
                    answer +=1
    
    return answer