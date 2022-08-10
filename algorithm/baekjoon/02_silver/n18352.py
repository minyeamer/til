"""
1. Idea
- BFS
- 시작 노드 X부터 연결된 노드를 순차적으로 방문하면서 X로부터 떨어진 거리를 기록
- 거리가 K와 같은 노드를 출력하고, 해당하는 노드가 없을 경우 -1을 출력
- 탐색하는 노드의 거리가 K를 넘어가면 탐색을 중지하여 시간 단축

2. Time Complexity
- BFS: O(N+M) = 1,300,000

3. Data Size
- N: 2 <= int <= 300,000
- M: 1 <= int <= 1,000,000
- K: 1 <= int <= 300,000
- X: 1 <= int <= N
- A, B: 1 <= int <= N
"""

from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
nodes = [[] for _ in range(N+1)]
visited = [False] * (N+1)
dists = [0] * (N+1)

for _ in range(M):
    A, B = map(int, input().split())
    nodes[A].append(B)

queue = deque()
queue.append(X)
visited[X] = True

while queue:
    city = queue.popleft()

    for next in nodes[city]:
        if not visited[next] and dists[city] < K:
            queue.append(next)
            visited[next] = True
            dists[next] = dists[city]+1

targets = [i for i,d in enumerate(dists) if d==K]
if targets:
    for target in targets:
        print(target)
else:
    print(-1)