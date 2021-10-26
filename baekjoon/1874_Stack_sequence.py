import sys

input = sys.stdin.readline
# 스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 제일 나중에 들어간 자료가 제일 먼저 나오는 (LIFO, Last in First out) 특성을 가지고 있다.
N = int(input())
stack = []
result = []
count = 0
for i in range(N):
    num = int(input())
    while count < num:
        count += 1
        stack.append(count)
        result.append('+')
    if stack[-1] == num:  # 지금num 이 stack-1보다
        print(stack[-1])
        stack.pop()
        result.append('-')
    else:
        break
if len(stack) != 0:
    print('NO')
else:
    for each in result:
        print(each)
# 1st input
# [1 2 3 4 5 6 7 8]
# find 4
# [1] +
# [1 2] +
# [1 2 3] +
# [1 2 3 4] +
# [1 2 3] -
# find 3
# [1 2] -
# find 6
# [1 2 5] +
# [1 2 5 6] +
# [1 2 5] -
# find 8
# [1 2 5 7] +
# [1 2 5 7 8] +
# [1 2 5 7] -
# find 7
# [1 2 5] -
# find 5
# [1 2] -
# find 2
# [1] -
# find 1
# [] -
