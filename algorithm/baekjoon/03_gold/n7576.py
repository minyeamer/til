"""
0. Link
- https://www.acmicpc.net/problem/7576

1. Idea
- BFS를 활용한 시뮬레이션을 통해 모든 토마토가 익을 떄까지 걸리는 최소 기간을 계산
- 초기엔 안익은 토마토의 기준에서 매번 익은 토마토까지의 최단거리를 탐색하여,   
  O(N^4)의 시간 복잡도로 시간 초과가 발생
- 이후 익은 토마토의 기준에서 시뮬레이션을 단 한번만 수행하여 각각의 칸에 도달하는데 걸리는 거리값을 갱신
- 모두 익지 못하는 상황에 대해 1안에선 에러를 발생시켜 처리했고, 2안에선 종료 코드를 실행해 처리

2. Time Complexity
- O(N^2) = 1,000,000

3. Data Size
- M,N: 2 <= int <= 1,000
- t in [1,0,-1]
"""

from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
days = 0

# ============== 1안 (시간초과) =============

def bfs(graph, start, n, m, vistied):
    queue = deque([start])
    dist = 0

    dy = [0,1,0,-1]
    dx = [-1,0,1,0]

    while queue:
        for _ in range(len(queue)):
            y,x = queue.popleft()
            if graph[y][x] == 1:
                return dist
            for i in range(4):
                ny,nx = y+dy[i],x+dx[i]
                if 0<=ny<n and 0<=nx<m and not vistied[ny][nx] and graph[ny][nx]!=-1:
                    queue.append((ny,nx))
                    vistied[ny][nx] = True
        dist += 1
    raise Exception()

try:
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                vistied = [[False] * M for _ in range(N)]
                vistied[i][j] = True
                days = max(days, bfs(box, (i,j), N, M, vistied))
    print(days)
except Exception:
    print(-1)

# =============== 2안 (통과) ===============

queue = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i,j))

def bfs(graph, queue, n, m):
    dy = [0,1,0,-1]
    dx = [-1,0,1,0]

    while queue:
        y,x = queue.popleft()
        for i in range(4):
            ny,nx = y+dy[i],x+dx[i]
            if 0<=ny<n and 0<=nx<m and graph[ny][nx]==0:
                graph[ny][nx] = graph[y][x] + 1
                queue.append((ny,nx))

bfs(box, queue, N, M)
for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            print(-1)
            exit(0)
        days = max(days, box[i][j])
print(days-1)