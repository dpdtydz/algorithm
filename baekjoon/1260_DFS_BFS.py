import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
# input
link = []
for _ in range(N + 1):
    link.append([0] * (N + 1))
for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    link[v1][v2], link[v2][v1] = 1, 1


# n->m linkedlist
# 깊이탐색시작
# input (4 5 1)
#정점의 개수 4
#간선이 5/ 처음시작하는곳이1
# node 4
# node 1
# 처음시작은 항상 1
# dfs
#   [1]
# [2][3]
#[4]
# 일때 node의 rote는 1-> 2 -> 4 ->3
#bfs
#       [1]
#     [2] [3]
#    [4]
#일때  node의 rote는 1->2->3->4



def dfs(v):
    global visited
    visited = [0] * (N + 1)
    seq = [v]
    res = []

    while seq:
        p = seq.pop()
        if not visited[p]:
            visited[p] = 1
            res.append(str(p))
            for i in range(N, 0, -1):
                if link[p][i]:
#링크에 left 값과 right 값을 가져와 sequnce에 그대로 쌓는다. 하지만 왼쪽 단차로 내려가기떄문에 n은 0부터 -1 칸일때까지 간다
# WHY? 깊이탐색은 단방향이기때문에.
                    seq.append(i)
                    # 결국엔 i가돌면서 간선 전과 후로 반복하여 pop or append [A]<-[B]<-[c]
                    #  [A] [B]<-C] / D<-B or D<-C
                    # [A] [D] <-[B] <-[C]
    return res


# 너비탐색 시작
def bfs(v):
    global visited
    visited = [0] * (N + 1)
    seq = deque([V])
    res = []

    while seq:
        p = seq.popleft()
        if not visited[p]:
            visited[p] = 1
            res.append(str(p))
            for i in range(1, N + 1):
                if link[p][i]:
                    seq.append(i)
                    # 스택의 자유로은 left/right가 자유롭다 -> p_left/ p_ppend <-out <-in
    return res


result_1 = map(str, dfs(V))
result_2 = map(str, bfs(V))

print(' '.join(result_1))
print(' '.join(result_2))
