"""
0. Link
- https://www.acmicpc.net/problem/1389

1. Idea
- BFS
- 1부터 N까지의 번호에 대해 매번 BFS를 수행하면서 다른 모든 노드와의 거리를 파악
- 가장 작은 거리의 합을 가진 노드의 인덱스 번호를 출력

2. Time Complexity
- O(N^2+NM) = 510,000

3. Data Size
- N: 2 <= int <= 100
- M: 1 <= int <= 5,000
"""

from collections import deque
import sys
input = sys.stdin.readline

def bfs(target, nodes):
    num = [0] * (N+1)
    queue = deque([target])
    visited = [False] * (N+1)
    visited[target] = True

    while queue:
        node = queue.popleft()
        for next in nodes[node]:
            if not visited[next]:
                num[next] = num[node]+1
                visited[next] = True
                queue.append(next)
    return sum(num)

N, M = map(int, input().split())
rels = [list() for _ in range(N+1)]
kevin = [0] * (N+1)

for _ in range(M):
    A, B = map(int, input().split())
    rels[A].append(B)
    rels[B].append(A)

for i in range(1,N+1):
    kevin[i] = bfs(i, rels)

print(kevin.index(min(kevin[1:])))