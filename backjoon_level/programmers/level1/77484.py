def solution(lottos, win_nums):
    count = 0
    special = 0
    for i in range(len(lottos)):
        if lottos[i] == 0:
            special += 1
        for j in range(len(win_nums)):
            if lottos[i] == win_nums[j]:
                count += 1
    max_result = count + special
    if count == 6:
        rank = 1
    elif count == 5:
        rank = 2
    elif count == 4:
        rank = 3
    elif count == 3:
        rank = 4
    elif count == 2:
        rank = 5
    else:
        rank = 6

    if max_result == 6:
        ranks = 1
    elif max_result == 5:
        ranks = 2
    elif max_result == 4:
        ranks = 3
    elif max_result == 3:
        ranks = 4
    elif max_result == 2:
        ranks = 5
    else:
        ranks = 6
    answer = [ranks,rank]
    return answer