n = int(input())
graph = []
num = []

for i in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def DFS(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        # x가 0보다 작거나
        # x가 지금돌고 있는 n보다 크거나 같거나
        # y가 0보다 작거나
        # y가 지금돌고 있는 n보다 크거나 같거나
        # 즉 x나 y나 지금돌고 있는 곳을 찾아간다
        return False

    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        # 만약 1번을 찾았다면 그자리는 0으로 바꿔준다
        for i in range(4):
            # 4번을 반복하는데
            nx = x + dx[i]
            ny = y + dy[i]
            # 새로운 x는 x에서 x의 변화량만큼 4방향을 체크해야함 같은게 있는지
            DFS(nx, ny)
            # 위에서 찾은 새로운x와y를 dfs에 다시 재귀해서 돌려준다
        return True
    return False


count = 0
result = 0
#다음 단지를 위해 초기화
for i in range(n):
    for j in range(n):
        if DFS(i, j):
            num.append(count)
            result += 1
            count = 0
            #흐름이 끊기면 0으로 초기화
            # 만약 DFS에서 True값이 나오면 count를 증가해준다

num.sort()  # 정렬해주고
print(result)
for i in range(len(num)):
    print(num[i])
    #각 단지마다 증가된 숫자를 알려준다
