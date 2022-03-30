from itertools import combinations
import sys

n, m = map(int, sys.stdin.readline().split())
s, chicken, house = [], [], []

for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    s.append(a)
    # 모든 맵을 리스트에 저장
    for j in range(n):
        if a[j] == 2:
            chicken.append([i, j])
        if a[j] == 1:
            house.append([i, j])
            #리스트에서 각 위치에 따라 2=치킨,1=집 으로 분류해준다. 좌표를 넣어주기 때문에 (3,1)형태로 들어감
chicken = combinations(chicken, m)
# 치긴집과의 거리가 가장 먼 순서로 M개만큼 추려야함
result = 100000000
for k in chicken:
    min_result = 0
    for i, j in house:
        min_num = 100000000
        for x, y in k:
            min_num = min(min_num, abs(x - i) + abs(y - j))
            # 좌표를 찾아서 각 집을 기준으로 치킨집을 찾고, 공식에 따라 거리르 계산
        min_result += min_num
    result = min(result, min_result)

print(result)
