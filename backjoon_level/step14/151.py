def solution(estimates, k):
    a = [10, 1, 10, 1, 1, 4, 3, 10]
    k = 6
    deque(a)
    answer = findMax(a, k)
    return answer


def deque(list):
    for i in range(0, len(list)):
        list[i] = int(list[i])


def findMax(list, k):
    size = len(list)
    max_temp = list[0]

    for start in range(0, size - k + 1):
        sums = list[start]

        for i in range(1, k):
            sums += list[start + i]

        if sums > max_temp:
            max_temp = sums
    return max
