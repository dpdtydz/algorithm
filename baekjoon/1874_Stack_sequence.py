import sys

input = sys.stdin.readline

N = int(input())
stack = []
result = []
count = 0
for i in range(N):
    num = int(input())
    while count < num:
        count +=1
        stack.append(count)
        result.append('+')
    if stack[-1] ==num : #지금num 이 stack-1보다
        stack.pop()
        result.append('-')
    else:
        break

if len(stack) != 0:
    print('NO')
else:
    for each in result:
        print(each)