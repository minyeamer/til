"""
0. Link
- https://www.acmicpc.net/problem/11725

1. Idea
- BFS
- 1번 노드부터 BFS를 수행하면서 다음 노드에 순차적으로 접근
- 다음 노드가 이미 방문한 노드의 경우 부모 노드라 판단하여 배열에 저장
- 부모 노드가 저장된 배열에 대해 2번 노드부터 순차적으로 부모 노드를 출력

2. Time Complexity
- O(N+E) = 200,000

3. Data Size
- N: 2 <= int <= 100,000
"""

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
parents = [1] * (N+1)

for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

queue = deque([1])
visited[1] = True
while queue:
    node = queue.popleft()
    for next in graph[node]:
        if not visited[next]:
            queue.append(next)
            visited[next] = True
        else:
            parents[node] = next

for parent in parents[2:]:
    print(parent)