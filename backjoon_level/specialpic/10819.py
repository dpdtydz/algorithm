# 문제
# N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.
#
# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|
#
# 입력
# 첫째 줄에 N (3 ≤ N ≤ 8)이 주어진다. 둘째 줄에는 배열 A에 들어있는 정수가 주어진다. 배열에 들어있는 정수는 -100보다 크거나 같고, 100보다 작거나 같다.
#
# 출력
# 첫째 줄에 배열에 들어있는 수의 순서를 적절히 바꿔서 얻을 수 있는 식의 최댓값을 출력한다.

# dfs
# def dfs(depth):
#     if depth == n:
#         res.append(sum(abs(li[i + 1] - li[i]) for i in range(n - 1)))
#         return
#
#     for i in range(n):
#         if check[i]:
#             continue
#         li.append(nums[i])
#         check[i] = 1
#         dfs(depth + 1)
#         li.pop()
#         check[i] = 0
#
#
# n = int(input())
# # nums = [map(int, input().split())]
# nums = list(map(int, input().split()))
# li, res = [], []
# check = [0] * n
# dfs(0)
# print(max(res))

# permutations
from itertools import permutations
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

per = permutations(a)
ans = 0

for i in per:
    s = 0
    for j in range(len(i) - 1):
        s += abs(i[j] - i[j + 1])
    if s > ans:
        ans = s

print(ans)
