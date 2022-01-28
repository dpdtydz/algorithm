# 축구를 재미있게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 한다. 위의 예제와 같은 경우에는 1, 4번이 스타트 팀, 2, 3번 팀이 링크 팀에 속하면 스타트 팀의 능력치는 6, 링크 팀의 능력치는 6이 되어서 차이가 0이 되고 이 값이 최소이다.
#
# ## 입력
#
# 첫째 줄에 N(4 ≤ N ≤ 20, N은 짝수)이 주어진다. 둘째 줄부터 N개의 줄에 S가 주어진다. 각 줄은 N개의 수로 이루어져 있고, i번 줄의 j번째 수는 Sij 이다. Sii는 항상 0이고, 나머지 Sij는 1보다 크거나 같고, 100보다 작거나 같은 정수이다.
#
# ## 출력
#
# 첫째 줄에 스타트 팀과 링크 팀의 능력치의 차이의 최솟값을 출력한다.

from itertools import combinations as c

n = int(input())
array = [i for i in range(n)]
matrix = []
for _ in range(n):
    matrix.append((list((map(int, input().split())))))
result = int(1e9)
for r1 in c(array, n // 2):  # n/2 만큼
    start, link = 0, 0
    r2 = list(set(array) - set(r1))  # 중복제거
    for r in c(r1, 2):
        start += matrix[r[0]][r[1]]
        start += matrix[r[1]][r[0]]
    for r in c(r2, 2):
        link += matrix[r[0]][r[1]]
        link += matrix[r[1]][r[0]]
    result = min(result, abs(start - link))  # 횟수는 무조건 정수

print(result)
