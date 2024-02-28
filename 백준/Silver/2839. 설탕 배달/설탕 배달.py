kg = int(input())

def num_bag(kg):
    kg_5 = kg //5
    kg_3 = 0
    if kg_5 * 5 == kg:
        return kg_5
    else:
        for i in range(kg//5,-1,-1):
            need_3 = kg-i*5
            if need_3 % 3==0:
                kg_3 = need_3 // 3
                return i+kg_3
        if kg_3 == 0:
            return -1
print(num_bag(kg))