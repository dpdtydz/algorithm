# ## 문제
#
# 수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.
#
# 1. 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 2. 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 3. 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 4. 범위 : N개의 수들 중 최댓값과 최솟값의 차이
#
# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.
#
# ## 입력
#
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.
#
# ## 출력
#
# 첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
#
# 둘째 줄에는 중앙값을 출력한다.
#
# 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
#
# 넷째 줄에는 범위를 출력한다.

from collections import Counter
import sys


def artih_mean(list):
    result = sum(list)
    return result / len(list)


def get_median(list):
    centerIndex = len(list) // 2
    return (list[centerIndex] + list[-centerIndex - 1]) / 2


def get_counter(list):
    nums_s = Counter(list).most_common()
    if len(nums_s) > 1:
        if nums_s[0][1] == nums_s[1][1]:
            return nums_s[1][0]
        else:
            return nums_s[0][0]
    else:
        return nums_s[0][0]


def get_gap(list):
    max_number = max(list)
    min_number = min(list)
    return max_number - min_number


num_list = []
for _ in range(int(sys.stdin.readline())):
    num_list.append(int(sys.stdin.readline()))
num_list.sort()
print('%.0f' % artih_mean(num_list))
print('%.0f' % get_median(num_list))
print(get_counter(num_list))
print(get_gap(num_list))
