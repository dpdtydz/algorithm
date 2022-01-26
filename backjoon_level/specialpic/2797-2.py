def dfs(depth):
    if depth == n:
        res.append(sum((li[i] + li[i+1] + li[i+2]) for i in range(n - 1)))
        return

    for i in range(n):
        if check[i]:
            continue
        li.append(nums[i])
        check[i] = 1
        dfs(depth + 1)
        li.pop()
        check[i] = 0


n, m = map(int, input().split())
# nums = [map(int, input().split())]
nums = list(map(int, input().split()))
li, res = [], []
check = [0] * n
dfs(0)
print(max(res))
