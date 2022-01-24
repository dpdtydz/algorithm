# ## 수 정렬하기 2
#
# ## 문제
#
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
#
# ## 입력
#
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
#
# ## 출력
#
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
# merge
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array)
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    #분할 좌,우
    i, j, k = 0, 0, 0
    #분할 완료된 배열끼리 비교
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = array[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
    # 먼저 끝나면?
    if i == len(left):
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
    return array


n = int(input())
num = list()
for _ in range(n):
    num.append(int(input()))

num = merge_sort(num)

for i in num:
    print(i)
