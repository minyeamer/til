"""
0. Link
- https://www.acmicpc.net/problem/7569

1. Idea
- BFS
- 7576번 토마토 문제에서 하나의 차원이 추가된 버전입니다.
- 차원이 늘어난만큼 N의 최대 길이가 감소했기 때문에 여전히 BFS로 해결할 수 있습니다.
- 익은 토마토의 기준에서 전체 상자를 BFS로 완전탐색하면서 안익은 토마토까지의 최소 거리를 기록합니다.
- 최소 거리의 최댓값이 곧 토마토들이 모두 익는 최소 일수이며,   
  모든 토마토가 다 익었을 경우에 최소 일수를 출력하고, 그렇지 않은 경우엔 -1을 출력합니다.

2. Time Complexity
- O(N^3) = 1,000,000

3. Data Size
- M,N: 2 <= int <= 100
- H: 1 <= int <= 100
- t in [1,0,-1]
"""

from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
queue = deque([(h,r,c) for h in range(H) for r in range(N) for c in range(M) if box[h][r][c]==1])
days = 0

dz = [0,0,0,0,1,-1]
dy = [0,1,0,-1,0,0]
dx = [-1,0,1,0,0,0]

while queue:
    z,y,x = queue.popleft()
    days = max(days, box[z][y][x])
    for i in range(6):
        nz,ny,nx = z+dz[i],y+dy[i],x+dx[i]
        if 0<=nz<H and 0<=ny<N and 0<=nx<M and box[nz][ny][nx]==0:
            box[nz][ny][nx] = box[z][y][x] + 1
            queue.append((nz,ny,nx))

if 0 in {cell for layer in box for row in layer for cell in row}:
    print(-1)
else:
    print(days-1)